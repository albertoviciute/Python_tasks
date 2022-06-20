# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.


class Movie:
    def __init__(self, title: str, director: str, budget: int):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        if self.budget > 100000000:
            print(True)
        else:
            print(False)

movie_1 = Movie('Midsommar', 'Ari Aster', 9000000)
movie_1.was_expensive()

movie_2 = Movie('Venom', 'Ruben Fleischer', 116000000)
movie_2.was_expensive()