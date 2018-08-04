import pygame

# 1 innitilize
pygame.init()

pygame.display.set_caption("pong game")

# 2 Set up game window
size = (600, 600)
BG_COLOR = (98, 244, 66)
canvas = pygame.display.set_mode(size)

clock = pygame.time.Clock()

paddle_image = pygame.image.load("assets/paddle.png")
ball_image = pygame.image.load("assets/ball.png")

x1 = 0
y1 = 100

x2 = 570
y2 = 100

x3 = 300
y3 = 300

w_pressed = False
s_pressed = False
o_pressed = False
l_pressed = False
ball_v_x = 2
ball_v_y = 2
loop = True


while loop:
#     pooling
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False # action => exit game
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_pressed = True
            if e.key == pygame.K_o:
                o_pressed = True
            if e.key == pygame.K_s:
                s_pressed = True
            if e.key == pygame.K_l:
                l_pressed = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_pressed = False
            if e.key == pygame.K_o:
                o_pressed = False
            if e.key == pygame.K_s:
                s_pressed = False
            if e.key == pygame.K_l:
                l_pressed = False
    if w_pressed:
        y1 -= 5
    if s_pressed:
        y1 += 5
    if o_pressed:
        y2 -= 5
    if l_pressed:
        y2 += 5
    if x3 >= 570 or x3 <= 0:
        ball_v_x = -ball_v_x
    if y3 >= 601 or y3 <= 0:
        ball_v_y = -ball_v_y

    x3 += ball_v_x
    y3 += ball_v_y

    # x3 -= 2
    # y3 += 0

    # x3 += 0
    # y3 += 2

    # x3 += 0
    # y3 -= 2

    # x3 -= 2
    # y3 -= 2

    # x3 += 2
    # y3 += 2

    # x3 += 2
    # y3 -= 2

    # x3 -= 2
    # y3 += 2

    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image, (x2, y2))
    canvas.blit(ball_image, (x3, y3))
    clock.tick(60)
    pygame.display.flip()