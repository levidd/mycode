#!/usr/bin/env python3

import requests

def api_slice(json2python):
    poke_pic = ""
    temp = json2python.get("sprites")
    if "other" in temp and "official-artwork" in temp.get("other"):
        poke_pic = temp.get("other").get("official-artwork").get('front_default')
    if poke_pic == "":
        poke_pic = temp.get("front_default")
    return poke_pic

print(api_slice(requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json())) # this is a temporary link
