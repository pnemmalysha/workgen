# 

import kivy
kivy.require('2.1.0')

from kivy.app import App
# from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.gridlayout import GridLayout
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
            if 'object' not in str(obj.__getattribute__(i)) else None


class CustomLabel(Label):
    def __init__(self, **kwargs):
        self.text = ''
        self.color = [0, 0, 0, 1]
        super(CustomLabel, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 1, 1, 0.5)
            self.rect = Rectangle(size = self.size, pos = self.pos)

        def update_rect(instance, value):
            instance.rect.size = instance.size
            instance.rect.pos = instance.pos
            # Helper.help(self)
            # Helper.help(self.rect)

        self.bind(pos=update_rect, size=update_rect)


class LeftCol_Left(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol_Left, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [1, 1, 1, 1]
        self.spacing = 1
        # Helper.help(self)

        self.add_widget(CustomLabel(text = "Имя ОСП"))
        self.add_widget(CustomLabel(text = "Дата"))
        self.add_widget(CustomLabel(text = "Имя wap"))
        self.add_widget(CustomLabel(text = "MAC wap"))
        self.add_widget(CustomLabel(text = "Модель wap"))
        self.add_widget(CustomLabel(text = "Порт на sw"))
        self.add_widget(CustomLabel(text = "Имя sw"))
        self.add_widget(CustomLabel(text = "Модель sw"))
        self.add_widget(CustomLabel(text = "SN sw"))


class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.multiline = False
        self.write_tab = False


class LeftCol_Right(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol_Right, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(CustomTextInput(text = "LeftCol_Right_1"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_2"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_3"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_4"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_5"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_6"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_7"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_8"))
        self.add_widget(CustomTextInput(text = "LeftCol_Right_9"))



class LeftCol(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol, self).__init__(**kwargs)

        self.add_widget(LeftCol_Left(size_hint=(.5, 1)))
        self.add_widget(LeftCol_Right())


class RigthCol_Top(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthCol_Top, self).__init__(**kwargs)
        # Helper.help(self)

        self.add_widget(Button(text = "RigthCol\n_Top_1"))
        self.add_widget(Button(text = "RigthCol\n_Top_2"))
        self.add_widget(Button(text = "RigthCol\n_Top_3"))
        self.add_widget(Button(text = "RigthCol\n_Top_4"))


class RigthCol(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthCol, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(RigthCol_Top(size_hint_y = 0.2))
        self.add_widget(Button(text = "RigthCol"))


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.add_widget(LeftCol())
        self.add_widget(RigthCol())


class FlexLabel(Label):
    def __init__(self, **kwargs):
        super(FlexLabel, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = self.texture_size

        def update_label(instance, value):
            instance.size = instance.texture_size

        self.bind(texture_size=update_label)


class Signature(AnchorLayout):
    def __init__(self, **kwargs):
        super(Signature, self).__init__(**kwargs)
        self.anchor_x = 'right'
        self.anchor_y = 'bottom'
        self.padding = [5, 5, 5, 5]
        my_lbl = FlexLabel(text = 'Misha was here',
                       color = [1, 1, 1, 0.2])
        self.add_widget(my_lbl)


class RootWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWindow, self).__init__(**kwargs)

        self.add_widget(MainWindow())
        self.add_widget(Signature())



class WorkGenApp(App):
    def build(self):
        w = RootWindow()
        return w


if __name__ == '__main__':
    WorkGenApp().run()
