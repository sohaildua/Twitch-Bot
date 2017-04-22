import cfg
import utils

import socket
import re
import time, thread
from time import sleep
import requests

import random

import requests
import random


def poke(pokemon):
#pokemon = input("ur poekmmdmdm")\
    try:
        url = 'http://pokeapi.co/api/v2/pokemon/{}'.format(pokemon)
        print url

        resp = requests.get(url)
        print resp

        print resp.json()['types'][0]['type']['name']
        mylist = resp.json()['moves']

        myvalues = [i['move'] for i in mylist if 'move' in i]
        myattacks =[i['name'] for i in myvalues if 'name' in i]


        name = resp.json()['name']
        weight = resp.json()['weight']
        breed = resp.json()["types"][0]['type']['name']
        attacks = random.sample(set(myattacks), 4)
        limyne = "Nice to meet you My friend!!!! My name is "+ name + " i am slimmer than you only "+ str(weight)+ " pounds and i am a "+breed+" pokemon and my favourite attacks are "+ attacks[0] +", "+ attacks[1] +" ,"+ attacks[2] + " and " + attacks[3]
        return limyne
    except:
        return "no pokemon Sry!!!!!"






def main():

    s = socket.socket()

    s.connect((cfg.HOST,cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    print(CHAT_MSG)
    utils.chat(s, "Hi everyone!")
    thread.start_new_thread(utils.threadFillOpList,())
    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n")
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)

            print response

            if message.strip()  == "!time":
                utils.chat(s,"it is currently "+time.asctime())
            elif message.strip() == "!steam":
                utils.chat(s,"http://steamcommunity.com/id/sdgamer007.Please Send me friend request on steam")
            elif message.startswith('!pokemon') :
                print "zsslsl"+ message
                x, y = message.split(' ')
                print

                resp = poke(str(y.strip()))
                print resp

                utils.chat(s,resp)

        sleep(1)
if __name__ == '__main__':
    main()