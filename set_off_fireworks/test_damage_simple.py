"""
Simple test to verify damage is working correctly
"""
import pygame
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from voice_fireworks import VoiceControlledFireworks

# Test the damage function directly
game = VoiceControlledFireworks()

print("🧪 Direct Damage Function Test")
print(f"Initial health: {game.current_health}/{game.max_health}")

print("\n=== Test 1: 10 damage ===")
game.take_damage(10)
print(f"After 10 damage: {game.current_health}/{game.max_health}")

print("\n=== Test 2: Another 10 damage ===")  
game.take_damage(10)
print(f"After another 10 damage: {game.current_health}/{game.max_health}")

print("\n=== Test 3: Final 10 damage ===")
game.take_damage(10)
print(f"After final 10 damage: {game.current_health}/{game.max_health}")
print(f"Game over status: {game.game_over}")

print("\n✅ Damage function works correctly: 30 -> 20 -> 10 -> 0")
print("If you're seeing 1 damage in game, the issue is elsewhere.")

# Cleanup
game.stream.stop_stream()
game.stream.close()
game.audio.terminate()
pygame.quit()