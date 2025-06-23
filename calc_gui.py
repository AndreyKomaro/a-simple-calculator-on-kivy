from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from calc_logic import logic

"""Интерфейс программы"""

SIZE = 30
win = ''


class Calculator(BoxLayout):

    def __init__(self, **kwargs):

        global SIZE
        global win
        super(Calculator, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.cols = 2

        self.window = TextInput(text='', font_size=SIZE,
                                base_direction="rtl",
                                readonly=True, multiline=False,
                                size_hint=(1, .2))
        self.add_widget(self.window)
        win = self.window

        buttons = GridLayout(cols=5, rows=5, spacing=10)
        elems = ('7', '8', '9', '/', 'C',
                 '4', '5', '6', 'x', '<',
                 '1', '2', '3', '-', '%',
                 '0', '.', '=', '+', '√',
                 '+/-', 'e+', 'e-')
        for elem in elems:
            if elem == 'C':
                buttons.add_widget(Button(text=elem, font_size=SIZE,
                                          on_press=logic,
                                          background_normal='',
                                          background_color=(1, 0, 0, 1)))
            else:
                buttons.add_widget(Button(text=elem, font_size=SIZE,
                                          on_press=logic))
        self.add_widget(buttons)
