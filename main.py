
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp

from jnius import autoclass


# Android classes
PythonActivity = autoclass("org.kivy.android.PythonActivity")
Intent = autoclass("android.content.Intent")
Uri = autoclass("android.net.Uri")


class SweetyMovieApp(App):

    def build(self):
        self.title = "SweetyMovieApp"

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15)
        )

        title = Label(
            text="SweetyMovieApp",
            font_size="28sp",
            size_hint_y=None,
            height=dp(70)
        )

        subtitle = Label(
            text="Watch movies on YouTube",
            font_size="18sp",
            size_hint_y=None,
            height=dp(50)
        )

        self.video_url = TextInput(
            hint_text="Enter YouTube URL",
            multiline=False,
            size_hint_y=None,
            height=dp(55)
        )

        self.video_url.text = (
            "https://www.youtube.com/watch?v=M7lc1UVf-VE"
        )

        play_button = Button(
            text="▶ Open in YouTube",
            font_size="18sp",
            size_hint_y=None,
            height=dp(60)
        )

        play_button.bind(
            on_press=self.open_youtube
        )

        self.status = Label(
            text="Ready to open YouTube",
            font_size="14sp"
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(self.video_url)
        layout.add_widget(play_button)
        layout.add_widget(self.status)

        return layout

    def open_youtube(self, instance):
        url = self.video_url.text.strip()

        if not url:
            self.status.text = "Please enter a YouTube URL"
            return

        if not (
            url.startswith("https://www.youtube.com/")
            or url.startswith("https://youtu.be/")
            or url.startswith("https://m.youtube.com/")
        ):
            self.status.text = "Enter a valid YouTube URL"
            return

        try:
            activity = PythonActivity.mActivity

            # Create ACTION_VIEW Intent
            intent = Intent(
                Intent.ACTION_VIEW,
                Uri.parse(url)
            )

            # Try to open specifically in the YouTube app
            intent.setPackage("com.google.android.youtube")

            activity.startActivity(intent)

            self.status.text = "Opening YouTube..."

        except Exception:
            # Fallback: open the URL using another supported app
            try:
                activity = PythonActivity.mActivity

                fallback_intent = Intent(
                    Intent.ACTION_VIEW,
                    Uri.parse(url)
                )

                activity.startActivity(fallback_intent)

                self.status.text = (
                    "Opening YouTube URL in another app..."
                )

            except Exception as error:
                self.status.text = (
                    "Unable to open video: " + str(error)
                )


if __name__ == "__main__":
    SweetyMovieApp().run()
