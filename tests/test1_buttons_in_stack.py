import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput


class MainWindow(StackLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)


        for i in range(25):
            btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.333))
            self.add_widget(btn)


class WorkGenApp(App):
    def build(self):
        w = MainWindow()
        return w


if __name__ == '__main__':
    WorkGenApp().run()
