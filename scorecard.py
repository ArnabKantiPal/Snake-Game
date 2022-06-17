from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",10,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(0 , 270)
        self.write(f"Score : {self.score}" , align=ALIGN  , font=FONT)
        self.hideturtle()
    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)
    def game_over(self):
        self.goto(0 , 0)
        self.write("game over" , align=ALIGN  , font=  ("Arial", 20 ,"normal"))
