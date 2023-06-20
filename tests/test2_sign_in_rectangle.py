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
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput


class Helper():
    def help(obj):
        print('\033[1m' + '\033[31m' + str(obj) + '\033[0m')
        print(obj.__dir__())
        for i in obj.__dir__():
            print(i, obj.__getattribute__(i)) \
            if 'object' not in str(obj.__getattribute__(i)) else None


class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)

        self.text = 'Misha was here yesterday'
        self.color = [1, 1, 1, 0.2]
        self.size_hint = (None, None)
        self.size = self.texture_size
        Helper.help(self)

        with self.canvas:
            Color(1, 1, 0, 0.1)
            self.rect = Rectangle(size = self.size, pos = self.pos)

        def update_rect(instance, value):
            instance.rect.size = instance.size
            instance.rect.pos = instance.pos
            Helper.help(self)

        self.bind(pos=update_rect, size=update_rect)

        def update_label(instance, value):
            instance.size = instance.texture_size

        self.bind(texture_size=update_label)




class Signature(AnchorLayout):
    def __init__(self, **kwargs):
        super(Signature, self).__init__(**kwargs)
        self.anchor_x = 'right'
        self.anchor_y = 'bottom'
        my_lbl = MyLabel()
        # Helper.help(my_lbl)
        self.add_widget(my_lbl)
        self.add_widget(Label(text = '_____ was ____'))
        self.add_widget(Button(size_hint = (None, None), size = (40, 30)), index = 3)


class WorkGenApp(App):
    def build(self):
        w = Signature()
        return w


if __name__ == '__main__':
    WorkGenApp().run()
