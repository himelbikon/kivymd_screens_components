from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
import os


Builder.load_file(os.getcwd() + '/kv_files/home_screen.kv')


class HomeScreen(Screen):
    pass
