from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
import webbrowser

class SweetyMovieApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=dp(15), spacing=dp(10))
        title = Label(text="SweetyMovieApp", font_size="26sp", bold=True, size_hint_y=None, height=dp(60))
        subtitle = Label(text="Watch your favorite movies", font_size="15sp", size_hint_y=None, height=dp(40))
        root.add_widget(title)
        root.add_widget(subtitle)
        scroll = ScrollView()
        movie_list = BoxLayout(orientation="vertical", spacing=dp(10), size_hint_y=None)
        movie_list.bind(minimum_height=movie_list.setter('height'))
        movies = [{"title": "Movie 1", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"title": "Movie 2", "url": "https://www.youtube.com/watch?v=ScMzIvxBSi4"}]
        for movie in movies:
            box = BoxLayout(orientation="vertical", size_hint_y=None, height=dp(100), spacing=dp(5))
            box.add_widget(Label(text=movie["title"], font_size="18sp", size_hint_y=None, height=dp(40)))
            btn = Button(text="Watch on YouTube", size_hint_y=None, height=dp(50))
            btn.bind(on_press=lambda x, url=movie["url"]: webbrowser.open(url))
            box.add_widget(btn)
            movie_list.add_widget(box)
        scroll.add_widget(movie_list)
        root.add_widget(scroll)
        return root

if __name__ == '__main__':
    SweetyMovieApp().run()
