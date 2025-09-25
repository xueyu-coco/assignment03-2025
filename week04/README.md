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

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- LMStudio running locally on port 1234
- Compatible AI model (e.g., Meta-Llama-3-8B-Instruct-GGUF)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd week04
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start LMStudio**
   - Launch LMStudio application
   - Load your preferred language model
   - Ensure server is running on `http://localhost:1234`

5. **Run the application**
   ```bash
   streamlit run lmstudio_chatbot.py
   ```

6. **Access the app**
   - Open your browser to `http://localhost:8501`
   - Start chatting with Lucky AI!

## 📋 Requirements

```txt
streamlit>=1.50.0
openai>=1.0.0
pandas>=2.0.0
numpy>=1.20.0
```

## 🎯 Usage Guide

### Basic Chat
Simply type your message in the chat input field and press Enter. Lucky AI will respond based on the selected personality.

### Fortune Telling Games

#### 🔮 Tarot Reading
1. Type `tarot reading` in the chat
2. Click on any of the 18 displayed cards
3. Receive your personalized tarot interpretation

#### ⭐ Horoscope
1. Click the 🔄 refresh icon to switch to horoscope mode
2. Type `horoscope` in the chat
3. Select your zodiac sign from the 12 options
4. Get your detailed daily fortune

### Memory Features
- Lucky AI automatically remembers information you share
- View remembered details in the "🧠 Memory" sidebar section
- Clear memory using the "🧹 Clear Memory" button

### AI Personalities
Use the sidebar dropdown to switch between different AI assistants:
- **Programming Tutor**: For coding questions and technical help
- **Creative Writer**: For writing assistance and storytelling
- **Life Coach**: For personal development and motivation
- **Study Buddy**: For academic support and learning
- **Travel Guide**: For travel planning and recommendations

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

## 🔧 Troubleshooting

### Common Issues

**LMStudio Connection Error**
- Ensure LMStudio is running on port 1234
- Check if your AI model is properly loaded
- Verify network connectivity to localhost

**Memory Not Working**
- Check if session state is properly initialized
- Verify regex patterns in `extract_user_info()`
- Clear browser cache and restart the app

**Cards/Horoscope Not Displaying**
- Check for JavaScript errors in browser console
- Ensure all session states are properly managed
- Try refreshing the page

**Styling Issues**
- Clear browser cache
- Check for CSS conflicts in custom styles
- Verify Streamlit version compatibility

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

*Last updated: September 25, 2025*