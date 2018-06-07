import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager #para funcionar o gerenciamento de telas
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.core.window import Window

Window.softinput_mode = 'below_target' #PARA QUE O TECLADO N ESCONDA OS INPUT
Window.clearcolor =[1,1,1,1] #ALTERA A COR DE FUNDO PARA BRANCO


class GerTela(ScreenManager):
    def __init__(self, **kwargs):
        super(GerTela, self).__init__(**kwargs)


class MenuApp(App):
    def build(self):
        return GerTela()

janela = MenuApp()
janela.run()