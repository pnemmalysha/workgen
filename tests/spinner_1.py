import kivy
kivy.require('2.1.0')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


class MySpinner(Spinner):
    def __init__(self, **kwargs):
        super(MySpinner, self).__init__(**kwargs)
        self.text='Home'
        self.values=('Home', 'Work', 'Other', 'Custom')
        self.size_hint=(1, None)
        self.height = 44
        # self.size=(100, 44)
        self.pos_hint={'center_x': 0.5, 'center_y': 0.5}
        self.bind(text=self.show_selected_value)
    
    def show_selected_value(self, text, val):
        print('The spinner', self, 'has text', self.text)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.add_widget(MySpinner())
        self.add_widget(MySpinner())


class MyApp(App):
    def build(self):
        w = MainWindow()
        return w


if __name__ == '__main__':
    MyApp().run()
