#!/usr/bin/env python3
"""
Test Tarot Card functionality in English
"""

import random

# Test the English tarot cards
TAROT_CARDS = {
    "The Fool": {
        "meaning": "New beginnings, innocence, spontaneity, free spirit",
        "interpretation": "The Fool represents a new journey and infinite possibilities. It's time to step out of your comfort zone and embrace the unknown adventure."
    },
    "The Magician": {
        "meaning": "Willpower, creativity, focus, skill", 
        "interpretation": "The Magician symbolizes that you have all the tools and abilities needed to achieve your goals."
    },
    "The High Priestess": {
        "meaning": "Intuition, mystery, inner wisdom, subconscious",
        "interpretation": "The High Priestess reminds you to listen to your inner voice. Trust your intuition, it will guide you to the right path."
    }
}

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

def test_tarot_triggers():
    """Test different trigger phrases"""
    test_phrases = [
        "tarot reading",
        "tarot",
        "TAROT READING",
        "塔罗牌抽签",
        "I want a tarot reading"
    ]
    
    print("=== Testing Tarot Trigger Phrases ===\n")
    
    for phrase in test_phrases:
        if "塔罗牌抽签" in phrase or "tarot reading" in phrase.lower() or "tarot" in phrase.lower():
            print(f"✅ '{phrase}' - TRIGGERS tarot reading")
        else:
            print(f"❌ '{phrase}' - does NOT trigger")
    print()

def simulate_card_draw():
    """Simulate drawing a random card"""
    card_names = list(TAROT_CARDS.keys())
    selected_card = random.choice(card_names)
    interpretation = interpret_tarot_card(selected_card)
    
    print("=== Simulated Tarot Card Draw ===\n")
    print(interpretation)

# Run tests
test_tarot_triggers()
simulate_card_draw()