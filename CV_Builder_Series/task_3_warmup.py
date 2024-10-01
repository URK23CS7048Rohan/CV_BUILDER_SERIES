import cv2
import numpy as np
import random
import time

# Constants
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
BALL_RADIUS = 20
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 40
OBSTACLE_SPEED = 10
GROUND_LEVEL = SCREEN_HEIGHT - 50
JUMP_HEIGHT = 80  # Reduced the jump height for better responsiveness
GRAVITY = 10      # Increased gravity for faster descent
FPS = 30

# Game States
RUNNING = 0
GAME_OVER = 1
state = RUNNING

# Initialize game variables
ball_pos = [50, GROUND_LEVEL - BALL_RADIUS]
obstacles = []
obstacle_timer = 0
is_jumping = False
jump_counter = 0
score = 0

# Initialize the screen
screen = np.ones((SCREEN_HEIGHT, SCREEN_WIDTH), dtype=np.uint8) * 255

# Function to draw objects on the screen
def draw_objects():
    global screen, ball_pos, obstacles, score

    # Clear screen
    screen[:] = 255

    # Draw ground
    cv2.line(screen, (0, GROUND_LEVEL), (SCREEN_WIDTH, GROUND_LEVEL), (0, 0, 0), 2)

    # Draw ball (dino)
    cv2.circle(screen, (ball_pos[0], ball_pos[1]), BALL_RADIUS, (0, 0, 0), -1)

    # Draw obstacles
    for obs in obstacles:
        cv2.rectangle(screen, (obs[0], obs[1]), (obs[0] + obs[2], obs[1] + obs[3]), (0, 0, 0), -1)

    # Draw score
    score_text = f'Score: {score}'
    cv2.putText(screen, score_text, (600, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Function to handle the jump physics
def handle_jump():
    global is_jumping, jump_counter, ball_pos

    if is_jumping:
        if jump_counter >= -JUMP_HEIGHT:
            ball_pos[1] = GROUND_LEVEL - BALL_RADIUS - (JUMP_HEIGHT - abs(jump_counter))
            jump_counter -= GRAVITY  # Ball falls faster with increased gravity
        else:
            is_jumping = False
            jump_counter = JUMP_HEIGHT

# Function to handle obstacle movement, spawning, and collision detection
def handle_obstacles():
    global obstacles, score, state, obstacle_timer

    # Move obstacles
    for obs in obstacles:
        obs[0] -= OBSTACLE_SPEED

    # Remove off-screen obstacles
    obstacles = [obs for obs in obstacles if obs[0] + obs[2] > 0]

    # Collision detection
    for obs in obstacles:
        if (obs[0] <= ball_pos[0] <= obs[0] + obs[2] and
            ball_pos[1] + BALL_RADIUS >= obs[1]):
            state = GAME_OVER

    # Spawn new obstacles
    if time.time() - obstacle_timer > random.uniform(1.5, 2.5):
        height = random.randint(30, 70)
        obstacles.append([SCREEN_WIDTH, GROUND_LEVEL - height, OBSTACLE_WIDTH, height])
        obstacle_timer = time.time()

# Function to reset the game
def reset_game():
    global ball_pos, obstacles, is_jumping, jump_counter, score, state, obstacle_timer
    ball_pos = [50, GROUND_LEVEL - BALL_RADIUS]
    obstacles = []
    is_jumping = False
    jump_counter = JUMP_HEIGHT
    score = 0
    state = RUNNING
    obstacle_timer = time.time()

# Main game loop
def game_loop():
    global is_jumping, state, score

    while True:
        if state == GAME_OVER:
            # Display Game Over and Restart instructions
            cv2.putText(screen, 'GAME OVER', (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 - 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
            cv2.putText(screen, 'Press R to Restart or Q to Quit', (SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 2 + 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow('Advanced Dino Game', screen)
            
            key = cv2.waitKey(0) & 0xFF
            if key == ord('r'):
                reset_game()
            elif key == ord('q'):
                break
        else:
            # Increment score over time
            score += 1

            # Handle jumping
            handle_jump()

            # Handle obstacle movement and spawning
            handle_obstacles()

            # Draw objects
            draw_objects()

            # Show the screen
            cv2.imshow('Advanced Dino Game', screen)

            # Check for keypresses
            key = cv2.waitKey(1000 // FPS) & 0xFF
            if key == ord('q'):
                break
            elif key == ord(' '):
                if not is_jumping:
                    is_jumping = True
                    jump_counter = JUMP_HEIGHT

    cv2.destroyAllWindows()

# Start the game loop
reset_game()
game_loop()
