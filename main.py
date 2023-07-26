# 

import kivy
kivy.require('2.2.1')

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
from kivy.uix.spinner import Spinner
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
import time
# import random


class Helper():
    def help(obj):
        print('\033[1m' + '\033[31m' + str(obj) + '\033[0m')
        print(obj.__dir__())
        for i in obj.__dir__():
            print(i, obj.__getattribute__(i)) \
            # if 'object' not in str(obj.__getattribute__(i)) else None


class Bank:
    OSP = {'label': "Имя ОСП", 'data': "Новосибирск РЦ"}
    DATE = {'label': "Дата", 'data': time.strftime("%d.%m.%Y %H:%M МСК", time.localtime())}
    WAPNAME = {'label': "Имя wap", 'data': "wap-nsk-rc-done-11"}
    WAPMAC = {'label': "MAC wap", 'data': "78:45:58:70:a9:70"}
    WAPMODEL = {'label': "Модель wap", 'data': "UniFi AP-AC-Mesh"}
    PORTNUM = {'label': "Порт на sw", 'data': "3"}
    SWNAME = {'label': "Имя sw", 'data': "sw-nsk-rc-ku-5-1"}
    SWMODEL = {'label': "Модель sw", 'data': "Cisco"}
    SWSN = {'label': "SN sw", 'data': "JTV2149106P"}


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
    def __init__(self, **kwargs):
        super(LeftCol_Left, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [1, 1, 1, 1]
        self.spacing = 1
        # Helper.help(self)

        self.cl1 = CustomLabel()
        self.cl2 = CustomLabel()
        self.cl3 = CustomLabel()
        self.cl4 = CustomLabel()
        self.cl5 = CustomLabel()
        self.cl6 = CustomLabel()
        self.cl7 = CustomLabel()
        self.cl8 = CustomLabel()
        self.cl9 = CustomLabel()
        self.clset = (self.cl1, self.cl2, self.cl3, self.cl4,
                     self.cl5,self.cl6, self.cl7, self.cl8, self.cl9)
        for cl_ in self.clset:
            self.add_widget(cl_)
        self.bind(pos=self.show, size=self.show)

    def show(self, inst, val):
        #! заполняются не сразу при создании, а при изменении размера
        self.cl1.text = Bank.OSP['label']
        self.cl2.text = Bank.DATE['label']
        self.cl3.text = Bank.WAPNAME['label']
        self.cl4.text = Bank.WAPMAC['label']
        self.cl5.text = Bank.WAPMODEL['label']
        self.cl6.text = Bank.PORTNUM['label']
        self.cl7.text = Bank.SWNAME['label']
        self.cl8.text = Bank.SWMODEL['label']
        self.cl9.text = Bank.SWSN['label']



class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.multiline = False
        self.write_tab = False
        # Helper.help(self)


class LeftCol_Right(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol_Right, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.cti1 = CustomTextInput(text = Bank.OSP['data'])
        self.cti2 = CustomTextInput(text = Bank.DATE['data'])
        self.cti3 = CustomTextInput(text = Bank.WAPNAME['data'])
        self.cti4 = CustomTextInput(text = Bank.WAPMAC['data'])
        self.cti5 = CustomTextInput(text = Bank.WAPMODEL['data'])
        self.cti6 = CustomTextInput(text = Bank.PORTNUM['data'])
        self.cti7 = CustomTextInput(text = Bank.SWNAME['data'])
        self.cti8 = CustomTextInput(text = Bank.SWMODEL['data'])
        self.cti9 = CustomTextInput(text = Bank.SWSN['data'])
        self.ctiset = (self.cti1, self.cti2, self.cti3, self.cti4,
                     self.cti5,self.cti6, self.cti7, self.cti8, self.cti9)
        for cti_ in self.ctiset:
            self.add_widget(cti_)
            cti_.bind(text=self.write_bank)

    def write_bank(self, inst, val):
        Bank.OSP['data'] = self.cti1.text
        Bank.DATE['data'] = self.cti2.text
        Bank.WAPNAME['data'] = self.cti3.text
        Bank.WAPMAC['data'] = self.cti4.text
        Bank.WAPMODEL['data'] = self.cti5.text
        Bank.PORTNUM['data'] = self.cti6.text
        Bank.SWNAME['data'] = self.cti7.text
        Bank.SWMODEL['data'] = self.cti8.text
        Bank.SWSN['data'] = self.cti9.text

    def dark(self, template):
        if template == 'Ошибки на порту':
            for cti in [self.cti2, self.cti3, self.cti4, self.cti5]:
                cti.background_color = [1, 1, 1, 0.5]
        if template == 'Недоступна точка доступа':
            for cti in self.children:
                cti.background_color = [1, 1, 1, 1]



class LeftCol(BoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol, self).__init__(**kwargs)

        self.lcl = LeftCol_Left(size_hint=(.5, 1))
        self.add_widget(self.lcl)
        self.lcr = LeftCol_Right()
        self.add_widget(self.lcr)


class GenerateButton(Button):
    def __init__(self, **kwargs):
        super(GenerateButton, self).__init__(**kwargs)
        self.background_down = 'atlas://data/images/defaulttheme/button'
        self.background_normal = 'atlas://data/images/defaulttheme/button_pressed'
        self.background_color = [0, 1, 0, 1]
        self.font_size = self.font_size * 1.1
        # self.bold = True
        # self.color = [0, 0, 0, 1]
        self.text = 'GENERATE'


class RigthCol_Top(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthCol_Top, self).__init__(**kwargs)
        # Helper.help(self)

        self.bclear = Button(text = "Clear")
        self.add_widget(self.bclear)
        self.bundo = Button(text = "Undo")
        self.add_widget(self.bundo)
        self.bredo = Button(text = "Redo")
        self.add_widget(self.bredo)
        self.gb = GenerateButton()
        self.add_widget(self.gb)
        self.bclear.bind(on_press=self.do_clear)
        self.bundo.bind(on_press=self.do_undo)
        self.bredo.bind(on_press=self.do_redo)
        self.gb.bind(on_press=self.refresh_result)

    def refresh_result(self, instance):
        # print(f'The button {instance.text} is being pressed')
        self.parent.result.text = 'Добрый день. Заявка для ОПВТ.'
        if self.parent.msp.text == 'Недоступна точка доступа':
            self.parent.result.text = f"""Добрый день
Заявка для ОПВТ.
В ОСП {Bank.OSP['data']} недоступна точка доступа после {Bank.DATE['data']}
{Bank.WAPNAME['data']} {Bank.WAPMAC['data']} - {Bank.WAPMODEL['data']}
Была подключена в {Bank.PORTNUM['data']} порт коммутатора {Bank.SWNAME['data']} ({Bank.SWMODEL['data']}, SN: {Bank.SWSN['data']}).
Прошу проверить/перезагрузить ТД."""
        if self.parent.msp.text == 'Ошибки на порту':
            self.parent.result.text = f"""Добрый день
Заявка для ОПВТ.
В ОСП {Bank.OSP['data']} растут ошибки на порту {Bank.PORTNUM['data']} коммутатора {Bank.SWNAME['data']} ({Bank.SWMODEL['data']}, SN: {Bank.SWSN['data']}).
Прошу проверить целостность кабельной линии, переобжать коннекторы при необходимости."""
        self.parent.result.select_all()
        self.parent.result.copy()
        self.parent.result.cancel_selection()


    def do_clear(self, instance):
        for cti_ in self.parent.parent.lc.lcr.ctiset:
            cti_.select_all()
            cti_.cut()

    def do_undo(self, instance):
        for cti_ in self.parent.parent.lc.lcr.ctiset:
            cti_.do_undo()

    def do_redo(self, instance):
        for cti_ in self.parent.parent.lc.lcr.ctiset:
            cti_.do_redo()


class ResultTextInput(TextInput):
    def __init__(self, **kwargs):
        super(ResultTextInput, self).__init__(**kwargs)
        # Helper.help(self)

        self.text = ''


class MySpinner(Spinner):
    def __init__(self, **kwargs):
        super(MySpinner, self).__init__(**kwargs)
        self.text='Недоступна точка доступа'
        self.values=('Недоступна точка доступа', 'Ошибки на порту')
        self.size_hint=(1, None)
        self.height = 44
        # self.size=(100, 44)
        self.pos_hint={'center_x': 0.5, 'center_y': 0.5}
        self.bind(text=self.handle_selected_value)


    def handle_selected_value(self, text, val):
        # print('The spinner', self, 'has text', self.text)
        self.parent.parent.lc.lcr.dark(self.text)



class RigthCol(BoxLayout):
    def __init__(self, **kwargs):
        super(RigthCol, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.rct = RigthCol_Top(size_hint_y = 0.2)
        self.msp = MySpinner()
        self.result = ResultTextInput()

        self.add_widget(self.msp)
        self.add_widget(self.rct)
        self.add_widget(self.result)
        # print(Helper.help(self.result.parent))


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.lc = LeftCol()
        self.add_widget(self.lc)
        self.rc = RigthCol()
        self.add_widget(self.rc)


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

        self.mw = MainWindow()
        self.add_widget(self.mw)
        self.sign = Signature()
        self.add_widget(self.sign)


class WorkGenApp(App):
    def build(self):
        self.w = RootWindow()
        return self.w


if __name__ == '__main__':
    WorkGenApp().run()
