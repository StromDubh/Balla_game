# Balla Game

Balla is a simple arcade-style game built with **Python** and **Pygame**.  
You control a paddle to keep the ball bouncing, while avoiding hazards and collecting points.

---

## Gameplay

- Control the paddle with **Left/Right Arrow Keys** (or **A/D**).
- You can stop the ball with the spacebar. 
- **Green Box** → +1 score when the ball hits it.
- **Red Box** → Lose 1 life when the ball hits it.
- You start with **5 lives**.
- **Game Over** when lives reach 0.
- Press **R** to restart or **ESC** to quit.

### Special Mechanic
- Hold **SPACE** as the ball touches the paddle to **catch/hold** the ball.
- While held, the ball sticks above the paddle and follows it.
- Release **SPACE** to launch the ball upward again.

---

## Installation & Running

1. Make sure you have **Python 3.10+** installed.  
   You can check with:
   ```bash
   python --version

   pip install pygame

   git clone https://github.com/StromDubh/Balla_game.git
cd Balla_game

