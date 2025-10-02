import streamlit as st
from openai import OpenAI
import re
import random
import datetime

# Tarot Cards Data
TAROT_CARDS = {
    "The Fool": {
        "meaning": "New beginnings, innocence, spontaneity, free spirit",
        "interpretation": "The Fool represents a new journey and infinite possibilities. It's time to step out of your comfort zone and embrace the unknown adventure. Keep an open mind, trust your intuition, and don't be bound by past experiences."
    },
    "The Magician": {
        "meaning": "Willpower, creativity, focus, skill",
        "interpretation": "The Magician symbolizes that you have all the tools and abilities needed to achieve your goals. Now is the time to act, use your skills and willpower to create the reality you want."
    },
    "The High Priestess": {
        "meaning": "Intuition, mystery, inner wisdom, subconscious",
        "interpretation": "The High Priestess reminds you to listen to your inner voice. The answers are within you, gain insight through meditation and introspection. Trust your intuition, it will guide you to the right path."
    },
    "The Empress": {
        "meaning": "Fertility, motherhood, creativity, nature",
        "interpretation": "The Empress represents a period of abundance and creativity. This is a time to harvest results and enjoy the beauty of life. Focus on your creative projects and nurture the people and things you love."
    },
    "The Emperor": {
        "meaning": "Authority, structure, control, stability",
        "interpretation": "The Emperor symbolizes order and stability. Now you need to establish clear goals and structured plans. Exercise your leadership abilities and create a safe and stable environment for yourself and others."
    },
    "The Hierophant": {
        "meaning": "Tradition, spiritual guidance, learning, morality",
        "interpretation": "The Hierophant reminds you to seek wisdom and guidance. You may need to learn from experienced people or re-examine traditional values. Education and spiritual growth are important to you now."
    },
    "The Lovers": {
        "meaning": "Love, relationships, choices, harmony",
        "interpretation": "The Lovers card indicates that important relationships or choices are coming. This may involve love, friendship, or important life decisions. Follow your heart and make choices that align with your values."
    },
    "The Chariot": {
        "meaning": "Willpower, victory, determination, control",
        "interpretation": "The Chariot symbolizes victory through willpower and determination. Now is the time to overcome obstacles and advance your goals. Stay focused and disciplined, success is ahead."
    },
    "Strength": {
        "meaning": "Inner strength, courage, patience, self-control",
        "interpretation": "The Strength card reminds you that true strength comes from within. Handle difficult situations with gentleness and patience, not with violence or anger. You are stronger than you think."
    },
    "The Hermit": {
        "meaning": "Introspection, seeking truth, guidance, solitude",
        "interpretation": "The Hermit suggests you need some alone time to reflect and find answers. Temporarily withdraw from the noise of the outside world and gain wisdom and guidance through introspection."
    },
    "Wheel of Fortune": {
        "meaning": "Fate, change, cycles, opportunity",
        "interpretation": "The Wheel of Fortune indicates that major changes in life are coming. These changes may be beyond your control, but they bring new opportunities. Keep an open mind and adapt to change."
    },
    "Justice": {
        "meaning": "Fairness, balance, truth, karma",
        "interpretation": "The Justice card reminds you to handle things fairly and honestly. Your actions will have corresponding consequences, now is the time to take responsibility and seek balance."
    },
    "The Hanged Man": {
        "meaning": "Sacrifice, waiting, different perspective, pause",
        "interpretation": "The Hanged Man suggests you need to look at the situation from a different angle. Sometimes pausing and waiting is wiser than rushing into action. This pause will bring new insights."
    },
    "Death": {
        "meaning": "Transformation, endings, rebirth, release",
        "interpretation": "Death represents major transformation and new beginnings. Some things need to end to make room for new things. Embrace change, it will bring growth and rebirth."
    },
    "Temperance": {
        "meaning": "Balance, patience, moderation, harmony",
        "interpretation": "The Temperance card reminds you to seek balance and harmony in life. Patiently integrate different elements, avoid extremes, and find the middle way."
    },
    "The Devil": {
        "meaning": "Bondage, temptation, materialism, addiction",
        "interpretation": "The Devil card warns that you may be bound or troubled by certain things. Examine your dependencies and bad habits, remember you have the power to break free from these bonds. Freedom is in your hands."
    },
    "The Tower": {
        "meaning": "Sudden change, destruction, revelation, awakening",
        "interpretation": "The Tower represents sudden change and the collapse of old structures. While this may be unsettling, it clears the way for real growth and new beginnings."
    },
    "The Star": {
        "meaning": "Hope, inspiration, healing, guidance",
        "interpretation": "The Star card brings hope and inspiration. After experiencing difficulties, now is the time to heal and find direction again. Believe in the future and maintain an optimistic attitude."
    },
    "The Moon": {
        "meaning": "Illusion, intuition, fear, subconscious",
        "interpretation": "The Moon card reminds you to be careful of illusions and self-deception. Trust your intuition, but also rationally analyze the situation. Face your fears, they are often not as scary as they seem."
    },
    "The Sun": {
        "meaning": "Joy, success, vitality, enlightenment",
        "interpretation": "The Sun card brings positive energy and success. This is a period of happiness, achievement, and celebration. Enjoy the beauty of life and share your joy."
    },
    "Judgement": {
        "meaning": "Rebirth, inner calling, forgiveness, awakening",
        "interpretation": "The Judgement card represents spiritual awakening and rebirth. Listen to your inner calling and prepare to welcome a new stage of life. Forgive the past and embrace the future."
    },
    "The World": {
        "meaning": "Completion, achievement, journey's end, fulfillment",
        "interpretation": "The World card represents the achievement of goals and the completion of a journey. You have reached an important milestone, now you can enjoy success and prepare for the beginning of the next cycle."
    }
}

