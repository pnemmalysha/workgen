import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput


class MainWindow(StackLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.add_widget(Button(text = "Hi there!", size_hint=(None, None)))
        self.add_widget(Button(text = "Hi there 2!!", size_hint=(None, None)))
        self.add_widget(Button(text = "Hi there 3!!!", size_hint=(None, None)))


class WorkGenApp(App):
    def build(self):
        w = MainWindow()
        return w


if __name__ == '__main__':
    WorkGenApp().run()
