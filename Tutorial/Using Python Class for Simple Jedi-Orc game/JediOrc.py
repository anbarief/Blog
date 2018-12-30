import turtle
import time

jedi_gif = "jedi.gif"
orc_gif = "orc.gif"
darkorc_gif = "darkorc.gif"
damaged_gif = "damaged.gif" 

turtle.register_shape( jedi_gif )
turtle.register_shape( orc_gif )
turtle.register_shape( darkorc_gif )
turtle.register_shape( damaged_gif )

class JediLuke:
    def __init__(self):
        self.power = 200
        self.health = 200

        self.img = turtle.Turtle( shape = jedi_gif )
        self.damaged_img = turtle.Turtle( shape = damaged_gif, visible = False )
    
        self.img.penup()
        self.damaged_img.penup()

    def lightsaber_attack(self, enemy):
        self.img.setpos(enemy.img.pos()[0], enemy.img.pos()[1])
        enemy.damaged_img.showturtle()
        enemy.health += - self.power
        time.sleep(1)

        enemy.damaged_img.hideturtle()
        if enemy.health < 0:
            enemy.img.hideturtle()
        
        self.img.setpos(200, 0)

    def change_pos(self, pos):
        self.img.setpos(pos[0], pos[1])
        self.damaged_img.setpos(pos[0], pos[1] + 150)
       

class Orc:
    def __init__(self, health, gif_image):
        self.power = 100
        self.health = health

        self.img = turtle.Turtle( shape = gif_image )
        self.damaged_img = turtle.Turtle( shape = damaged_gif, visible = False )
    
        self.img.penup()
        self.damaged_img.penup()

    def attack(self, enemy):
        current_pos = self.img.pos()
        self.img.setpos(enemy.img.pos()[0], enemy.img.pos()[1])
        enemy.damaged_img.showturtle()
        enemy.health += - self.power
        
        time.sleep(1)

        enemy.damaged_img.hideturtle()
        if enemy.health < 0:
            enemy.img.hideturtle()

        self.img.setpos(current_pos[0], current_pos[1])

    def change_pos(self, pos):
        self.img.setpos(pos[0], pos[1])
        self.damaged_img.setpos(pos[0], pos[1] + 150)

luke = JediLuke()
luke.change_pos( [200, 0] )
        
orc_1 = Orc( health = 400 , gif_image = orc_gif)
orc_1.change_pos( [-200, 100] )

orc_2 = Orc( health = 200, gif_image = darkorc_gif )
orc_2.change_pos( [-200, -100] )

#Simulation:
# - luke.attack( orc_ 1 )
# - luke.attack( orc_ 2 )
# - orc_2.attack( luke )
