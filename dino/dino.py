from machine import Pin, I2C, reset
import sh1106
import framebuf
import time
from sprites import dino, cactoos

# --- پین‌ها ---
jump_button = Pin(15, Pin.IN, Pin.PULL_UP)
reset_button = Pin(16, Pin.IN, Pin.PULL_UP)

# --- OLED ---
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = sh1106.SH1106_I2C(128, 64, i2c, reset_button, 0x3c)
oled.sleep(False)
oled.invert(1)

# --- Framebuffers ---
fb_dino = framebuf.FrameBuffer(dino, 24, 24, framebuf.MONO_HLSB)
fb_cactus = framebuf.FrameBuffer(cactoos, 13, 26, framebuf.MONO_HLSB)

# --- ابعاد ---
dino_w, dino_h = 24, 24
cactus_w, cactus_h = 13, 26

# --- موقعیت‌ها ---
ground_y = 40
xd = 20
yc = 64 - cactus_h
jump_y = ground_y

# --- پرش ---
is_jumping = False
jump_velocity = -7
gravity = 1
initial_jump_velocity = -7
button_was_pressed = False

# --- امتیاز ---
score = 0
cactus_x = 128

def blit_transparent(fb, x_off, y_off, width, height):
    for y in range(height):
        for x in range(width):
            if fb.pixel(x, y):
                oled.pixel(x + x_off, y + y_off, 1)

def pixel_collision(fb1, x1, y1, w1, h1, fb2, x2, y2, w2, h2):
    x_overlap_start = max(x1, x2)
    x_overlap_end = min(x1 + w1, x2 + w2)
    y_overlap_start = max(y1, y2)
    y_overlap_end = min(y1 + h1, y2 + h2)
    for y in range(y_overlap_start, y_overlap_end):
        for x in range(x_overlap_start, x_overlap_end):
            px1 = x - x1
            py1 = y - y1
            px2 = x - x2
            py2 = y - y2
            if fb1.pixel(px1, py1) and fb2.pixel(px2, py2):
                return True
    return False

def draw_game_over():
    oled.fill_rect(20, 20, 88, 24, 1)  # پس‌زمینه سیاه (به خاطر invert)
    oled.text("GAME OVER", 28, 28, 0)  # متن سفید (invert روشنه پس 0 سفیده)
    oled.show()

def draw_score(score):
    oled.text("Score:{}".format(score), 64, 0, 1)
    

def run_game():
    global is_jumping, jump_velocity, jump_y, cactus_x, score

    # مقداردهی اولیه
    is_jumping = False
    jump_velocity = initial_jump_velocity
    jump_y = ground_y
    cactus_x = 128
    score = 0

    while True:
        oled.fill(0)

        # کنترل پرش
        if not jump_button.value() and not is_jumping:
            is_jumping = True
            jump_velocity = initial_jump_velocity

        if is_jumping:
            jump_y += jump_velocity
            jump_velocity += gravity
            if jump_y >= ground_y:
                jump_y = ground_y
                is_jumping = False

        # حرکت کاکتوس
        cactus_x -= 3
        if cactus_x < -cactus_w:
            cactus_x = 128
            score += 1

        # رسم اشیاء
        blit_transparent(fb_dino, xd, jump_y, dino_w, dino_h)
        blit_transparent(fb_cactus, cactus_x, yc, cactus_w, cactus_h)

        # نمایش امتیاز
        oled.text("Score:" + str(score), 70, 0, 1)

        # بررسی برخورد
        if pixel_collision(fb_dino, xd, jump_y, dino_w, dino_h,
                           fb_cactus, cactus_x, yc, cactus_w, cactus_h):
            oled.show()
            draw_game_over()
            break

        oled.show()
        time.sleep(0.03)

# --- حلقه اصلی ---
while True:
    run_game()
    # منتظر فشار دادن دکمه ریست بمون
    while reset_button.value():
        time.sleep(0.01)



