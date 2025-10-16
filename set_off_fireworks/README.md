# Voice-Controlled Fireworks 🎆🎤

An interactive voice-controlled fireworks display with **New Year Monster Hunt Mode**! Use your voice to launch fireworks, destroy monsters, and survive an epic New Year celebration battle with spectacular effects.

## 🌟 Features

### 🎮 Dual Game Modes
- **Normal Mode**: Classic voice-controlled fireworks display for peaceful celebration
- **Monster Hunt Mode**: Intense New Year themed monster hunting with combat mechanics
- **Real-time Mode Switching**: Press 'M' to switch between modes instantly

### 🎤 Voice Control System
- **Volume-Reactive Fireworks**: Speak into your microphone to launch fireworks
- **Dynamic Sizing**: Louder voice = Bigger fireworks with larger blast radius
- **Ultra-Sensitive Detection**: Advanced voice volume detection with 3x signal amplification
- **Smart Cooldown**: Intelligent timing with 150ms response time for rapid-fire capability
- **Threshold Intelligence**: Automatic noise floor adjustment for different environments

### 👹 Monster Hunt Mode - Complete Combat System
- **Evil Monsters**: AI-driven monsters with glowing red eyes and unpredictable movement
- **Voice Combat**: Use voice-controlled fireworks as weapons to destroy monsters
- **Player Health System**: Start with 30 HP, lose health from monster attacks
- **Monster Fireballs**: Enemies launch fireballs that deal 10 damage on hit
- **Defensive Mechanics**: Use firework explosions to destroy incoming fireballs
- **Scoring System**: Earn points for each monster destroyed
- **Dynamic Spawning**: Monsters appear every 3 seconds (max 8 on screen)
- **Collision Detection**: Firework explosions destroy monsters within blast radius
- **Real-time Stats**: Live monster count, score tracking, and health display
- **Game Over System**: Death and restart mechanics with 'R' key revival

### 🎆 Spectacular Visual Effects
- **Realistic Rocket Launch**: Rockets fly from bottom to target with trails
- **Multi-Color Explosions**: 5 different color schemes (Red-Orange-Yellow, Blue-Purple-Pink, Green variations, Orange variations, Purple-Pink)
- **Particle Physics**: Gravity-affected particles with realistic movement
- **Glow Effects**: Beautiful particle glow and fade effects
- **Animated Background**: Twinkling stars in a night sky

### 🔊 Dynamic Sound Effects
- **Dual Audio System**: Launch sounds + explosion sounds for complete audio experience
- **Launch Audio**: Realistic whoosh/rocket launch sounds with frequency sweeps
- **Size-Based Audio**: Different sound effects for different firework sizes
- **Realistic Explosion Sounds**: Procedurally generated explosion audio with harmonics and noise
- **Volume Scaling**: Louder fireworks produce louder, deeper sounds
- **Crackle Effects**: Large fireworks include authentic crackling sounds
- **Multi-layered Audio**: Base sounds + harmonics + noise + crackle for realism
- **Enhanced Sensitivity**: More responsive voice detection for easier triggering

### 🎨 Interactive Interface
- **Real-time Volume Indicator**: Visual bar showing current voice volume
- **Color-coded Feedback**: Green (good level), Yellow (loud), Red (very loud)
- **Live Statistics**: Track total fireworks launched and active fireworks
- **On-screen Instructions**: Clear usage guidelines displayed

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Microphone connected and working
- Audio drivers properly configured

### Installation

1. **Navigate to project directory**:
   ```bash
   cd set_off_fireworks
   ```

2. **Activate virtual environment**:
   ```bash
   # Windows
   .\venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python voice_fireworks.py
```

## 🎮 How to Use

### Controls
- **🎤 Speak into microphone**: Launch fireworks (volume determines size and power)
- **M**: Switch between Normal and Monster Hunt modes
- **SPACE**: Manual test firework launch
- **R**: Restart game (when game over in Monster Hunt mode)
- **ESC**: Exit the application

