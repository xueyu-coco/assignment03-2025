import pygame
import numpy as np
import pyaudio
import threading
import queue
import math
import random
import time
from collections import deque

class Firework:
    def __init__(self, x, y, target_x, target_y, size_multiplier=1.0):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.size_multiplier = size_multiplier
        self.exploded = False
        self.particles = []
        
        # Launch rocket properties
        self.rocket_x = x
        self.rocket_y = y
        self.rocket_speed = 8 + size_multiplier * 2
        self.rocket_color = (255, 255, 255)
        
        # Explosion properties
        self.explosion_size = int(50 + size_multiplier * 100)
        self.particle_count = int(30 + size_multiplier * 50)
        
        # Random explosion colors
        color_sets = [
            [(255, 100, 100), (255, 200, 100), (255, 255, 100)],  # Red-Orange-Yellow
            [(100, 100, 255), (200, 100, 255), (255, 100, 255)],  # Blue-Purple-Pink
            [(100, 255, 100), (100, 255, 200), (200, 255, 100)],  # Green variations
            [(255, 200, 0), (255, 150, 0), (255, 100, 0)],        # Orange variations
            [(200, 0, 255), (150, 0, 255), (255, 0, 200)]         # Purple-Pink
        ]
        self.colors = random.choice(color_sets)
        
    def update(self):
        if not self.exploded:
            # Move rocket towards target
            dx = self.target_x - self.rocket_x
            dy = self.target_y - self.rocket_y
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance < self.rocket_speed:
                # Reached target, explode!
                self.exploded = True
                self.create_explosion()
            else:
                # Move rocket
                self.rocket_x += (dx / distance) * self.rocket_speed
                self.rocket_y += (dy / distance) * self.rocket_speed
        else:
            # Update explosion particles
            for particle in self.particles[:]:
                particle['x'] += particle['vx']
                particle['y'] += particle['vy']
                particle['vy'] += 0.2  # Gravity
                particle['life'] -= 1
                particle['size'] *= 0.98  # Shrink over time
                
                if particle['life'] <= 0 or particle['size'] < 1:
                    self.particles.remove(particle)
    
    def create_explosion(self):
        """Create explosion particles"""
        for _ in range(self.particle_count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 12) * self.size_multiplier
            
            particle = {
                'x': self.target_x,
                'y': self.target_y,
                'vx': math.cos(angle) * speed,
                'vy': math.sin(angle) * speed - random.uniform(2, 5),
                'color': random.choice(self.colors),
                'life': random.randint(30, 80),
                'size': random.uniform(3, 8) * self.size_multiplier
            }
            self.particles.append(particle)
    
    def draw(self, screen):
        if not self.exploded:
            # Draw rocket
            pygame.draw.circle(screen, self.rocket_color, 
                             (int(self.rocket_x), int(self.rocket_y)), 3)
            # Draw rocket trail
            trail_length = 20
            for i in range(trail_length):
                alpha = (trail_length - i) / trail_length * 100
                trail_y = self.rocket_y + i * 2
                if trail_y < screen.get_height():
                    color = (255, 255, 255, int(alpha))
                    s = pygame.Surface((6, 6), pygame.SRCALPHA)
                    pygame.draw.circle(s, color, (3, 3), 3)
                    screen.blit(s, (int(self.rocket_x) - 3, int(trail_y) - 3))
        else:
            # Draw explosion particles
            for particle in self.particles:
                if particle['size'] > 0:
                    # Create glow effect
                    glow_size = int(particle['size'] * 2)
                    glow_alpha = max(10, particle['life'] * 2)
                    
                    # Outer glow
                    glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
                    glow_color = (*particle['color'], glow_alpha // 3)
                    pygame.draw.circle(glow_surf, glow_color, 
                                     (glow_size, glow_size), glow_size)
                    screen.blit(glow_surf, (int(particle['x']) - glow_size, 
                                          int(particle['y']) - glow_size))
                    
                    # Main particle
                    pygame.draw.circle(screen, particle['color'],
                                     (int(particle['x']), int(particle['y'])),
                                     int(particle['size']))
    
    def is_finished(self):
        return self.exploded and len(self.particles) == 0


class VoiceControlledFireworks:
    def __init__(self, width=1200, height=800):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Voice-Controlled Fireworks 🎆")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        
        # Audio settings
        self.sample_rate = 44100
        self.chunk_size = 1024
        self.audio_format = pyaudio.paFloat32
        
        # Initialize audio
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=self.audio_format,
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        # Voice analysis
        self.volume_history = deque(maxlen=30)
        self.volume_threshold = 0.01  # Minimum volume to trigger fireworks
        self.max_volume = 0.5  # Maximum expected volume for scaling
        
        # Fireworks
        self.fireworks = []
        self.last_firework_time = 0
        self.firework_cooldown = 0.3  # Minimum time between fireworks (seconds)
        
        # Background and effects
        self.background_color = [10, 10, 30]  # Dark blue night sky
        self.stars = self.create_stars()
        
        # Statistics
        self.total_fireworks = 0
        self.current_volume = 0
        
    def create_stars(self):
        """Create background stars"""
        stars = []
        for _ in range(100):
            star = {
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height // 2),
                'brightness': random.uniform(50, 200),
                'twinkle_speed': random.uniform(0.02, 0.05)
            }
            stars.append(star)
        return stars
    
    def analyze_audio(self):
        """Analyze audio input for volume"""
        try:
            audio_data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            audio_array = np.frombuffer(audio_data, dtype=np.float32)
            
            # Calculate volume (RMS)
            volume = np.sqrt(np.mean(audio_array**2))
            volume = min(volume, self.max_volume)  # Cap the volume
            
            self.volume_history.append(volume)
            self.current_volume = volume
            
            return volume
        except Exception as e:
            print(f"Audio error: {e}")
            return 0
    
    def should_launch_firework(self, volume):
        """Determine if we should launch a firework based on volume"""
        current_time = time.time()
        
        # Check cooldown
        if current_time - self.last_firework_time < self.firework_cooldown:
            return False
        
        # Check volume threshold
        if volume < self.volume_threshold:
            return False
        
        # Add some randomness to make it more natural
        probability = min(1.0, volume / self.max_volume * 2)
        return random.random() < probability
    
    def create_firework(self, volume):
        """Create a new firework based on volume"""
        # Launch position (bottom of screen)
        launch_x = random.randint(100, self.width - 100)
        launch_y = self.height - 50
        
        # Target position (upper area of screen)
        target_x = random.randint(100, self.width - 100)
        target_y = random.randint(100, self.height // 2)
        
        # Size based on volume (logarithmic scaling for better control)
        volume_normalized = volume / self.max_volume
        size_multiplier = 0.3 + (volume_normalized ** 0.7) * 2.0
        
        firework = Firework(launch_x, launch_y, target_x, target_y, size_multiplier)
        self.fireworks.append(firework)
        self.total_fireworks += 1
        self.last_firework_time = time.time()
    
    def update_background(self):
        """Update background with twinkling stars"""
        # Base night sky color
        self.screen.fill(self.background_color)
        
        # Draw twinkling stars
        current_time = time.time()
        for star in self.stars:
            brightness = star['brightness'] + 50 * math.sin(current_time * star['twinkle_speed'])
            brightness = max(50, min(255, brightness))
            color = (int(brightness), int(brightness), int(brightness * 0.9))
            pygame.draw.circle(self.screen, color, (star['x'], star['y']), 1)
    
    def draw_volume_indicator(self):
        """Draw volume level indicator"""
        # Volume bar
        bar_width = 300
        bar_height = 20
        bar_x = 50
        bar_y = 50
        
        # Background bar
        pygame.draw.rect(self.screen, (50, 50, 50), 
                        (bar_x, bar_y, bar_width, bar_height))
        
        # Volume level
        volume_width = int((self.current_volume / self.max_volume) * bar_width)
        volume_width = min(volume_width, bar_width)
        
        # Color based on volume level
        if self.current_volume < self.volume_threshold:
            color = (100, 100, 100)  # Gray - too quiet
        elif self.current_volume < self.max_volume * 0.3:
            color = (100, 255, 100)  # Green - good level
        elif self.current_volume < self.max_volume * 0.7:
            color = (255, 255, 100)  # Yellow - loud
        else:
            color = (255, 100, 100)  # Red - very loud
        
        pygame.draw.rect(self.screen, color,
                        (bar_x, bar_y, volume_width, bar_height))
        
        # Border
        pygame.draw.rect(self.screen, (255, 255, 255),
                        (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Labels
        font = pygame.font.Font(None, 36)
        volume_text = f"Voice Volume: {self.current_volume:.3f}"
        text_surface = font.render(volume_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (bar_x, bar_y - 35))
    
    def draw_instructions(self):
        """Draw usage instructions"""
        font = pygame.font.Font(None, 32)
        instructions = [
            "🎆 Voice-Controlled Fireworks 🎆",
            "",
            "🎤 Speak into your microphone to launch fireworks!",
            "📢 Louder voice = Bigger fireworks",
            "🔇 Quiet voice = Small fireworks",
            "🎯 Try different volumes for different effects",
            "",
            "Press ESC to exit"
        ]
        
        for i, instruction in enumerate(instructions):
            color = (255, 255, 255)
            if "🎆" in instruction:
                color = (255, 200, 100)
            elif "🎤" in instruction or "📢" in instruction:
                color = (100, 255, 100)
            
            text_surface = font.render(instruction, True, color)
            self.screen.blit(text_surface, (50, 120 + i * 35))
    
    def draw_statistics(self):
        """Draw fireworks statistics"""
        font = pygame.font.Font(None, 28)
        stats = [
            f"Total Fireworks Launched: {self.total_fireworks}",
            f"Active Fireworks: {len(self.fireworks)}"
        ]
        
        for i, stat in enumerate(stats):
            text_surface = font.render(stat, True, (200, 200, 255))
            self.screen.blit(text_surface, (self.width - 300, 50 + i * 30))
    
    def run(self):
        """Main game loop"""
        print("🎆 Voice-Controlled Fireworks Started!")
        print("🎤 Speak into your microphone to launch fireworks!")
        print("📢 Louder voice = Bigger fireworks")
        print("Press ESC to exit")
        
        running = True
        
        try:
            while running:
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        elif event.key == pygame.K_SPACE:
                            # Manual firework for testing
                            self.create_firework(self.max_volume * 0.5)
                
                # Analyze voice input
                volume = self.analyze_audio()
                
                # Launch fireworks based on voice
                if self.should_launch_firework(volume):
                    self.create_firework(volume)
                
                # Update fireworks
                for firework in self.fireworks[:]:
                    firework.update()
                    if firework.is_finished():
                        self.fireworks.remove(firework)
                
                # Draw everything
                self.update_background()
                
                # Draw fireworks
                for firework in self.fireworks:
                    firework.draw(self.screen)
                
                # Draw UI
                self.draw_volume_indicator()
                self.draw_instructions()
                self.draw_statistics()
                
                pygame.display.flip()
                self.clock.tick(60)
                
        except KeyboardInterrupt:
            print("\n🎆 Fireworks show ended!")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            # Cleanup
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            pygame.quit()

if __name__ == "__main__":
    try:
        fireworks = VoiceControlledFireworks()
        fireworks.run()
    except Exception as e:
        print(f"❌ Failed to start fireworks: {e}")
        input("Press Enter to exit...")