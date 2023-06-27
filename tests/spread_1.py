import kivy
kivy.require('2.1.0')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle


class Helper():
    def help(obj):
        print('\033[1m' + '\033[31m' + str(obj) + '\033[0m')
        print(obj.__dir__())
        for i in obj.__dir__():
            print(i, obj.__getattribute__(i)) \
            # if 'object' not in str(obj.__getattribute__(i)) else None


# class LeftCol(BoxLayout):
#     def __init__(self, mainwindow, **kwargs):
#         super(LeftCol, self).__init__(**kwargs)

#         lcl = LeftCol_Left(mainwindow, size_hint=(.5, 1))
#         self.add_widget(lcl)
#         self.add_widget(LeftCol_Right(mainwindow))

class RigthRigthCol(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthRigthCol, self).__init__(**kwargs)

        self.rrrc_1 = Button()
        self.rrrc_1.text = '1'
        self.add_widget(self.rrrc_1)
        self.rrrc_2 = Button()
        self.rrrc_2.text = '2'
        self.add_widget(self.rrrc_2)
        self.rrrc_3 = Button()
        self.rrrc_3.text = '3'
        self.add_widget(self.rrrc_3)
        self.rrrc_3.bind(on_press=self.backbackaway)

    def backbackaway(self, instance):
        # нажатием влиять на кнопку, определенную на два класса Layout выше
        # self.rrrc_3.text = 'back\nback\naway\naffect'
        # self.parent.orientation = 'horizontal'
        self.parent.parent.lc.text = 'back\nback\naway\naffect'
        self.parent.parent.orientation = 'vertical'




class RigthCol(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthCol, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.rrc_top = Button()
        self.rrc_top.text = 'top'
        self.add_widget(self.rrc_top)
        self.rrc_bottom = RigthRigthCol()
        # self.rrc_bottom.text = '2'
        self.add_widget(self.rrc_bottom)

        self.rrc_top.bind(on_press=self.backcallback)
        # Helper.help(self)

    def backcallback(self, instance):
        # нажатием влиять на кнопку, определенную в вышестоящем классе Layout
        self.parent.lc.text = 'back to the future'
        Helper.help(self)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.bank = {'OSP': {'label': "Имя ОСП", 'data': "Новосибирск РЦ"},
                     'SWMODEL': {'label': "Модель sw", 'data': "Cisco"},
                     }

        self.lc = Button()
        self.lc.text = 'kiss my ass'
        self.add_widget(self.lc)
        self.rc = Button()
        self.rc.text = '[ PRESS ME ]'
        self.add_widget(self.rc)
        self.rrc = RigthCol()
        self.add_widget(self.rrc)

        self.rc.bind(on_press=self.callback)

    def callback(self, instance):
        print(f'The button {instance.text} is being pressed')
        # нажатие влияет на кнопку в том же классе Layout
        if self.lc.text == 'kiss my ass':
            self.lc.text = 'no way...'
        else:
            self.lc.text = 'kiss my ass'
        # нажатием влиять на кнопку, определенную в нижележащем классе Layout
        pass
        self.rrc.rrc_top.text = 'top, it is work!'







class RootWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWindow, self).__init__(**kwargs)

        self.add_widget(MainWindow())


class WorkGenApp(App):
    def build(self):
        w = RootWindow()
        return w


if __name__ == '__main__':
    WorkGenApp().run()
