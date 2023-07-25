import kivy
kivy.require('2.1.0')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.config import Config
print(Config.get('input','mouse'))
Config.set('input', 'mouse', 'mouse,disable_multitouch')
print(Config.get('input','mouse'))

class Helper():
    def help(obj):
        print('\033[1m' + '\033[31m' + str(obj) + '\033[0m')
        print(obj.__dir__())
        for i in obj.__dir__():
            print(i, obj.__getattribute__(i)) \
            # if 'object' not in str(obj.__getattribute__(i)) else None


class MiniButt(Button):
    def __init__(self, **kwargs):
        super(MiniButt, self).__init__(**kwargs)
        self.text = 'mini butt'
        self.size_hint = (None, None)
        self.size = (200, 200)
        # Helper.help(self)
    
    def on_touch_down(self, touch):
        print(touch)
        # Helper.help(touch)
        print(touch.button)
        print('collide_point:', self.collide_point(*touch.pos))
        if self.collide_point(touch.x, touch.y) is False:
            return super(MiniButt, self).on_touch_down(touch)
        if touch.button == 'left':
            self.text = 'левой'
        elif touch.button == 'right':
            self.text = 'правой'
        elif touch.button == 'middle':
            self.text = 'раз, два, три'
        else:
            pass
        return super(MiniButt, self).on_touch_down(touch)




class MainWindow(AnchorLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.add_widget(MiniButt())


class MyApp(App):
    def build(self):
        w = MainWindow()
        return w


if __name__ == '__main__':
    MyApp().run()
