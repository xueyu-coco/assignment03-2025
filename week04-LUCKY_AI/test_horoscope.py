#!/usr/bin/env python3
"""
Test Horoscope functionality
"""

import datetime

# Test zodiac signs data
ZODIAC_SIGNS = {
    "aries": "Aries ♈",
    "taurus": "Taurus ♉", 
    "gemini": "Gemini ♊",
    "cancer": "Cancer ♋",
    "leo": "Leo ♌",
    "virgo": "Virgo ♍",
    "libra": "Libra ♎", 
    "scorpio": "Scorpio ♏",
    "sagittarius": "Sagittarius ♐",
    "capricorn": "Capricorn ♑",
    "aquarius": "Aquarius ♒",
    "pisces": "Pisces ♓"
}

def test_horoscope_triggers():
    """Test different trigger phrases for horoscope"""
    test_phrases = [
        "horoscope",
        "zodiac",
        "HOROSCOPE",
        "aries",
        "I want my horoscope",
        "tell me about virgo"
    ]
    
    print("=== Testing Horoscope Trigger Phrases ===\n")
    
    for phrase in test_phrases:
        if ("horoscope" in phrase.lower() or 
            "zodiac" in phrase.lower() or 
            any(sign.lower() in phrase.lower() for sign in ZODIAC_SIGNS.keys())):
            print(f"✅ '{phrase}' - TRIGGERS horoscope reading")
        else:
            print(f"❌ '{phrase}' - does NOT trigger")
    print()

def generate_sample_horoscope(sign):
    """Generate a sample horoscope"""
    today = datetime.datetime.now().strftime("%B %d, %Y")
    horoscope = f"""
🌟 **{ZODIAC_SIGNS[sign]} - Daily Horoscope for {today}**

**Overall Fortune:** ⭐⭐⭐⭐☆ (4/5 stars)

**Love & Relationships:** 💕
Today brings harmony to your relationships. Single? Keep your eyes open for meaningful connections.

**Career & Studies:** 💼  
Your hard work is starting to pay off. Focus on collaborative projects and networking.

**Financial Insight:** 💰
Be cautious with major purchases. It's a good day for budgeting and financial planning.

**Health & Wellness:** 🌿
Pay attention to your mental health. Take time for relaxation and self-care.

**Lucky Numbers:** 7, 14, 23
**Lucky Color:** Deep Blue 💙

Remember, you create your own destiny! ✨
    """.strip()
    return horoscope

# Run tests
test_horoscope_triggers()

# Generate sample horoscope
print("=== Sample Horoscope Generation ===\n")
sample_horoscope = generate_sample_horoscope("leo")
print(sample_horoscope)