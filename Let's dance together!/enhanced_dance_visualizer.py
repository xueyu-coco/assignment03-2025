import pygame
import numpy as np
import math
import sys
import os

class EnhancedDancer:
    def __init__(self, x, y, size=50, style="human"):
        self.x = x
        self.y = y
        self.size = size
        self.style = style
        self.dance_move = "idle"
        self.move_progress = 0
        self.color = (255, 255, 255)
        self.available_moves = [
            "idle", "wave", "spin", "jump", "slide", "pop", "lock", "moonwalk", "shuffle", "break", "t-pose"
        ]
        self.available_styles = [
            "human", "abstract", "robot", "hiphop", "ballet", "jazz", "funk", "cartoon", "animal"
        ]
        
    def update_dance_move(self, music_features, current_time):
        """Update dance moves based on music features"""
        tempo = music_features.get('tempo', 120)
        energy = music_features.get('energy', 0.5)
        beat_strength = music_features.get('beat_strength', 0)
        mood = music_features.get('mood', 'neutral')
        
        # Trigger new moves on beat points
        if beat_strength > 0.8:
            # Pick move based on style and mood
            if self.style == "hiphop":
                moves = ["pop", "lock", "wave", "slide", "break"]
            elif self.style == "ballet":
                moves = ["spin", "jump", "t-pose", "idle"]
            elif self.style == "robot":
                moves = ["robot", "wave", "spin", "idle"]
            elif self.style == "cartoon":
                moves = ["t-pose", "jump", "wave", "spin"]
            else:
                moves = self.available_moves
                
            self.dance_move = np.random.choice(moves)
            self.move_progress = 0
            
            # Change color based on energy and mood
            if mood == "energetic":
                self.color = (255, 80, 80)
            elif mood == "happy":
                self.color = (80, 255, 120)
            elif mood == "calm":
                self.color = (80, 180, 255)
            else:
                self.color = (
                    int(energy * 255),
                    int((1 - energy) * 255),
                    150
                )
        
        self.move_progress += 0.1
        
    def draw(self, screen):
        """Draw the dancer with different styles"""
        if self.style == "human":
            self.draw_human_dancer(screen)
        elif self.style == "abstract":
            self.draw_abstract_dancer(screen)
        elif self.style == "robot":
            self.draw_robot_dancer(screen)
        elif self.style == "hiphop":
            self.draw_hiphop_dancer(screen)
        elif self.style == "ballet":
            self.draw_ballet_dancer(screen)
        elif self.style == "cartoon":
            self.draw_cartoon_dancer(screen)
        elif self.style == "animal":
            self.draw_animal_dancer(screen)
        else:
            self.draw_human_dancer(screen)
            
    def draw_human_dancer(self, screen):
        """Draw human-style dancer"""
        # Head
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y - 60)), 20)
        
        # Body
        pygame.draw.rect(screen, self.color, (int(self.x - 15), int(self.y - 40), 30, 80))
        
        # Animated arms based on dance move
        if self.dance_move == "wave":
            arm_angle = math.sin(self.move_progress * 3) * 1.2
        elif self.dance_move == "pop":
            arm_angle = 1.5 if int(self.move_progress * 4) % 2 else 0.3
        elif self.dance_move == "t-pose":
            arm_angle = math.pi/2
        else:
            arm_angle = math.sin(self.move_progress * 3) * 0.8
            
        arm_length = 40
        left_arm_x = self.x - math.cos(arm_angle) * arm_length
        left_arm_y = self.y - 20 + math.sin(arm_angle) * arm_length
        right_arm_x = self.x + math.cos(arm_angle) * arm_length
        right_arm_y = self.y - 20 + math.sin(arm_angle) * arm_length
        
        pygame.draw.line(screen, self.color, (self.x, self.y - 20), (left_arm_x, left_arm_y), 5)
        pygame.draw.line(screen, self.color, (self.x, self.y - 20), (right_arm_x, right_arm_y), 5)
        
        # Animated legs based on dance move
        if self.dance_move == "jump":
            leg_angle = math.sin(self.move_progress * 4) * 0.8
            leg_offset = abs(math.sin(self.move_progress * 4)) * 20
        elif self.dance_move == "moonwalk":
            leg_angle = math.sin(self.move_progress * 6) * 0.3
            leg_offset = 0
        else:
            leg_angle = math.sin(self.move_progress * 2 + 1) * 0.5
            leg_offset = 0
            
        leg_length = 50
        left_leg_x = self.x - math.cos(leg_angle) * leg_length
        left_leg_y = self.y + 40 + abs(math.sin(leg_angle)) * leg_length - leg_offset
        right_leg_x = self.x + math.cos(leg_angle) * leg_length
        right_leg_y = self.y + 40 + abs(math.sin(leg_angle)) * leg_length - leg_offset
        
        pygame.draw.line(screen, self.color, (self.x, self.y + 40), (left_leg_x, left_leg_y), 6)
        pygame.draw.line(screen, self.color, (self.x, self.y + 40), (right_leg_x, right_leg_y), 6)
    
    def draw_abstract_dancer(self, screen):
        """Draw abstract-style dancer"""
        points = []
        for i in range(8):
            angle = i * math.pi/4 + self.move_progress + math.sin(self.move_progress) * 0.5
            radius = 30 + 20 * math.sin(self.move_progress * 2 + i)
            px = self.x + math.cos(angle) * radius
            py = self.y + math.sin(angle) * radius
            points.append((px, py))
        
        if len(points) >= 3:
            pygame.draw.polygon(screen, self.color, points)
    
    def draw_robot_dancer(self, screen):
        """Draw robot-style dancer"""
        # Body
        body_rect = pygame.Rect(self.x - 25, self.y - 50, 50, 100)
        pygame.draw.rect(screen, self.color, body_rect)
        
        # Head
        head_rect = pygame.Rect(self.x - 15, self.y - 80, 30, 30)
        pygame.draw.rect(screen, self.color, head_rect)
        
        # Mechanical joints with movement
        if self.dance_move == "robot":
            joint_offset = int(self.move_progress * 2) % 2 * 10
        else:
            joint_offset = math.sin(self.move_progress * 4) * 5
            
        pygame.draw.circle(screen, (255, 255, 255), 
                          (int(self.x), int(self.y - 25 + joint_offset)), 5)
        pygame.draw.circle(screen, (255, 255, 255), 
                          (int(self.x), int(self.y + 25 + joint_offset)), 5)
    
    def draw_hiphop_dancer(self, screen):
        """Draw hip-hop style dancer"""
        self.draw_human_dancer(screen)
        # Add baggy clothes effect and cap
        pygame.draw.rect(screen, (100, 100, 100), (self.x-20, self.y-45, 40, 90))
        pygame.draw.ellipse(screen, (200, 0, 0), (self.x-25, self.y-85, 50, 15))
        
    def draw_ballet_dancer(self, screen):
        """Draw ballet style dancer"""
        self.draw_human_dancer(screen)
        # Add tutu and hair bun
        pygame.draw.circle(screen, (255, 200, 255), (int(self.x), int(self.y)), 40, 3)
        pygame.draw.circle(screen, (150, 100, 50), (int(self.x), int(self.y-70)), 8)
        
    def draw_cartoon_dancer(self, screen):
        """Draw cartoon style dancer"""
        # Bigger head, exaggerated features
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y - 50)), 30)
        # Big smile
        pygame.draw.arc(screen, (0, 0, 0), (self.x-15, self.y-55, 30, 20), 0, math.pi, 3)
        # Big eyes
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x-10), int(self.y-60)), 5)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x+10), int(self.y-60)), 5)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x-8), int(self.y-58)), 2)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x+12), int(self.y-58)), 2)
        
        # Body with cartoon proportions
        pygame.draw.ellipse(screen, self.color, (self.x-20, self.y-30, 40, 60))
        
    def draw_animal_dancer(self, screen):
        """Draw animal style dancer"""
        self.draw_human_dancer(screen)
        # Add ears
        pygame.draw.circle(screen, (150, 75, 0), (int(self.x-15), int(self.y-75)), 8)
        pygame.draw.circle(screen, (150, 75, 0), (int(self.x+15), int(self.y-75)), 8)
        # Add tail
        tail_x = self.x + math.sin(self.move_progress * 4) * 20
        tail_y = self.y + 40
        pygame.draw.line(screen, (150, 75, 0), (self.x, self.y+40), (tail_x, tail_y), 6)


