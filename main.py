from kivy.config import Config

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image

from calc_gui import Calculator


class MyApp(App):
    title = 'Калькулятор'

    def build(self):
        Window.clearcolor = (0.7, 0.7, 0.7, 1)
        Window.add_widget(Image(source='Pro.png', size_hint=(.35, None),
                                pos_hint={'right': .97, 'top': .26}))
        return Calculator()


if __name__ == '__main__':
    MyApp().run()
