'''Hangman Game

Works on Linux and Windows.
Python 3.7.
Created by k3itaro-k


PUNTOS FALTANTES

1. Función hangman que dibuje al ahorcado, debe estar presente en todas las pantallas hasta en la de derrota
    con todo y el nombre en grande.(dejar al ultimo)
3. Limpiar las palabras de acentos, solo para la detección, para la impresión debe estar bien escrita. implementar en select a word?
    que retorne una lista de palabras una limpia y normal?
5. Revisar las condicionaes si se adivino la palabra o no
6. Refactorizar en una función la comparación de las letras en las palabras.
8. Pasar el flujo de ejecucion a main()  IN PROCESS
7. Tratar de usar comprehension
8. Poner mensaje de perdedor.
9. Hacer una comprobacion para que el usuario sea advertido cuando ingrese letras que ya ingreso antes.
10. Analizar la dinamica de los niveles de juego ¿dejar estaticos el numero de intentos en cada nivel de dificultad?

'''
import os
import random
from typing import List

from art import text2art as t2a

def clear_screen():
    if os.name =='posix':
        os.system('clear')
    else:
        os.system('cls')

def ascii_art(phrase: str, font=None) -> str:
    if font == None:
        art = t2a(phrase)
    else:
        art = t2a(phrase,font=font)
    print(art)

def select_word() -> str:
    with open('data.txt', 'r', encoding='utf-8') as f:
        words = f.read().split('\n')

    word = words[random.randint(0, len(words) - 1)]
    return word

def ask_for_a_letter() -> str:
    try:
        print('Por favor de una letra para adivinar la palabra:')
        letter = input()
        if not letter.isalpha():
            raise TypeError('El caracter ingresado no es una letra')
        return letter
    except Exception as e:
        print(e)

def print_word(word_list):
    return ''.join(word_li)

def hangman_ascii(n: int) -> str:
    pass

def game_level() -> str:
    print('Please, select difficulty level.')
    print('For easy type "e".')
    print('For medium type "m".')
    print('For hard type "h".')
    try:
        level = input('Type your selecction: ').lower()
        if not (level == 'h' or level == 'm' or level == 'e'):
            raise ValueError(level)    
    except ValueError as e:
        print('¡Error! Your value {} is not on the difficulty level. Please run the program again.'.format(e))    
    return level

def number_of_attempts(level: str, word: str) -> List[int]:
    # li = [attempts, word_len]
    word_len = len(word)
    li = [0,word_len]

    if level == 'e':
        attempts = word_len * 2
    elif level == 'm':
        attempts = int(word_len * 1.5)
    else:
        attempts = word_len * 1

    li[0]= attempts
    return li

def main():
    # title screen
    clear_screen()
    print('*' * 90)
    ascii_art('HANGMAN GAME')
    print('*' * 90)
    print('\n' * 3)
    print('¡Welcome to the hangman game!')
    level = game_level()
    word = select_word()
    list_of_attempts = number_of_attempts(level, word)
    secret_word = ['_' for letter in range(len(word))]
    # game screen
    while list_of_attempts[0] > 0:
        clear_screen()
        print('*' * 90)
        ascii_art('HANGMAN GAME')
        print('*' * 90)
        print(word) # this is for debug
        print('You have {} attempts and your word have {} letters left to guess.'.format(list_of_attempts[0],list_of_attempts[1]))
        print('\n' * 3)
        word_li = [x for x in word]
        print(word_li)
        print('\n' * 3)
        print(secret_word)
        print('\n' * 3)
        letter = ask_for_a_letter()

        if letter in word_li:
            idx = 0

            for x in word_li:

                if letter == x:
                    secret_word[idx] = letter
                    list_of_attempts[1] -= 1
                    print(list_of_attempts[1])

                idx += 1
        
        if list_of_attempts[1] == 0:
            clear_screen()
            print('*' * 90)
            ascii_art('HANGMAN GAME')
            print('*' * 90)
            print('¡You guessed the word: {}!'.format(word))
            break
            
        list_of_attempts[0] -= 1

if __name__=='__main__':
    main()






