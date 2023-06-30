import kivy
kivy.require('2.1.0')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.add_widget(Label(text = 'Hi there!'))


class MyApp(App):
    def build(self):
        w = MainWindow()
        return w


if __name__ == '__main__':
    MyApp().run()