### Game Modes

#### 🎆 Normal Mode
1. **Speak normally**: Creates medium-sized fireworks for beautiful displays
2. **Speak loudly**: Creates large, spectacular fireworks with wider explosions
3. **Whisper**: Creates small, delicate fireworks for subtle effects
4. **Stay quiet**: No fireworks launch - enjoy the peaceful night sky

#### 👹 Monster Hunt Mode - Survival Combat
1. **Voice-Controlled Combat**: Use your voice to launch firework weapons
   - **Louder voice** = **Bigger explosions** = **More damage area**
   - **Rapid speaking** = **Rapid-fire mode** for intense battles
   
2. **Monster AI System**:
   - **Random Movement**: Monsters move unpredictably across the screen
   - **Attack Patterns**: Each monster attacks every 3-6 seconds
   - **Fireball Projectiles**: Orange-red fireballs with trailing effects
   - **Collision Physics**: Realistic monster-firework interaction
   
3. **Player Health & Defense**:
   - **30 HP Starting Health**: Displayed as green health bar at bottom
   - **10 Damage per Hit**: Monster fireballs deal significant damage (1/3 of total health)
   - **Defensive Strategy**: Use firework explosions to destroy incoming fireballs
   - **Death & Revival**: Game over at 0 HP, press 'R' to restart with full health
   
4. **Combat Mechanics**:
   - **Blast Radius**: Firework explosions affect all enemies within radius
   - **Fireball Interception**: Your explosions can destroy enemy projectiles
   - **Score System**: 1 point per monster destroyed
   - **Survival Challenge**: Monsters spawn continuously - how long can you last?
   
5. **Tactical Elements**:
   - **Area Denial**: Large fireworks clear multiple monsters
   - **Precise Targeting**: Small fireworks for single-monster elimination
   - **Resource Management**: Balance attack frequency with defensive positioning
   - **Timing Strategy**: Coordinate attacks with monster spawn patterns

### Volume Indicator
- **Gray Bar**: Too quiet (below threshold)
- **Green Bar**: Good volume level
- **Yellow Bar**: Loud volume (big fireworks)
- **Red Bar**: Very loud (maximum fireworks)

## 🎮 Advanced Game Mechanics

### 🏴‍☠️ Monster AI & Behavior
- **Intelligent Movement**: Monsters use realistic physics with direction changes
- **Collision Avoidance**: Monsters bounce off screen edges naturally
- **Unpredictable Patterns**: Random direction shifts every few seconds
- **Size Variation**: Monsters spawn in different sizes (20-40 pixels)
- **Color Diversity**: 5 different monster types with unique color schemes
- **Attack AI**: Each monster has individual attack timers and cooldowns
- **Pulsing Animation**: Monsters pulse and blink for menacing visual effect

### ⚔️ Combat System Details
- **Fireball Physics**: Enemy projectiles follow realistic ballistic trajectories
- **Trail Effects**: Fireballs leave glowing orange trails for visual impact
- **Collision Detection**: Precise hit detection for both players and monsters
- **Damage Calculation**: Health system with visual feedback
- **Defensive Options**: Players can shoot down incoming fireballs
- **Area of Effect**: Firework explosions affect multiple targets simultaneously
- **Combat Feedback**: Visual and audio cues for hits, misses, and kills

### 🎯 Strategic Depth
- **Voice Strategy**: Different vocal techniques for different combat situations
  - **Quick bursts**: Rapid-fire small fireworks for precise targeting
  - **Sustained loud voice**: Large area-denial explosions
  - **Rhythmic speaking**: Create defensive walls of explosions
  - **Volume modulation**: Mix large and small fireworks tactically
  
- **Positioning Tactics**: 
  - Monsters spawn from edges - anticipate movement patterns
  - Use large explosions to control monster group movements
  - Create safe zones with overlapping explosion coverage
  - Time attacks to intercept monster attack patterns

