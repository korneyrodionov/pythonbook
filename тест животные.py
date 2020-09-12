#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Ответ верный')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input ('Ответ неверный. Попробуйте еще раз. ')
            attempt = attempt + 1
          
    if attempt == 3:
        print('Правильный ответ: ' + answer)

score = 0
print('тест "Животные"')
guess1 = input('Какой медведь живет за полярным кругом? ')
check_guess(guess1, 'белый')
guess2 = input('Какое сухопутное животное самое быстрое? ')
check_guess(guess2, 'гепард')
guess3 = input('Какое животное самое большое? ')
check_guess(guess3, 'синий кит')
guess4 = input('У какого животного есть хобот? ')
check_guess(guess4, 'слон')
guess5 = input('Какое млекопитающее умеет летать? ')
check_guess(guess5, 'летучая мышь')
guess6 = input('Сколько сердец у осьминога? ')
check_guess(guess6, 'три')
guess7 = input('Какое из этих животных рыба? \n \
1) Кит\n 2) Дельфин\n 3) Акула\n 4) Кальмар\n \
Введите 1, 2, 3 или 4. ')
check_guess(guess7, '3')


print('Вы набрали очков: ' +str(score))
