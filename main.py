from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp

Window.clearcolor = (0.08, 0.08, 0.12, 1)

MOVIES = [
    {"title": "Sweety Love Story", "year": "2024", "rating": "9.2"},
    {"title": "Yashu Action", "year": "2024", "rating": "9.0"},
    {"title": "Sweety Drama", "year": "2023", "rating": "8.8"},
    {"title": "Love in Gooty", "year": "2023", "rating": "8.9"},
    {"title": "Pathapatnam Diaries", "year": "2024", "rating": "8.7"},
    {"title": "Sweety Hits", "year": "2022", "rating": "9.1"},
]

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        title = Label(text="[b]Sweety Movie App[/b]", markup=True, font_size='24sp', size_hint_y=None, height=dp(60), color=(1,0.4,0.6,1))
        main.add_widget(title)

        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=dp(10), size_hint_y=None, padding=dp(5))
        grid.bind(minimum_height=grid.setter('height'))

        for movie in MOVIES:
            card = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(70), padding=dp(10))
            card.canvas.before.clear = None
            info = BoxLayout(orientation='vertical')
            info.add_widget(Label(text=f"[b]{movie['title']}[/b]", markup=True, halign='left', font_size='16sp'))
            info.add_widget(Label(text=f"{movie['year']} | Rating: {movie['rating']}", font_size='12sp', color=(0.7,0.7,0.7,1)))
            btn = Button(text="PLAY", size_hint_x=None, width=dp(70), background_color=(1,0.3,0.5,1))
            btn.bind(on_release=lambda x, m=movie: self.play_movie(m))
            card.add_widget(info)
            card.add_widget(btn)
            grid.add_widget(card)

        scroll.add_widget(grid)
        main.add_widget(scroll)
        self.add_widget(main)

    def play_movie(self, movie):
        self.manager.get_screen('detail').set_movie(movie)
        self.manager.current = 'detail'

class DetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))
        self.title_label = Label(text="", font_size='22sp', markup=True)
        self.info_label = Label(text="", font_size='16sp')
        back = Button(text="Back to Home", size_hint_y=None, height=dp(50), background_color=(0.3,0.3,0.8,1))
        back.bind(on_release=lambda x: setattr(self.manager, 'current', 'home'))
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.info_label)
        self.layout.add_widget(back)
        self.add_widget(self.layout)

    def set_movie(self, movie):
        self.title_label.text = f"[b]{movie['title']}[/b]"
        self.info_label.text = f"Year: {movie['year']}\nRating: {movie['rating']}\n\nSweety special movie for Yashu!"

class SweetyMovieApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(DetailScreen(name='detail'))
        return sm

if __name__ == '__main__':
    SweetyMovieApp().run()