- **Survival Strategies**:
  - **Early Game**: Focus on learning monster movement patterns
  - **Mid Game**: Balance offense and defense as spawn rate increases  
  - **Late Game**: Master rapid-fire techniques for crowd control
  - **Expert Level**: Use fireball interception for advanced defense
  - **Hardcore Mode**: With only 30 HP, every hit counts - prioritize defense!

### 📊 Progression & Scoring
- **Score Multipliers**: Consecutive kills without taking damage boost points
- **Survival Time**: Track how long you survive against endless waves
- **Efficiency Rating**: Monitor fireworks-to-kills ratio for skill assessment
- **Health Management**: Strategic healing through perfect defensive play
- **Personal Bests**: Challenge yourself to beat previous high scores

### 🔧 Technical Game Mechanics
- **Frame Rate**: Locked 60 FPS for smooth gameplay
- **Physics Engine**: Custom particle and collision system
- **Audio Processing**: Real-time voice analysis with sub-100ms latency
- **Memory Management**: Automatic cleanup of expired game objects
- **Performance Scaling**: Optimized for different hardware configurations

## 🔧 Technical Implementation Details
### Audio Processing Engine
- **Sample Rate**: 44.1 kHz professional audio quality
- **Chunk Size**: 1024 samples for optimal latency vs quality
- **Volume Analysis**: Enhanced RMS with 2x signal amplification + 1.5x sensitivity boost
- **Ultra Sensitivity**: Extremely low threshold (0.002) for maximum responsiveness
- **Fast Response**: Shorter volume history (20 samples) for quicker reaction
- **Smart Smoothing**: Weighted average with recent samples for stability
- **Threshold Detection**: Automatic noise floor adjustment for different environments
- **Voice Pattern Recognition**: Advanced algorithms detect speech vs background noise

### Sound Effects System
- **Dual Audio Engine**: Launch sounds + explosion sounds
- **Launch Audio**: Frequency sweep whoosh (40-180 Hz) with pink noise
- **Launch Duration**: 0.8-1.2 seconds based on firework size
- **Audio Generation**: Real-time procedural sound synthesis
- **Sound Sample Rate**: 22.05 kHz for effects
- **Explosion Frequency**: 60-250 Hz based on firework size
- **Harmonic Layers**: Base tone + 2nd/3rd harmonics for richness
- **Noise Component**: Realistic explosion texture
- **Envelope Shaping**: Exponential decay with size-based duration
- **Crackle Effects**: High-frequency sparkle sounds for large fireworks

### Game Physics & Rendering
- **Launch Speed**: 8-12 pixels/frame (velocity based on voice volume)
- **Explosion Dynamics**: 50-150 particles (volume-dependent distribution)
- **Particle Count**: 30-80 particles per firework with realistic physics
- **Gravity Simulation**: 0.2 pixels/frame² downward acceleration
- **Particle Decay**: 98% size reduction per frame for natural fade
- **Collision Detection**: Pixel-perfect collision algorithms for all game objects
- **Monster AI**: State-based behavior system with pathfinding
- **Fireball Physics**: Realistic projectile motion with atmospheric effects

### Combat System Architecture  
- **Health Management**: Integer-based health system with damage calculation
- **Attack Patterns**: Procedural monster attack timing with randomization
- **Defensive Mechanics**: Real-time projectile interception system
- **Score Calculation**: Event-driven scoring with multiplier support
- **Game State Management**: Finite state machine for game flow control
- **Object Pooling**: Efficient memory management for particles and projectiles

### Performance
- **Frame Rate**: 60 FPS
- **Resolution**: 1200x800 (configurable)
- **Memory Efficient**: Automatic particle cleanup
- **CPU Optimized**: Efficient audio processing

## 🎯 Advanced Gameplay Tips & Strategies

