import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (320,600)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return  Builder.load_file('main.kv')


MainApp().run()