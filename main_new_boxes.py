import kivy
kivy.require('2.1.0')

from kivy.app import App
# from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput



class LeftCol_Left(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol_Left, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # check what attributes is
        print(self.__dir__())
        for i in self.__dir__():
            print(i, self.__getattribute__(i))

        self.add_widget(Button(text = "LeftCol_Left_1"))
        self.add_widget(Button(text = "LeftCol_Left_2"))
        self.add_widget(Button(text = "LeftCol_Left_3"))
        self.add_widget(Button(text = "LeftCol_Left_4"))
        self.add_widget(Button(text = "LeftCol_Left_5"))
        self.add_widget(Button(text = "LeftCol_Left_6"))
        self.add_widget(Button(text = "LeftCol_Left_7"))
        self.add_widget(Button(text = "LeftCol_Left_8"))
        self.add_widget(Button(text = "LeftCol_Left_9"))


class LeftCol_Right(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol_Right, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Button(text = "LeftCol_Right_1"))
        self.add_widget(Button(text = "LeftCol_Right_2"))
        self.add_widget(Button(text = "LeftCol_Right_3"))
        self.add_widget(Button(text = "LeftCol_Right_4"))
        self.add_widget(Button(text = "LeftCol_Right_5"))
        self.add_widget(Button(text = "LeftCol_Right_6"))
        self.add_widget(Button(text = "LeftCol_Right_7"))
        self.add_widget(Button(text = "LeftCol_Right_8"))
        self.add_widget(Button(text = "LeftCol_Right_9"))



class LeftCol(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol, self).__init__(**kwargs)

        self.add_widget(LeftCol_Left(size_hint=(.5, 1)))
        self.add_widget(LeftCol_Right())


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