### 🏆 Mastering Voice Control
- **Breath Control**: Use diaphragmatic breathing for sustained loud voices
- **Voice Modulation**: Practice quick volume changes for tactical flexibility  
- **Rhythm Techniques**: Develop personal vocal rhythms for consistent firework timing
- **Environment Adaptation**: Adjust speaking volume based on room acoustics
- **Microphone Positioning**: Optimal distance is 6-12 inches from mouth

### ⚡ Combat Mastery
- **Pattern Recognition**: Learn monster spawn locations and movement patterns
- **Defensive Priority**: Always prioritize destroying incoming fireballs
- **Area Control**: Use large explosions to funnel monsters into kill zones
- **Health Conservation**: Perfect defensive play prevents all damage
- **Emergency Tactics**: Rapid-fire small fireworks for desperate situations

### 🎖️ Advanced Techniques
- **Fireball Interception**: Precisely time explosions to destroy multiple enemy projectiles
- **Monster Herding**: Use explosion positions to guide monster movement
- **Spawn Camping**: Position attacks at monster spawn points for immediate kills
- **Chain Reactions**: Create overlapping explosions for maximum area coverage
- **Voice Stamina**: Pace yourself for extended gameplay sessions

### � Performance Optimization
- **Score Efficiency**: Aim for high monster-kills per firework ratio
- **Survival Metrics**: Track personal best survival times
- **Accuracy Training**: Practice precise targeting for single-monster elimination
- **Endurance Building**: Gradually increase session length for stamina
- **Skill Progression**: Master normal mode before attempting monster hunt

## 🎭 Customization & Modding

```
set_off_fireworks/
├── venv/                    # Virtual environment
├── voice_fireworks.py       # Main application
├── audio_loopback.py        # Audio testing utility
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## � Customization

### Difficulty Adjustment
Edit `voice_fireworks.py` for custom challenge levels:
```python
# Monster spawn rate (seconds between spawns)
self.monster_spawn_timer = 3.0    # Decrease for harder difficulty

# Player health
self.player_health = 30           # Reduce for hardcore mode  

# Monster damage
fireball_damage = 10              # Increase for extreme challenge (currently 1/3 of health)

# Monster speed range
speed = random.uniform(0.5, 2.0)  # Increase max for faster monsters
```

### Visual Customization
```python
# Custom firework colors
color_sets = [
    [(255, 0, 0), (255, 100, 0), (255, 255, 0)],    # Red-Orange-Yellow
    [(0, 100, 255), (100, 0, 255), (255, 0, 255)],  # Blue-Purple-Pink
    [(0, 255, 0), (100, 255, 100), (200, 255, 200)], # Green variations
    # Add your custom color schemes here
]

# Monster appearance
monster_colors = [
    (150, 0, 0),      # Dark red
    (0, 100, 0),      # Dark green
    (100, 0, 100),    # Purple
    # Add more monster types
]
```

### Audio Sensitivity Tuning
```python
# Voice detection sensitivity
self.volume_threshold = 0.002     # Lower = more sensitive
self.max_volume = 0.5            # Adjust based on microphone
self.firework_cooldown = 0.15    # Time between launches (seconds)

# Audio amplification
self.signal_amplification = 2.0   # Increase for quieter microphones
self.sensitivity_boost = 1.5      # Additional sensitivity multiplier
```

### Gameplay Modifications
```python
# Firework power scaling
explosion_size = int(50 + size_multiplier * 100)    # Blast radius
particle_count = int(30 + size_multiplier * 50)     # Explosion intensity

