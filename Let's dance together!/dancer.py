import pygame
import numpy as np
import math

class Dancer:
    def __init__(self, x, y, size=50, style="human"):
        self.x = x
        self.y = y
        self.size = size
        self.style = style
        self.joints = {}
        self.dance_move = "idle"
        self.move_progress = 0
        self.color = (255, 255, 255)
        
    def update_dance_move(self, music_features, current_time):
        """Update dance moves based on music features"""
        tempo = music_features.get('tempo', 120)
        energy = music_features.get('energy', 0.5)
        beat_strength = music_features.get('beat_strength', 0)
        
        # Trigger new moves on beat points
        if beat_strength > 0.8:
            moves = ["wave", "spin", "jump", "slide"]
            self.dance_move = np.random.choice(moves)
            self.move_progress = 0
            # Change color based on energy
            self.color = (
                int(energy * 255),
                int((1 - energy) * 255),
                150
            )
        
        self.move_progress += 0.1
        
    def draw(self, screen):
        """Draw the dancer"""
        if self.style == "human":
            self.draw_human_dancer(screen)
        elif self.style == "abstract":
            self.draw_abstract_dancer(screen)
        elif self.style == "robot":
            self.draw_robot_dancer(screen)
    
    def draw_human_dancer(self, screen):
        """Draw human-style dancer"""
        # Body
        body_height = self.size * 1.5
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y - body_height//2)), self.size//3)
        pygame.draw.rect(screen, self.color, (int(self.x - self.size//6), int(self.y - body_height//2), 
                                            self.size//3, body_height))
        
        # Move limbs based on dance moves
        if self.dance_move == "wave":
            arm_angle = math.sin(self.move_progress) * 0.8
            leg_angle = math.sin(self.move_progress + 1) * 0.4
        elif self.dance_move == "spin":
            arm_angle = self.move_progress * 2
            leg_angle = self.move_progress * 2
        else:  # idle
            arm_angle = 0.3
            leg_angle = 0.2
            
        # Arms
        arm_length = self.size * 0.8
        left_arm_x = self.x - math.cos(arm_angle) * arm_length
        left_arm_y = self.y - body_height//4 + math.sin(arm_angle) * arm_length
        right_arm_x = self.x + math.cos(arm_angle) * arm_length  
        right_arm_y = self.y - body_height//4 + math.sin(arm_angle) * arm_length
        
        pygame.draw.line(screen, self.color, (self.x, self.y - body_height//4), 
                         (left_arm_x, left_arm_y), 3)
        pygame.draw.line(screen, self.color, (self.x, self.y - body_height//4), 
                         (right_arm_x, right_arm_y), 3)
        
        # Legs
        leg_length = self.size
        left_leg_x = self.x - math.cos(leg_angle) * leg_length
        left_leg_y = self.y + body_height//2 + math.sin(leg_angle) * leg_length
        right_leg_x = self.x + math.cos(leg_angle) * leg_length
        right_leg_y = self.y + body_height//2 + math.sin(leg_angle) * leg_length
        
        pygame.draw.line(screen, self.color, (self.x, self.y + body_height//2), 
                         (left_leg_x, left_leg_y), 4)
        pygame.draw.line(screen, self.color, (self.x, self.y + body_height//2), 
                         (right_leg_x, right_leg_y), 4)
    
    def draw_abstract_dancer(self, screen):
        """Draw abstract-style dancer"""
        points = []
        for i in range(8):
            angle = i * math.pi/4 + self.move_progress
            radius = self.size * (0.8 + 0.4 * math.sin(self.move_progress + i))
            x = self.x + math.cos(angle) * radius
            y = self.y + math.sin(angle) * radius
            points.append((x, y))
        
        pygame.draw.polygon(screen, self.color, points)
        
    def draw_robot_dancer(self, screen):
        """Draw robot-style dancer"""
        # Implement robot dance style
        body_rect = pygame.Rect(self.x - self.size//2, self.y - self.size, self.size, self.size*1.5)
        pygame.draw.rect(screen, self.color, body_rect)
        
        # Mechanical joint animation
        joint_offset = math.sin(self.move_progress * 2) * 10
        pygame.draw.circle(screen, (200, 200, 200), 
                          (int(self.x), int(self.y - self.size//2 + joint_offset)), 8)