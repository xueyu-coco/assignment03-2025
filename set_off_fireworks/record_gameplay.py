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

class GameplayRecorder:
    def __init__(self):
        self.recording = False
        self.frames = []
        self.frame_count = 0
        self.max_frames = 600  # 10 seconds at 60 FPS
        self.recording_states = []
        
    def add_frame(self, surface, state_info=""):
        """Add a frame to the recording with state information"""
        if self.recording and self.frame_count < self.max_frames:
            # Convert pygame surface to numpy array
            frame_array = pygame.surfarray.array3d(surface)
            frame_array = np.transpose(frame_array, (1, 0, 2))
            
            # Convert to PIL Image for text overlay
            frame_image = Image.fromarray(frame_array)
            
            # Add state information overlay
            if state_info:
                draw = ImageDraw.Draw(frame_image)
                try:
                    # Try to use a system font
                    font = ImageFont.truetype("arial.ttf", 24)
                except:
                    # Fallback to default font
                    font = ImageFont.load_default()
                
                # Add text with background
                text_bbox = draw.textbbox((0, 0), state_info, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                # Background rectangle
                draw.rectangle([10, 10, 20 + text_width, 20 + text_height], 
                             fill=(0, 0, 0, 128))
                draw.text((15, 15), state_info, fill=(255, 255, 255), font=font)
            
            self.frames.append(np.array(frame_image))
            self.recording_states.append(state_info)
            self.frame_count += 1
            
    def start_recording(self):
        """Start recording gameplay"""
        self.recording = True
        self.frames = []
        self.frame_count = 0
        self.recording_states = []
        print("🎬 Recording started!")
        
    def stop_recording(self):
        """Stop recording gameplay"""
        self.recording = False
        print(f"🎬 Recording stopped! Captured {len(self.frames)} frames")
        
    def save_gif(self, filename="gameplay_demo.gif", fps=30):
        """Save recorded frames as GIF"""
        if not self.frames:
            print("❌ No frames to save!")
            return
            
        print(f"💾 Saving GIF with {len(self.frames)} frames...")
        
        # Reduce frame rate by skipping frames
        skip_factor = 60 // fps  # Convert from 60 FPS to desired FPS
        selected_frames = self.frames[::skip_factor]
        
        # Save as GIF
        imageio.mimsave(filename, selected_frames, fps=fps, loop=0)
        print(f"✅ GIF saved as: {filename}")
        print(f"📊 Final GIF: {len(selected_frames)} frames at {fps} FPS")

class RecordableFireworks(VoiceControlledFireworks):
    def __init__(self):
        super().__init__()
        self.recorder = GameplayRecorder()
        self.demo_sequence = [
            {"action": "start_recording", "delay": 1.0},
            {"action": "show_normal_mode", "delay": 3.0},
            {"action": "switch_to_monster_hunt", "delay": 1.0},
            {"action": "simulate_voice_input", "delay": 2.0},
            {"action": "wait_for_monsters", "delay": 5.0},
            {"action": "simulate_combat", "delay": 8.0},
            {"action": "simulate_damage", "delay": 3.0},
            {"action": "game_over_sequence", "delay": 3.0},
            {"action": "restart_game", "delay": 2.0},
            {"action": "stop_recording", "delay": 1.0}
        ]
        self.demo_step = 0
        self.demo_timer = 0
        self.auto_demo = True
        self.last_demo_time = time.time()
        
    def run_demo(self):
        """Run automated demo sequence"""
        self.recorder.start_recording()
        
        try:
            running = True
            while running and self.demo_step < len(self.demo_sequence):
                current_time = time.time()
                dt = current_time - self.last_demo_time
                self.last_demo_time = current_time
                
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                
                # Execute demo sequence
                if self.auto_demo:
                    self.demo_timer += dt
                    current_step = self.demo_sequence[self.demo_step]
                    
                    if self.demo_timer >= current_step["delay"]:
                        self.execute_demo_action(current_step["action"])
                        self.demo_step += 1
                        self.demo_timer = 0
                
                # Update game logic
                self.update_game_logic()
                
                # Get current state for overlay
                state_info = self.get_current_state_info()
                
                # Record frame
                self.recorder.add_frame(self.screen, state_info)
                
                # Draw and update
                pygame.display.flip()
                self.clock.tick(60)
                
        except KeyboardInterrupt:
            print("\n🎬 Demo interrupted!")
        finally:
            self.recorder.stop_recording()
            self.recorder.save_gif("voice_fireworks_demo.gif", fps=15)
            
            # Cleanup
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            pygame.quit()
    
    def execute_demo_action(self, action):
        """Execute a demo action"""
        if action == "start_recording":
            print("🎬 Demo: Starting recording")
            
        elif action == "show_normal_mode":
            print("🎆 Demo: Showing normal mode")
            self.game_mode = "normal"
            # Create some manual fireworks
            for i in range(3):
                self.create_firework(0.3 + i * 0.2)
                
        elif action == "switch_to_monster_hunt":
            print("👹 Demo: Switching to monster hunt mode")
            self.game_mode = "monster_hunt"
            self.reset_game()
            
        elif action == "simulate_voice_input":
            print("🎤 Demo: Simulating voice input")
            # Simulate voice-controlled fireworks
            for i in range(5):
                volume = 0.2 + random.random() * 0.4
                self.create_firework(volume)
                
        elif action == "wait_for_monsters":
            print("⏳ Demo: Waiting for monsters to spawn")
            # Let monsters spawn naturally
            
        elif action == "simulate_combat":
            print("⚔️ Demo: Simulating combat")
            # Create fireworks to fight monsters
            for i in range(10):
                if random.random() < 0.7:  # 70% chance to create firework
                    volume = 0.4 + random.random() * 0.4
                    self.create_firework(volume)
                    
        elif action == "simulate_damage":
            print("💔 Demo: Simulating player damage")
            # Take some damage
            self.take_damage(20)  # Take 2/3 health damage
            
        elif action == "game_over_sequence":
            print("💀 Demo: Game over sequence")
            # Take final damage
            self.take_damage(10)
            
        elif action == "restart_game":
            print("🔄 Demo: Restarting game")
            self.reset_game()
            
        elif action == "stop_recording":
            print("🛑 Demo: Stopping recording")
    
    def update_game_logic(self):
        """Update game logic without voice input"""
        # Update fireworks
        for firework in self.fireworks[:]:
            firework.update()
            if firework.is_finished():
                self.fireworks.remove(firework)
        
        # Monster hunt mode updates
        if self.game_mode == "monster_hunt" and not self.game_over:
            self.spawn_monster()
            self.update_monsters()
            self.update_fireballs()
            self.check_monster_collisions()
            self.check_firework_interceptions()
        
        # Draw everything
        self.update_background()
        
        # Draw monsters and fireballs (in monster hunt mode)
        if self.game_mode == "monster_hunt":
            self.draw_monsters()
            self.draw_fireballs()
        
        # Draw fireworks
        for firework in self.fireworks:
            firework.draw(self.screen)
        
        # Draw UI
        self.draw_volume_indicator()
        self.draw_instructions()
        self.draw_statistics()
        
        # Draw health bar (in monster hunt mode)
        if self.game_mode == "monster_hunt":
            self.draw_health_bar()
        
        # Draw game over screen if needed
        if self.game_over:
            self.draw_game_over()
    
    def get_current_state_info(self):
        """Get current game state for overlay"""
        if self.game_mode == "normal":
            return f"Normal Mode | Fireworks: {len(self.fireworks)}"
        else:
            if self.game_over:
                return f"Game Over | Score: {self.score} | Health: 0/30"
            else:
                monsters_alive = sum(1 for m in self.monsters if m.alive)
                fireballs_count = len([f for f in self.fireballs if f.alive])
                return f"Monster Hunt | Health: {self.current_health}/30 | Score: {self.score} | Monsters: {monsters_alive} | Fireballs: {fireballs_count}"

if __name__ == "__main__":
    try:
        print("🎮 Starting Voice-Controlled Fireworks Demo Recording...")
        print("🎬 This will create an automated gameplay demonstration")
        
        demo_game = RecordableFireworks()
        demo_game.run_demo()
        
        print("✅ Demo recording completed!")
        print("📁 Check 'voice_fireworks_demo.gif' for the gameplay demonstration")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        input("Press Enter to exit...")