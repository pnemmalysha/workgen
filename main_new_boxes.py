import kivy
kivy.require('2.1.0')

from kivy.app import App
# from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput



class LeftCol(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol, self).__init__(**kwargs)

        self.add_widget(Button(text = "LeftCol_Left"))
        self.add_widget(Button(text = "LeftCol_Right"))


class RigthCol(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthCol, self).__init__(**kwargs)
        self.add_widget(Button(text = "RigthCol"))


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.add_widget(LeftCol())
        self.add_widget(RigthCol())


class WorkGenApp(App):
    def build(self):
        w = MainWindow()
        return w


if __name__ == '__main__':
    WorkGenApp().run()
