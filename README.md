<h1 align="center">🕹️ NekoBoy Games</h1>
<p align="center">MicroPython for a 3D-Printed Pico Game Console</p>

---

## 🐾 What is NekoBoy?

**NekoBoy** is a compact and adorable DIY handheld game console with a cat-inspired 3D-printed design.  
It’s powered by a Raspberry Pi Pico, a 1.3" SH1106 OLED display, and two push buttons.

This project is perfect for learning **MicroPython** and building simple retro-style games with limited controls.

🔗 3D model available on Thingiverse:  
👉 [NekoBoy on Thingiverse](https://www.thingiverse.com/thing:7047175)

---

## 🧰 Hardware Used

| Component                   | Description                     |
|----------------------------|---------------------------------|
| Microcontroller            | Raspberry Pi Pico               |
| Display                    | 1.3" SH1106 I2C OLED            |
| Inputs                     | 2× Push Buttons                 |
| Power & Programming        | Micro USB Cable                 |
| Enclosure                  | 3D-Printed NekoBoy Case         |

---

## 🔌 Wiring (Pinout)

| Function        | OLED Pin | Pico Pin   |
|----------------|----------|------------|
| I2C Clock      | SCL      | **GP1**    |
| I2C Data       | SDA      | **GP0**    |
| Left Button    | -        | **GP15**   |
| Right Button   | -        | **GP16**   |

> ⚠️ Make sure buttons use internal pull-ups or configure with `Pin.PULL_UP` in code.

---

## 🎮 Included Games

### 🎹 `bongocat.py`
Tap the buttons to animate a bongo-playing cat!  
Just for fun and a cuteness overload 😸

---

### 🧱 `breakout.py`
A basic version of the classic **Breakout / Arkanoid** game.  
Move the paddle, bounce the ball, and break those bricks!

---

### 🦖 `dino.py`
A simple remake of the **Chrome Dino** game.  
Jump over obstacles and survive as long as you can!

---

## 🚀 How to Run

1. Flash your Pico with the latest MicroPython firmware
2. Wire the hardware according to the pinout
3. Copy the game `.py` file(s) and any extra assets to your Pico using **Thonny**
4. Power on the console and enjoy playing!

---
