from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.utils import platform
import webbrowser

class SweetyMovieApp(App):
    def build(self):
        self.title = "SweetyMovieApp"

        root = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        title = Label(
            text="SweetyMovieApp",
            font_size="26sp",
            bold=True,
            size_hint_y=None,
            height=dp(60)
        )

        subtitle = Label(
            text="Watch your favorite movies on YouTube",
            font_size="15sp",
            size_hint_y=None,
            height=dp(40)
        )

        root.add_widget(title)
        root.add_widget(subtitle)

        scroll = ScrollView()
        movie_list = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            size_hint_y=None
        )
        movie_list.bind(
            minimum_height=movie_list.setter('height')
        )

        movies = [
            {
                "title": "Movie Trailer 1",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "title": "Movie Trailer 2",
                "url": "https://www.youtube.com/watch?v=ScMzIvxBSi4"
            }
        ]

        for movie in movies:
            movie_box = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=dp(100),
                spacing=dp(5)
            )

            movie_title = Label(
                text=movie["title"],
                font_size="18sp",
                size_hint_y=None,
                height=dp(40)
            )

            watch_button = Button(
                text="Watch on YouTube",
                size_hint_y=None,
                height=dp(50)
            )
            # Lambda lo url fix cheyali
            watch_button.bind(on_press=lambda instance, url=movie["url"]: self.open_youtube(url))

            movie_box.add_widget(movie_title)
            movie_box.add_widget(watch_button)
            movie_list.add_widget(movie_box)

        scroll.add_widget(movie_list)
        root.add_widget(scroll)

        return root

    def open_youtube(self, url):
        if platform == 'android':
            # Android lo Intent tho open avthundi
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            PythonActivity.mCurrentActivity.startActivity(intent)
        else:
            webbrowser.open(url)

if __name__ == '__main__':
    SweetyMovieApp().run()
