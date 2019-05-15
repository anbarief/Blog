from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock

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
            self.parent.game_update = Clock.schedule_interval(self.parent.update, 0.01)
            self.text = "Reset"
        else:
            self.parent.reset()


class Bird(Image):
    def __init__(self):
        super().__init__(source = flappy_down)
        self.height_frac = 0.5 - 0.5*(50/Window.size[1])
        self.fall = 0

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if self.parent.gameover != True:
            self.height_frac += 0.25
            self.source = flappy_up
            self.fall = 0
    
    def update(self):
        self.height_frac += -1/100
        self.fall += 1
        self.pos_hint = {'x': 0.5 - 0.5*(50/Window.size[0]), 'y': self.height_frac}
        if self.source != flappy_down and self.fall == 15:
            self.source = flappy_down


class Game(FloatLayout):
    def __init__(self):
        super().__init__()
        self.gameover = True
        self.start()

    def start(self):
        self.background = Image(source = background_img_address)
        self.bird = Bird()
        self.resetbtn = ResetBtn()
        self.score = Label(text = "0", font_size = 25)

        self.add_widget(self.background)
        self.add_widget(self.bird)
        self.add_widget(self.resetbtn)
        self.add_widget(self.score)
        
        self.background.size_hint = (1, 1)
        self.background.pos_hint = {'x': 0, 'y': 0}
        self.bird.size_hint = (50/Window.size[0], 50/Window.size[1])
        self.bird.pos_hint = {'x': 0.5 - 0.5*(50/Window.size[0]), \
                              'y': 0.5 - 0.5*(50/Window.size[1])}
        self.resetbtn.size_hint = (0.1, 0.1)
        self.resetbtn.pos_hint = {'x': 0.05, 'y': 0.85}
        self.score.size_hint = (0.1, 0.1)
        self.score.pos_hint = {'x': 0.7, 'y': 0.85}

    def update(self, dt):
        score_number = float(self.score.text)
        score_number += 100*dt
        self.score.text = str(int(score_number))
        self.bird.update()

    def reset(self):
        self.gameover = True
        Clock.unschedule(self.game_update)
        self.clear_widgets()
        self.start()


class FlApp(App):
    def build(self):
        g = Game()
        return g


if __name__ == "__main__":
    FlApp().run()
