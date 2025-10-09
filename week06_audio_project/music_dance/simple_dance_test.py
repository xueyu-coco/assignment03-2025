import pygame
import numpy as np
import math
import sys

# Simple test version without librosa
class SimpleDanceTest:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Simple Dance Test")
        self.clock = pygame.time.Clock()
        self.running = True
        self.time = 0
        
    def draw_test_dancer(self, x, y, time_offset=0):
        """Draw a simple animated test dancer"""
        # Body
        body_color = (
            int(128 + 127 * math.sin(self.time + time_offset)),
            int(128 + 127 * math.sin(self.time + time_offset + 1)),
            200
        )
        
        # Head
        pygame.draw.circle(self.screen, body_color, (int(x), int(y - 60)), 20)
        
        # Body
        pygame.draw.rect(self.screen, body_color, (int(x - 15), int(y - 40), 30, 80))
        
        # Arms (animated)
        arm_angle = math.sin(self.time * 3 + time_offset) * 0.8
        arm_length = 40
        left_arm_x = x - math.cos(arm_angle) * arm_length
        left_arm_y = y - 20 + math.sin(arm_angle) * arm_length
        right_arm_x = x + math.cos(arm_angle) * arm_length
        right_arm_y = y - 20 + math.sin(arm_angle) * arm_length
        
        pygame.draw.line(self.screen, body_color, (x, y - 20), (left_arm_x, left_arm_y), 5)
        pygame.draw.line(self.screen, body_color, (x, y - 20), (right_arm_x, right_arm_y), 5)
        
        # Legs (animated)
        leg_angle = math.sin(self.time * 2 + time_offset + 1) * 0.5
        leg_length = 50
        left_leg_x = x - math.cos(leg_angle) * leg_length
        left_leg_y = y + 40 + math.sin(leg_angle) * leg_length
        right_leg_x = x + math.cos(leg_angle) * leg_length
        right_leg_y = y + 40 + math.sin(leg_angle) * leg_length
        
        pygame.draw.line(self.screen, body_color, (x, y + 40), (left_leg_x, left_leg_y), 6)
        pygame.draw.line(self.screen, body_color, (x, y + 40), (right_leg_x, right_leg_y), 6)
    
    def draw_background(self):
        """Draw animated background"""
        # Animated background color
        bg_color = (
            int(30 + 20 * math.sin(self.time * 0.5)),
            int(40 + 30 * math.sin(self.time * 0.7)),
            int(60 + 40 * math.sin(self.time * 0.3))
        )
        self.screen.fill(bg_color)
        
        # Simple spectrum bars
        for i in range(20):
            bar_height = 100 + 150 * math.sin(self.time * 2 + i * 0.3)
            bar_width = 50
            x = i * 60
            y = 800 - bar_height
            
            color = (
                100 + int(155 * (i / 20)),
                100,
                200
            )
            
            pygame.draw.rect(self.screen, color, (x, y, bar_width, bar_height))
    
    def run(self):
        """Main loop"""
        print("Starting Simple Dance Test...")
        print("Press ESC to exit, SPACE to toggle animation")
        
        animate = True
        
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_SPACE:
                        animate = not animate
                        print(f"Animation {'ON' if animate else 'OFF'}")
            
            # Update time
            if animate:
                self.time += 0.05
            
            # Draw everything
            self.draw_background()
            
            # Draw three test dancers
            self.draw_test_dancer(300, 400, 0)      # Left dancer
            self.draw_test_dancer(600, 400, 1)      # Middle dancer  
            self.draw_test_dancer(900, 400, 2)      # Right dancer
            
            # Draw info
            font = pygame.font.Font(None, 48)
            info_text = f"Simple Dance Test - Time: {self.time:.1f}"
            text_surface = font.render(info_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (20, 20))
            
            # Instructions
            font_small = pygame.font.Font(None, 36)
            instructions = [
                "ESC: Exit",
                "SPACE: Toggle Animation",
                "Close window to exit"
            ]
            
            for i, instruction in enumerate(instructions):
                text_surface = font_small.render(instruction, True, (200, 200, 200))
                self.screen.blit(text_surface, (20, 80 + i * 40))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        print("Simple Dance Test completed!")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    test = SimpleDanceTest()
    test.run()