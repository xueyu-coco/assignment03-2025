import pygame
import numpy as np
import pyaudio
import threading
import queue
import math
import random
import time
from collections import deque
import os
from PIL import Image, ImageDraw, ImageFont
import imageio

# Import the main game class
from voice_fireworks import VoiceControlledFireworks

class EnhancedGameplayRecorder:
    def __init__(self):
        self.recording = False
        self.frames = []
        self.frame_count = 0
        self.max_frames = 1200  # 20 seconds at 60 FPS
        
    def add_frame_with_overlay(self, surface, state_info, action_info=""):
        """Add frame with enhanced overlay information"""
        if self.recording and self.frame_count < self.max_frames:
            # Convert pygame surface to numpy array
            frame_array = pygame.surfarray.array3d(surface)
            frame_array = np.transpose(frame_array, (1, 0, 2))
            
            # Convert to PIL Image
            frame_image = Image.fromarray(frame_array)
            draw = ImageDraw.Draw(frame_image)
            
            try:
                font_large = ImageFont.truetype("arial.ttf", 28)
                font_small = ImageFont.truetype("arial.ttf", 20)
            except:
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()
            
            # Main state info (top-left)
            if state_info:
                self.draw_text_with_background(draw, state_info, (15, 15), font_large, (255, 255, 255), (0, 0, 0, 180))
            
            # Action info (top-right)
            if action_info:
                text_bbox = draw.textbbox((0, 0), action_info, font=font_small)
                text_width = text_bbox[2] - text_bbox[0]
                x_pos = frame_image.width - text_width - 20
                self.draw_text_with_background(draw, action_info, (x_pos, 15), font_small, (255, 255, 0), (0, 0, 0, 180))
            
            # Frame counter (bottom-right)
            frame_text = f"Frame: {self.frame_count}"
            frame_bbox = draw.textbbox((0, 0), frame_text, font=font_small)
            frame_width = frame_bbox[2] - frame_bbox[0]
            frame_x = frame_image.width - frame_width - 15
            frame_y = frame_image.height - 35
            self.draw_text_with_background(draw, frame_text, (frame_x, frame_y), font_small, (255, 255, 255), (0, 0, 0, 120))
            
            self.frames.append(np.array(frame_image))
            self.frame_count += 1
    
    def draw_text_with_background(self, draw, text, position, font, text_color, bg_color):
        """Draw text with background rectangle"""
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Background rectangle
        bg_rect = [position[0] - 5, position[1] - 2, 
                  position[0] + text_width + 10, position[1] + text_height + 4]
        draw.rectangle(bg_rect, fill=bg_color)
        
        # Text
        draw.text(position, text, fill=text_color, font=font)
    
    def start_recording(self):
        self.recording = True
        self.frames = []
        self.frame_count = 0
        print("🎬 Enhanced recording started!")
    
    def stop_recording(self):
        self.recording = False
        print(f"🎬 Enhanced recording stopped! Captured {len(self.frames)} frames")
    
    def save_gif(self, filename="enhanced_gameplay.gif", fps=20):
        if not self.frames:
            print("❌ No frames to save!")
            return
        
        print(f"💾 Creating enhanced GIF with {len(self.frames)} frames...")
        
        # Select frames for optimal GIF size
        skip_factor = max(1, 60 // fps)
        selected_frames = self.frames[::skip_factor]
        
        # Save as GIF with optimization
        imageio.mimsave(filename, selected_frames, fps=fps, loop=0, optimize=True)
        print(f"✅ Enhanced GIF saved as: {filename}")
        print(f"📊 Final GIF: {len(selected_frames)} frames at {fps} FPS")

class ComprehensiveFireworksDemo(VoiceControlledFireworks):
    def __init__(self):
        super().__init__()
        self.recorder = EnhancedGameplayRecorder()
        self.demo_phase = 0
        self.phase_timer = 0
        self.last_update_time = time.time()
        
        # Comprehensive demo phases
        self.demo_phases = [
            {"name": "Introduction", "duration": 3.0, "action": "show_intro"},
            {"name": "Normal Mode Demo", "duration": 5.0, "action": "normal_mode_demo"},
            {"name": "Switch to Monster Hunt", "duration": 2.0, "action": "switch_mode"},
            {"name": "Voice Input Simulation", "duration": 4.0, "action": "voice_simulation"},
            {"name": "Monster Spawning", "duration": 3.0, "action": "monster_spawn"},
            {"name": "Combat Phase 1", "duration": 6.0, "action": "combat_phase_1"},
            {"name": "Fireball Interception", "duration": 4.0, "action": "interception_demo"},
            {"name": "Intense Combat", "duration": 5.0, "action": "intense_combat"},
            {"name": "Take Damage", "duration": 3.0, "action": "take_damage"},
            {"name": "Critical Health", "duration": 4.0, "action": "critical_health"},
            {"name": "Game Over", "duration": 3.0, "action": "game_over"},
            {"name": "Restart & Recovery", "duration": 3.0, "action": "restart"},
            {"name": "Final Showcase", "duration": 4.0, "action": "final_showcase"}
        ]
        
        self.current_action = ""
        self.firework_spawn_timer = 0
        
    def run_comprehensive_demo(self):
        """Run comprehensive gameplay demonstration"""
        self.recorder.start_recording()
        
        try:
            running = True
            print("🎮 Starting comprehensive demo...")
            
            while running and self.demo_phase < len(self.demo_phases):
                current_time = time.time()
                dt = current_time - self.last_update_time
                self.last_update_time = current_time
                
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                
                # Update phase timer
                self.phase_timer += dt
                current_phase = self.demo_phases[self.demo_phase]
                
                # Execute current phase
                if self.phase_timer <= current_phase["duration"]:
                    self.execute_phase_action(current_phase["action"], dt)
                    self.current_action = f"Phase: {current_phase['name']}"
                else:
                    # Move to next phase
                    self.demo_phase += 1
                    self.phase_timer = 0
                    if self.demo_phase < len(self.demo_phases):
                        print(f"🎬 Phase {self.demo_phase + 1}: {self.demo_phases[self.demo_phase]['name']}")
                
                # Update game
                self.update_game_state()
                
                # Get state info
                state_info = self.get_detailed_state_info()
                
                # Record frame with enhanced overlay
                self.recorder.add_frame_with_overlay(self.screen, state_info, self.current_action)
                
                pygame.display.flip()
                self.clock.tick(60)
                
        except KeyboardInterrupt:
            print("\n🎬 Demo interrupted!")
        finally:
            self.recorder.stop_recording()
            self.recorder.save_gif("comprehensive_fireworks_demo.gif", fps=20)
            
            # Cleanup
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            pygame.quit()
    
    def execute_phase_action(self, action, dt):
        """Execute specific phase actions"""
        if action == "show_intro":
            self.game_mode = "normal"
            
        elif action == "normal_mode_demo":
            self.game_mode = "normal"
            # Create beautiful fireworks display
            if random.random() < 0.1:  # 10% chance per frame
                volume = 0.3 + random.random() * 0.5
                self.create_firework(volume)
                
        elif action == "switch_mode":
            if self.phase_timer > 1.0:  # Switch after 1 second
                self.game_mode = "monster_hunt"
                self.reset_game()
                
        elif action == "voice_simulation":
            # Simulate voice input with varying volumes
            if random.random() < 0.15:
                volume = 0.2 + random.random() * 0.6
                self.create_firework(volume)
                
        elif action == "monster_spawn":
            # Let monsters spawn naturally
            pass
            
        elif action == "combat_phase_1":
            # Regular combat with moderate fireworks
            if random.random() < 0.12:
                volume = 0.4 + random.random() * 0.4
                self.create_firework(volume)
                
        elif action == "interception_demo":
            # Focus on showing fireball interception
            if len(self.fireballs) > 0 and random.random() < 0.3:
                # Target fireballs with larger explosions
                volume = 0.6 + random.random() * 0.3
                self.create_firework(volume)
                
        elif action == "intense_combat":
            # Rapid-fire combat
            if random.random() < 0.25:
                volume = 0.5 + random.random() * 0.4
                self.create_firework(volume)
                
        elif action == "take_damage":
            # Simulate taking damage
            if self.phase_timer > 1.5 and self.current_health > 20:
                self.take_damage(10)
                
        elif action == "critical_health":
            # Desperate defense at low health
            if random.random() < 0.2:
                volume = 0.7 + random.random() * 0.3
                self.create_firework(volume)
                
        elif action == "game_over":
            # Take final damage
            if self.phase_timer > 1.0 and not self.game_over:
                self.take_damage(20)
                
        elif action == "restart":
            # Restart the game
            if self.phase_timer > 1.5:
                self.reset_game()
                
        elif action == "final_showcase":
            # Final fireworks display
            if random.random() < 0.18:
                volume = 0.4 + random.random() * 0.5
                self.create_firework(volume)
    
    def update_game_state(self):
        """Update all game systems"""
        # Update fireworks
        for firework in self.fireworks[:]:
            firework.update()
            if firework.is_finished():
                self.fireworks.remove(firework)
        
        # Monster hunt updates
        if self.game_mode == "monster_hunt" and not self.game_over:
            self.spawn_monster()
            self.update_monsters()
            self.update_fireballs()
            self.check_monster_collisions()
            self.check_firework_interceptions()
        
        # Draw everything
        self.update_background()
        
        if self.game_mode == "monster_hunt":
            self.draw_monsters()
            self.draw_fireballs()
        
        for firework in self.fireworks:
            firework.draw(self.screen)
        
        self.draw_volume_indicator()
        self.draw_instructions()
        self.draw_statistics()
        
        if self.game_mode == "monster_hunt":
            self.draw_health_bar()
        
        if self.game_over:
            self.draw_game_over()
    
    def get_detailed_state_info(self):
        """Get detailed state information for overlay"""
        if self.game_mode == "normal":
            return f"🎆 NORMAL MODE | Fireworks: {len(self.fireworks)}"
        else:
            if self.game_over:
                return f"💀 GAME OVER | Final Score: {self.score}"
            else:
                monsters_alive = sum(1 for m in self.monsters if m.alive)
                fireballs_active = len([f for f in self.fireballs if f.alive])
                health_status = "🟢" if self.current_health > 20 else "🟡" if self.current_health > 10 else "🔴"
                return f"⚔️ MONSTER HUNT {health_status} | HP: {self.current_health}/30 | Score: {self.score} | Monsters: {monsters_alive} | Fireballs: {fireballs_active}"

if __name__ == "__main__":
    try:
        print("🎮 Starting Comprehensive Voice-Controlled Fireworks Demo...")
        print("🎬 This will create a complete gameplay demonstration showing all features")
        print("📺 Demo will showcase: Normal mode, Monster hunt, Combat, Interception, Damage, Game over")
        
        demo = ComprehensiveFireworksDemo()
        demo.run_comprehensive_demo()
        
        print("✅ Comprehensive demo completed!")
        print("📁 Check 'comprehensive_fireworks_demo.gif' for the complete demonstration")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")