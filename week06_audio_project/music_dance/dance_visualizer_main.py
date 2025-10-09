import pygame
import numpy as np
import librosa
import sys
import math
from music_analyzer import MusicAnalyzer
from dancer import Dancer

class DanceVisualizer:
    def __init__(self, width=1200, height=800):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("AI Music Visual Dance")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        
        self.music_analyzer = MusicAnalyzer()
        self.dancers = []
        self.current_time = 0
        self.is_playing = False
        
        # Create multiple dancers with different styles
        self.create_dancers()
        
        # Visualization elements
        self.spectrum_bars = []
        self.beat_circles = []
        
    def create_dancers(self):
        """Create dancers with more styles"""
        styles = ["human", "abstract", "robot", "hiphop", "ballet", "cartoon", "animal"]
        positions = [(200, 400), (400, 400), (600, 400), (800, 400), (1000, 400)]
        for i, (x, y) in enumerate(positions):
            style = styles[i % len(styles)]
            dancer = Dancer(x, y, size=40, style=style)
            self.dancers.append(dancer)
        # For multiplayer/AI: self.dancers could be dynamically added
    
    def load_music(self, file_path):
        """Load music file"""
        try:
            self.music_analyzer.load_audio(file_path)
            self.music_analyzer.extract_features()
            
            # Initialize PyGame music playback
            pygame.mixer.music.load(file_path)
            print("Music loaded successfully!")
            return True
        except Exception as e:
            print(f"Music loading failed: {e}")
            return False
    
    def play_music(self):
        """Start playing music"""
        pygame.mixer.music.play()
        self.is_playing = True
        self.start_time = pygame.time.get_ticks()
    
    def get_current_music_features(self):
        """Get music features for current moment"""
        if not self.is_playing:
            return {}
            
        current_time_ms = pygame.time.get_ticks() - self.start_time
        current_time = current_time_ms / 1000.0  # Convert to seconds
        
        # Check if we're on a beat point
        beat_strength = 0
        for beat_time in self.music_analyzer.beat_frames:
            if abs(current_time - beat_time) < 0.1:  # Near beat point
                beat_strength = 1.0
                break
        
        # Simple energy calculation (should be calculated in real-time in actual project)
        energy = 0.5 + 0.3 * math.sin(current_time * 2)
        
        return {
            'tempo': self.music_analyzer.tempo,
            'energy': energy,
            'beat_strength': beat_strength,
            'mood': self.music_analyzer.mood,
            'current_time': current_time
        }
    
    def draw_background(self, music_features):
        """Draw dynamic background with light and particle effects"""
        # Change background color based on music mood
        mood_colors = {
            "energetic": (50, 50, 100),
            "happy": (80, 40, 120), 
            "calm": (30, 60, 90),
            "neutral": (40, 40, 60)
        }
        base_color = mood_colors.get(music_features.get('mood', 'neutral'), (40, 40, 60))
        beat_pulse = music_features.get('beat_strength', 0) * 50
        bg_color = (
            min(255, base_color[0] + beat_pulse),
            min(255, base_color[1] + beat_pulse//2),
            min(255, base_color[2] + beat_pulse)
        )
        self.screen.fill(bg_color)
        # Light effect: radial glow on strong beat
        if music_features.get('beat_strength', 0) > 0.8:
            for i in range(5):
                alpha = 80 - i*15
                radius = 120 + i*30
                s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                pygame.draw.circle(s, (255,255,180,alpha), (self.width//2, self.height//2), radius)
                self.screen.blit(s, (0,0))
        # Particle effect: draw random sparkles on energetic mood
        if music_features.get('mood', '') == 'energetic':
            for _ in range(30):
                px = np.random.randint(0, self.width)
                py = np.random.randint(0, self.height)
                color = (255, 255, np.random.randint(180,255))
                pygame.draw.circle(self.screen, color, (px, py), np.random.randint(1,4))
    
    def draw_audio_visualization(self, music_features):
        """Draw audio visualization with spectrum and glow"""
        num_bars = 32
        for i in range(num_bars):
            bar_height = 100 + 150 * math.sin(self.current_time * 2 + i * 0.2)
            bar_width = self.width // num_bars - 2
            x = i * (bar_width + 2)
            y = self.height - bar_height
            color = (
                100 + int(155 * (i / num_bars)),
                100 + int(80 * abs(math.sin(self.current_time + i))),
                200
            )
            pygame.draw.rect(self.screen, color, (x, y, bar_width, bar_height))
            # Add glow effect
            if i % 8 == 0:
                s = pygame.Surface((bar_width*3, int(bar_height)), pygame.SRCALPHA)
                pygame.draw.ellipse(s, (255,255,180,60), (0,0,bar_width*3,int(bar_height)))
                self.screen.blit(s, (x-bar_width, y-10))
    # Future: AI dance, multiplayer, custom style hooks
    def add_ai_dance_generation(self):
        """Use machine learning to generate dance moves (stub)"""
        pass

    def add_multiplayer(self):
        """Enable multiple dancers to interact (stub)"""
        pass

    def add_custom_dance_styles(self):
        """Allow user to upload custom dance styles (stub)"""
        pass
    
    def run(self):
        """Main loop"""
        running = True
        
        # Load test music (you need to prepare an MP3 file)
        music_loaded = self.load_music("test_music.mp3")
        if not music_loaded:
            print("Please prepare an MP3 file and name it 'test_music.mp3'")
            return
        
        self.play_music()
        
        while running:
            self.current_time = pygame.time.get_ticks() / 1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.is_playing:
                            pygame.mixer.music.pause()
                            self.is_playing = False
                        else:
                            pygame.mixer.music.unpause()  
                            self.is_playing = True
            
            # Get current music features
            music_features = self.get_current_music_features()
            
            # Draw
            self.draw_background(music_features)
            self.draw_audio_visualization(music_features)
            
            # Update and draw dancers
            for dancer in self.dancers:
                dancer.update_dance_move(music_features, self.current_time)
                dancer.draw(self.screen)
            
            # Display information
            font = pygame.font.Font(None, 36)
            info_text = f"Tempo: {music_features.get('tempo', 0):.1f} BPM | Mood: {music_features.get('mood', 'unknown')}"
            text_surface = font.render(info_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (20, 20))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = DanceVisualizer()
    visualizer.run()