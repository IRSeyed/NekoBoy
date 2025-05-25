# NekoBoy

🕹️ NekoBoy Games – MicroPython for a 3D-Printed Pico Game Console

This repo includes simple MicroPython games built for NekoBoy, a 3D-printed handheld game console powered by a Raspberry Pi Pico, a 1.3" SH1106 OLED display, and two push buttons.

    💡 The 3D design for NekoBoy is available on Thingiverse:
    👉 https://www.thingiverse.com/thing:7047175

🐾 What is NekoBoy?

NekoBoy is a compact and adorable DIY game console with a cat-inspired design. It’s ideal for learning MicroPython and building simple retro-style games with limited controls.
🧰 Hardware Used

    Raspberry Pi Pico

    1.3" SH1106 I2C OLED Display

    2x Push Buttons

    Micro USB cable (for power & code upload)

    3D-printed NekoBoy case (Thingiverse link)

🔌 Wiring (Pinout)
Component	Raspberry Pi Pico Pin
OLED SCL	GP1
OLED SDA	GP0
Button Left	GP15
Button Right	GP16

Make sure your buttons are connected with internal pull-ups (or use PULL_UP in code).
🎮 Included Games
🎹 bongocat.py

Tap the buttons to animate a bongo-playing cat! Just for fun and cuteness overload 😸
🧱 breakout.py

A basic version of the Breakout/Arkanoid game. Move the paddle and keep the ball bouncing!

    📁 This game comes with additional file(s). Be sure to copy all associated files to your Pico.

🦖 dino.py

A simple version of the offline Dino game – jump over obstacles and survive as long as you can!

    📁 May include extra files (like assets or score tracking). Check the folder contents.

🚀 How to Run

    Flash your Pico with the latest MicroPython firmware

    Wire the hardware according to the pinout

    Copy the .py game file (and any required files) to the Pico using Thonny

    Connect your OLED and buttons, and power it on – you're ready to play!