# Tarot Game Functions


def interpret_tarot_card(card_name):
    """Generate tarot card interpretation"""
    if card_name in TAROT_CARDS:
        card_info = TAROT_CARDS[card_name]
        interpretation = f"""
🔮 **You drew: {card_name}**

**Meaning:** {card_info['meaning']}

**Interpretation:** {card_info['interpretation']}

May this card bring you insight and guidance. Remember, tarot cards are just tools - the real answers lie within your heart. ✨
        """.strip()
        return interpretation
    return "Unknown card"

# Zodiac Signs Data
ZODIAC_SIGNS = {
    "Aries": "♈ Aries (March 21 - April 19)",
    "Taurus": "♉ Taurus (April 20 - May 20)", 
    "Gemini": "♊ Gemini (May 21 - June 20)",
    "Cancer": "♋ Cancer (June 21 - July 22)",
    "Leo": "♌ Leo (July 23 - August 22)",
    "Virgo": "♍ Virgo (August 23 - September 22)",
    "Libra": "♎ Libra (September 23 - October 22)",
    "Scorpio": "♏ Scorpio (October 23 - November 21)",
    "Sagittarius": "♐ Sagittarius (November 22 - December 21)",
    "Capricorn": "♑ Capricorn (December 22 - January 19)",
    "Aquarius": "♒ Aquarius (January 20 - February 18)",
    "Pisces": "♓ Pisces (February 19 - March 20)"
}

def generate_horoscope(zodiac_sign):
    """Generate horoscope for selected zodiac sign"""
    today = datetime.datetime.now().strftime("%B %d, %Y")
    
    horoscope = f"""
🌟 **{ZODIAC_SIGNS[zodiac_sign]} - Daily Horoscope for {today}**

**Overall Rating:** ⭐⭐⭐⭐☆ (4/5 stars)

**💖 Love & Relationships:**
The stars align favorably for matters of the heart today. Single {zodiac_sign}s may find meaningful connections through unexpected encounters. Those in relationships should focus on open communication and understanding.

**💼 Career & Studies:**
Your natural talents shine bright today. It's an excellent time to showcase your skills and take initiative on important projects. Trust your instincts when making professional decisions.

**💰 Financial Fortune:**
Exercise caution with major purchases today. Small investments or savings plans initiated now may yield positive results in the future. Focus on building long-term financial stability.

**🌿 Health & Wellness:**
Pay attention to your body's signals and maintain a balanced lifestyle. Light exercise and proper hydration will boost your energy levels throughout the day.

**🍀 Lucky Elements:**
- Lucky Numbers: 7, 14, 23
- Lucky Color: Emerald Green
- Lucky Direction: Southeast

**✨ Daily Affirmation:**
"I embrace the opportunities that come my way and trust in my ability to make positive choices."

May the cosmic energy guide you toward prosperity and happiness! 🌟
    """.strip()
    
    return horoscope

