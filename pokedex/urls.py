from django.conf.urls import include, url
from pokedex import views as pokedex_views

urlpatterns = [
    url(
        r"^api/pokedex/pokemons",
        pokedex_views.find_pokemons,
        name="pokemon_encounters",
    ),
]
