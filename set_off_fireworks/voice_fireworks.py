import pygame
import numpy as np
import pyaudio
import threading
import queue
import math
import random
import time
from collections import deque

class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(20, 40)
        self.color = random.choice([
            (150, 0, 0),      # Dark red
            (0, 100, 0),      # Dark green  
            (100, 0, 100),    # Purple
            (100, 100, 0),    # Dark yellow
            (0, 0, 150)       # Dark blue
        ])
        self.speed = random.uniform(0.5, 2.0)
        self.direction = random.uniform(0, 2 * math.pi)
        self.health = 1
        self.alive = True
        self.blink_timer = 0
        self.spawn_time = time.time()
        self.last_attack_time = 0
        self.attack_cooldown = random.uniform(2.0, 5.0)  # Random attack interval
        
    def update(self, screen_width, screen_height):
        """Update monster position and behavior"""
        if not self.alive:
            return
            
        # Move monster
        self.x += math.cos(self.direction) * self.speed
        self.y += math.sin(self.direction) * self.speed
        
        # Bounce off screen edges
        if self.x <= self.size or self.x >= screen_width - self.size:
            self.direction = math.pi - self.direction
        if self.y <= self.size or self.y >= screen_height - self.size:
            self.direction = -self.direction
            
        # Keep within bounds
        self.x = max(self.size, min(screen_width - self.size, self.x))
        self.y = max(self.size, min(screen_height - self.size, self.y))
        
        # Occasionally change direction for unpredictable movement
        if random.random() < 0.02:
            self.direction += random.uniform(-0.5, 0.5)
            
        self.blink_timer += 1
        
    def draw(self, screen):
        """Draw the monster with evil eyes"""
        if not self.alive:
            return
            
        # Main body (pulsing effect)
        pulse = 1 + 0.1 * math.sin(self.blink_timer * 0.1)
        current_size = int(self.size * pulse)
        
        # Monster body
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), current_size)
        
        # Evil eyes
        eye_offset = current_size // 3
        eye_size = max(3, current_size // 8)
        
        # Left eye
        pygame.draw.circle(screen, (255, 0, 0), 
                         (int(self.x - eye_offset), int(self.y - eye_offset)), eye_size)
        # Right eye  
        pygame.draw.circle(screen, (255, 0, 0),
                         (int(self.x + eye_offset), int(self.y - eye_offset)), eye_size)
        
        # Mouth (evil grin)
        mouth_points = [
            (int(self.x - eye_offset), int(self.y + eye_offset)),
            (int(self.x), int(self.y + eye_offset + 5)),
            (int(self.x + eye_offset), int(self.y + eye_offset))
        ]
        pygame.draw.polygon(screen, (0, 0, 0), mouth_points)
        
    def check_collision(self, firework):
        """Check if firework explosion hits this monster"""
        if not self.alive or not firework.exploded:
            return False
            
        # Check distance to explosion center
        distance = math.sqrt((self.x - firework.target_x)**2 + (self.y - firework.target_y)**2)
        explosion_radius = firework.explosion_size
        
        return distance < explosion_radius + self.size
        
    def take_damage(self):
        """Monster takes damage and dies"""
        self.alive = False
    
    def should_attack(self, current_time):
        """Check if monster should attack player"""
        return (self.alive and 
                current_time - self.last_attack_time > self.attack_cooldown)
    
    def attack_player(self, player_x, player_y, current_time):
        """Create fireball aimed at player"""
        if self.should_attack(current_time):
            self.last_attack_time = current_time
            self.attack_cooldown = random.uniform(3.0, 6.0)  # Reset cooldown
            return Fireball(self.x, self.y, player_x, player_y)
        return None

class Fireball:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 3.0
        self.size = 8
        self.color = (255, 100, 0)  # Orange-red fireball
        self.trail = []
        self.alive = True
        
        # Calculate direction
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx*dx + dy*dy)
        if distance > 0:
            self.vel_x = (dx / distance) * self.speed
            self.vel_y = (dy / distance) * self.speed
        else:
            self.vel_x = 0
            self.vel_y = 0
    
    def update(self, screen_width, screen_height):
        """Update fireball position"""
        if not self.alive:
            return
            
        # Add current position to trail
        self.trail.append((self.x, self.y))
        if len(self.trail) > 10:
            self.trail.pop(0)
            
        # Move fireball
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Check if fireball is off screen
        if (self.x < -50 or self.x > screen_width + 50 or 
            self.y < -50 or self.y > screen_height + 50):
            self.alive = False
    
    def draw(self, screen):
        """Draw fireball with trail effect"""
        if not self.alive:
            return
            
        # Draw trail
        for i, (trail_x, trail_y) in enumerate(self.trail):
            alpha = (i + 1) / len(self.trail)
            trail_size = int(self.size * alpha * 0.7)
            trail_color = (int(255 * alpha), int(100 * alpha), 0)
            if trail_size > 0:
                pygame.draw.circle(screen, trail_color, (int(trail_x), int(trail_y)), trail_size)
        
        # Draw main fireball
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        # Inner glow
        pygame.draw.circle(screen, (255, 255, 100), (int(self.x), int(self.y)), self.size // 2)
    
    def check_collision_with_firework(self, firework):
        """Check collision with firework explosion"""
        if not self.alive or not firework.exploded:
            return False
            
        distance = math.sqrt((self.x - firework.target_x)**2 + (self.y - firework.target_y)**2)
        return distance < firework.explosion_size + self.size
    
    def check_collision_with_player(self, player_x, player_y, player_radius=30):
        """Check collision with player area (bottom center)"""
        if not self.alive:
            return False
            
        distance = math.sqrt((self.x - player_x)**2 + (self.y - player_y)**2)
        return distance < player_radius + self.size

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
        
        # Play launch sound when firework is created
        self.play_launch_sound()
        
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
        """Create explosion particles and intercept fireballs"""
        # Generate and play explosion sound
        self.play_explosion_sound()
        
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
    
    def intercept_fireballs(self, fireballs):
        """Check if this firework explosion can intercept any fireballs"""
        if not self.exploded:
            return []
            
        intercepted_fireballs = []
        for fireball in fireballs:
            if not fireball.alive:
                continue
                
            # Calculate distance from explosion center to fireball
            distance = math.sqrt((fireball.x - self.target_x)**2 + (fireball.y - self.target_y)**2)
            
            # If fireball is within explosion radius, intercept it
            if distance <= self.explosion_size + fireball.size:
                intercepted_fireballs.append(fireball)
                fireball.alive = False
                
        return intercepted_fireballs
    
    def play_launch_sound(self):
        """Generate and play launch sound when firework is fired"""
        try:
            # Generate launch/whoosh sound
            sample_rate = 22050
            duration = 0.8 + self.size_multiplier * 0.4  # Launch sound duration
            
            # Create time array
            t = np.linspace(0, duration, int(sample_rate * duration))
            
            # Generate launch sound components based on size
            if self.size_multiplier < 0.5:
                # Small firework launch
                base_freq = 80 + random.randint(0, 40)
                sweep_range = 60
                noise_intensity = 0.2
            elif self.size_multiplier < 1.0:
                # Medium firework launch
                base_freq = 60 + random.randint(0, 30)
                sweep_range = 80
                noise_intensity = 0.3
            else:
                # Large firework launch
                base_freq = 40 + random.randint(0, 20)
                sweep_range = 100
                noise_intensity = 0.4
            
            # Create frequency sweep (whoosh effect)
            frequency_sweep = base_freq + sweep_range * np.exp(-3 * t)
            
            # Generate whoosh sound with frequency sweep
            whoosh_wave = np.sin(2 * np.pi * frequency_sweep * t)
            
            # Add pink noise for realistic launch texture
            noise = np.random.normal(0, noise_intensity, len(t))
            
            # Combine whoosh and noise
            launch_wave = 0.7 * whoosh_wave + 0.3 * noise
            
            # Apply launch envelope (quick attack, gradual decay)
            attack_time = 0.1
            attack_samples = int(sample_rate * attack_time)
            
            envelope = np.ones_like(t)
            # Quick attack
            envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
            # Gradual decay
            envelope[attack_samples:] = np.exp(-2 * (t[attack_samples:] - attack_time))
            
            launch_wave *= envelope
            
            # Add subtle crackle for larger launches
            if self.size_multiplier > 0.6:
                crackle_freq = 400 + random.randint(0, 200)
                crackle = 0.15 * np.sin(2 * np.pi * crackle_freq * t) * np.random.choice([0, 1], len(t), p=[0.8, 0.2])
                launch_wave += crackle * envelope
            
            # Normalize and convert to pygame format
            launch_wave = np.clip(launch_wave, -1, 1)
            launch_wave = (launch_wave * 32767).astype(np.int16)
            
            # Create stereo sound
            stereo_wave = np.column_stack((launch_wave, launch_wave))
            
            # Play the launch sound
            launch_sound = pygame.sndarray.make_sound(stereo_wave)
            launch_volume = min(0.6, 0.2 + self.size_multiplier * 0.4)  # Volume based on size
            launch_sound.set_volume(launch_volume)
            launch_sound.play()
            
        except Exception as e:
            # If sound generation fails, continue without sound
            print(f"Launch sound generation error: {e}")
            pass
    
    def play_explosion_sound(self):
        """Generate and play explosion sound based on firework size"""
        try:
            # Generate explosion sound based on size
            sample_rate = 22050
            duration = 0.5 + self.size_multiplier * 0.3  # Bigger fireworks = longer sound
            
            # Create time array
            t = np.linspace(0, duration, int(sample_rate * duration))
            
            # Generate explosion sound components
            if self.size_multiplier < 0.5:
                # Small firework - higher pitch, shorter
                frequency = 150 + random.randint(0, 100)
                noise_intensity = 0.3
                fade_speed = 8
            elif self.size_multiplier < 1.0:
                # Medium firework
                frequency = 100 + random.randint(0, 80)
                noise_intensity = 0.5
                fade_speed = 6
            else:
                # Large firework - lower pitch, longer, more intense
                frequency = 60 + random.randint(0, 60)
                noise_intensity = 0.7
                fade_speed = 4
            
            # Create explosion sound with multiple components
            # Base explosion (sine wave with rapid decay)
            base_wave = np.sin(2 * np.pi * frequency * t)
            
            # Add harmonics for richness
            harmonic1 = 0.5 * np.sin(2 * np.pi * frequency * 2 * t)
            harmonic2 = 0.3 * np.sin(2 * np.pi * frequency * 3 * t)
            
            # Add noise for realistic explosion texture
            noise = np.random.normal(0, noise_intensity, len(t))
            
            # Combine components
            sound_wave = base_wave + harmonic1 + harmonic2 + noise
            
            # Apply exponential decay envelope
            envelope = np.exp(-fade_speed * t)
            sound_wave *= envelope
            
            # Add crackle effect for larger fireworks
            if self.size_multiplier > 0.7:
                crackle_frequency = 800 + random.randint(0, 400)
                crackle = 0.2 * np.sin(2 * np.pi * crackle_frequency * t) * np.random.choice([0, 1], len(t), p=[0.7, 0.3])
                crackle *= envelope * 2  # Faster decay for crackle
                sound_wave += crackle
            
            # Normalize and convert to pygame format
            sound_wave = np.clip(sound_wave, -1, 1)
            sound_wave = (sound_wave * 32767).astype(np.int16)
            
            # Create stereo sound
            stereo_wave = np.column_stack((sound_wave, sound_wave))
            
            # Play the sound
            sound = pygame.sndarray.make_sound(stereo_wave)
            sound.set_volume(min(0.8, 0.3 + self.size_multiplier * 0.5))  # Volume based on size
            sound.play()
            
        except Exception as e:
            # If sound generation fails, continue without sound
            print(f"Sound generation error: {e}")
            pass
    
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
        # Initialize pygame and display
        pygame.init()
        
        # Initialize audio mixer for sound effects
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        
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
        
        # Voice analysis (Ultra sensitive settings)
        self.volume_history = deque(maxlen=20)  # Shorter history for faster response
        self.volume_threshold = 0.002  # Even lower threshold for maximum sensitivity
        self.max_volume = 0.2  # Lower max volume for easier triggering of large fireworks
        
        # Fireworks
        self.fireworks = []
        self.last_firework_time = 0
        self.firework_cooldown = 0.15  # Faster cooldown for more responsive firing
        
        # Background and effects
        self.background_color = [10, 10, 30]  # Dark blue night sky
        self.stars = self.create_stars()
        
        # Game modes and monster system
        self.game_mode = "monster_hunt"  # "normal" or "monster_hunt"
        self.monsters = []
        self.fireballs = []  # Monster fireballs attacking player
        self.score = 0
        self.last_monster_spawn = 0
        self.monster_spawn_interval = 3.0  # Spawn monster every 3 seconds
        self.max_monsters = 8  # Maximum monsters on screen
        
        # Player health system
        self.max_health = 30
        self.current_health = self.max_health
        self.player_x = self.width // 2  # Player position (bottom center)
        self.player_y = self.height - 50
        self.game_over = False
        
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
        """Analyze audio input for volume with enhanced sensitivity"""
        try:
            audio_data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            audio_array = np.frombuffer(audio_data, dtype=np.float32)
            
            # Apply audio amplification for better sensitivity
            audio_array = audio_array * 2.0  # Amplify signal by 2x
            
            # Calculate volume (RMS) with enhanced processing
            volume = np.sqrt(np.mean(audio_array**2))
            
            # Apply additional sensitivity boost
            volume = volume * 1.5  # Additional 1.5x boost
            
            # Smooth volume using recent history for stability
            if len(self.volume_history) > 0:
                # Use weighted average with recent samples
                recent_avg = np.mean(list(self.volume_history)[-5:]) if len(self.volume_history) >= 5 else 0
                volume = 0.7 * volume + 0.3 * recent_avg  # Blend current with recent
            
            volume = min(volume, self.max_volume)  # Cap the volume
            
            self.volume_history.append(volume)
            self.current_volume = volume
            
            return volume
        except Exception as e:
            print(f"Audio error: {e}")
            return 0
    
    def should_launch_firework(self, volume):
        """Determine if we should launch a firework based on volume with ultra sensitivity"""
        current_time = time.time()
        
        # Check cooldown
        if current_time - self.last_firework_time < self.firework_cooldown:
            return False
        
        # Check volume threshold (ultra sensitive)
        if volume < self.volume_threshold:
            return False
        
        # Enhanced probability calculation for better responsiveness
        # Lower threshold needed, higher chance of firing
        base_probability = 0.8  # High base probability
        volume_boost = (volume / self.volume_threshold) * 0.2  # Additional boost based on volume
        probability = min(1.0, base_probability + volume_boost)
        
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
    
    def spawn_monster(self):
        """Spawn a new monster at random edge of screen"""
        current_time = time.time()
        
        # Check if we should spawn a monster
        if (current_time - self.last_monster_spawn < self.monster_spawn_interval or 
            len(self.monsters) >= self.max_monsters):
            return
            
        # Spawn at random edge
        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            x, y = random.randint(50, self.width - 50), 50
        elif edge == 'bottom':
            x, y = random.randint(50, self.width - 50), self.height - 50
        elif edge == 'left':
            x, y = 50, random.randint(50, self.height - 50)
        else:  # right
            x, y = self.width - 50, random.randint(50, self.height - 50)
            
        monster = Monster(x, y)
        self.monsters.append(monster)
        self.last_monster_spawn = current_time
    
    def update_monsters(self):
        """Update all monsters and handle their attacks"""
        current_time = time.time()
        
        # Update monster positions and handle attacks
        for monster in self.monsters[:]:
            if monster.alive:
                monster.update(self.width, self.height)
                
                # Monster attacks player
                fireball = monster.attack_player(self.player_x, self.player_y, current_time)
                if fireball:
                    self.fireballs.append(fireball)
            else:
                # Remove dead monsters after a short delay
                if current_time - monster.spawn_time > 1.0:
                    self.monsters.remove(monster)
    
    def update_fireballs(self):
        """Update monster fireballs and check collisions"""
        for fireball in self.fireballs[:]:
            if fireball.alive:
                fireball.update(self.width, self.height)
                
                # Check collision with player
                if fireball.check_collision_with_player(self.player_x, self.player_y):
                    fireball.alive = False
                    self.take_damage(10)  # 10 damage per hit
            else:
                self.fireballs.remove(fireball)
    
    def check_firework_interceptions(self):
        """Check if any exploding fireworks can intercept fireballs"""
        for firework in self.fireworks:
            if firework.exploded:
                # Let this firework try to intercept fireballs
                intercepted = firework.intercept_fireballs(self.fireballs)
                if intercepted:
                    # Add special visual feedback for successful interception
                    for intercepted_fireball in intercepted:
                        # Create bright flash particles at interception point
                        for _ in range(10):
                            flash_particle = {
                                'x': intercepted_fireball.x,
                                'y': intercepted_fireball.y,
                                'vx': random.uniform(-3, 3),
                                'vy': random.uniform(-3, 3),
                                'color': (255, 255, 255),  # White flash
                                'life': 15,
                                'size': random.uniform(2, 5)
                            }
                            firework.particles.append(flash_particle)
                    
                    # Optional: Add score bonus for defensive play
                    if len(intercepted) > 0:
                        self.score += len(intercepted)  # Bonus points for interceptions
    
    def take_damage(self, damage):
        """Player takes damage"""
        self.current_health = max(0, self.current_health - damage)
        if self.current_health <= 0:
            self.game_over = True
    
    def check_monster_collisions(self):
        """Check if any fireworks hit monsters"""
        for firework in self.fireworks:
            if firework.exploded:
                for monster in self.monsters:
                    if monster.alive and monster.check_collision(firework):
                        monster.take_damage()
                        self.score += 1
                        # Visual feedback - could add particle effect here
    
    def draw_monsters(self):
        """Draw all monsters"""
        for monster in self.monsters:
            monster.draw(self.screen)
    
    def draw_fireballs(self):
        """Draw all monster fireballs"""
        for fireball in self.fireballs:
            fireball.draw(self.screen)
    
    def draw_health_bar(self):
        """Draw player health bar at bottom of screen"""
        bar_width = 400
        bar_height = 20
        bar_x = (self.width - bar_width) // 2
        bar_y = self.height - 40
        
        # Background (empty health)
        pygame.draw.rect(self.screen, (100, 0, 0), 
                        (bar_x, bar_y, bar_width, bar_height))
        
        # Health bar (current health)
        health_ratio = self.current_health / self.max_health
        current_width = int(bar_width * health_ratio)
        
        # Color changes based on health level
        if health_ratio > 0.6:
            color = (0, 255, 0)  # Green
        elif health_ratio > 0.3:
            color = (255, 255, 0)  # Yellow
        else:
            color = (255, 0, 0)  # Red
            
        if current_width > 0:
            pygame.draw.rect(self.screen, color,
                            (bar_x, bar_y, current_width, bar_height))
        
        # Border
        pygame.draw.rect(self.screen, (255, 255, 255),
                        (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Health text
        font = pygame.font.Font(None, 24)
        health_text = f"Health: {self.current_health}/{self.max_health}"
        text_surface = font.render(health_text, True, (255, 255, 255))
        text_x = bar_x + (bar_width - text_surface.get_width()) // 2
        self.screen.blit(text_surface, (text_x, bar_y - 25))
    
    def draw_game_over(self):
        """Draw game over screen"""
        if not self.game_over:
            return
            
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        text_x = (self.width - game_over_text.get_width()) // 2
        text_y = (self.height - game_over_text.get_height()) // 2 - 50
        self.screen.blit(game_over_text, (text_x, text_y))
        
        # Final score
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        score_x = (self.width - score_text.get_width()) // 2
        score_y = text_y + 80
        self.screen.blit(score_text, (score_x, score_y))
        
        # Restart instruction
        restart_font = pygame.font.Font(None, 28)
        restart_text = restart_font.render("Press R to Restart or ESC to Exit", True, (200, 200, 200))
        restart_x = (self.width - restart_text.get_width()) // 2
        restart_y = score_y + 50
        self.screen.blit(restart_text, (restart_x, restart_y))
    
    def reset_game(self):
        """Reset game to initial state"""
        self.current_health = self.max_health
        self.game_over = False
        self.score = 0
        self.monsters.clear()
        self.fireballs.clear()
        self.fireworks.clear()
        self.last_monster_spawn = 0
        print("🎆 Game Reset! New Year Monster Hunt Restarted!")
    
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
        font = pygame.font.Font(None, 24)
        volume_text = f"Vol: {self.current_volume:.2f}"
        text_surface = font.render(volume_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (bar_x, bar_y - 28))
    
    def draw_instructions(self):
        """Draw usage instructions"""
        font = pygame.font.Font(None, 24)
        
        if self.game_mode == "monster_hunt":
            instructions = [
                "🎆 New Year Monster Hunt",
                "🎤 Voice → Launch Fireworks",
                "👹 Destroy Monsters | 🔥 Block Fireballs",
                "❤️ 50 HP | R = Restart | ESC = Exit"
            ]
        else:
            instructions = [
                "🎆 Voice Fireworks",
                "🎤 Speak → Launch", 
                "📢 Loud = Big",
                "M = Monster Mode | ESC = Exit"
            ]
        
        for i, instruction in enumerate(instructions):
            color = (255, 255, 255)
            if "🎆" in instruction:
                color = (255, 200, 100)
            elif "🎤" in instruction or "📢" in instruction:
                color = (100, 255, 100)
            
            text_surface = font.render(instruction, True, color)
            self.screen.blit(text_surface, (50, 120 + i * 25))
    
    def draw_statistics(self):
        """Draw game statistics and score"""
        font = pygame.font.Font(None, 24)
        
        if self.game_mode == "monster_hunt":
            # Monster hunt mode - show score prominently
            score_text = f"🏆 Score: {self.score}"
            text_surface = font.render(score_text, True, (255, 215, 0))  # Gold color
            self.screen.blit(text_surface, (self.width - 150, 30))
            
            # Additional stats
            small_font = pygame.font.Font(None, 18)
            stats = [
                f"Monsters: {len([m for m in self.monsters if m.alive])}",
                f"Fireworks: {len(self.fireworks)}"
            ]
            
            for i, stat in enumerate(stats):
                text_surface = small_font.render(stat, True, (200, 200, 255))
                self.screen.blit(text_surface, (self.width - 120, 65 + i * 20))
        else:
            # Normal mode - show firework stats
            small_font = pygame.font.Font(None, 20)
            stats = [
                f"Total: {self.total_fireworks}",
                f"Active: {len(self.fireworks)}"
            ]
            
            for i, stat in enumerate(stats):
                text_surface = small_font.render(stat, True, (200, 200, 255))
                self.screen.blit(text_surface, (self.width - 120, 50 + i * 22))
    
    def run(self):
        """Main game loop"""
        if self.game_mode == "monster_hunt":
            print("🎆 New Year Monster Hunt Mode Started!")
            print("🎤 Use voice to launch fireworks and destroy monsters! | ESC → Exit")
        else:
            print("🎆 Voice Fireworks Started!")
            print("🎤 Speak → Fireworks | ESC → Exit")
        
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
                        elif event.key == pygame.K_m:
                            # Toggle game mode
                            if self.game_mode == "normal":
                                self.game_mode = "monster_hunt"
                                self.reset_game()
                                print("🎆 Switched to New Year Monster Hunt Mode!")
                            else:
                                self.game_mode = "normal"
                                self.monsters.clear()  # Clear all monsters
                                self.fireballs.clear()  # Clear all fireballs
                                print("🎆 Switched to Normal Fireworks Mode!")
                        elif event.key == pygame.K_r:
                            # Restart game
                            if self.game_over:
                                self.reset_game()
                
                # Skip game updates if game is over
                if not self.game_over:
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
                
                # Monster hunt mode specific updates
                if self.game_mode == "monster_hunt" and not self.game_over:
                    self.spawn_monster()
                    self.update_monsters()
                    self.update_fireballs()
                    self.check_monster_collisions()
                    self.check_firework_interceptions()  # Check firework-fireball interceptions
                
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