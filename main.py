import turtle
import random

# --- Oyun değişkenleri ---
score = 0
time_left = 10

# --- Ekran değişkenleri ---
drawing_board = turtle.Screen()
drawing_board.setup(width=600,height=600)
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")

# --- Skor göstergesi ---
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-250, 250)
score_display.write(f"Skor: {score}", font=("Arial", 20, "bold"))

# --- Kaplumbağayı rastgele spawn et ---
def spawn_random():
    x = random.randint(-250, 250)
    y = random.randint(-250, 200)
    player.goto(x, y)

# --- Sayaç göstergesi ---
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(110, 250)
timer_display.write(f"Süre: {time_left}", font=("Arial", 20, "bold"))

# --- Kaplumbağa karakteri ---
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# --- Tıklanınca skor artır ---
def click_handler(x, y):
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Skor: {score}", font=("Arial", 20, "bold"))
    spawn_random()

player.onclick(click_handler)

# --- Geri sayım ---
def countdown():
    global time_left
    timer_display.clear()
    if time_left > 0:
        timer_display.write(f"Süre: {time_left}", font=("Arial", 20, "bold"))
        time_left -= 1
        spawn_random()  # her saniye yeni yere geçsin
        drawing_board.ontimer(countdown, 1000)
    else:
        timer_display.write("SÜRE BİTTİ!", font=("Arial", 20, "bold"))
        player.hideturtle()

# --- Oyunu başlat ---
countdown()
drawing_board.mainloop()
