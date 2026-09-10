from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp

Window.clearcolor = (0.09, 0.09, 0.12, 1)

MOVIES = [
    {"title": "Sweety Love Story", "year": "2024", "rating": "8.5", "genre": "Romance"},
    {"title": "Yashu The Hero", "year": "2024", "rating": "9.0", "genre": "Action"},
    {"title": "Sweety Movie Special", "year": "2023", "rating": "8.8", "genre": "Drama"},
    {"title": "Love in Gooty", "year": "2023", "rating": "8.2", "genre": "Romance"},
    {"title": "Chillakur Diaries", "year": "2024", "rating": "7.9", "genre": "Comedy"},
    {"title": "Sweety & Yashu", "year": "2024", "rating": "9.2", "genre": "Romance"},
    {"title": "Andhra King", "year": "2022", "rating": "8.6", "genre": "Action"},
    {"title": "Movie Magic", "year": "2023", "rating": "8.0", "genre": "Drama"},
]

class MovieCard(BoxLayout):
    def __init__(self, movie, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(140)
        self.padding = dp(10)
        self.spacing = dp(5)

        # Background simulation with canvas is heavy, use simple BoxLayout
        with self.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(0.15, 0.15, 0.22, 1)
            self
