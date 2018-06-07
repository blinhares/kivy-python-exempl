import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager #para funcionar o gerenciamento de telas
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
####### MODULO NESCESSÁRIO PARA O EXEMPLO ######
from kivy.core.window import Window

Window.softinput_mode = 'below_target' #PARA QUE O TECLADO N ESCONDA OS INPUT
Window.clearcolor =[1,1,1,1] #ALTERA A COR DE FUNDO PARA BRANCO


################## OS COMANDOS DEVERÃO DESR INSERIDOS DENTRO DE CADA CLASSE SCREEN ENVOLVIDA #############
class TelaDois(Screen):
########################################################################################################################################################################
#################### PERMITE QUE O BOTÃO VOLTAR DO ANDROID OU ESC SEJAM UTILIZADOS PARA A MUDANÇA DE TELAS #############################################################
########################################################################################################################################################################
    ###### USAR EVENDO DE ENTRADA ###
    ##QUANDO O EVENTO OCORRER , CHAMAR A FUNC VOLTAR ###
    def on_pre_enter(self, *args):
        #DEFINIR EVENTO DE TECLADO
        Window.bind(on_keyboard=self.voltar)

    def voltar (sel,window, key,*args):
        #SE A TECLA FOR esc ENTAO
        if key == 27:
            #RETORNA O APP QUE ESTA RODANDO
            App.get_running_app().root.current = "tum"    #AQUI SE MUDA A JANELA QUE SE DESEJA
        return True #significa que tudo terminou bem

    #DEFINIR COMANDO NA SAIDA
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

########################################################################################################################################################################
#################### PERMITE QUE O BOTÃO VOLTAR DO ANDROID OU ESC SEJAM UTILIZADOS PARA A MUDANÇA DE TELAS #############################################################
########################################################################################################################################################################
class GerTela(ScreenManager):
    def __init__(self, **kwargs):
        super(GerTela, self).__init__(**kwargs)


class MenuApp(App):
    def build(self):
        return GerTela()

janela = MenuApp()
janela.run()