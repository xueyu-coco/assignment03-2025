import speech_recognition as sr
import threading
import queue
import pygame
import numpy as np
import pyaudio
import math
import sys
import time

class VoiceDanceController:
    """Base class for voice-controlled dancing"""
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Voice Command Dancer")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        
        # Audio setup for voice input
        self.audio = pyaudio.PyAudio()
        self.chunk = 512
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        
        self.current_time = 0
        self.dancers = []
        self.create_dancers()
        
    def create_dancers(self):
        """Create initial dancers"""
        positions = [(200, 300), (400, 300), (600, 300)]
        for i, (x, y) in enumerate(positions):
            dancer = {
                'x': x, 'y': y, 'size': 60, 'color': (255, 255, 255),
                'dance_move': 'idle', 'move_progress': 0, 'style': 'human'
            }
            self.dancers.append(dancer)
    
    def get_voice_features(self):
        """Get current voice input features"""
        try:
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)
            
            # Safe volume calculation with NaN protection
            if len(audio_data) > 0:
                mean_square = np.mean(audio_data**2)
                if mean_square > 0 and not np.isnan(mean_square):
                    volume = np.sqrt(mean_square) / 32768.0
                    volume = min(volume * 5.0, 1.0)  # Amplify sensitivity
                else:
                    volume = 0.0
            else:
                volume = 0.0
            
            # Ensure volume is a valid number
            if np.isnan(volume) or np.isinf(volume):
                volume = 0.0
            
            return {
                'volume': float(volume),
                'energy': float(volume),
                'beat_strength': 1.0 if volume > 0.3 else 0.0
            }
        except Exception as e:
            return {'volume': 0.0, 'energy': 0.0, 'beat_strength': 0.0}
    
    def update_dance_with_voice(self):
        """Update dance based on voice input"""
        voice_features = self.get_voice_features()
        
        for dancer in self.dancers:
            dancer['move_progress'] += 0.1
            
            # React to voice volume
            if voice_features['volume'] > 0.2:
                if dancer['dance_move'] == 'idle':
                    dancer['dance_move'] = 'wave'
                    dancer['move_progress'] = 0
    
    def draw_dancer(self, dancer):
        """Draw a single dancer"""
        x, y = dancer['x'], dancer['y']
        size = dancer['size']
        color = dancer['color']
        move = dancer['dance_move']
        progress = dancer['move_progress']
        
        # Head
        pygame.draw.circle(self.screen, color, (int(x), int(y - size)), size//3)
        
        # Body
        pygame.draw.rect(self.screen, color, (int(x - size//6), int(y - size//2), size//3, size))
        
        # Animated limbs based on dance move
        if move == 'wave':
            arm_angle = math.sin(progress * 3) * 1.2
        elif move == 'spin':
            arm_angle = progress * 2
        elif move == 'jump':
            arm_angle = math.sin(progress * 4) * 0.8
            y -= abs(math.sin(progress * 4)) * 20
        else:  # idle
            arm_angle = 0.3
        
        # Arms
        arm_length = size * 0.6
        left_arm_x = x - math.cos(arm_angle) * arm_length
        left_arm_y = y - size//4 + math.sin(arm_angle) * arm_length
        right_arm_x = x + math.cos(arm_angle) * arm_length
        right_arm_y = y - size//4 + math.sin(arm_angle) * arm_length
        
        pygame.draw.line(self.screen, color, (x, y - size//4), (left_arm_x, left_arm_y), 4)
        pygame.draw.line(self.screen, color, (x, y - size//4), (right_arm_x, right_arm_y), 4)
        
        # Legs
        leg_angle = math.sin(progress * 2 + 1) * 0.5
        leg_length = size * 0.8
        left_leg_x = x - math.cos(leg_angle) * leg_length
        left_leg_y = y + size//2 + abs(math.sin(leg_angle)) * leg_length
        right_leg_x = x + math.cos(leg_angle) * leg_length
        right_leg_y = y + size//2 + abs(math.sin(leg_angle)) * leg_length
        
        pygame.draw.line(self.screen, color, (x, y + size//2), (left_leg_x, left_leg_y), 5)
        pygame.draw.line(self.screen, color, (x, y + size//2), (right_leg_x, right_leg_y), 5)
    
    def draw_combined_visualization(self, voice_features):
        """Draw background and voice visualization"""
        # Background based on voice input with safe conversion
        volume = voice_features.get('volume', 0.0)
        
        # Ensure volume is a valid number
        if np.isnan(volume) or np.isinf(volume):
            volume = 0.0
        
        bg_color = (
            max(0, min(255, int(30 + volume * 100))),
            max(0, min(255, int(40 + volume * 80))),
            max(0, min(255, int(60 + volume * 120)))
        )
        self.screen.fill(bg_color)
        
        # Voice volume bars
        num_bars = 20
        for i in range(num_bars):
            bar_height = 50 + volume * 200 * math.sin(self.current_time * 2 + i * 0.3)
            bar_width = self.width // num_bars - 2
            x = i * (bar_width + 2)
            y = self.height - abs(bar_height)
            
            color = (
                max(0, min(255, int(100 + 155 * volume))), 
                100, 
                200
            )
            pygame.draw.rect(self.screen, color, (x, y, bar_width, abs(bar_height)))
        
        # Draw all dancers
        for dancer in self.dancers:
            self.draw_dancer(dancer)


class VoiceCommandDancer(VoiceDanceController):
    """Voice command controlled dancer with speech recognition"""
    
    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.command_queue = queue.Queue()
        self.listening = True
        
        # Calibrate microphone for ambient noise
        print("Calibrating microphone for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Calibration complete!")
        
        # Start speech recognition thread
        self.speech_thread = threading.Thread(target=self.listen_commands)
        self.speech_thread.daemon = True
        self.speech_thread.start()
        
        # English voice commands
        self.commands = {
            "dance": "dance",
            "spin": "spin", 
            "jump": "jump",
            "stop": "stop",
            "bigger": "bigger",
            "smaller": "smaller",
            "red": "red",
            "blue": "blue",
            "green": "green",
            "yellow": "yellow",
            "white": "white",
            "wave": "wave",
            "move": "dance",
            "rotate": "spin",
            "leap": "jump",
            "halt": "stop",
            "large": "bigger",
            "small": "smaller",
            "tiny": "smaller"
        }
        
        print("Voice Command Dancer initialized!")
        print("Available commands:", list(self.commands.keys()))
    
    def listen_commands(self):
        """Listen for voice commands continuously"""
        while self.listening:
            try:
                with self.microphone as source:
                    print("Listening for commands...")
                    # Listen with shorter timeout and phrase limit
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=2)
                
                # Recognize speech in English
                try:
                    command = self.recognizer.recognize_google(audio, language='en-US')
                    command = command.lower()
                    print(f"Recognized command: {command}")
                    
                    # Check for matching commands
                    for key, action in self.commands.items():
                        if key in command:
                            self.command_queue.put(action)
                            print(f"Command matched: {key} -> {action}")
                            break
                    else:
                        print("No matching command found")
                        
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Speech recognition service error: {e}")
                        
            except sr.WaitTimeoutError:
                # Normal timeout, continue listening
                pass
            except Exception as e:
                print(f"Speech recognition error: {e}")
                time.sleep(0.1)
    
    def process_voice_commands(self):
        """Process voice command queue"""
        try:
            while not self.command_queue.empty():
                command = self.command_queue.get_nowait()
                self.execute_command(command)
        except queue.Empty:
            pass
    
    def execute_command(self, command):
        """Execute voice command on all dancers"""
        print(f"Executing command: {command}")
        
        for dancer in self.dancers:
            if command == "dance":
                dancer['dance_move'] = "wave"
                dancer['move_progress'] = 0
            elif command == "spin":
                dancer['dance_move'] = "spin"
                dancer['move_progress'] = 0
            elif command == "jump":
                dancer['dance_move'] = "jump"
                dancer['move_progress'] = 0
            elif command == "stop":
                dancer['dance_move'] = "idle"
            elif command == "bigger":
                dancer['size'] = min(120, dancer['size'] + 15)
            elif command == "smaller":
                dancer['size'] = max(30, dancer['size'] - 15)
            elif command == "red":
                dancer['color'] = (255, 80, 80)
            elif command == "blue":
                dancer['color'] = (80, 80, 255)
            elif command == "green":
                dancer['color'] = (80, 255, 80)
            elif command == "yellow":
                dancer['color'] = (255, 255, 80)
            elif command == "white":
                dancer['color'] = (255, 255, 255)
    
    def run(self):
        """Main loop with voice command processing"""
        running = True
        
        self.stream.start_stream()
        print("\n" + "="*60)
        print("🎤 VOICE COMMAND DANCER SYSTEM STARTED! 🎤")
        print("="*60)
        print("Try saying commands like:")
        print("  Movement: 'dance', 'spin', 'jump', 'stop'")
        print("  Size: 'bigger', 'smaller'")
        print("  Colors: 'red', 'blue', 'green', 'yellow', 'white'")
        print("  Alternative words: 'move', 'rotate', 'leap', 'halt'")
        print("="*60)
        
        while running:
            self.current_time = pygame.time.get_ticks() / 1000.0
            
            # Handle pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        # Manual test command
                        self.command_queue.put("dance")
            
            # Process voice commands
            self.process_voice_commands()
            
            # Update dance with voice input
            self.update_dance_with_voice()
            
            # Draw everything
            voice_features = self.get_voice_features()
            self.draw_combined_visualization(voice_features)
            
            # Draw command hints and status
            self.draw_command_interface(voice_features)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        # Cleanup
        self.listening = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        pygame.quit()
        sys.exit()
    
    def draw_command_interface(self, voice_features):
        """Draw voice command interface and status"""
        font_large = pygame.font.Font(None, 32)
        font_medium = pygame.font.Font(None, 24)
        font_small = pygame.font.Font(None, 20)
        
        # Title
        title_text = font_large.render("🎤 Voice Command Dancer", True, (255, 255, 255))
        self.screen.blit(title_text, (20, 20))
        
        # Voice level indicator
        volume = voice_features.get('volume', 0)
        volume_text = f"Voice Level: {volume:.2f}"
        volume_color = (255, 255, 255) if volume < 0.1 else (255, 255, 0) if volume < 0.3 else (255, 100, 100)
        vol_surface = font_medium.render(volume_text, True, volume_color)
        self.screen.blit(vol_surface, (20, 60))
        
        # Voice level bar
        bar_width = 200
        bar_height = 10
        pygame.draw.rect(self.screen, (100, 100, 100), (20, 85, bar_width, bar_height))
        pygame.draw.rect(self.screen, volume_color, (20, 85, int(bar_width * volume), bar_height))
        
        # Command categories
        y_offset = 120
        categories = [
            ("Movement Commands:", ["dance", "spin", "jump", "stop"]),
            ("Size Commands:", ["bigger", "smaller"]),
            ("Color Commands:", ["red", "blue", "green", "yellow", "white"]),
            ("Alternative Words:", ["move", "rotate", "leap", "halt"])
        ]
        
        for category, commands in categories:
            cat_surface = font_medium.render(category, True, (200, 255, 200))
            self.screen.blit(cat_surface, (20, y_offset))
            y_offset += 25
            
            cmd_text = ", ".join(commands)
            cmd_surface = font_small.render(cmd_text, True, (180, 180, 180))
            self.screen.blit(cmd_surface, (40, y_offset))
            y_offset += 30
        
        # Controls
        controls = [
            "ESC: Exit",
            "SPACE: Test dance command",
            "Speak clearly into microphone"
        ]
        
        for i, control in enumerate(controls):
            control_surface = font_small.render(control, True, (150, 150, 255))
            self.screen.blit(control_surface, (20, self.height - 80 + i * 20))
        
        # Dancer info
        dancer_info = f"Dancers: {len(self.dancers)} | Active moves: {sum(1 for d in self.dancers if d['dance_move'] != 'idle')}"
        info_surface = font_small.render(dancer_info, True, (255, 255, 255))
        self.screen.blit(info_surface, (self.width - 300, 20))


# Test the voice command system
if __name__ == "__main__":
    try:
        print("Initializing Voice Command Dancer...")
        print("Make sure you have a working microphone!")
        
        # Check if microphone is available
        import speech_recognition as sr
        r = sr.Recognizer()
        mic_list = sr.Microphone.list_microphone_names()
        print(f"Available microphones: {len(mic_list)}")
        
        if len(mic_list) == 0:
            print("No microphones detected! Please connect a microphone.")
            input("Press Enter to exit...")
            sys.exit()
        
        dancer = VoiceCommandDancer()
        dancer.run()
        
    except ImportError as e:
        print(f"Missing required package: {e}")
        print("Please install: pip install SpeechRecognition pyaudio")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"Error starting voice command dancer: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")