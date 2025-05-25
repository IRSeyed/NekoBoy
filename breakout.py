from machine import Pin, I2C
import sh1106
import time

btn_left = Pin(15, Pin.IN, Pin.PULL_UP)
btn_right = Pin(16, Pin.IN, Pin.PULL_UP)

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = sh1106.SH1106_I2C(128, 64, i2c)
oled.sleep(False)
oled.invert(0)

paddle_width = 20
paddle_height = 3
ball_size = 3
screen_width = 128
screen_height = 64

paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 10

ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 1
ball_dy = -1

brick_rows = 3
brick_cols = 8
brick_width = screen_width // brick_cols
brick_height = 5
bricks = [[1 for _ in range(brick_cols)] for _ in range(brick_rows)]

def draw():
    oled.fill(0)

    oled.fill_rect(paddle_x, paddle_y, paddle_width, paddle_height, 1)

    oled.fill_rect(ball_x, ball_y, ball_size, ball_size, 1)

    for row in range(brick_rows):
        for col in range(brick_cols):
            if bricks[row][col]:
                x = col * brick_width
                y = row * brick_height + 2
                oled.fill_rect(x, y, brick_width - 1, brick_height - 1, 1)

    oled.show()

def update_ball():
    global ball_x, ball_y, ball_dx, ball_dy, bricks

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x <= 0 or ball_x + ball_size >= screen_width:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    if (paddle_y <= ball_y + ball_size <= paddle_y + paddle_height and
            paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_dy *= -1

    for row in range(brick_rows):
        for col in range(brick_cols):
            if bricks[row][col]:
                brick_x = col * brick_width
                brick_y = row * brick_height + 2
                if (brick_x < ball_x < brick_x + brick_width and
                        brick_y < ball_y < brick_y + brick_height):
                    bricks[row][col] = 0
                    ball_dy *= -1
                    return

def update_paddle():
    global paddle_x
    speed = 3

    if not btn_left.value():
        paddle_x += speed
    if not btn_right.value():
        paddle_x -= speed

    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width

while True:
    update_paddle()
    update_ball()
    draw()
    time.sleep(0.02)

    if ball_y > screen_height:
        oled.fill(0)
        oled.text("Game Over", 30, 30, 1)
        oled.show()
        break
