from django.shortcuts import render
from django.http import JsonResponse
from pokemon_v2.models import *
from pokemon_v2.serializers import *
import json
# Create your views here.


def get_pokemon_sprites(obj):

    sprites_object = PokemonSprites.objects.get(pokemon_id=obj)
    sprites_data = json.loads(sprites_object.sprites)
    host = "raw.githubusercontent.com/PokeAPI/sprites/master/"

    def replace_sprite_url(d):
        for key, value in d.items():
            if isinstance(value, dict):
                replace_sprite_url(value)
            else:
                if d[key]:
                    d[key] = "https://" + host + \
                        d[key].replace("/media/", "")

    replace_sprite_url(sprites_data)

    default = ''
    shiny = ''
    if 'other' in sprites_data and 'official-artwork' in sprites_data['other']:
        if 'front_default' in sprites_data['other']['official-artwork'] and sprites_data['other']['official-artwork']['front_default']:
            default = sprites_data['other']['official-artwork']['front_default']
        if 'front_shiny' in sprites_data['other']['official-artwork'] and sprites_data['other']['official-artwork']['front_shiny']:
            shiny = sprites_data['other']['official-artwork']['front_shiny']
    if not default:
        if 'front_default' in sprites_data and sprites_data['front_default']:
            default = sprites_data['front_default']
    if not shiny:
        if 'front_shiny' in sprites_data and sprites_data['front_shiny']:
            shiny = sprites_data['front_shiny']
    return {
        'default': default,
        'shiny': shiny,
    }


def get_pokemon_types(obj):

    poke_types = []
    objects = PokemonType.objects.filter(pokemon=obj)
    for o in objects:
        poke_types.append({
            'id': o.type.id,
            'name': o.type.name,
        })

    return poke_types


def get_pokemon_detail(p):
    return {
        'id': p.id,
        'name': p.name,
        'sprite': get_pokemon_sprites(p),
        'types': get_pokemon_types(p)
    }


def find_pokemons(request):
    limit = int(request.GET.get('limit', 100))
    offset = int(request.GET.get('offset', 0))
    pokemons = []
    for p in Pokemon.objects.filter(is_default=True).order_by('id')[offset:offset+limit]:
        pokemons.append(get_pokemon_detail(p))
    return JsonResponse({'list': pokemons})
