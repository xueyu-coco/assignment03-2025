import pygame
import numpy as np
import pyaudio
import threading
import queue
import math
import sys
from scipy.signal import find_peaks
from collections import deque

class RealTimeVoiceDancer:
    def __init__(self, x, y, size=50, style="human"):
        self.x = x
        self.y = y
        self.base_size = size
        self.size = size
        self.style = style
        self.color = (255, 255, 255)
        self.dance_move = "idle"
        self.move_progress = 0
        self.rotation = 0
        self.jump_height = 0
        self.wave_amplitude = 0
        
        # Voice response parameters
        self.volume_sensitivity = 1.0
        self.pitch_sensitivity = 1.0
        self.speech_rate_sensitivity = 1.0
        
    def update_from_voice(self, voice_features):
        """Update dancer based on real-time voice characteristics"""
        volume = voice_features.get('volume', 0)
        pitch = voice_features.get('pitch', 0)
        speech_rate = voice_features.get('speech_rate', 0)
        is_shouting = voice_features.get('is_shouting', False)
        is_high_pitch = voice_features.get('is_high_pitch', False)
        is_fast_speech = voice_features.get('is_fast_speech', False)
        
        # Volume controls size
        self.size = self.base_size + int(volume * 50)
        self.size = max(20, min(120, self.size))
        
        # Loud shouting → spinning and red color
        if is_shouting:
            self.dance_move = "spin"
            self.color = (255, 50, 50)  # Red
            self.rotation += 10
            
        # High pitch → jumping and green color
        elif is_high_pitch:
            self.dance_move = "jump"
            self.color = (50, 255, 50)  # Green
            self.jump_height = min(50, int(pitch * 30))
            
        # Fast speech → waving and blue color
        elif is_fast_speech:
            self.dance_move = "wave"
            self.color = (50, 50, 255)  # Blue
            self.wave_amplitude = min(30, int(speech_rate * 20))
            
        # Low activity → idle and white
        else:
            self.dance_move = "idle"
            self.color = (255, 255, 255)
            
        self.move_progress += 0.15
        
    def draw(self, screen):
        """Draw the dancer with voice-responsive animations"""
        # Calculate current position with animations
        current_x = self.x
        current_y = self.y
        
        if self.dance_move == "jump":
            current_y -= self.jump_height * abs(math.sin(self.move_progress))
        elif self.dance_move == "wave":
            current_x += self.wave_amplitude * math.sin(self.move_progress * 2)
            
        # Draw based on style
        if self.style == "human":
            self.draw_human_dancer(screen, current_x, current_y)
        elif self.style == "abstract":
            self.draw_abstract_dancer(screen, current_x, current_y)
        elif self.style == "robot":
            self.draw_robot_dancer(screen, current_x, current_y)
            
    def draw_human_dancer(self, screen, x, y):
        """Draw human-style dancer with voice animations"""
        # Head
        head_size = max(10, self.size // 3)
        pygame.draw.circle(screen, self.color, (int(x), int(y - self.size)), head_size)
        
        # Body
        body_height = self.size
        body_width = self.size // 3
        pygame.draw.rect(screen, self.color, 
                        (int(x - body_width//2), int(y - self.size//2), 
                         body_width, body_height))
        
        # Arms with animations
        arm_length = self.size * 0.6
        if self.dance_move == "wave":
            arm_angle = math.sin(self.move_progress * 3) * 1.5
        elif self.dance_move == "spin":
            arm_angle = self.move_progress * 2
        else:
            arm_angle = 0.3
            
        left_arm_x = x - math.cos(arm_angle) * arm_length
        left_arm_y = y - self.size//4 + math.sin(arm_angle) * arm_length
        right_arm_x = x + math.cos(arm_angle) * arm_length
        right_arm_y = y - self.size//4 + math.sin(arm_angle) * arm_length
        
        pygame.draw.line(screen, self.color, (x, y - self.size//4), 
                        (left_arm_x, left_arm_y), max(2, self.size//15))
        pygame.draw.line(screen, self.color, (x, y - self.size//4), 
                        (right_arm_x, right_arm_y), max(2, self.size//15))
        
        # Legs
        leg_length = self.size * 0.8
        leg_angle = math.sin(self.move_progress) * 0.5
        
        left_leg_x = x - math.cos(leg_angle) * leg_length//2
        left_leg_y = y + self.size//2 + math.sin(leg_angle) * leg_length//2
        right_leg_x = x + math.cos(leg_angle) * leg_length//2
        right_leg_y = y + self.size//2 + math.sin(leg_angle) * leg_length//2
        
        pygame.draw.line(screen, self.color, (x, y + self.size//2), 
                        (left_leg_x, left_leg_y), max(3, self.size//12))
        pygame.draw.line(screen, self.color, (x, y + self.size//2), 
                        (right_leg_x, right_leg_y), max(3, self.size//12))
    
    def draw_abstract_dancer(self, screen, x, y):
        """Draw abstract-style dancer"""
        points = []
        num_points = 8
        for i in range(num_points):
            angle = i * 2 * math.pi / num_points + self.move_progress
            radius = self.size * (0.8 + 0.4 * math.sin(self.move_progress + i))
            px = x + math.cos(angle) * radius
            py = y + math.sin(angle) * radius
            points.append((px, py))
        
        if len(points) >= 3:
            pygame.draw.polygon(screen, self.color, points)
    
    def draw_robot_dancer(self, screen, x, y):
        """Draw robot-style dancer"""
        # Body
        body_rect = pygame.Rect(x - self.size//2, y - self.size, self.size, self.size*1.5)
        pygame.draw.rect(screen, self.color, body_rect)
        
        # Head
        head_size = self.size//2
        head_rect = pygame.Rect(x - head_size//2, y - self.size*1.5, head_size, head_size)
        pygame.draw.rect(screen, self.color, head_rect)
        
        # Mechanical joints
        joint_offset = math.sin(self.move_progress * 3) * 8
        pygame.draw.circle(screen, (255, 255, 255), 
                          (int(x), int(y - self.size//2 + joint_offset)), 6)


class VoiceDanceController:
    def __init__(self, width=1200, height=800):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Real-Time Voice Dance Controller")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        
        # Audio settings
        self.sample_rate = 44100
        self.chunk_size = 4096
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
        
        # Voice analysis parameters
        self.audio_buffer = deque(maxlen=10)  # Store last 10 chunks
        self.volume_history = deque(maxlen=30)  # Volume history
        self.pitch_history = deque(maxlen=20)   # Pitch history
        self.speech_rate_history = deque(maxlen=15)  # Speech rate history
        
        # Thresholds for voice characteristics
        self.shout_threshold = 0.3
        self.high_pitch_threshold = 300  # Hz
        self.fast_speech_threshold = 0.5
        
        # Create dancers
        self.dancers = []
        self.create_dancers()
        
        # Background and effects
        self.background_color = [30, 30, 50]
        self.current_time = 0
        
    def create_dancers(self):
        """Create multiple dancers with different styles"""
        styles = ["human", "abstract", "robot"]
        positions = [(300, 400), (600, 400), (900, 400)]
        
        for i, (x, y) in enumerate(positions):
            style = styles[i % len(styles)]
            dancer = RealTimeVoiceDancer(x, y, size=50, style=style)
            self.dancers.append(dancer)
    
    def analyze_audio_chunk(self, audio_data):
        """Analyze audio chunk for voice characteristics"""
        if len(audio_data) == 0:
            return {}
            
        # Convert to numpy array
        audio_array = np.frombuffer(audio_data, dtype=np.float32)
        
        # Volume analysis
        volume = np.sqrt(np.mean(audio_array**2))  # RMS volume
        volume = min(1.0, volume * 5)  # Normalize and boost
        
        # Pitch detection using autocorrelation
        pitch = self.detect_pitch(audio_array)
        
        # Speech rate detection (zero crossing rate)
        speech_rate = self.detect_speech_rate(audio_array)
        
        # Store in history
        self.volume_history.append(volume)
        if pitch > 0:
            self.pitch_history.append(pitch)
        self.speech_rate_history.append(speech_rate)
        
        # Determine voice characteristics
        is_shouting = volume > self.shout_threshold
        is_high_pitch = pitch > self.high_pitch_threshold if pitch > 0 else False
        is_fast_speech = speech_rate > self.fast_speech_threshold
        
        return {
            'volume': volume,
            'pitch': pitch,
            'speech_rate': speech_rate,
            'is_shouting': is_shouting,
            'is_high_pitch': is_high_pitch,
            'is_fast_speech': is_fast_speech
        }
    
    def detect_pitch(self, audio_data):
        """Detect fundamental frequency using autocorrelation"""
        try:
            # Apply window to reduce edge effects
            windowed = audio_data * np.hanning(len(audio_data))
            
            # Autocorrelation
            autocorr = np.correlate(windowed, windowed, mode='full')
            autocorr = autocorr[autocorr.size // 2:]
            
            # Find peaks in autocorrelation
            min_period = int(self.sample_rate / 800)  # 800 Hz max
            max_period = int(self.sample_rate / 80)   # 80 Hz min
            
            autocorr_segment = autocorr[min_period:max_period]
            if len(autocorr_segment) > 0:
                peak_index = np.argmax(autocorr_segment) + min_period
                if autocorr[peak_index] > 0.1 * autocorr[0]:  # Threshold
                    frequency = self.sample_rate / peak_index
                    return frequency
            
            return 0
        except:
            return 0
    
    def detect_speech_rate(self, audio_data):
        """Detect speech rate using zero crossing rate"""
        try:
            # Zero crossing rate
            zero_crossings = np.sum(np.abs(np.diff(np.sign(audio_data))))
            zcr = zero_crossings / len(audio_data)
            return min(1.0, zcr * 10)  # Normalize
        except:
            return 0
    
    def update_background(self, voice_features):
        """Update background color based on voice activity"""
        volume = voice_features.get('volume', 0)
        is_shouting = voice_features.get('is_shouting', False)
        is_high_pitch = voice_features.get('is_high_pitch', False)
        is_fast_speech = voice_features.get('is_fast_speech', False)
        
        # Base color
        target_color = [30, 30, 50]
        
        # Modify based on voice characteristics
        if is_shouting:
            target_color = [80 + int(volume * 100), 20, 20]  # Red background
        elif is_high_pitch:
            target_color = [20, 80 + int(volume * 100), 20]  # Green background
        elif is_fast_speech:
            target_color = [20, 20, 80 + int(volume * 100)]  # Blue background
        else:
            intensity = int(volume * 80)
            target_color = [30 + intensity, 30 + intensity, 50 + intensity]
        
        # Smooth transition
        for i in range(3):
            self.background_color[i] += (target_color[i] - self.background_color[i]) * 0.1
    
    def draw_voice_visualization(self, voice_features):
        """Draw real-time voice analysis visualization"""
        volume = voice_features.get('volume', 0)
        pitch = voice_features.get('pitch', 0)
        speech_rate = voice_features.get('speech_rate', 0)
        
        # Volume bar
        volume_bar_width = int(volume * 400)
        pygame.draw.rect(self.screen, (255, 255, 255), 
                        (50, 50, volume_bar_width, 20))
        pygame.draw.rect(self.screen, (100, 100, 100), 
                        (50, 50, 400, 20), 2)
        
        # Pitch indicator
        if pitch > 0:
            pitch_y = 150 - int((pitch - 80) / 400 * 80)  # Map 80-480 Hz to y position
            pitch_y = max(70, min(150, pitch_y))
            pygame.draw.circle(self.screen, (255, 255, 0), (100, pitch_y), 8)
        
        # Speech rate bar
        speech_rate_width = int(speech_rate * 200)
        pygame.draw.rect(self.screen, (0, 255, 255), 
                        (50, 180, speech_rate_width, 15))
        pygame.draw.rect(self.screen, (100, 100, 100), 
                        (50, 180, 200, 15), 2)
        
        # Labels
        font = pygame.font.Font(None, 24)
        labels = [
            f"Volume: {volume:.2f} {'(SHOUTING!)' if voice_features.get('is_shouting') else ''}",
            f"Pitch: {pitch:.0f} Hz {'(HIGH!)' if voice_features.get('is_high_pitch') else ''}",
            f"Speech Rate: {speech_rate:.2f} {'(FAST!)' if voice_features.get('is_fast_speech') else ''}"
        ]
        
        for i, label in enumerate(labels):
            color = (255, 255, 255)
            if "!" in label:
                color = (255, 255, 0)
            text_surface = font.render(label, True, color)
            self.screen.blit(text_surface, (300, 50 + i * 30))
    
    def draw_instructions(self):
        """Draw usage instructions"""
        font = pygame.font.Font(None, 28)
        instructions = [
            "Real-Time Voice Dance Controller",
            "",
            "Voice Actions:",
            "🗣️  SHOUT LOUDLY → Dancers spin and turn RED",
            "🎵  HIGH PITCH voice → Dancers jump and turn GREEN", 
            "⚡  FAST SPEECH → Dancers wave and turn BLUE",
            "📏  VOLUME controls dancer size",
            "",
            "Try different voice styles and watch the dancers respond!"
        ]
        
        for i, instruction in enumerate(instructions):
            color = (255, 255, 255)
            if "→" in instruction:
                color = (255, 255, 150)
            elif instruction.startswith("Real-Time"):
                color = (150, 255, 150)
                
            text_surface = font.render(instruction, True, color)
            self.screen.blit(text_surface, (50, 250 + i * 35))
    
    def run(self):
        """Main loop"""
        print("Starting Real-Time Voice Dance Controller...")
        print("🎤 Microphone calibration...")
        
        # Calibrate microphone
        calibration_frames = 20
        noise_samples = []
        for _ in range(calibration_frames):
            try:
                audio_data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                audio_array = np.frombuffer(audio_data, dtype=np.float32)
                noise_level = np.sqrt(np.mean(audio_array**2))
                noise_samples.append(noise_level)
            except:
                continue
        
        if noise_samples:
            avg_noise = np.mean(noise_samples)
            self.shout_threshold = max(0.1, avg_noise * 10)
            print(f"🎤 Calibration complete. Noise level: {avg_noise:.4f}")
            print(f"🎤 Shout threshold: {self.shout_threshold:.4f}")
        
        print("🎤 Voice controller is active!")
        print("💡 Try: shouting, high-pitch sounds, fast speech!")
        
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
                            # Recalibrate microphone
                            print("🎤 Recalibrating microphone...")
                
                # Read audio
                try:
                    audio_data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                    voice_features = self.analyze_audio_chunk(audio_data)
                except:
                    voice_features = {}
                
                # Update background
                self.update_background(voice_features)
                
                # Update dancers
                for dancer in self.dancers:
                    dancer.update_from_voice(voice_features)
                
                # Draw everything
                bg_color = [int(c) for c in self.background_color]
                self.screen.fill(bg_color)
                
                # Draw dancers
                for dancer in self.dancers:
                    dancer.draw(self.screen)
                
                # Draw visualizations
                self.draw_voice_visualization(voice_features)
                self.draw_instructions()
                
                pygame.display.flip()
                self.clock.tick(60)
                
        except KeyboardInterrupt:
            print("\n🎤 Voice controller stopped by user")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            # Cleanup
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    try:
        controller = VoiceDanceController()
        controller.run()
    except Exception as e:
        print(f"❌ Failed to start voice dance controller: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")