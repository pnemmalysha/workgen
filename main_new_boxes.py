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
    def __init__(self, MainWindow, **kwargs):
        super(LeftCol_Left, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [1, 1, 1, 1]
        self.spacing = 1
        # Helper.help(self)

        self.add_widget(CustomLabel(text = MainWindow.bank['OSP']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['DATE']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['WAPNAME']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['WAPMAC']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['WAPMODEL']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['PORTNUM']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['SWNAME']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['SWMODEL']['label']))
        self.add_widget(CustomLabel(text = MainWindow.bank['SWSN']['label']))


class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.multiline = False
        self.write_tab = False
        # Helper.help(self)


class LeftCol_Right(BoxLayout):
    def __init__(self, MainWindow, **kwargs):
        super(LeftCol_Right, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(CustomTextInput(text = MainWindow.bank['OSP']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['DATE']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['WAPNAME']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['WAPMAC']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['WAPMODEL']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['PORTNUM']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['SWNAME']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['SWMODEL']['data']))
        self.add_widget(CustomTextInput(text = MainWindow.bank['SWSN']['data']))


class LeftCol(BoxLayout):
    def __init__(self, MainWindow, **kwargs):
        super(LeftCol, self).__init__(**kwargs)

        lcl = LeftCol_Left(MainWindow, size_hint=(.5, 1))
        self.add_widget(lcl)
        self.add_widget(LeftCol_Right(MainWindow))


class GenerateButton(Button):
    def __init__(self, **kwargs):
        super(GenerateButton, self).__init__(**kwargs)
        self.background_down = 'atlas://data/images/defaulttheme/button'
        self.background_normal = 'atlas://data/images/defaulttheme/button_pressed'
        self.background_color = [0, 1, 0, 1]
        self.font_size = 18
        # self.bold = True
        # self.color = [0, 0, 0, 1]
        self.text = 'GENERATE'


class RigthCol_Top(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthCol_Top, self).__init__(**kwargs)
        # Helper.help(self)

        self.add_widget(Button(text = "RigthCol\n_Top_1"))
        self.add_widget(Button(text = "RigthCol\n_Top_2"))
        self.add_widget(Button(text = "RigthCol\n_Top_3"))
        self.add_widget(GenerateButton())


class ResultTextInput(TextInput):
    def __init__(self, MainWindow, **kwargs):
        super(ResultTextInput, self).__init__(**kwargs)
        # Helper.help(self)

        self.text = f"""Добрый день
Заявка для ОПВТ.
В ОСП {MainWindow.bank['OSP']['data']} недоступна точка доступа после {MainWindow.bank['DATE']['data']}
{MainWindow.bank['WAPNAME']['data']} {MainWindow.bank['WAPMAC']['data']} - {MainWindow.bank['WAPMODEL']['data']}
Была подключена в {MainWindow.bank['PORTNUM']['data']} порт коммутатора {MainWindow.bank['SWNAME']['data']} ({MainWindow.bank['SWMODEL']['data']}, SN: {MainWindow.bank['SWSN']['data']}).
Прошу проверить/перезагрузить ТД."""



class RigthCol(BoxLayout):
    def __init__(self, MainWindow, **kwargs):
        super(RigthCol, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(RigthCol_Top(size_hint_y = 0.2))

        result = ResultTextInput(MainWindow)
        self.add_widget(result)
        # print(Helper.help(result.parent))


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.bank = {'OSP': {'label': "Имя ОСП", 'data': "Новосибирск РЦ"},
                     'DATE': {'label': "Дата", 'data': "26.06.2023 17:10 МСК"},
                     'WAPNAME': {'label': "Имя wap", 'data': "wap-nsk-rc-done-11"},
                     'WAPMAC': {'label': "MAC wap", 'data': "78:45:58:70:a9:70"},
                     'WAPMODEL': {'label': "Модель wap", 'data': "UniFi AP-AC-Mesh"},
                     'PORTNUM': {'label': "Порт на sw", 'data': "3"},
                     'SWNAME': {'label': "Имя sw", 'data': "sw-nsk-rc-ku-5-1"},
                     'SWMODEL': {'label': "Модель sw", 'data': "Cisco"},
                     'SWSN': {'label': "SN sw", 'data': "JTV2149106P"},
                     }

        lc = LeftCol(self)
        self.add_widget(lc)
        rc = RigthCol(self)
        self.add_widget(rc)


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
