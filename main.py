import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class HiWindow(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Hi bro!'


class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result = ''
        self.cols = 3
        self.rows = 9
        self.orientation = 'tb-lr'
        #self.spacing = [5, 5]
        #self.padding = [10, 10, 10, 10]
        self.add_widget(Label(text = 'OSP'))
        self.add_widget(Label(text = 'DATE'))
        self.add_widget(Label(text = 'WAP'))
        self.add_widget(Label(text = 'MAC'))
        self.add_widget(Label(text = 'MODEL'))
        self.add_widget(Label(text = 'N'))
        self.add_widget(Label(text = 'SW'))
        self.add_widget(Label(text = 'CISCO'))
        self.add_widget(Label(text = 'SN'))

        self.OSP = TextInput(text='Новосибирск РЦ')
        self.add_widget(self.OSP)
        self.DATE = TextInput(text='27.04.2023 17:10 МСК')
        self.add_widget(self.DATE)
        self.WAP = TextInput(text='wap-nsk-rc-done-11')
        self.add_widget(self.WAP)
        self.MAC = TextInput(text='78:45:58:70:a9:70')
        self.add_widget(self.MAC)
        self.MODEL = TextInput(text='UniFi AP-AC-Mesh')
        self.add_widget(self.MODEL)
        self.N = TextInput(text='3')
        self.add_widget(self.N)
        self.SW = TextInput(text='sw-nsk-rc-ku-5-1')
        self.add_widget(self.SW)
        self.CISCO = TextInput(text='Cisco')
        self.add_widget(self.CISCO)
        self.SN = TextInput(text='JTV2149106P')
        self.add_widget(self.SN)

        self.butt_generate = Button(text = 'Generate')
        self.butt_generate.bind(on_press=self.gen_result)
        self.add_widget(self.butt_generate)
        self.butt_clear = Button(text = 'Clear')
        self.butt_clear.bind(on_press=self.clear_inputs)
        self.add_widget(self.butt_clear)
        self.add_widget(Label(text = 'result', color = [255, 1, 255, 1], font_size = '25sp'))
        
        self.add_widget(Label(text = self.result, color = [255, 1, 255, 1], font_size = '15sp'))

    def gen_result(self, *args, **kwargs):
        self.result = f"""Добрый день
Заявка для ОПВТ.
В ОСП {self.OSP.text} недоступна точка доступа после {self.DATE.text}
{self.WAP.text} {self.MAC.text} - {self.MODEL.text}
Была подключена в {self.N.text} порт коммутатора {self.SW.text} ({self.CISCO.text}, SN: {self.SN.text}).
Прошу проверить/перезагрузить ТД."""
        self.print_result()
        return self.result

    def gen_test(self, *args, **kwargs):
        print('ooppss')

    def print_result(self, *args, **kwargs):
        self.add_widget(TextInput(text = self.result))

    def clear_result(self, *args, **kwargs):
        pass

    def clear_inputs(self, *args, **kwargs):
        self.OSP.text = ''
        self.DATE.text = ''
        self.WAP.text = ''
        self.MAC.text = ''
        self.MODEL.text = ''
        self.N.text = ''
        self.SW.text = ''
        #self.CISCO.text = ''
        self.SN.text = ''



class WorkGenApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    WorkGenApp().run()