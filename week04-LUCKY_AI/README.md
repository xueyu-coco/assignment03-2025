# 🍀 Lucky AI - Your Personal Fortune-Telling Assistant

A sophisticated AI chatbot application built with Streamlit, featuring interactive tarot card readings, horoscope predictions, and advanced memory capabilities.

## ✨ Features

### 🔮 **Tarot Card Reading**
- Interactive tarot card selection with 22 Major Arcana cards
- Detailed interpretations with meaning and guidance
- Mystical interface with randomized card layouts
- Trigger phrases: `tarot reading`, `tarot cards`, `draw tarot`, `塔罗牌抽签`

### ⭐ **Daily Horoscope**
- Complete zodiac sign predictions for all 12 signs
- Daily fortune covering love, career, finance, and health
- Lucky numbers and colors included
- Trigger phrases: `horoscope`, `zodiac`, `daily fortune`, `my sign`

### 🧠 **Advanced Memory System**
- Remembers user's personal information (name, age, location, preferences)
- Contextual conversations with personalized responses
- Memory display in sidebar with clear/manage options
- Automatic information extraction from natural conversation

### 🎭 **Multiple AI Personalities**
- **Programming Tutor**: Code help and technical guidance
- **Creative Writer**: Story writing and creative assistance
- **Life Coach**: Personal development and motivation
- **Study Buddy**: Academic support and learning help
- **Travel Guide**: Travel tips and destination advice

### 🎤 **Voice Input Interface**
- Simulated voice-to-text functionality
- Interactive recording interface
- Voice message conversion (demo implementation)

### 🎨 **Enhanced User Experience**
- Typewriter effect for AI responses
- Custom CSS styling with modern design
- Responsive layout with sidebar navigation
- Smooth animations and transitions

## 🚀 Installation & Running Lucky AI

### System Requirements
- **Python**: 3.8 or higher
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Memory**: Minimum 4GB RAM (8GB+ recommended for AI model)
- **Storage**: 2GB free space for models and dependencies
- **Internet**: Required for initial setup and model downloads

### AI Backend Options