# Memory System Functions
def extract_user_info(message):
    """Extract important user information from messages"""
    user_info = {}
    
    # Extract age first (to avoid conflicts with name patterns)
    age_patterns = [
        r"i am (\d+) years old",
        r"i'm (\d+) years old",
        r"my age is (\d+)",
        r"(\d+) years old"
    ]
    
    for pattern in age_patterns:
        match = re.search(pattern, message.lower())
        if match:
            user_info['age'] = match.group(1)
            break
    
    # Extract name patterns (more specific to avoid age conflicts)
    name_patterns = [
        r"my name is ([a-zA-Z]+)",
        r"call me ([a-zA-Z]+)",
        r"i'm ([a-zA-Z]+)(?:\s|,|\.|\sand)",  # Don't capture if followed by numbers
        r"i am ([a-zA-Z]+)(?:\s|,|\.|\sand)",
        # Chinese patterns (commented out for English interface)
        # r"名字是(\w+)",
        # r"我叫(\w+)", 
        # r"我是(\w+)"
    ]
    
    for pattern in name_patterns:
        match = re.search(pattern, message.lower())
        if match:
            name = match.group(1)
            # Make sure it's not a number or age-related
            if not name.isdigit() and name not in ['years', 'old']:
                user_info['name'] = name.capitalize()
                break
    
    # Extract location
    location_patterns = [
        r"i live in ([a-zA-Z]+)",
        r"i'm from ([a-zA-Z]+)",
        r"i am from ([a-zA-Z]+)"
    ]
    
    for pattern in location_patterns:
        match = re.search(pattern, message.lower())
        if match:
            user_info['location'] = match.group(1).capitalize()
            break
    
    # Extract preferences
    if 'favorite' in message.lower() or 'like' in message.lower():
        if 'color' in message.lower():
            color_match = re.search(r'favorite color is (\w+)', message.lower())
            if color_match:
                user_info['favorite_color'] = color_match.group(1)
        
        if 'food' in message.lower():
            food_match = re.search(r'favorite food is ([^.]+)', message.lower())
            if food_match:
                user_info['favorite_food'] = food_match.group(1).strip()
    
    return user_info

def update_memory(user_info):
    """Update the memory with new user information"""
    if 'user_memory' not in st.session_state:
        st.session_state.user_memory = {}
    
    for key, value in user_info.items():
        st.session_state.user_memory[key] = value

def get_memory_context():
    """Get memory context to add to system prompt"""
    if 'user_memory' not in st.session_state or not st.session_state.user_memory:
        return ""
    
    memory_items = []
    for key, value in st.session_state.user_memory.items():
        if key == 'name':
            memory_items.append(f"The user's name is {value}")
        elif key == 'age':
            memory_items.append(f"The user is {value} years old")
        elif key == 'location':
            memory_items.append(f"The user lives in {value}")
        elif key == 'favorite_color':
            memory_items.append(f"The user's favorite color is {value}")
        elif key == 'favorite_food':
            memory_items.append(f"The user's favorite food is {value}")
    
    if memory_items:
        return f"\n\nIMPORTANT - Remember these details about the user:\n" + "\n".join(f"- {item}" for item in memory_items) + "\nUse this information naturally in your responses when appropriate."
    
    return ""

