import pygame
import random

# ---------- Init ----------
pygame.init()

# ---------- Colors ----------
white = (255, 255, 255)
black = (0, 0, 0)
red   = (213, 50, 80)
blue  = (50, 153, 213)

# ---------- Screen ----------
dis_width, dis_height = 800, 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Balla')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_score(score):
    text = font.render("Score: " + str(score), True, white)
    dis.blit(text, (10, 10))

def gameLoop():
    # ---- Paddle ----
    paddle_len = 120
    paddle_thickness = 6
    paddle_speed = 7
    paddle_x = (dis_width - paddle_len) // 2
    paddle_y = dis_height - 60

    # ---- Box (outlined) ----
    box_size = 40
    box_x = random.randint(0, dis_width - box_size)
    box_y = random.randint(0, dis_height - 200)

    # ---- Ball (bouncing) ----
    ball_r = 10
    ball_x = dis_width // 2
    ball_y = dis_height // 2
    ball_dx = random.choice([-1, 1]) * 5
    ball_dy = random.choice([-1, 1]) * 4

    score = 0
    running = True
    while running:
        # ---- Events ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # ---- Paddle movement (track velocity) ----
        keys = pygame.key.get_pressed()
        prev_paddle_x = paddle_x
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            paddle_x += paddle_speed
        paddle_x = max(0, min(paddle_x, dis_width - paddle_len))
        paddle_vx = paddle_x - prev_paddle_x  # pixels this frame

        # ---- Ball movement ----
        ball_x += ball_dx
        ball_y += ball_dy

        # ---- Wall bounces ----
        if ball_x - ball_r <= 0:
            ball_x = ball_r
            ball_dx *= -1
        elif ball_x + ball_r >= dis_width:
            ball_x = dis_width - ball_r
            ball_dx *= -1

        if ball_y - ball_r <= 0:
            ball_y = ball_r
            ball_dy *= -1

        # ---- Paddle collision: circle-rect + steering ----
        paddle_rect = pygame.Rect(paddle_x, paddle_y - paddle_thickness//2,
                                  paddle_len, paddle_thickness)

        if ball_dy > 0:  # only when moving down
            # closest point on paddle to ball center
            closest_x = max(paddle_rect.left, min(ball_x, paddle_rect.right))
            closest_y = max(paddle_rect.top,  min(ball_y, paddle_rect.bottom))
            dx = ball_x - closest_x
            dy = ball_y - closest_y
            if dx*dx + dy*dy <= ball_r * ball_r:
                ball_y = paddle_rect.top - ball_r - 0.1
                ball_dy = -abs(ball_dy)
                hit_offset = (ball_x - paddle_rect.centerx) / (paddle_len / 2)  # -1..1
                ball_dx += hit_offset * 3.5
                ball_dx += paddle_vx * 0.5
                max_speed = 9
                if ball_dx >  max_speed: ball_dx =  max_speed
                if ball_dx < -max_speed: ball_dx = -max_speed

        # ---- Bottom bounce ----
        if ball_y + ball_r >= dis_height:
            ball_y = dis_height - ball_r
            ball_dy *= -1

        # ---- Scoring: ball vs box ----
        box_rect = pygame.Rect(box_x, box_y, box_size, box_size)
        # circle-rect check
        closest_x = max(box_rect.left, min(ball_x, box_rect.right))
        closest_y = max(box_rect.top,  min(ball_y, box_rect.bottom))
        dx = ball_x - closest_x
        dy = ball_y - closest_y
        if dx*dx + dy*dy <= ball_r * ball_r:
            score += 1
            # spawn new box
            box_x = random.randint(0, dis_width - box_size)
            box_y = random.randint(0, dis_height - 200)

        # ---- Draw ----
        dis.fill(black)
        pygame.draw.line(dis, white, (paddle_x, paddle_y),
                         (paddle_x + paddle_len, paddle_y), paddle_thickness)
        pygame.draw.rect(dis, red, box_rect, 3)  # outlined box
        pygame.draw.circle(dis, blue, (int(ball_x), int(ball_y)), ball_r)
        draw_score(score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    gameLoop()

