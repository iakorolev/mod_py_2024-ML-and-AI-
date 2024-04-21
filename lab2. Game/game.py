from tkinter import *
import random

# Константы
WIDTH = 500  # Ширина окна
HEIGHT = 500  # Высота окна
BG_COLOR = "white"
MAIN_BALL_COLOR = "blue"
MAIN_BALL_RADIUS = 25
BAD_COLOR = "red"
COLORS = [
    "#F0F8FF",
    "burlywood2",
    BAD_COLOR,
    "pink",
    BAD_COLOR,
    "gold",
    "chartreuse",
    BAD_COLOR,
    "darkgreen",
    "gainsboro",
]
NUM_OF_BALLS = 9
MAX_RADIUS = 35
MIN_RADIUS = 15
DELAY = 30
INIT_DX = 1
INIT_DY = 1
ZERO = 0


# Функции и классы для игры

class Ball:

    def __init__(self, x, y, r, color, speedx=1, speedy=1):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.speedx = speedx
        self.speedy = speedy

    def draw(self):
        canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color,
            outline=self.color if self.color != BAD_COLOR else "black",
        )

    def hide(self):
        canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=BG_COLOR,
            outline=BG_COLOR,
        )

    def is_collision(self, ball):
        a = abs(self.x + self.speedx - ball.x)
        b = abs(self.y + self.speedy - ball.y)
        return (a * a + b * b) ** 0.5 <= self.r + ball.r

    def movement(self):
        if (self.x + self.r + self.speedx >= WIDTH) or (
            self.x - self.r + self.speedx <= 0
        ):
            self.speedx = -self.speedx
        if (self.y + self.r + self.speedy >= HEIGHT) or (
            self.y - self.r + self.speedy <= 0
        ):
            self.speedy = -self.speedy
        for ball in balls:
            if self.is_collision(ball):
                if ball.color != BAD_COLOR:
                    ball.hide()
                    balls.remove(ball)
                    self.speedx = -self.speedx
                    self.speedy = -self.speedy
                else:
                    self.speedx = self.speedy = 0
        self.hide()
        self.x += self.speedx
        self.y += self.speedy
        if self.speedx * self.speedy != 0:
            self.draw()

    def move_bad(self):
        if (self.x + self.r + self.speedx >= WIDTH) or (
            self.x - self.r + self.speedx <= 0
        ):
            self.speedx = -self.speedx
        if (self.y + self.r + self.speedy >= HEIGHT) or (
            self.y - self.r + self.speedy <= 0
        ):
            self.speedy = -self.speedy
        for ball in balls:
            if ball != self:
                if self.is_collision(ball):
                    self.speedx = -self.speedx
                    self.speedy = -self.speedy
        self.hide()
        self.x += self.speedx
        self.y += self.speedy
        self.draw()


def click(event):
    global main_ball
    if event.num == 1:
        if "main_ball" not in globals():  # старт
            main_ball = Ball(
                event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, INIT_DX, INIT_DY
            )
            if main_ball.x > WIDTH / 2:
                main_ball.speedx = -main_ball.speedx
            if main_ball.y > HEIGHT / 2:
                main_ball.speedy = -main_ball.speedy
            main_ball.draw()
        else:  # turn left
            if main_ball.speedy * main_ball.speedx > 0:
                main_ball.speedy = -main_ball.speedy
            else:
                main_ball.speedx = -main_ball.speedx
    elif event.num == 3:  # right mouse button: turn right
        if main_ball.speedy * main_ball.speedx > 0:
            main_ball.speedx = -main_ball.speedx
        else:
            main_ball.speedy = -main_ball.speedy


# count the number of bad balls
def count_bad_balls(list_of_balls):
    result = 0
    for ball in list_of_balls:
        if ball.color == BAD_COLOR:
            result += 1
    return result


def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        next_ball = Ball(
            random.choice(range(MAX_RADIUS, WIDTH - MAX_RADIUS)),
            random.choice(range(MAX_RADIUS, HEIGHT - MAX_RADIUS)),
            random.choice(range(MIN_RADIUS, MAX_RADIUS)),
            random.choice(COLORS),
        )
        is_collision = False
        for ball in lst:
            if next_ball.is_collision(ball):
                is_collision = True
                break
        if not is_collision:
            lst.append(next_ball)
            next_ball.draw()
    return lst


def main():
    global main_ball
    if "main_ball" in globals():
        main_ball.movement()
        for ball in balls:
            if ball.color == BAD_COLOR:  # Двигаем только опасные шары
                ball.move_bad()
        if len(balls) - num_of_bad_balls == 0:
            canvas.create_text(
                WIDTH / 2, HEIGHT / 2, text="YOU WON!", font="Arial 20", fill="lime"
            )
            main_ball.speedx = main_ball.speedy = 0
        elif main_ball.speedx * main_ball.speedy == 0:
            canvas.create_text(
                WIDTH / 2, HEIGHT / 2, text="YOU LOSE!", font="Arial 20", fill="red"
            )
    root.after(DELAY, main)


# Tkinter

root = Tk()

x = int((root.winfo_screenwidth() / 2) - (WIDTH / 2))
y = int((root.winfo_screenheight() / 2) - (HEIGHT / 2))

root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

# Окно

root.title("Игра с шарами")

root.bind("<Button-1>", click)
root.bind("<Button-3>", click, "+")

icon = PhotoImage(file="image\icon.png")
root.iconphoto(False, icon)

# Canvas

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
balls = create_list_of_balls(NUM_OF_BALLS)
num_of_bad_balls = count_bad_balls(balls)
main()
if "main_ball" in globals():
    del main_ball
root.mainloop()