class EnhancedDanceVisualizer:
    def __init__(self, width=1200, height=800):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Enhanced AI Music Visual Dance - All Styles & Effects")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        
        self.current_time = 0
        self.is_playing = False
        self.start_time = 0
        self.tempo = 120
        self.energy = 0.5
        self.mood = "neutral"
        
        # Create dancers with different styles
        self.create_dancers()
        
        # Particle system
        self.particles = []
        
    def create_dancers(self):
        """Create dancers with more styles"""
        styles = ["human", "abstract", "robot", "hiphop", "ballet", "cartoon", "animal"]
        positions = [(150, 400), (300, 400), (450, 400), (600, 400), (750, 400), (900, 400), (1050, 400)]
        
        self.dancers = []
        for i, (x, y) in enumerate(positions):
            if i < len(styles):
                style = styles[i]
                dancer = EnhancedDancer(x, y, size=40, style=style)
                self.dancers.append(dancer)
        
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
        """Get simulated music features with more variation"""
        current_time_ms = pygame.time.get_ticks() - self.start_time
        current_time = current_time_ms / 1000.0
        
        # Simulate beat detection with variable timing
        beat_period = 60.0 / self.tempo
        beat_strength = 1.0 if (current_time % beat_period) < 0.1 else 0.0
        
        # Simulate energy changes with multiple frequencies
        energy = 0.5 + 0.3 * math.sin(current_time * 0.5) + 0.2 * math.sin(current_time * 1.3)
        energy = max(0, min(1, energy))
        
        # Change mood over time
        mood_cycle = current_time % 20  # 20 second cycle
        if mood_cycle < 5:
            mood = "energetic"
        elif mood_cycle < 10:
            mood = "happy"
        elif mood_cycle < 15:
            mood = "calm"
        else:
            mood = "neutral"
        
        return {
            'tempo': self.tempo,
            'energy': energy,
            'beat_strength': beat_strength,
            'mood': mood,
            'current_time': current_time
        }
    
    def update_particles(self, music_features):
        """Update particle system"""
        # Add new particles on strong beats
        if music_features.get('beat_strength', 0) > 0.5:
            for _ in range(5):
                particle = {
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'vx': np.random.uniform(-2, 2),
                    'vy': np.random.uniform(-2, 2),
                    'life': 60,
                    'max_life': 60,
                    'color': (255, 255, np.random.randint(100, 255))
                }
                self.particles.append(particle)
        
        # Update existing particles
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def draw_particles(self):
        """Draw particle effects"""
        for particle in self.particles:
            alpha = int(255 * (particle['life'] / particle['max_life']))
            size = int(5 * (particle['life'] / particle['max_life']))
            if size > 0:
                color = (*particle['color'], alpha)
                s = pygame.Surface((size*2, size*2), pygame.SRCALPHA)
                pygame.draw.circle(s, color, (size, size), size)
                self.screen.blit(s, (particle['x']-size, particle['y']-size))
    
    def draw_background(self, music_features):
        """Draw dynamic background with light and particle effects"""
        # Background color based on mood
        mood_colors = {
            "energetic": (70, 20, 120),
            "happy": (100, 60, 20), 
            "calm": (20, 60, 100),
            "neutral": (40, 40, 60)
        }
        
        base_color = mood_colors.get(music_features.get('mood', 'neutral'), (40, 40, 60))
        beat_pulse = music_features.get('beat_strength', 0) * 80
        energy = music_features.get('energy', 0.5)
        
        bg_color = (
            min(255, base_color[0] + beat_pulse + int(energy * 30)),
            min(255, base_color[1] + beat_pulse//2 + int(energy * 20)),
            min(255, base_color[2] + beat_pulse + int(energy * 40))
        )
        
        self.screen.fill(bg_color)
        
        # Light effect: radial glow on strong beat
        if music_features.get('beat_strength', 0) > 0.5:
            for i in range(3):
                alpha = 60 - i*20
                radius = 150 + i*50
                s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                pygame.draw.circle(s, (255, 255, 180, alpha), (self.width//2, self.height//2), radius)
                self.screen.blit(s, (0,0))
        
        # Energy sparkles
        if energy > 0.7:
            for _ in range(int(energy * 20)):
                px = np.random.randint(0, self.width)
                py = np.random.randint(0, self.height)
                color = (255, 255, np.random.randint(180, 255))
                pygame.draw.circle(self.screen, color, (px, py), np.random.randint(1, 3))
    
    def draw_audio_visualization(self, music_features):
        """Draw enhanced audio visualization"""
        num_bars = 40
        energy = music_features.get('energy', 0.5)
        
        for i in range(num_bars):
            # Multiple frequency components
            bar_height = 50 + 100 * math.sin(self.current_time * 2 + i * 0.15) * energy
            bar_height += 50 * math.sin(self.current_time * 4 + i * 0.3) * energy
            bar_height = abs(bar_height)
            
            bar_width = self.width // num_bars - 2
            x = i * (bar_width + 2)
            y = self.height - bar_height
            
            # Rainbow colors
            hue = (i / num_bars + self.current_time * 0.1) % 1.0
            color = pygame.Color(0)
            color.hsva = (hue * 360, 100, int(50 + energy * 50), 100)
            
            pygame.draw.rect(self.screen, color, (x, y, bar_width, bar_height))
            
            # Add glow effect on every 4th bar
            if i % 4 == 0 and bar_height > 100:
                s = pygame.Surface((bar_width*3, int(bar_height)), pygame.SRCALPHA)
                glow_color = (*color[:3], 80)
                pygame.draw.ellipse(s, glow_color, (0, 0, bar_width*3, int(bar_height)))
                self.screen.blit(s, (x-bar_width, y-10))
    
    def run(self):
        """Main loop"""
        print("Starting Enhanced AI Music Visual Dance...")
        print("Features:")
        print("  - 7 different dance styles")
        print("  - Advanced particle effects")
        print("  - Dynamic lighting")
        print("  - Enhanced music visualization")
        print("")
        print("Controls:")
        print("  SPACE: Play/Pause music")
        print("  ESC: Exit")
        print("  Mouse click: Change tempo")
        print("  Arrow keys: Change mood")
        
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
                        elif event.key == pygame.K_UP:
                            self.mood = "energetic"
                            print("Mood: Energetic")
                        elif event.key == pygame.K_DOWN:
                            self.mood = "calm"
                            print("Mood: Calm")
                        elif event.key == pygame.K_LEFT:
                            self.mood = "neutral"
                            print("Mood: Neutral")
                        elif event.key == pygame.K_RIGHT:
                            self.mood = "happy"
                            print("Mood: Happy")
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # Change tempo on mouse click
                        self.tempo = 80 + (pygame.mouse.get_pos()[0] / self.width) * 160
                        print(f"Tempo changed to: {self.tempo:.1f} BPM")
                
                # Get current music features
                music_features = self.get_current_music_features()
                music_features['mood'] = self.mood  # Override with manual mood
                
                # Update systems
                self.update_particles(music_features)
                
                # Update dancers
                for dancer in self.dancers:
                    dancer.update_dance_move(music_features, self.current_time)
                
                # Draw everything
                self.draw_background(music_features)
                self.draw_audio_visualization(music_features)
                self.draw_particles()
                
                # Draw dancers
                for dancer in self.dancers:
                    dancer.draw(self.screen)
                
                # Draw UI
                font = pygame.font.Font(None, 36)
                info_text = f"Tempo: {music_features.get('tempo', 0):.1f} BPM | Energy: {music_features.get('energy', 0):.2f} | Mood: {music_features.get('mood', 'unknown')}"
                text_surface = font.render(info_text, True, (255, 255, 255))
                self.screen.blit(text_surface, (20, 20))
                
                # Draw style labels
                font_small = pygame.font.Font(None, 24)
                styles = ["Human", "Abstract", "Robot", "Hip-Hop", "Ballet", "Cartoon", "Animal"]
                for i, style in enumerate(styles):
                    if i < len(self.dancers):
                        text_surface = font_small.render(style, True, (200, 200, 200))
                        x = self.dancers[i].x - 25
                        y = self.dancers[i].y + 80
                        self.screen.blit(text_surface, (x, y))
                
                # Draw controls
                font_small = pygame.font.Font(None, 24)
                controls = ["SPACE: Play/Pause", "ESC: Exit", "Click: Tempo", "Arrows: Mood"]
                for i, control in enumerate(controls):
                    text_surface = font_small.render(control, True, (180, 180, 180))
                    self.screen.blit(text_surface, (20, self.height - 120 + i * 25))
                
                pygame.display.flip()
                self.clock.tick(60)
                
        except Exception as e:
            print(f"Error during execution: {e}")
            import traceback
            traceback.print_exc()
        finally:
            print("Shutting down...")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    try:
        visualizer = EnhancedDanceVisualizer()
        visualizer.run()
    except Exception as e:
        print(f"Failed to start visualizer: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")