import pygame
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from voice_fireworks import VoiceControlledFireworks

class HealthTestGame(VoiceControlledFireworks):
    def __init__(self):
        super().__init__()
        self.test_phase = 0
        self.test_timer = 0
        self.damage_dealt = 0
        
    def run_health_test(self):
        """Run health system test"""
        try:
            running = True
            clock = pygame.time.Clock()
            
            print(f"🩺 Health Test Started!")
            print(f"🎯 Initial Health: {self.current_health}/{self.max_health}")
            
            while running:
                dt = clock.tick(60) / 1000.0  # Convert to seconds
                self.test_timer += dt
                
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # Manual damage test
                            print(f"💥 Manual damage test: Taking 10 damage")
                            print(f"📊 Before: {self.current_health}/{self.max_health}")
                            self.take_damage(10)
                            self.damage_dealt += 10
                            print(f"📊 After: {self.current_health}/{self.max_health}")
                            print(f"📊 Total damage dealt: {self.damage_dealt}")
                            print("=" * 50)
                        elif event.key == pygame.K_r:
                            # Reset health
                            print("🔄 Resetting health to full")
                            self.reset_game()
                            self.damage_dealt = 0
                
                # Automatic damage test every 3 seconds
                if self.test_timer >= 3.0 and self.current_health > 0:
                    print(f"⏰ Automatic damage test: Taking 10 damage")
                    print(f"📊 Before: {self.current_health}/{self.max_health}")
                    self.take_damage(10)
                    self.damage_dealt += 10
                    print(f"📊 After: {self.current_health}/{self.max_health}")
                    print(f"📊 Total damage dealt: {self.damage_dealt}")
                    print("=" * 50)
                    self.test_timer = 0
                
                # Update and draw
                self.update_background()
                
                # Draw health bar
                self.draw_health_bar()
                
                # Draw instructions
                font = pygame.font.Font(None, 36)
                instructions = [
                    "Health System Test",
                    f"Current Health: {self.current_health}/{self.max_health}",
                    f"Total Damage Dealt: {self.damage_dealt}",
                    "",
                    "SPACE = Manual 10 damage",
                    "R = Reset health to full",
                    "ESC = Exit"
                ]
                
                for i, text in enumerate(instructions):
                    if text:
                        color = (255, 255, 255)
                        if "Current Health" in text:
                            if self.current_health <= 10:
                                color = (255, 0, 0)  # Red for low health
                            elif self.current_health <= 20:
                                color = (255, 255, 0)  # Yellow for medium health
                            else:
                                color = (0, 255, 0)  # Green for high health
                        
                        text_surface = font.render(text, True, color)
                        self.screen.blit(text_surface, (50, 50 + i * 40))
                
                # Game over message
                if self.game_over:
                    font_large = pygame.font.Font(None, 72)
                    game_over_text = font_large.render("GAME OVER", True, (255, 0, 0))
                    text_rect = game_over_text.get_rect(center=(self.width//2, self.height//2))
                    self.screen.blit(game_over_text, text_rect)
                
                pygame.display.flip()
                
        except KeyboardInterrupt:
            print("\n🩺 Health test interrupted!")
        finally:
            # Cleanup
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            pygame.quit()

if __name__ == "__main__":
    try:
        print("🩺 Starting Health System Test...")
        print("📋 This will test if damage is correctly applied")
        print("🎯 Expected: 10 damage per hit, 3 hits to game over (30 -> 20 -> 10 -> 0)")
        
        test_game = HealthTestGame()
        test_game.run_health_test()
        
    except Exception as e:
        print(f"❌ Health test failed: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")