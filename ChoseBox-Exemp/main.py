from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class Tarefas (GridLayout):
    pass

class Test(App):
    def build(self):
        return Tarefas()

Test().run()