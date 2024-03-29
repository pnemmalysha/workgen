'''
Bubble
======

Test of the widget Bubble.
'''

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble, BubbleContent, BubbleButton


class MyBubbleContent(BubbleContent):
    def __init__(self, **kwargs):
        super(MyBubbleContent, self).__init__(**kwargs)
        pass


class MyBubbleButton(BubbleButton):
    def __init__(self, **kwargs):
        super(MyBubbleButton, self).__init__(**kwargs)
        pass


class cut_copy_paste(Bubble):
    def __init__(self, **kwargs):
        super(cut_copy_paste, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (160, 120)
        self.pos_hint = {'center_x': .5, 'y': .6}
        self.bubcont = MyBubbleContent()
        self.bubcont.add_widget(MyBubbleButton(text = 'Cut', size_hint_y = 1))
        self.bubcont.add_widget(MyBubbleButton(text = 'Copy', size_hint_y = 1))
        self.bubcont.add_widget(MyBubbleButton(text = 'Paste', size_hint_y = 1))
        self.add_widget(self.bubcont)
        pass


class BubbleShowcase(FloatLayout):

    def __init__(self, **kwargs):
        super(BubbleShowcase, self).__init__(**kwargs)
        self.but_bubble = Button(text='Press to show bubble')
        self.but_bubble.bind(on_release=self.show_bubble)
        self.add_widget(self.but_bubble)

    def show_bubble(self, *l):
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = cut_copy_paste()
            self.add_widget(bubb)
        else:
            values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                'top_mid', 'top_right', 'right_top', 'right_mid',
                'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
            index = values.index(self.bubb.arrow_pos)
            self.bubb.arrow_pos = values[(index + 1) % len(values)]


class TestBubbleApp(App):

    def build(self):
        return BubbleShowcase()


if __name__ == '__main__':
    TestBubbleApp().run()