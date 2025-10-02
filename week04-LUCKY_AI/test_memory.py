#!/usr/bin/env python3
"""
Simple test script to verify the memory extraction functionality
"""

import re

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
        r"名字是(\w+)",
        r"我叫(\w+)",
        r"我是(\w+)"
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

# Test cases
test_messages = [
    "Hi, my name is John and I'm 30 years old",
    "I am Alice, I live in Seattle and my favorite color is blue",
    "Call me Bob, I am 25 years old and I'm from Boston",
    "我叫小王",
    "My favorite food is pizza and I like reading books"
]

print("=== Memory Extraction Test ===\n")

for i, message in enumerate(test_messages, 1):
    print(f"Test {i}: {message}")
    extracted = extract_user_info(message)
    print(f"Extracted: {extracted}")
    print("-" * 50)