#AUTHORS:
#ANA CRISTINO PRIETO
#ANDREA GARCIA RUIZ
#PAULA SANCHEZ SANZ

import pygame
import sys
import random
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BIRD_SIZE = 30
PIPE_WIDTH = 60
PIPE_GAP = 150
PIPE_SPEED = 3
GRAVITY = 0.3
JUMP_STRENGTH = -6

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235) 
GREEN = (34, 139, 34)  
PURPLE = (128, 0, 128) 
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

class GameState(Enum):
    START_SCREEN = 0
    PLAYING = 1
    GAME_OVER = 2

class Bird:
    def __init__(self):
        self.x = WINDOW_WIDTH // 4
        self.y = WINDOW_HEIGHT // 2
        self.velocity = 0
        self.size = BIRD_SIZE
        self.invincible_timer = 0
        
    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Limit falling speed
        if self.velocity > 6:
            self.velocity = 6
        
        # Update invincibility timer
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
    
    def jump(self):
        self.velocity = JUMP_STRENGTH
    
    def draw(self, screen):
        # Flash if invincible
        if self.invincible_timer > 0 and self.invincible_timer % 10 < 5:
            return  # Don't draw bird (flashing effect)
        
        # Draw bird body
        pygame.draw.circle(screen, PURPLE, (int(self.x), int(self.y)), self.size // 2)
        
        # Draw bird eye
        eye_x = int(self.x + 8)
        eye_y = int(self.y - 5)
        pygame.draw.circle(screen, WHITE, (eye_x, eye_y), 6)
        pygame.draw.circle(screen, BLACK, (eye_x + 2, eye_y), 3)
        
        # Draw bird beak
        beak_points = [
            (int(self.x + self.size // 2), int(self.y)),
            (int(self.x + self.size // 2 + 15), int(self.y - 3)),
            (int(self.x + self.size // 2 + 15), int(self.y + 3))
        ]
        pygame.draw.polygon(screen, ORANGE, beak_points)
    
    def make_invincible(self):
        self.invincible_timer = 120  # 2 seconds at 60 FPS
    
    def is_invincible(self):
        return self.invincible_timer > 0
    
    def get_rect(self):
        return pygame.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)

class Pipe:
    def __init__(self, x, gap_size=PIPE_GAP):
        self.x = x
        self.gap_size = gap_size
        self.gap_y = random.randint(100, WINDOW_HEIGHT - self.gap_size - 100)
        self.width = PIPE_WIDTH
        self.passed = False
        
    def update(self):
        self.x -= PIPE_SPEED
    
    def draw(self, screen):
        # Top pipe
        top_pipe_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        pygame.draw.rect(screen, GREEN, top_pipe_rect)
        pygame.draw.rect(screen, BLACK, top_pipe_rect, 2)
        
        # Bottom pipe
        bottom_pipe_rect = pygame.Rect(self.x, self.gap_y + self.gap_size, self.width, WINDOW_HEIGHT - self.gap_y - self.gap_size)
        pygame.draw.rect(screen, GREEN, bottom_pipe_rect)
        pygame.draw.rect(screen, BLACK, bottom_pipe_rect, 2)
        
        # Pipe caps
        cap_height = 30
        cap_width = self.width + 10
        
        # Top cap
        top_cap_rect = pygame.Rect(self.x - 5, self.gap_y - cap_height, cap_width, cap_height)
        pygame.draw.rect(screen, GREEN, top_cap_rect)
        pygame.draw.rect(screen, BLACK, top_cap_rect, 2)
        
        # Bottom cap
        bottom_cap_rect = pygame.Rect(self.x - 5, self.gap_y + self.gap_size, cap_width, cap_height)
        pygame.draw.rect(screen, GREEN, bottom_cap_rect)
        pygame.draw.rect(screen, BLACK, bottom_cap_rect, 2)
    
    def get_rects(self):
        top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        bottom_rect = pygame.Rect(self.x, self.gap_y + self.gap_size, self.width, WINDOW_HEIGHT - self.gap_y - self.gap_size)
        return [top_rect, bottom_rect]
    
    def is_off_screen(self):
        return self.x + self.width < 0

class FlappyBirdGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.lives = 3
        self.game_state = GameState.START_SCREEN
        
        # Spawn first pipe
        self.pipe_timer = 0
        self.pipe_spawn_delay = 90  # frames between pipes
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.game_state == GameState.START_SCREEN:
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                elif self.game_state == GameState.PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()
                elif self.game_state == GameState.GAME_OVER:
                    if event.key == pygame.K_r:
                        self.restart_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_state == GameState.START_SCREEN:
                    self.start_game()
                elif self.game_state == GameState.PLAYING:
                    self.bird.jump()
        return True
    
    def start_game(self):
        self.game_state = GameState.PLAYING
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.lives = 3
        self.pipe_timer = 0
    
    def restart_game(self):
        self.start_game()
    
    def update(self):
        if self.game_state != GameState.PLAYING:
            return
        
        # Update bird
        self.bird.update()
        
        # Check if bird hits ground or ceiling
        if self.bird.y + self.bird.size // 2 >= WINDOW_HEIGHT or self.bird.y - self.bird.size // 2 <= 0:
            if not self.bird.is_invincible():
                self.lose_life()
        
        # Calculate difficulty based on score (faster progression)
        current_gap_size = max(80, PIPE_GAP - (self.score // 2) * 6)  # Reduce gap every 2 points by 6px, minimum 80
        current_spawn_delay = max(40, self.pipe_spawn_delay - (self.score // 3) * 6)  # Increase frequency every 3 points by 6 frames, minimum 40 frames
        
        # Spawn pipes
        self.pipe_timer += 1
        if self.pipe_timer >= current_spawn_delay:
            self.pipes.append(Pipe(WINDOW_WIDTH, current_gap_size))
            self.pipe_timer = 0
        
        # Update pipes
        for pipe in self.pipes[:]:
            pipe.update()
            
            # Check collision
            if not self.bird.is_invincible():
                bird_rect = self.bird.get_rect()
                for pipe_rect in pipe.get_rects():
                    if bird_rect.colliderect(pipe_rect):
                        self.lose_life()
                        break
            
            # Check scoring
            if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                pipe.passed = True
                self.score += 1
            
            # Remove off-screen pipes
            if pipe.is_off_screen():
                self.pipes.remove(pipe)
    
    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_state = GameState.GAME_OVER
        else:
            # Reset bird position and make invincible
            self.bird.y = WINDOW_HEIGHT // 2
            self.bird.velocity = 0
            self.bird.make_invincible()
    
    def draw_hearts(self):
        heart_size = 20
        heart_spacing = 30
        start_x = WINDOW_WIDTH - (self.lives * heart_spacing) - 10
        start_y = 15
        
        for i in range(self.lives):
            heart_x = start_x + (i * heart_spacing)
            self.draw_heart(heart_x, start_y, heart_size)
    
    def draw_heart(self, x, y, size):
        # Draw heart shape using circles and triangle
        half_size = size // 2
        
        # Left circle
        pygame.draw.circle(self.screen, RED, (x - half_size // 2, y), half_size // 2)
        # Right circle  
        pygame.draw.circle(self.screen, RED, (x + half_size // 2, y), half_size // 2)
        
        # Bottom triangle
        triangle_points = [
            (x - half_size, y),
            (x + half_size, y),
            (x, y + half_size)
        ]
        pygame.draw.polygon(self.screen, RED, triangle_points)
    
    def draw_background(self):
        # Sky gradient
        for y in range(WINDOW_HEIGHT):
            color_ratio = y / WINDOW_HEIGHT
            r = int(135 + (255 - 135) * color_ratio)
            g = int(206 + (255 - 206) * color_ratio)
            b = int(235 + (255 - 235) * color_ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (WINDOW_WIDTH, y))
    
    def draw(self):
        self.draw_background()
        
        if self.game_state == GameState.START_SCREEN:
            # Title
            title_text = self.big_font.render("FLAPPY BIRD", True, WHITE)
            title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
            self.screen.blit(title_text, title_rect)
            
            # Instructions
            start_text = self.font.render("Press SPACE or Click to Start", True, WHITE)
            start_rect = start_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(start_text, start_rect)
            
            controls_text = self.font.render("SPACE or Click to Flap", True, WHITE)
            controls_rect = controls_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
            self.screen.blit(controls_text, controls_rect)
            
            # Draw a demo bird
            demo_bird = Bird()
            demo_bird.x = WINDOW_WIDTH // 2
            demo_bird.y = WINDOW_HEIGHT // 2 + 150
            demo_bird.draw(self.screen)
            
        elif self.game_state == GameState.PLAYING:
            # Draw pipes
            for pipe in self.pipes:
                pipe.draw(self.screen)
            
            # Draw bird
            self.bird.draw(self.screen)
            
            # Draw score
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            # Draw difficulty indicator
            current_gap_size = max(80, PIPE_GAP - (self.score // 2) * 6)
            difficulty_level = (PIPE_GAP - current_gap_size) // 6 + 1
            difficulty_text = self.font.render(f"Level: {difficulty_level}", True, WHITE)
            self.screen.blit(difficulty_text, (10, 50))
            
            # Draw hearts (lives)
            self.draw_hearts()
            
        elif self.game_state == GameState.GAME_OVER:
            # Draw pipes and bird (frozen)
            for pipe in self.pipes:
                pipe.draw(self.screen)
            self.bird.draw(self.screen)
            
            # Game over overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Game over text
            game_over_text = self.big_font.render("GAME OVER", True, RED)
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80))
            self.screen.blit(game_over_text, game_over_rect)
            
            # Final score
            final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30))
            self.screen.blit(final_score_text, final_score_rect)
            
            # Final level reached
            final_gap_size = max(80, PIPE_GAP - (self.score // 2) * 6)
            final_level = (PIPE_GAP - final_gap_size) // 6 + 1
            level_text = self.font.render(f"Level Reached: {final_level}", True, WHITE)
            level_rect = level_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
            self.screen.blit(level_text, level_rect)
            
            # Restart instruction
            restart_text = self.font.render("Press R to Restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = FlappyBirdGame()
    game.run()

