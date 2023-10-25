import turtle

# 함수: 글자 그리기
def draw_text(text, font_size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, align="center", font=("Arial", font_size, "normal"))

# Turtle 설정
screen = turtle.Screen()
screen.title("권동영")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(1)  # 그리는 속도 설정

# "권동영" 이름을 직접 그리기
t.color("blue")
t.pensize(5)

# 글자 "권" 그리기
t.penup()
t.goto(0, 0)
t.pendown()
t.goto(0, 100)
t.goto(50, 100)
t.goto(50, 0)
t.penup()
t.goto(100, 100)
t.pendown()
t.goto(50, 100)
t.goto(100, 0)

# 글자 "동" 그리기
t.penup()
t.goto(150, 0)
t.pendown()
t.goto(150, 100)
t.goto(200, 100)
t.goto(200, 0)
t.penup()
t.goto(250, 100)
t.pendown()
t.goto(200, 100)
t.goto(250, 0)

# 글자 "영" 그리기
t.penup()
t.goto(300, 0)
t.pendown()
t.goto(300, 100)
t.goto(350, 100)
t.goto(350, 0)
t.penup()
t.goto(400, 100)
t.pendown()
t.goto(350, 100)
t.goto(400, 0)

# 종료 이벤트 처리
def close_window():
    screen.bye()

screen.onkey(close_window, "Escape")
screen.listen()
turtle.done()