#### Option 1: LMStudio (Recommended)
- Download and install [LMStudio](https://lmstudio.ai/)
- Load a compatible model (e.g., Meta-Llama-3-8B-Instruct-GGUF)
- Start local server on port 1234

#### Option 2: Ollama
- Install [Ollama](https://ollama.ai/)
- Pull a model: `ollama pull llama2` or `ollama pull codellama`
- Start Ollama service

### Step-by-Step Setup

1. **Clone and Navigate**
   ```bash
   git clone <repository-url>
   cd week04-LUCKY_AI
   ```

2. **Environment Setup**
   ```bash
   # Create virtual environment
   python -m venv lucky_ai_env
   
   # Activate environment
   # Windows:
   lucky_ai_env\Scripts\activate
   
   # macOS/Linux:
   source lucky_ai_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   # Install all required packages
   pip install -r requirements.txt
   
   # Verify installation
   pip list | grep streamlit
   ```

4. **Start AI Backend**
   
   **For LMStudio:**
   ```bash
   # 1. Launch LMStudio application
   # 2. Go to "Models" tab and download a model
   # 3. Go to "Local Server" tab
   # 4. Load your model and click "Start Server"
   # 5. Verify server is running at http://localhost:1234
   ```
   
   **For Ollama:**
   ```bash
   # Start Ollama service
   ollama serve
   
   # In another terminal, pull a model
   ollama pull llama2
   ```

5. **Launch Lucky AI**
   ```bash
   # Run the Streamlit application
   streamlit run lmstudio_chatbot.py
   
   # Alternative: Run with custom port
   streamlit run lmstudio_chatbot.py --server.port 8502
   ```

6. **Access the Application**
   - **Local URL**: `http://localhost:8501`
   - **Network URL**: Available for other devices on same network
   - **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)

### Quick Start Commands
```bash
# Complete setup in one go (Windows)
git clone <repo> && cd week04-LUCKY_AI && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && streamlit run lmstudio_chatbot.py

# Complete setup in one go (macOS/Linux)
git clone <repo> && cd week04-LUCKY_AI && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && streamlit run lmstudio_chatbot.py
```

## 📋 Complete Requirements & Dependencies

### Core Dependencies
```txt
# Web Framework
streamlit>=1.28.0          # Modern web app framework
streamlit-chat>=0.1.1      # Enhanced chat components (optional)

# AI Integration
openai>=1.3.0              # OpenAI API compatibility
requests>=2.28.0           # HTTP requests for API calls

# Data Processing
pandas>=2.0.0              # Data manipulation and analysis
numpy>=1.24.0              # Numerical computing

# Alternative AI Backends
ollama>=0.1.7              # Local AI model runner (alternative to LMStudio)

# Optional Enhancements
python-dotenv>=1.0.0       # Environment variable management
pillow>=9.5.0              # Image processing for enhanced UI
matplotlib>=3.7.0          # Data visualization (if needed)
```

### Development Dependencies
```txt
# Testing
pytest>=7.4.0             # Testing framework
pytest-streamlit>=1.0.0   # Streamlit-specific testing

# Code Quality
black>=23.0.0              # Code formatting
flake8>=6.0.0              # Code linting
mypy>=1.5.0                # Type checking

# Documentation
sphinx>=7.0.0              # Documentation generation
sphinx-rtd-theme>=1.3.0    # ReadTheDocs theme
```

### System Requirements by Use Case

#### Personal Use (Minimum)
- **CPU**: 2 cores, 2.0 GHz
- **RAM**: 4GB (8GB recommended)
- **Storage**: 2GB free space
- **OS**: Windows 10, macOS 10.14, Ubuntu 18.04+

#### Educational/Classroom (Recommended)
- **CPU**: 4 cores, 2.5 GHz
- **RAM**: 8GB (16GB recommended)
- **Storage**: 5GB free space
- **Network**: Stable internet for model downloads

#### Production/Commercial (Optimal)
- **CPU**: 8+ cores, 3.0+ GHz
- **RAM**: 16GB+ (32GB for large models)
- **Storage**: 10GB+ SSD
- **GPU**: Optional, for accelerated inference

## 🎯 Complete User Interaction Guide

### 🚀 Getting Started
When you first launch Lucky AI, you'll see:
- **Main Chat Interface**: Central conversation area
- **Sidebar Navigation**: AI personality selector and memory display
- **Input Field**: Type your messages at the bottom
- **Control Buttons**: Various interactive elements

### 💬 Basic Chat Interactions

#### Starting a Conversation
```
User: "Hello Lucky AI!"
Lucky AI: "🍀 Greetings! I'm Lucky AI, your mystical companion. I can help with tarot readings, horoscope predictions, and much more. What brings you here today?"
```

#### Switching AI Personalities
1. **Access Sidebar**: Look for the dropdown menu labeled "Choose Your AI Assistant"
2. **Select Personality**: Choose from 5 different AI personalities:
   - **💻 Programming Tutor**: `"Can you help me debug this Python code?"`
   - **✍️ Creative Writer**: `"Help me write a fantasy story about dragons"`
   - **🎯 Life Coach**: `"I need motivation for my career goals"`
   - **📚 Study Buddy**: `"Explain quantum physics in simple terms"`
   - **🗺️ Travel Guide**: `"Plan a 7-day trip to Japan"`

### 🔮 Fortune Telling Features

#### Tarot Card Reading
**Trigger Phrases** (case-insensitive):
- `"tarot reading"`
- `"draw tarot cards"`
- `"I want a tarot reading"`
- `"塔罗牌抽签"` (Chinese)

**How It Works:**
1. Type any trigger phrase
2. Lucky AI displays 18 mystical tarot cards in a grid
3. Click on any card that calls to you
4. Receive detailed interpretation including:
   - Card name and traditional meaning
   - Personal guidance and advice
   - Spiritual insights for your current situation

**Example Interaction:**
```
User: "I need a tarot reading"
Lucky AI: "🔮 The cards are calling to you! Choose the card that resonates with your soul..."
[18 cards appear - user clicks "The Fool"]
Lucky AI: "✨ You've drawn The Fool! This card represents new beginnings and infinite possibilities..."
```

#### Daily Horoscope
**Trigger Phrases:**
- `"horoscope"`
- `"my zodiac sign"`
- `"daily fortune"`
- `"what's my horoscope?"`

**How It Works:**
1. Type any horoscope trigger phrase
2. 12 zodiac signs appear as clickable buttons
3. Select your zodiac sign
4. Receive comprehensive daily prediction covering:
   - **Love & Relationships**
   - **Career & Money**
   - **Health & Wellness**
   - **Lucky Numbers & Colors**

**Example Interaction:**
```
User: "What's my horoscope for today?"
Lucky AI: "⭐ The stars are aligned! Please select your zodiac sign..."
[12 zodiac buttons appear - user clicks "Leo"]
Lucky AI: "🦁 Leo Daily Fortune: Today brings powerful creative energy..."
```

### 🧠 Memory System Interactions

#### How Memory Works
Lucky AI automatically extracts and remembers:
- **Personal Info**: Name, age, location, occupation
- **Preferences**: Favorite colors, hobbies, interests
- **Conversation Context**: Previous topics and decisions
- **Relationship Status**: Family, friends, romantic relationships

#### Memory Examples
```
User: "Hi, I'm Sarah, 28 years old from New York. I work as a graphic designer."
Lucky AI: "Nice to meet you, Sarah! I'll remember that you're 28, from New York, and work in graphic design."

[Later in conversation]
User: "I'm feeling creative today"
Lucky AI: "That's wonderful, Sarah! As a graphic designer from New York, this creative energy could lead to some amazing design projects!"
```

#### Managing Memory
- **View Memory**: Check the "🧠 Memory" section in the sidebar
- **Clear Memory**: Click the "🧹 Clear Memory" button to reset
- **Update Info**: Simply tell Lucky AI new information naturally

### 🎤 Voice Input Feature (Demo)

#### Simulated Voice Interaction
1. **Find Voice Button**: Look for the 🎤 microphone icon
2. **Click to "Record"**: Simulates voice input capture
3. **Type Your Message**: Enter what you would say
4. **Voice Processing**: Lucky AI processes as if spoken

**Example:**
```
[User clicks 🎤 button]
Voice Input Box: "Tell me my fortune for love"
Lucky AI: "🎙️ I heard you asking about love fortune! Let me pull up your horoscope..."
```

### 🎮 Interactive Game Modes

#### Tarot Card Selection Interface
- **Grid Layout**: 18 cards arranged in 3 rows of 6
- **Hover Effects**: Cards glow when you hover over them
- **Click Response**: Immediate interpretation upon selection
- **Multiple Readings**: Draw multiple cards in one session

#### Zodiac Sign Selection
- **Visual Icons**: Each sign has its distinctive symbol
- **Date Ranges**: Hover to see birth date ranges
- **Instant Results**: Immediate horoscope generation
- **Daily Updates**: Fresh predictions each day

### 🎨 User Interface Elements

#### Sidebar Navigation
- **🤖 AI Personality Selector**: Dropdown menu
- **🧠 Memory Display**: Shows remembered information
- **🧹 Memory Management**: Clear/reset options
- **📊 Session Statistics**: Conversation metrics

#### Main Chat Area
- **💬 Message History**: Scrollable conversation log
- **⌨️ Input Field**: Type messages here
- **🔄 Refresh Options**: Reset conversation state
- **📱 Responsive Design**: Works on all screen sizes

#### Special Interactive Elements
- **Card Grid**: 3x6 grid for tarot selection
- **Zodiac Wheel**: Circular arrangement of star signs
- **Progress Indicators**: Show loading states
- **Notification Badges**: Highlight new features

### 🔧 Advanced Features

#### Conversation Context Awareness
```
User: "I drew The Fool card yesterday"
Lucky AI: "I remember your Fool card reading, Sarah! How did that new beginning energy manifest for you?"
```

#### Multi-Turn Fortune Telling
```
User: "Give me both tarot and horoscope"
Lucky AI: "Absolutely! Let's start with your tarot reading..."
[After tarot] "Now let's check your Leo horoscope for today..."
```

#### Personality Consistency
Each AI personality maintains its unique voice:
- **Programming Tutor**: Technical, educational tone
- **Creative Writer**: Imaginative, storytelling approach
- **Life Coach**: Motivational, supportive language
- **Study Buddy**: Patient, explanatory style
- **Travel Guide**: Enthusiastic, informative advice

### 🚨 Troubleshooting User Issues

#### Common User Problems & Solutions

**"The cards aren't appearing"**
- Refresh the page (Ctrl+F5)
- Clear browser cache
- Check if JavaScript is enabled

**"AI responses are slow"**
- Verify AI backend (LMStudio/Ollama) is running
- Check internet connection
- Restart the Streamlit application

**"Memory isn't working"**
- Speak in complete sentences with clear information
- Use phrases like "My name is..." or "I live in..."
- Check sidebar to see what's remembered

**"Wrong personality responding"**
- Check the selected personality in sidebar dropdown
- Refresh page to reset session state
- Explicitly mention desired personality in chat

### 📱 Multi-Device Usage
- **Desktop**: Full feature experience
- **Tablet**: Touch-optimized interface
- **Mobile**: Responsive design with simplified layout
- **Cross-Platform**: Works on Windows, macOS, Linux browsers

## 🛠️ Technical Architecture

### Core Components
- **Streamlit Frontend**: Modern web interface with custom CSS
- **OpenAI API Integration**: Compatible with LMStudio local server
- **Session State Management**: Persistent memory and game states
- **Modular Design**: Separate functions for different features

### File Structure
```
week04/
├── lmstudio_chatbot.py     # Main application file
├── requirements.txt        # Python dependencies
├── test_tarot_english.py   # Tarot functionality tests
├── test_horoscope.py      # Horoscope functionality tests
├── test_memory.py         # Memory system tests
└── README.md              # This documentation
```

### Key Functions
- `extract_user_info()`: Extracts personal information from messages
- `update_memory()`: Updates user memory in session state
- `interpret_tarot_card()`: Generates tarot card interpretations
- `generate_horoscope()`: Creates daily horoscope predictions

## 🎨 Customization

### Adding New Tarot Cards
Edit the `TAROT_CARDS` dictionary in `lmstudio_chatbot.py`:
```python
TAROT_CARDS = {
    "Your Card Name": {
        "meaning": "Brief meaning",
        "interpretation": "Detailed interpretation..."
    }
}
```

### Modifying AI Personalities
Update the `role_templates` dictionary to add or modify AI personalities:
```python
role_templates = {
    "Your Assistant": {
        "prompt": "Your system prompt here...",
        "temp": 0.7,
        "max_tokens": 1000
    }
}
```

### Styling Changes
Modify the CSS in the `st.markdown()` section at the beginning of the main file.

## 🔧 Technical Troubleshooting & Support

### Environment Setup Issues

#### Python Version Problems
```bash
# Check Python version
python --version

# If Python < 3.8, install newer version
# Windows: Download from python.org
# macOS: brew install python@3.11
# Linux: sudo apt install python3.11
```

#### Virtual Environment Issues
```bash
# If venv creation fails
python -m pip install --upgrade pip
python -m pip install virtualenv
python -m virtualenv lucky_ai_env

# Activation problems on Windows
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Package Installation Errors
```bash
# If pip install fails
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt --no-cache-dir

# For specific package issues
pip install streamlit==1.28.0
pip install openai==1.3.0
```

### AI Backend Configuration

#### LMStudio Setup Issues
1. **Download Problems**
   - Check internet connection
   - Use VPN if region-blocked
   - Try downloading from official website directly

2. **Model Loading Issues**
   - Ensure sufficient RAM (8GB+ for 7B models)
   - Close other applications to free memory
   - Try smaller models if hardware limited

3. **Server Connection Problems**
   ```bash
   # Test LMStudio server
   curl http://localhost:1234/v1/models
   
   # Expected response: JSON with model information
   # If fails: restart LMStudio, check firewall settings
   ```

#### Ollama Configuration
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull and test model
ollama pull llama2
ollama run llama2 "Hello, world!"

# Check if service is running
ollama ps
```

### Application Runtime Issues

#### Streamlit Startup Problems
```bash
# Clear Streamlit cache
streamlit cache clear

# Run with verbose logging
streamlit run lmstudio_chatbot.py --logger.level=debug

# Try different port
streamlit run lmstudio_chatbot.py --server.port 8502
```

#### Memory Issues
```bash
# Check system memory usage
# Windows: Task Manager
# macOS: Activity Monitor  
# Linux: htop or free -h

# Reduce memory usage
# Use smaller AI models
# Close unnecessary browser tabs
# Restart the application periodically
```

#### Browser Compatibility
- **Recommended**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Clear Cache**: Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (macOS)
- **Disable Extensions**: Try incognito/private mode
- **JavaScript**: Ensure JavaScript is enabled

### Feature-Specific Troubleshooting

#### Tarot Cards Not Displaying
```python
# Check browser console for errors (F12)
# Common fixes:
1. Refresh page (Ctrl+F5 or Cmd+Shift+R)
2. Clear browser cache and cookies
3. Disable ad blockers temporarily
4. Check if JavaScript is blocked
```

#### Horoscope Selection Issues
```python
# If zodiac buttons don't respond:
1. Check for JavaScript errors in console
2. Ensure session state is properly initialized
3. Try typing zodiac sign name instead of clicking
4. Restart Streamlit application
```

#### Memory System Not Working
```python
# Debug memory extraction:
1. Speak in clear, complete sentences
2. Use explicit phrases: "My name is John"
3. Check sidebar for memory display
4. Clear memory and try again
5. Check console for regex pattern errors
```

#### AI Response Issues
```python
# If AI doesn't respond or gives errors:
1. Check AI backend status (LMStudio/Ollama)
2. Verify model is loaded and running
3. Test with simple "Hello" message
4. Check network connectivity to localhost
5. Restart AI service if needed
```

### Performance Optimization

#### Speed Improvements
```bash
# Optimize Streamlit performance
streamlit run lmstudio_chatbot.py --server.enableCORS=false --server.enableXsrfProtection=false

# Reduce AI response time
# Use smaller models (3B instead of 7B)
# Reduce max_tokens in API calls
# Increase temperature for faster, less precise responses
```

#### Memory Usage Reduction
```python
# In lmstudio_chatbot.py, adjust these settings:
MAX_MEMORY_ITEMS = 10  # Reduce from 20
MAX_CHAT_HISTORY = 50  # Reduce from 100
RESPONSE_MAX_TOKENS = 500  # Reduce from 1000
```

### Development & Debugging

#### Enable Debug Mode
```python
# Add to top of lmstudio_chatbot.py
import logging
logging.basicConfig(level=logging.DEBUG)
st.set_option('client.showErrorDetails', True)
```

#### Testing Components
```bash
# Test individual components
python test_tarot_english.py
python test_horoscope.py
python test_memory.py

# Expected output: All tests should pass
```

#### Common Error Messages

**"Connection refused"**
- AI backend not running
- Wrong port configuration
- Firewall blocking connection

**"Model not found"**  
- Model not loaded in LMStudio
- Wrong model name in configuration
- Model download incomplete

**"Session state error"**
- Browser cache issues
- Streamlit version incompatibility
- Clear cache and restart

**"Import error"**
- Missing dependencies
- Virtual environment not activated
- Python path issues

### Getting Help

#### Self-Diagnosis Checklist
- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] All requirements installed
- [ ] AI backend running (LMStudio/Ollama)
- [ ] Browser JavaScript enabled
- [ ] No firewall blocking ports 8501/1234
- [ ] Sufficient system memory (4GB+)

