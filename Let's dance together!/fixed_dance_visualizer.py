import pygame
import numpy as np
import math
import sys
import os

# Simplified version without librosa dependency issues
class SimpleMusicDance:
    def __init__(self, width=1200, height=800):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("AI Music Visual Dance - Simplified")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        
        self.current_time = 0
        self.is_playing = False
        self.start_time = 0
        self.tempo = 120  # Default tempo
        self.energy = 0.5
        self.mood = "neutral"
        
        # Create dancers
        self.create_dancers()
        
    def create_dancers(self):
        """Create simple animated dancers"""
        self.dancers = [
            {"x": 300, "y": 400, "style": "human", "offset": 0},
            {"x": 600, "y": 400, "style": "abstract", "offset": 1},
            {"x": 900, "y": 400, "style": "robot", "offset": 2}
        ]
        
    def load_music(self, file_path):
        """Load music file"""
        try:
            if os.path.exists(file_path):
                pygame.mixer.music.load(file_path)
                print(f"Music loaded successfully: {file_path}")
                return True
            else:
                print(f"Music file not found: {file_path}")
                return False
        except Exception as e:
            print(f"Music loading failed: {e}")
            return False
    
    def play_music(self):
        """Start playing music"""
        try:
            pygame.mixer.music.play()
            self.is_playing = True
            self.start_time = pygame.time.get_ticks()
            print("Music started playing!")
        except Exception as e:
            print(f"Music playback failed: {e}")
    
    def get_current_music_features(self):
        """Get simulated music features"""
        current_time_ms = pygame.time.get_ticks() - self.start_time
        current_time = current_time_ms / 1000.0
        
        # Simulate beat detection
        beat_strength = 1.0 if int(current_time * 2) != int((current_time - 0.1) * 2) else 0.0
        
        # Simulate energy changes
        energy = 0.5 + 0.3 * math.sin(current_time * 0.5)
        
        return {
            'tempo': self.tempo,
            'energy': energy,
            'beat_strength': beat_strength,
            'mood': self.mood,
            'current_time': current_time
        }
    
    def draw_dancer(self, dancer_info, music_features):
        """Draw an animated dancer"""
        x = dancer_info["x"]
        y = dancer_info["y"]
        style = dancer_info["style"]
        offset = dancer_info["offset"]
        
        # Color based on energy
        energy = music_features.get('energy', 0.5)
        color = (
            int(energy * 255),
            int((1 - energy) * 255),
            150 + int(energy * 105)
        )
        
        if style == "human":
            self.draw_human_dancer(x, y, color, offset)
        elif style == "abstract":
            self.draw_abstract_dancer(x, y, color, offset)
        else:  # robot
            self.draw_robot_dancer(x, y, color, offset)
    
    def draw_human_dancer(self, x, y, color, offset):
        """Draw human-style dancer"""
        # Head
        pygame.draw.circle(self.screen, color, (int(x), int(y - 60)), 20)
        
        # Body
        pygame.draw.rect(self.screen, color, (int(x - 15), int(y - 40), 30, 80))
        
        # Animated arms
        arm_angle = math.sin(self.current_time * 3 + offset) * 0.8
        arm_length = 40
        left_arm_x = x - math.cos(arm_angle) * arm_length
        left_arm_y = y - 20 + math.sin(arm_angle) * arm_length
        right_arm_x = x + math.cos(arm_angle) * arm_length
        right_arm_y = y - 20 + math.sin(arm_angle) * arm_length
        
        pygame.draw.line(self.screen, color, (x, y - 20), (left_arm_x, left_arm_y), 5)
        pygame.draw.line(self.screen, color, (x, y - 20), (right_arm_x, right_arm_y), 5)
        
        # Animated legs
        leg_angle = math.sin(self.current_time * 2 + offset + 1) * 0.5
        leg_length = 50
        left_leg_x = x - math.cos(leg_angle) * leg_length
        left_leg_y = y + 40 + abs(math.sin(leg_angle)) * leg_length
        right_leg_x = x + math.cos(leg_angle) * leg_length
        right_leg_y = y + 40 + abs(math.sin(leg_angle)) * leg_length
        
        pygame.draw.line(self.screen, color, (x, y + 40), (left_leg_x, left_leg_y), 6)
        pygame.draw.line(self.screen, color, (x, y + 40), (right_leg_x, right_leg_y), 6)
    
    def draw_abstract_dancer(self, x, y, color, offset):
        """Draw abstract-style dancer"""
        points = []
        for i in range(8):
            angle = i * math.pi/4 + self.current_time + offset
            radius = 30 + 20 * math.sin(self.current_time * 2 + offset + i)
            px = x + math.cos(angle) * radius
            py = y + math.sin(angle) * radius
            points.append((px, py))
        
        if len(points) >= 3:
            pygame.draw.polygon(self.screen, color, points)
    
    def draw_robot_dancer(self, x, y, color, offset):
        """Draw robot-style dancer"""
        # Body
        body_rect = pygame.Rect(x - 25, y - 50, 50, 100)
        pygame.draw.rect(self.screen, color, body_rect)
        
        # Head
        head_rect = pygame.Rect(x - 15, y - 80, 30, 30)
        pygame.draw.rect(self.screen, color, head_rect)
        
        # Mechanical joints
        joint_offset = math.sin(self.current_time * 4 + offset) * 5
        pygame.draw.circle(self.screen, (255, 255, 255), 
                          (int(x), int(y - 25 + joint_offset)), 5)
        pygame.draw.circle(self.screen, (255, 255, 255), 
                          (int(x), int(y + 25 + joint_offset)), 5)
    
    def draw_background(self, music_features):
        """Draw dynamic background"""
        # Background color based on mood
        energy = music_features.get('energy', 0.5)
        beat_strength = music_features.get('beat_strength', 0)
        
        bg_color = (
            int(30 + energy * 50 + beat_strength * 30),
            int(40 + energy * 30 + beat_strength * 20),
            int(60 + energy * 70 + beat_strength * 50)
        )
        self.screen.fill(bg_color)
        
        # Simple spectrum visualization
        for i in range(32):
            bar_height = 50 + 200 * math.sin(self.current_time * 2 + i * 0.2) * energy
            bar_width = self.width // 32 - 2
            x = i * (bar_width + 2)
            y = self.height - abs(bar_height)
            
            color = (
                100 + int(155 * (i / 32)),
                100 + int(energy * 155),
                200
            )
            
            pygame.draw.rect(self.screen, color, (x, y, bar_width, abs(bar_height)))
    
    def run(self):
        """Main loop"""
        print("Starting AI Music Visual Dance...")
        print("Controls:")
        print("  SPACE: Play/Pause music")
        print("  ESC: Exit")
        print("  Mouse click: Change tempo")
        
        # Try to load music
        music_loaded = self.load_music("test_music.mp3")
        if music_loaded:
            self.play_music()
        else:
            print("Running without music - visual effects only")
        
        running = True
        
        try:
            while running:
                self.current_time = pygame.time.get_ticks() / 1000.0
                
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        elif event.key == pygame.K_SPACE:
                            if music_loaded:
                                if self.is_playing:
                                    pygame.mixer.music.pause()
                                    self.is_playing = False
                                    print("Music paused")
                                else:
                                    pygame.mixer.music.unpause()
                                    self.is_playing = True
                                    print("Music resumed")
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # Change tempo on mouse click
                        self.tempo = 80 + (pygame.mouse.get_pos()[0] / self.width) * 160
                        print(f"Tempo changed to: {self.tempo:.1f} BPM")
                
                # Get current music features
                music_features = self.get_current_music_features()
                
                # Draw everything
                self.draw_background(music_features)
                
                # Draw dancers
                for dancer in self.dancers:
                    self.draw_dancer(dancer, music_features)
                
                # Draw UI
                font = pygame.font.Font(None, 48)
                info_text = f"Tempo: {music_features.get('tempo', 0):.1f} BPM | Energy: {music_features.get('energy', 0):.2f}"
                text_surface = font.render(info_text, True, (255, 255, 255))
                self.screen.blit(text_surface, (20, 20))
                
                # Draw controls
                font_small = pygame.font.Font(None, 32)
                controls = ["SPACE: Play/Pause", "ESC: Exit", "Click: Change Tempo"]
                for i, control in enumerate(controls):
                    text_surface = font_small.render(control, True, (200, 200, 200))
                    self.screen.blit(text_surface, (20, self.height - 120 + i * 35))
                
                pygame.display.flip()
                self.clock.tick(60)
                
        except Exception as e:
            print(f"Error during execution: {e}")
        finally:
            print("Shutting down...")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    try:
        visualizer = SimpleMusicDance()
        visualizer.run()
    except Exception as e:
        print(f"Failed to start visualizer: {e}")
        input("Press Enter to exit...")