# Configure the page first (must be the first Streamlit command)
st.set_page_config(
    page_title="Lucky AI",
    page_icon="🍀",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
    .stChatMessage {
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .user-message {
        background-color: #e6f3ff;
    }
    .assistant-message {
        background-color: #f0f0f0;
    }
    
    /* Typewriter cursor effect */
    .typewriter-cursor {
        animation: blink 1s infinite;
        color: #333;
        font-weight: bold;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
    
    /* Smooth text appearance */
    .streaming-text {
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        line-height: 1.6;
    }
    
    /* File upload area styling */
    .file-upload-container {
        background-color: #f8f9fa;
        border: 2px dashed #dee2e6;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .file-upload-container:hover {
        border-color: #007bff;
        background-color: #f0f8ff;
    }
    
    /* File upload success styling */
    .file-success {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 10px;
        margin: 5px 0;
    }
    
    /* Voice input styling */
    .voice-button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        color: white;
        border: none;
        border-radius: 50%;
        padding: 15px;
        transition: all 0.3s ease;
    }
    
    .voice-button:hover {
        transform: scale(1.1);
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
    }
    
    .recording-indicator {
        animation: pulse 2s infinite;
        color: #ff4444;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    /* Chat input area enhancement */
    .chat-input-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Define AI role templates
role_templates = {
    "Programming Tutor": {
        "prompt": "You are a patient programming tutor who explains complex concepts in simple, understandable ways. You are skilled in multiple programming languages, can provide clear code examples, help students understand programming principles, and give practical programming advice and best practices.",
        "temp": 0.6,
        "max_tokens": 300
    },
    "Creative Writing Assistant": {
        "prompt": "You are a creative writing partner who helps users with story creation, poetry writing, and various forms of literary creation. You can provide plot suggestions, character development ideas, writing techniques, and inspire users' creative inspiration.",
        "temp": 0.8,
        "max_tokens": 300
    },
    "Language Learning Partner": {
        "prompt": "You are a language learning assistant who converses with users in the target language and corrects mistakes. You can explain grammar rules, provide vocabulary suggestions, conduct conversation practice, and help users improve their language skills in an encouraging way.",
        "temp": 0.7,
        "max_tokens": 250
    },
    "Data Analyst": {
        "prompt": "You are skilled at explaining data and charts, helping users understand the meaning behind data. You can perform data analysis, provide statistical insights, explain trends and patterns, and give data-driven advice and conclusions.",
        "temp": 0.5,
        "max_tokens": 280
    }
}

# Point to the local server
with st.sidebar:
    st.header("💬 New Chat")
    
    # Start new conversation button
    if st.button("Start New Chat", use_container_width=True):
        # Get current assistant config
        if "selected_assistant" in st.session_state:
            current_assistant = st.session_state["selected_assistant"]
        else:
            current_assistant = "Programming Tutor"
        
        assistant_config = role_templates[current_assistant]
        st.session_state.messages = [
            {"role": "system", "content": assistant_config["prompt"]},
            {"role": "assistant", "content": f"👋 Hello! I'm your {current_assistant} assistant. Ready to help you achieve your goals! What would you like to work on today?"}
        ]
        st.session_state["current_assistant"] = current_assistant
        st.rerun()
    
    st.divider()  # Add separator line
    
    st.header("🤖 AI Assistant Type")
    
    selected_role = st.selectbox(
        "Choose AI Role:",
        options=list(role_templates.keys()),
        index=0
    )
    
    # Store selected assistant in session state
    st.session_state["selected_assistant"] = selected_role
    
    # Get selected assistant settings
    assistant_config = role_templates[selected_role]
    
    st.divider()  # Add separator line
    
    st.header("🔮 Daily Fortune")
    
    # Daily fortune feature
    if st.button("✨ Check Today's Fortune", use_container_width=True):
        import random
        import datetime
        
        # Fortune categories and messages
        fortunes = {
            "Love": ["💕 Love is in the air today!", "💖 Your heart will find its way!", "💝 A romantic surprise awaits you!"],
            "Career": ["💼 Great opportunities are coming your way!", "📈 Your hard work will pay off today!", "🎯 Focus brings success today!"],
            "Health": ["🌱 Your energy levels are high today!", "💪 Take care of your body and mind!", "🧘 Balance is key to your wellbeing!"],
            "Money": ["💰 Financial luck is on your side!", "💎 A wise investment opportunity may appear!", "🪙 Save wisely, spend thoughtfully!"],
            "General": ["🌟 Today is full of possibilities!", "🍀 Luck follows you wherever you go!", "🌈 A beautiful day awaits you!"]
        }
        
        # Generate seed based on current date for consistent daily fortune
        today = datetime.date.today()
        random.seed(str(today))
        
        # Select random category and fortune
        category = random.choice(list(fortunes.keys()))
        fortune_message = random.choice(fortunes[category])
        
        # Display fortune
        st.success(f"**{category} Fortune:** {fortune_message}")
        
        # Add some mystical elements
        luck_score = random.randint(1, 100)
        st.info(f"🎲 Today's Luck Score: {luck_score}/100")
        
        lucky_numbers = random.sample(range(1, 50), 3)
        st.info(f"🔢 Lucky Numbers: {', '.join(map(str, lucky_numbers))}")
    
    st.header("📝 Chat History")
    
    # Memory Display Section
    st.markdown("### 🧠 Memory")
    if "user_memory" in st.session_state and st.session_state.user_memory:
        memory = st.session_state.user_memory
        
        # Display remembered information
        if memory.get("name"):
            st.markdown(f"**Name:** {memory['name']}")
        if memory.get("age"):
            st.markdown(f"**Age:** {memory['age']} years old")
        if memory.get("location"):
            st.markdown(f"**Location:** {memory['location']}")
        if memory.get("favorite_color"):
            st.markdown(f"**Favorite Color:** {memory['favorite_color']}")
        if memory.get("favorite_food"):
            st.markdown(f"**Favorite Food:** {memory['favorite_food']}")
        
        # Clear memory button
        if st.button("🧹 Clear Memory", use_container_width=True):
            st.session_state.user_memory = {}
            st.rerun()
    else:
        st.markdown("*No information remembered yet*")
    
    st.divider()
    
    # Clear conversation button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        # Get current assistant config
        if "selected_assistant" in st.session_state:
            current_assistant = st.session_state["selected_assistant"]
        else:
            current_assistant = "Programming Tutor"
        
        assistant_config = role_templates[current_assistant]
        st.session_state.messages = [
            {"role": "system", "content": assistant_config["prompt"]},
            {"role": "assistant", "content": f"Hello! I'm your {current_assistant} assistant. How can I help you today?"}
        ]
        st.rerun()  # Rerun to refresh interface
    
    # Display conversation history
    st.subheader("Recent Conversations")
    if "messages" in st.session_state and len(st.session_state.messages) > 1:
        # Extract recent user questions as conversation titles
        user_messages = [msg for msg in st.session_state.messages if msg["role"] == "user"]
        
        if user_messages:
            st.write("Recent chats:")
            # Display last 5 user questions
            for i, msg in enumerate(user_messages[-5:]):
                # Truncate to first 30 characters as title
                title = msg["content"][:30] + "..." if len(msg["content"]) > 30 else msg["content"]
                st.text(f"• {title}")
        else:
            st.write("No chat history available")
    else:
        st.write("No chat history available")
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
st.title("🍀 Lucky AI")
st.caption("🚀 Your Personal AI Assistant with Tarot Reading & Advanced Memory")

# Initialize messages with system prompt based on selected assistant  
if "messages" not in st.session_state:
    # Use the first role as default
    default_role = list(role_templates.keys())[0]
    default_config = role_templates[default_role]
    st.session_state["messages"] = [
        {"role": "system", "content": default_config["prompt"]},
        {"role": "assistant", "content": f"Hello! I'm your {default_role} assistant. How can I help you today?"}
    ]

# Update system prompt if assistant type changed
if "current_assistant" not in st.session_state or st.session_state["current_assistant"] != selected_role:
    st.session_state["current_assistant"] = selected_role
    st.session_state["messages"] = [
        {"role": "system", "content": assistant_config["prompt"]},
        {"role": "assistant", "content": f"Hello! I'm your {selected_role} assistant. How can I help you today?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Fortune Games - Floating horizontal layout above chat input
st.markdown("---")  # Separator line

# Initialize game mode if not exists
if "fortune_game_mode" not in st.session_state:
    st.session_state.fortune_game_mode = "tarot"

with st.container():
    # Create columns for title and refresh button
    col_title, col_refresh = st.columns([6, 1])
    
    with col_title:
        if st.session_state.fortune_game_mode == "tarot":
            st.markdown("### 🔮 Come and seek your fortune!")
            st.info("💡 **Try the Tarot game!** Type 'tarot reading' or '塔罗牌抽签' in the chat to start your mystical journey!")
            st.markdown("Let the ancient wisdom of tarot cards reveal what destiny has in store for you! ✨")
        else:
            st.markdown("### ⭐ Check your zodiac fortune!")
            st.info("💡 **Try the Horoscope game!** Type 'horoscope' or 'zodiac' in the chat to get your daily fortune!")
            st.markdown("Discover what the stars have planned for your zodiac sign today! 🌟")
    
    with col_refresh:
        if st.button("🔄", help="Switch between fortune games", key="switch_game"):
            if st.session_state.fortune_game_mode == "tarot":
                st.session_state.fortune_game_mode = "horoscope"
            else:
                st.session_state.fortune_game_mode = "tarot"
            st.rerun()

st.markdown("---")  # Separator line

# Enhanced Chat Input with Voice Recording Feature
st.markdown("### 💬 Chat Input")

# Create input area with voice recording
col_input, col_voice = st.columns([4, 1])

with col_input:
    prompt = st.chat_input("Type your message here...")

with col_voice:
    # Voice input button with enhanced styling
    voice_active = st.button(
        "🎤", 
        help="Click to activate voice input", 
        use_container_width=True,
        type="secondary"
    )

# Voice input modal/expander
if voice_active:
    with st.expander("�️ Voice Input", expanded=True):
        st.markdown("**Voice Recording Interface**")
        
        col_record, col_stop, col_send = st.columns(3)
        
        with col_record:
            if st.button("🔴 Record", use_container_width=True, type="primary"):
                st.session_state["recording"] = True
                st.success("🎤 Recording started...")
        
        with col_stop:
            if st.button("⏹️ Stop", use_container_width=True):
                st.session_state["recording"] = False
                st.info("⏹️ Recording stopped")
        
        with col_send:
            if st.button("📤 Send", use_container_width=True, type="secondary"):
                # Simulate voice-to-text conversion
                voice_text = "Hello, this is a voice message converted to text."
                st.success(f"✅ Voice message: '{voice_text}'")
                st.session_state.messages.append({"role": "user", "content": f"[Voice Message] {voice_text}"})
                st.rerun()
        
        # Recording status indicator
        if st.session_state.get("recording", False):
            st.markdown("🔴 **RECORDING...** Speak now!")
            st.progress(0.7)  # Simulate recording progress
        else:
            st.markdown("⚪ Ready to record")
        
        # Voice input instructions
        st.markdown("""
        **How to use voice input:**
        1. 🎤 Click 'Record' to start recording
        2. 🗣️ Speak your message clearly
        3. ⏹️ Click 'Stop' when finished
        4. 📤 Click 'Send' to add to chat
        
        *Note: This is a demo interface. Full implementation would require speech-to-text integration.*
        """)

# Handle any pending tarot card selection (in case of page refresh)
if st.session_state.get("tarot_active", False) and "tarot_cards" in st.session_state:
    with st.chat_message("assistant"):
        st.markdown("🔮 Please select a card to continue your tarot reading...")
        
        # Display card selection
        cols = st.columns(6)
        
        for i in range(min(18, len(st.session_state.tarot_cards))):
            col_idx = i % 6
            with cols[col_idx]:
                if st.button("🎴", key=f"pending_tarot_card_{i}", help="Click to select this card"):
                    selected_card = st.session_state.tarot_cards[i]
                    interpretation = interpret_tarot_card(selected_card)
                    
                    # Add tarot result to messages
                    st.session_state.messages.append({"role": "assistant", "content": interpretation})
                    
                    # Clear tarot state
                    st.session_state.tarot_active = False
                    if "tarot_cards" in st.session_state:
                        del st.session_state.tarot_cards
                    
                    st.rerun()

# Handle any pending horoscope selection (in case of page refresh)
if st.session_state.get("horoscope_active", False):
    with st.chat_message("assistant"):
        st.markdown("⭐ Please select your zodiac sign to continue your horoscope reading...")
        
        # Display zodiac sign selection
        cols = st.columns(4)
        
        for i, (sign, display_name) in enumerate(ZODIAC_SIGNS.items()):
            col_idx = i % 4
            with cols[col_idx]:
                if st.button(display_name, key=f"pending_zodiac_{sign}", use_container_width=True):
                    horoscope = generate_horoscope(sign)
                    
                    # Add horoscope result to messages
                    st.session_state.messages.append({"role": "assistant", "content": horoscope})
                    st.session_state.horoscope_active = False
                    st.rerun()

# Process text input
if prompt:
    # Check for tarot card request
    if "塔罗牌抽签" in prompt or "tarot reading" in prompt.lower() or "tarot" in prompt.lower():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Initialize tarot session state
        if "tarot_active" not in st.session_state:
            st.session_state.tarot_active = True
            st.session_state.tarot_cards = list(TAROT_CARDS.keys())
            random.shuffle(st.session_state.tarot_cards)
        
        # Display tarot card selection
        with st.chat_message("assistant"):
            st.markdown("🔮 Welcome to the mystical world of Tarot!")
            st.markdown("Please select a card below and let the universe reveal the answers for you...")
            
            # Display card selection
            cols = st.columns(6)
            
            for i in range(min(18, len(st.session_state.tarot_cards))):  # Display 18 cards (3 rows)
                col_idx = i % 6
                with cols[col_idx]:
                    if st.button("🎴", key=f"tarot_card_{i}", help="Click to select this card"):
                        selected_card = st.session_state.tarot_cards[i]
                        interpretation = interpret_tarot_card(selected_card)
                        
                        # Add tarot result to messages and display immediately
                        st.session_state.messages.append({"role": "assistant", "content": interpretation})
                        
                        # Clear tarot state
                        st.session_state.tarot_active = False
                        if "tarot_cards" in st.session_state:
                            del st.session_state.tarot_cards
                        
                        st.rerun()
    
    # Check for horoscope request
    elif "horoscope" in prompt.lower() or "zodiac" in prompt.lower() or any(sign.lower() in prompt.lower() for sign in ZODIAC_SIGNS.keys()):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Initialize horoscope session state
        if "horoscope_active" not in st.session_state:
            st.session_state.horoscope_active = True
        
        # Display zodiac sign selection
        with st.chat_message("assistant"):
            st.markdown("⭐ Welcome to your personal horoscope reading!")
            st.markdown("Please select your zodiac sign to discover your daily fortune...")
            
            # Display zodiac sign selection in a grid
            cols = st.columns(4)
            
            for i, (sign, display_name) in enumerate(ZODIAC_SIGNS.items()):
                col_idx = i % 4
                with cols[col_idx]:
                    if st.button(display_name, key=f"zodiac_{sign}", use_container_width=True):
                        horoscope = generate_horoscope(sign)
                        
                        # Add to messages and clear horoscope state
                        st.session_state.messages.append({"role": "assistant", "content": horoscope})
                        st.session_state.horoscope_active = False
                        st.rerun()
    
    elif not st.session_state.get("tarot_active", False) and not st.session_state.get("horoscope_active", False):
        # Normal chat processing (only if no fortune games are active)
        # Extract and update user information from the message
        user_info = extract_user_info(prompt)
        if user_info:
            update_memory(user_info)
            # Show a subtle notification about remembered information
            memory_items = [f"{k}: {v}" for k, v in user_info.items()]
            st.info(f"💭 Remembered: {', '.join(memory_items)}")
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Get current assistant configuration
        current_assistant = st.session_state.get("selected_assistant", "Programming Tutor")
        current_config = role_templates[current_assistant]
        
        # Create enhanced messages with memory context
        enhanced_messages = st.session_state.messages.copy()
        
        # Update system message with memory context
        memory_context = get_memory_context()
        if enhanced_messages and enhanced_messages[0]["role"] == "system":
            enhanced_messages[0]["content"] = current_config["prompt"] + memory_context
        
        # Create API call with streaming enabled using assistant's default settings
        response = client.chat.completions.create(
            model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
            messages=enhanced_messages,
            temperature=current_config["temp"],
            max_tokens=current_config["max_tokens"],
            stream=True,  # Enable streaming for typewriter effect
        )

        # Create message container for enhanced typewriter effect
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Stream the response with realistic typewriter effect
            try:
                for chunk in response:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        # Display with animated cursor effect using custom CSS class
                        message_placeholder.markdown(
                            f'<div class="streaming-text">{full_response}<span class="typewriter-cursor">▌</span></div>', 
                            unsafe_allow_html=True
                        )
                        # Add small delay for more realistic typing effect
                        import time
                        time.sleep(0.01)
            except Exception as e:
                st.error(f"Error in streaming: {e}")
                full_response = "Sorry, there was an error generating the response."
            
            # Remove cursor and show final clean response
            message_placeholder.markdown(f'<div class="streaming-text">{full_response}</div>', unsafe_allow_html=True)
        
        # Add the complete response to session state
        st.session_state.messages.append({"role": "assistant", "content": full_response})