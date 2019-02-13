import turtle

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
        self.damaged_img = turtle.Turtle( shape = damaged_gif )
        self.damaged_img.hideturtle()

        self.img.penup()
        self.damaged_img.penup()

    def lightsaber_attack(self, enemy):
        current_pos = self.img.pos()
        
        self.img.setpos(enemy.img.pos()[0], enemy.img.pos()[1])
        enemy.damaged_img.showturtle()
        enemy.health = enemy.health - self.power

        if enemy.health < 0:
            enemy.img.hideturtle()
            enemy.damaged_img.hideturtle()
        
        self.img.setpos(current_pos[0], current_pos[1])
        enemy.damaged_img.hideturtle()

    def change_pos(self, pos_x, pos_y):
        self.img.setpos(pos_x, pos_y)
        self.damaged_img.setpos(pos_x, pos_y)


class Orc:
    def __init__(self, orcshape_gif):
        self.power = 200
        self.health = 200
        self.img = turtle.Turtle( shape = orcshape_gif )
        self.damaged_img = turtle.Turtle( shape = damaged_gif )
        self.damaged_img.hideturtle()

        self.img.penup()
        self.damaged_img.penup()

    def attack(self, enemy):
        current_pos = self.img.pos()
        
        self.img.setpos(enemy.img.pos()[0], enemy.img.pos()[1])
        enemy.damaged_img.showturtle()

        enemy.health = enemy.health - self.power

        if enemy.health < 0:
            enemy.img.hideturtle()
            enemy.damaged_img.hideturtle()
        
        self.img.setpos(current_pos[0], current_pos[1])
        enemy.damaged_img.hideturtle()

    def change_pos(self, pos_x, pos_y):
        self.img.setpos(pos_x, pos_y)
        self.damaged_img.setpos(pos_x, pos_y)        

## SIMULATION:      
luke = JediLuke()
redorc = Orc( orc_gif )
darkorc = Orc( darkorc_gif )
luke.change_pos( 200, 0 )
redorc.change_pos( -200, 100 )
darkorc.change_pos( -200, -100 )
