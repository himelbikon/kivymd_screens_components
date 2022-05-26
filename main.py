from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel

from screens.home_screen import HomeScreen
from screens.download_screen import DownloadScreen


class MyScreenManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        pass


MainApp().run()
