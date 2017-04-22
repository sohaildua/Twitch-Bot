import requests
import random


def poke(pokemon):
#pokemon = input("ur poekmmdmdm")
    try:
        url = "http://pokeapi.co/api/v2/pokemon/"+pokemon

        resp = requests.get(url)

        print(resp.json()["types"][0]['type']['name'])
        mylist = resp.json()["moves"]

        myvalues = [i['move'] for i in mylist if 'move' in i]
        myattacks =[i['name'] for i in myvalues if 'name' in i]


        name = resp.json()["name"]
        weight = resp.json()["weight"]
        breed = resp.json()["types"][0]['type']['name']
        attacks = random.sample(set(myattacks), 4)
        limyne = "Nice to meet you My friend!!!! My name is "+ name + " i am slimmer than you only "+ str(weight)+ " pounds and i am a "+breed+" pokemon and my favourite attacks are "+ attacks[0] +", "+ attacks[1] +" ,"+ attacks[2] + " and " + attacks[3]
        return limyne

    except:
        return "jsjjs"