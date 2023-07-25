import matplotlib.pyplot as plt
import kivy
kivy.require('2.1.0')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.add_widget(Label(text = 'Hi there!'))
        self.add_widget(MyButton())


class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.text = 'press_me'
    
    def on_release(self):
        Graphic().draw()
        return super().on_release()



class Graphic:

    def draw(self, listx=None, listy=None, nolisty=None):
        """Отрисовываем график по оси X и Y."""

        print('Отрисовываем график по оси X и Y.')
        listx = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        listy = [56.9, 54.2, 53.3, None, None, 49.1, 47.8, 65.9, 65.8]
        nolisty = [None, None, None, 0, 0, None, None, None, None]
        print(listx)
        print(listy)
        fig, ax = plt.subplots()
        ax.plot(listx, listy, 'b|-')
        if nolisty:
            ax.plot(listx, nolisty, 'r|-')
        plt.show()


class MyApp(App):
    def build(self):
        w = MainWindow()
        return w


if __name__ == '__main__':
    MyApp().run()
