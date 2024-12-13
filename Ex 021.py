""" Tocando Música em Python """
from pygame import mixer
from time import sleep

mixer.init()
print("Sua Música vai começar em breve\n")

sleep(2)

mixer.music.load('Ex 021.mp3')
mixer.music.play()
print("Tocando...\n")
stop = input("Digite algo para interromper a musica: ")
