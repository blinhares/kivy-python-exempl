import kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.factory import Factory


Window.softinput_mode = 'below_target' #PARA QUE O TECLADO N ESCONDA OS INPUT
Window.clearcolor =[1,1,1,1] #ALTERA A COR DE FUNDO PARA BRANCO



class MenuApp(App):

    pass


janela = MenuApp()
janela.run()