#### Community Support
1. **Check Issues**: Search existing GitHub issues
2. **Create Issue**: Provide system info, error logs, steps to reproduce
3. **Discord/Forums**: Join community discussions
4. **Documentation**: Re-read setup instructions carefully

#### Professional Support
For business or educational use:
- Technical consultation available
- Custom deployment assistance
- Feature development requests
- Training and workshop sessions

---

**Need immediate help?** Run the built-in diagnostics:
```bash
python -c "import streamlit, openai, pandas, numpy; print('All packages imported successfully!')"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the amazing web framework
- **LMStudio**: For local AI model hosting
- **OpenAI**: For the API compatibility
- **Tarot Community**: For traditional card meanings and interpretations

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the test files for usage examples
3. Create an issue in the repository

---

**Made with ❤️ and ✨ for fortune-telling enthusiasts and AI lovers alike!**

## 🔮 Sample Screenshots

*Add screenshots of your application here showing:*
- Main chat interface
- Tarot card selection
- Horoscope zodiac selection  
- Memory sidebar
- Different AI personalities

---

*Last updated: October 21, 2025*

## 🔮 Additional Resources

### Video Tutorials
- **Setup Guide**: Step-by-step installation walkthrough
- **Feature Demo**: Complete functionality demonstration  
- **Troubleshooting**: Common issues and solutions
- **Advanced Usage**: Power user tips and tricks

### Example Conversations
- **Tarot Reading Session**: Full interactive card reading
- **Horoscope Consultation**: Daily fortune telling experience
- **Memory Demonstration**: How AI remembers personal details
- **Multi-Personality Chat**: Switching between different AI assistants

### Community & Support
- **GitHub Repository**: Source code and issue tracking
- **Discord Server**: Real-time community support
- **Documentation Wiki**: Comprehensive guides and tutorials
- **Blog Posts**: Use cases and success stories

**Ready to discover your fortune with Lucky AI? Let the mystical journey begin! 🌟✨**