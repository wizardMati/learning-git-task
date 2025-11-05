import random
from datetime import datetime

class Title:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = 0

    def play(self):
        self.plays += 1

    def add_views(self, n):
        if n > 0:
            self.plays += n

    def __str__(self):
        raise NotImplementedError

class Movie(Title):
    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)

    def __str__(self):
        return f"{self.title} ({self.year})"

class Series(Title):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        s = f"S{self.season:02d}"
        e = f"E{self.episode:02d}"
        return f"{self.title} {s}{e}"

def get_movies(library):
    movies = [item for item in library if isinstance(item, Movie)]
    return sorted(movies, key=lambda m: m.title.lower())

def get_series(library):
    series = [item for item in library if isinstance(item, Series)]
    return sorted(series, key=lambda s: (s.title.lower(), s.season, s.episode))

def search(library, title):
    title_lower = title.lower()
    for item in library:
        if item.title.lower() == title_lower:
            return item
    return None

def generate_views(library):
    if not library:
        return
    item = random.choice(library)
    views = random.randint(1, 100)
    item.add_views(views)

def generate_views_n_times(library, n=10):
    for _ in range(n):
        generate_views(library)

def top_titles(library, top_n=3, content_type=None):
    filtered = library
    if content_type == "movies":
        filtered = [item for item in library if isinstance(item, Movie)]
    elif content_type == "series":
        filtered = [item for item in library if isinstance(item, Series)]
    sorted_list = sorted(filtered, key=lambda it: (-it.plays, it.title.lower()))
    return sorted_list[:top_n]

def add_season(library, title, year, genre, season_number, episodes_count):
    for ep in range(1, episodes_count + 1):
        s = Series(title=title, year=year, genre=genre, season=season_number, episode=ep)
        library.append(s)

def count_episodes_in_library(library, series_title):
    title_lower = series_title.lower()
    count = sum(1 for item in library if isinstance(item, Series) and item.title.lower() == title_lower)
    return count

def populate_library_example():
    lib = []
    lib.append(Movie("Pulp Fiction", 1994, "Crime"))
    lib.append(Movie("The Shawshank Redemption", 1994, "Drama"))
    lib.append(Movie("Inception", 2010, "Sci-Fi"))
    lib.append(Movie("The Matrix", 1999, "Sci-Fi"))
    lib.append(Movie("Interstellar", 2014, "Sci-Fi"))
    lib.append(Series("The Simpsons", 1989, "Animation", season=1, episode=1))
    lib.append(Series("The Simpsons", 1989, "Animation", season=1, episode=2))
    lib.append(Series("The Simpsons", 1989, "Animation", season=1, episode=5))
    add_season(lib, title="Stranger Things", year=2016, genre="Sci-Fi", season_number=1, episodes_count=8)
    add_season(lib, title="Breaking Bad", year=2008, genre="Crime", season_number=1, episodes_count=7)
    return lib

def main():
    print("Biblioteka filmów.")
    library = populate_library_example()
    generate_views_n_times(library, n=10)
    today_str = datetime.now().strftime("%d.%m.%Y")
    print(f"\nNajpopularniejsze filmy i seriale dnia {today_str}\n")
    top3 = top_titles(library, top_n=3)
    for i, t in enumerate(top3, start=1):
        print(f"{i}. {t} — {t.plays} odtworzeń")
    print("\nFilmy (alfabetycznie):")
    for movie in get_movies(library):
        print(f"- {movie} — {movie.plays} odtworzeń")
    print("\nSeriale (alfabetycznie):")
    for series in get_series(library):
        print(f"- {series} — {series.plays} odtworzeń")
    query = "Inception"
    found = search(library, query)
    if found:
        print(f"\nWyszukano '{query}': {found} — {found.plays} odtworzeń")
    else:
        print(f"\nNie znaleziono tytułu '{query}' w bibliotece.")
    series_title = "Stranger Things"
    episodes = count_episodes_in_library(library, series_title)
    print(f"\nW bibliotece jest {episodes} odcinków serialu '{series_title}'.")

if __name__ == "__main__":
    main()