# Monster behavior
attack_cooldown = random.uniform(2.0, 5.0)          # Attack frequency
max_monsters = 8                                     # Simultaneous monsters
```

## 📁 Project Structure

```
set_off_fireworks/
├── venv/                    # Virtual environment
├── voice_fireworks.py       # Main game application (990+ lines)
├── audio_loopback.py        # Audio testing utility
├── requirements.txt         # Dependencies
└── README.md               # This comprehensive guide
```

## 🔬 Code Architecture

### Core Classes
- **VoiceControlledFireworks**: Main game engine and state manager
- **Monster**: AI-driven enemy with attack capabilities  
- **Fireball**: Enemy projectile with physics simulation
- **Firework**: Player weapon with explosion mechanics
- **Particle**: Visual effect system for explosions

### Key Systems
- **Audio Processing Thread**: Real-time microphone analysis
- **Game State Manager**: Mode switching and game flow control
- **Physics Engine**: Collision detection and movement simulation
- **Rendering Pipeline**: Optimized graphics with 60 FPS performance
- **UI System**: Health bars, score display, and status indicators

## 🔍 Troubleshooting

### Common Issues

#### No Fireworks Launching
- Check microphone permissions
- Verify microphone is working (test in other apps)
- Adjust `volume_threshold` if too sensitive/insensitive
- Try speaking closer to microphone

#### Audio Errors
- Ensure no other apps are using microphone
- Check audio drivers are up to date
- Try different sample rates in code
- Restart application

#### Performance Issues
- Close other applications
- Lower resolution in code
- Reduce particle count
- Check CPU usage

#### No Sound Detection
```python
# Test microphone independently
python audio_loopback.py
```

### System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- Integrated audio
- Microphone input

**Recommended:**
- Python 3.9+
- 8GB RAM
- Dedicated graphics
- High-quality microphone

## 🎯 Future Enhancements & Roadmap

### 🚀 Planned Features
- **Multiplayer Support**: Voice-controlled team battles with friends
- **Achievement System**: Unlock rewards for completing challenges
- **Power-ups**: Temporary abilities like rapid-fire or mega-explosions  
- **Boss Monsters**: Special large enemies with unique attack patterns
- **Voice Commands**: Specific words trigger different firework types
- **Music Synchronization**: Sync fireworks to background music beats
- **Custom Levels**: User-created monster wave patterns
- **VR Support**: Virtual reality fireworks combat experience

### 🎮 Gameplay Expansions
- **Multiple Weapon Types**: Different voice patterns unlock new firework styles
- **Environmental Hazards**: Dynamic obstacles and terrain effects
- **Monster Evolution**: Enemies that adapt to player strategies
- **Combo System**: Chain kills for bonus points and special effects
- **Shield Mechanics**: Temporary protection abilities
- **Time-based Challenges**: Survival mode with increasing difficulty
- **Campaign Mode**: Progressive levels with storyline

### 🛠️ Technical Improvements  
- **Mobile App**: Smartphone version with touch controls
- **Cloud Saves**: Preserve progress across devices
- **AI Voice Recognition**: Distinguish between players in multiplayer
- **Performance Optimization**: Support for 4K displays and high refresh rates
- **Accessibility Features**: Visual indicators for hearing-impaired players
- **Machine Learning**: AI that learns and adapts to player voice patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🎊 Enjoy the Show!

Have fun creating your own voice-controlled fireworks display! Try different speaking patterns, volumes, and timing to create unique firework shows.

---

*Created: October 10, 2025*  
*Last Updated: October 16, 2025*  
*Voice-Controlled Fireworks Combat Game - Where Your Voice Becomes Your Weapon!* 🎆⚔️✨

**Version 2.1 Features:**
- ✅ Complete combat system with player health and monster attacks
- ✅ Advanced AI monster behavior with fireball projectiles  
- ✅ Defensive mechanics and projectile interception
- ✅ Comprehensive game mechanics with survival elements
- ✅ English localization for international accessibility
- ✅ Professional documentation with advanced strategies
- 🆕 **Balanced Gameplay**: Reduced player health to 30 HP for increased challenge
- 🆕 **Enhanced Difficulty**: Each fireball hit now deals 1/3 of total health damage