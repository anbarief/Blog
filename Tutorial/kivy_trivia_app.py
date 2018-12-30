import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty


trivias = (("What is the capital city of Singapore?", ["Singapore", \
                                                       "Bukit Timah", \
                                                       "Raffles Place", \
                                                       "Orchard Road"], "Singapore") , \
           ("What year is Indonesia's Independence?", ["1946", \
                                                        "1964", \
                                                        "1945", \
                                                        "1899"], "1945") , \
           ("What is ASEAN stands for?", ["Asia's Economic Analogy", \
                                          "Association of East Asian", \
                                          "Association of Southeast Asian Nations", \
                                          "None of the above"], "Association of Southeast Asian Nations"), \
           ("Who is the first vice president of Indonesia?", ["Agus Salim", \
                                                              "Ahmad Dahlan", \
                                                              "Soekarno", \
                                                              "Mohammad Hatta"], "Mohammad Hatta"), \
           ("Which one is a data type in Python?", ["if statement", \
                                                    "for statement", \
                                                    "string", \
                                                    "looping"], "string"), \
           ("In what year was ASEAN created?", ["1876", \
                                                "1934", \
                                                "1985", \
                                                "1967"], "1967"),
            )

nt = len(trivias)

class OptionButton(Button):
    #Class for each option button
    def __init__(self, option):
        super().__init__(text = option)
        self.text_size = (self.width, None)

    def on_release(self):
        #Method called when an option is pressed
        super().on_release()
        if self.parent.answer == self.text:
            self.parent.parent.newquestion()
    

class Question(Label):
    #Class for the question label
    pass


class Options(GridLayout):
    #Class of Grid layout to contain the 4 option buttons
    options = ListProperty([""])

    def __init__(self, options, answer):
        super().__init__(rows = 2, cols = 2)
        self.a = OptionButton(option = options[0])
        self.b = OptionButton(option = options[1])
        self.c = OptionButton(option = options[2])
        self.d = OptionButton(option = options[3])
        self.add_widget(self.a)
        self.add_widget(self.b)
        self.add_widget(self.c)
        self.add_widget(self.d)
        self.answer = answer
        self.options = options
        
    def on_options(self, instance, new_options):
        self.a.text = new_options[0]
        self.b.text = new_options[1]
        self.c.text = new_options[2]
        self.d.text = new_options[3]


class AppGrid(FloatLayout):
    #This class will be used for root widget to contain the question and 4 options
    def __init__(self):
        super().__init__()
        self.rand = random.randint(0, nt-1)
        self.question = Question(text = trivias[self.rand][0])
        self.choices = Options(trivias[self.rand][1], trivias[self.rand][2])
        self.add_widget(self.question)
        self.add_widget(self.choices)
        self.question.size_hint = (0.5, 0.3)
        self.question.pos_hint = {'x': 0.25, 'y': 0.7}
        self.choices.size_hint = (0.5, 0.6)
        self.choices.pos_hint = {'x': 0.25, 'y': 0.1}
        
    def newquestion(self):
        #Method used to pick a new question
        rand = random.randint(0, nt-1)
        while rand == self.rand:
            rand = random.randint(0, nt-1)
        self.rand = rand
            
        self.question.text = trivias[self.rand][0]
        self.choices.options = trivias[self.rand][1]
        self.choices.answer = trivias[self.rand][2]

        
class TriviaApp(App):
    def build(self):
        root = AppGrid()
        return root

app = TriviaApp()
app.run()
