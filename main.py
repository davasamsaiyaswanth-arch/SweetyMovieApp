"""
💎 SWEETY MOBILE APP - Android / iOS Version
Made for Yashu - Kivy Version

Install: pip install kivy kivymd requests pillow

Run: python SweetyMobileApp_Kivy.py

For Android APK: buildozer android debug
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.network.urlrequest import UrlRequest
import json, os, requests

TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE" # Yashu ikkada nee key paste chey
TMDB_BASE = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w300"
LANG_MAP = {"Telugu":"te", "Tamil":"ta", "Kannada":"kn", "Malayalam":"ml"}

class MovieCard(BoxLayout):
    def __init__(self, movie, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=140, padding=5, spacing=10, **kwargs)
        self.movie = movie
        
        # Poster
        if movie.get("poster_path"):
            img_url = IMAGE_BASE + movie["poster_path"]
            poster = AsyncImage(source=img_url, size_hint_x=0.35)
            self.add_widget(poster)
        else:
            self.add_widget(Label(text="🎬", font_size=50, size_hint_x=0.35))
        
        # Details
        details = BoxLayout(orientation='vertical', spacing=2)
        details.add_widget(Label(text=movie["title"][:30], font_size=15, bold=True, color=(1,0.7,0,1), halign='left', text_size=(None,None), size_hint_y=0.3))
        details.add_widget(Label(text=f"{movie['lang']} | {movie['year']} | ⭐ {movie['rating']}", font_size=12, halign='left', size_hint_y=0.2))
        details.add_widget(Label(text=f"🎬 {movie['theatre'][:10]}", font_size=11, halign='left', size_hint_y=0.2))
        details.add_widget(Label(text=f"📺 {movie['ott'][:25]}", font_size=11, halign='left', color=(0,1,0.5,1), size_hint_y=0.2))
        details.add_widget(Label(text=movie["status"][:30], font_size=10, halign='left', color=(0.5,0.5,1,1), size_hint_y=0.1))
        self.add_widget(details)

class SweetyMobileApp(App):
    def build(self):
        self.title = "💎 Sweety Movie Tracker - Yashu"
        self.api_key = self.load_key()
        
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        root.add_widget(Label(text="💎 SWEETY MOBILE PRO MAX", font_size=20, bold=True, color=(1,0.7,0,1), size_hint_y=0.08))
        root.add_widget(Label(text="Search ANY South Movie 2000-2026 | Made for Yashu", font_size=11, color=(1,0.5,0.5,1), size_hint_y=0.05))
        
        # Search Bar
        search_box = BoxLayout(orientation='horizontal', size_hint_y=0.08, spacing=5)
        self.search_input = TextInput(hint_text="Baahubali, KGF, Kantara...", multiline=False, font_size=14)
        search_box.add_widget(self.search_input)
        search_box.add_widget(Button(text="🔍", size_hint_x=0.2, background_color=(1,0.7,0,1), on_press=self.search_movies))
        root.add_widget(search_box)
        
        # Buttons
        btns = BoxLayout(orientation='horizontal', size_hint_y=0.08, spacing=5)
        btns.add_widget(Button(text="🔥 Upcoming", background_color=(0.3,0.3,0.3,1), on_press=self.fetch_upcoming))
        btns.add_widget(Button(text="🎬 Now", background_color=(0.3,0.3,0.3,1), on_press=self.fetch_now))
        btns.add_widget(Button(text="⭐ Watchlist", background_color=(0.6,0.2,0.8,1), on_press=self.show_watchlist))
        root.add_widget(btns)
        
        # Movie List
        self.scroll = ScrollView()
        self.movie_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.movie_list.bind(minimum_height=self.movie_list.setter('height'))
        self.scroll.add_widget(self.movie_list)
        root.add_widget(self.scroll)
        
        self.status = Label(text="Ready Yashu! Type movie & Search...", size_hint_y=0.05, color=(0,1,0.5,1))
        root.add_widget(self.status)
        
        # Initial load
        self.fetch_popular()
        return root
    
    def load_key(self):
        if os.path.exists("sweety_config.json"):
            try:
                with open("sweety_config.json") as f:
                    return json.load(f).get("tmdb_api_key","")
            except:
                pass
        return TMDB_API_KEY if TMDB_API_KEY != "YOUR_TMDB_API_KEY_HERE" else ""
    
    def api_get(self, endpoint, params={}):
        if not self.api_key or self.api_key=="YOUR_TMDB_API_KEY_HERE":
            return None
        try:
            params["api_key"]=self.api_key
            r=requests.get(f"{TMDB_BASE}{endpoint}", params=params, timeout=10)
            return r.json() if r.status_code==200 else None
        except:
            return None
    
    def parse_movie(self, m, lang="Telugu"):
        movie_id=m.get("id")
        rd=m.get("release_date","")
        ott="Theatre Only"
        if self.api_key:
            prov=self.api_get(f"/movie/{movie_id}/watch/providers")
            if prov and "results" in prov and "IN" in prov["results"]:
                flat=prov["results"]["IN"].get("flatrate",[])
                if flat:
                    ott=", ".join([p["provider_name"] for p in flat[:2]])
        return {
            "id":movie_id, "title":m.get("title","Unknown"), "lang":lang,
            "year":rd[:4] if rd else "N/A", "theatre":rd or "N/A",
            "ott":ott, "rating":f"{m.get('vote_average',0):.1f}",
            "status":"OTT Available" if ott!="Theatre Only" else "In Theatres",
            "poster_path":m.get("poster_path",""), "overview":m.get("overview","")
        }
    
    def clear_list(self):
        self.movie_list.clear_widgets()
    
    def add_movies(self, movies):
        self.clear_list()
        for mv in movies[:40]:
            self.movie_list.add_widget(MovieCard(mv))
    
    def search_movies(self, *args):
        query=self.search_input.text.strip()
        if not query:
            return
        self.status.text=f"Searching '{query}'..."
        def run():
            data=self.api_get("/search/movie", {"query":query})
            movies=[]
            if data and "results" in data:
                for m in data["results"][:20]:
                    lang="Telugu"
                    if m.get("original_language")=="ta": lang="Tamil"
                    elif m.get("original_language")=="kn": lang="Kannada"
                    elif m.get("original_language")=="ml": lang="Malayalam"
                    movies.append(self.parse_movie(m, lang))
            self.add_movies(movies)
            self.status.text=f"Found {len(movies)} movies for '{query}'"
        import threading
        threading.Thread(target=run, daemon=True).start()
    
    def fetch_popular(self):
        def run():
            movies=[]
            for lang_name, code in LANG_MAP.items():
                data=self.api_get("/discover/movie", {"with_original_language":code, "sort_by":"popularity.desc", "primary_release_date.gte":"2000-01-01"})
                if data and "results" in data:
                    for m in data["results"][:6]:
                        movies.append(self.parse_movie(m, lang_name))
            self.add_movies(movies)
            self.status.text=f"Popular 2000-2026 | {len(movies)} movies"
        import threading
        threading.Thread(target=run, daemon=True).start()
    
    def fetch_upcoming(self, *args):
        self.status.text="Fetching Upcoming 2024-2026..."
        def run():
            movies=[]
            for lang_name, code in LANG_MAP.items():
                data=self.api_get("/discover/movie", {"with_original_language":code, "primary_release_date.gte":"2024-01-01", "sort_by":"primary_release_date.asc"})
                if data and "results" in data:
                    for m in data["results"][:5]:
                        movies.append(self.parse_movie(m, lang_name))
            self.add_movies(movies)
            self.status.text=f"Upcoming | {len(movies)} movies"
        import threading
        threading.Thread(target=run, daemon=True).start()
    
    def fetch_now(self, *args):
        self.fetch_popular()
    
    def show_watchlist(self, *args):
        self.status.text="Watchlist feature - Coming in PRO version! Yashu can add soon"

if __name__ == "__main__":
    SweetyMobileApp().run()
