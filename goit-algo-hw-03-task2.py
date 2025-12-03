import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        new_length = length / 3.0
        
        koch_curve(t, new_length, level - 1)
        t.left(60)
        koch_curve(t, new_length, level - 1)
        t.right(120)
        koch_curve(t, new_length, level - 1)
        t.left(60)
        koch_curve(t, new_length, level - 1)
        
def draw_koch_snowflake(t, length, level):
    for i in range(3):
        koch_curve(t, length, level)
        t.right(120)

def setup_and_run():
    while True:
        try:
            user_level = int(input("Введіть рівень рекурсії для Сніжинки Коха: "))
            if user_level < 0:
                 print("Рівень має бути невід'ємним числом.")
                 continue
            break
        except ValueError:
            print("Некоректний ввід. Будь ласка, введіть ціле число.")
            
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title(f"Сніжинка Коха (Рівень {user_level})")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    
    start_length = 300
    t.goto(-start_length / 2, start_length / (2 * 3**0.5))
    t.pendown()
    t.color("blue")
    
    draw_koch_snowflake(t, start_length, user_level)
    
    screen.mainloop()

if __name__ == "__main__":
    setup_and_run()