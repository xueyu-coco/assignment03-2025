import pygame
import math
import sys

def main():
    print("Initializing pygame...")
    pygame.init()
    
    print("Creating display...")
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Debug Dance Test")
    
    print("Setting up clock...")
    clock = pygame.time.Clock()
    
    print("Starting main loop...")
    running = True
    frame_count = 0
    
    while running:
        frame_count += 1
        if frame_count % 60 == 0:  # Print every second
            print(f"Frame {frame_count}")
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event received")
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESC pressed")
                    running = False
        
        # Simple drawing
        screen.fill((50, 50, 100))
        
        # Draw a simple animated circle
        time = pygame.time.get_ticks() / 1000.0
        x = 400 + 200 * math.sin(time)
        y = 300 + 100 * math.cos(time * 2)
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 30)
        
        # Draw text
        font = pygame.font.Font(None, 36)
        text = font.render(f"Frame: {frame_count}", True, (255, 255, 255))
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    print("Exiting...")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")