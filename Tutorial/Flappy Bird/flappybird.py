import random
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color

Window.size = (0.7*1368, 0.7*834)
flappy_down = "flappydown.png"
flappy_up = "flappyup.png"
collision = "collision.png"
background_img_address = "blue-ocean.png"


class ResetBtn(Button):
    def __init__(self):
        super().__init__(text = "Start", halign = "center", valign = "center")
        self.pressed_frq = 0
        
    def on_release(self):
        super().on_release()
        self.pressed_frq += 1
            
        if self.pressed_frq == 1:
            self.parent.gameover = False
            self.parent.game_update = Clock.schedule_interval(self.parent.update, 1/60)
            self.text = "Reset"
        else:
            self.parent.reset()
            

class Score(Label):
    def __init__(self):
        super().__init__(text = "0", font_size = 50)
        self.value = 0
        

class Bird(Image):
    def __init__(self):
        super().__init__(source = flappy_down)
        self.height_frac = 0.5
        self.fall = 0

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if not (self.parent.gameover):
            self.height_frac += 0.25
            self.source = flappy_up
            self.fall = 0
        
    def update(self, wall):
        self.fall += 1
        self.height_frac += -1/100
        self.pos_hint = {'x': 0.5, 'y': self.height_frac}
        if self.source != flappy_down and self.fall == 15:
            self.source = flappy_down

        kiwi_windowpos = [self.pos_hint['x']*Window.size[0], \
                          self.pos_hint['y']*Window.size[1]]
        
        if ((wall.pos[0] <=(kiwi_windowpos[0] + 25) <= wall.pos[0] + 50) \
           and (wall.pos[1] <=(kiwi_windowpos[1] + 25) <= wall.pos[1] + wall.size[1])) \
           or (kiwi_windowpos[1] + 25 <= 0) or (kiwi_windowpos[1] + 25 >= Window.size[1]):
            self.parent.gameover = True
            self.parent.game_over()
            
    def show_collision(self):
        image = Image(source = collision)
        self.parent.add_widget(image)
        image.pos_hint = self.pos_hint
        image.size_hint = (0.1, 0.1)

            
class Game(FloatLayout):
    def __init__(self):
        super().__init__()
        self.gameover = True        
        self.start()

    def start(self):
        self.background = Image(source = background_img_address)
        self.score = Score()
        self.resetbtn = ResetBtn()
        self.kiwi = Bird()

        self.add_widget(self.background)
        self.add_widget(self.resetbtn)
        self.add_widget(self.score)
        self.add_widget(self.kiwi)
        
        self.background.size_hint = (1, 1)
        self.background.pos_hint = {'x': 0, 'y': 0}

        self.score.size_hint = (0.25, 0.1)
        self.score.pos_hint = {'x': 0.7, 'y': 0.85}

        self.resetbtn.size_hint = (0.25, 0.1)
        self.resetbtn.pos_hint = {'x': 0.05, 'y': 0.85}
        
        self.kiwi.size_hint = (50/Window.size[0], 50/Window.size[1])
        self.kiwi.pos_hint = {'x': 0.5, 'y': 0.5}
        
        self.walls = []
        self.current_wall = None
        self.add_random_wall()

    def add_random_wall(self):
        height = random.uniform(100, 0.4*Window.size[1])
        pos_y = random.uniform(0, Window.size[1]*0.6)

        color = [random.uniform(0.3, 1) for i in range(4)]
        pos = (Window.size[0]*0.9, pos_y)
        size = (50, height)

        self.rect = Rectangle(pos=pos, size=size)
        self.color = Color(*color)
        self.canvas.add(self.color)
        self.canvas.add(self.rect)
        self.walls.append(self.rect)
        self.current_wall = self.rect

    def game_over(self):
        self.kiwi.show_collision()
        self.label = Label(text = "Game Over", halign = 'right', valign = 'center', font_size = 100)
        self.add_widget(self.label)
        self.label.size_hint = (0.5, 0.2)
        self.label.pos_hint = {'x': 0.25, 'y': 0.4}
        Clock.unschedule(self.game_update)
                    
    def update(self, dt):
        for i in self.walls:
            i.pos = (i.pos[0]-100*dt, i.pos[1])
        self.score.value += 100*dt
        self.score.text = str(int(self.score.value))
        self.walls = [i for i in self.walls if i.pos[0] >= -50]
        if self.walls[-1].pos[0] <= 0.5*Window.size[0] - 70:
            self.add_random_wall()
        self.kiwi.update(self.current_wall)

    def reset(self):
        Clock.unschedule(self.game_update)
        self.clear_widgets()
        self.gameover = True
        self.start()


class FlApp(App):
    def build(self):
        g= Game()
        return g

if __name__ == "__main__":
    FlApp().run()
