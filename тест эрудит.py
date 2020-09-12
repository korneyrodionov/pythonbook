#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:
        if guess.lower() == answer.lower():
            print('Ответ верный')
            score = score + 2 - attempt
            still_guessing = False
        else:
            if attempt < 1:
                guess = input ('Ответ НЕВЕРНЫЙ. Попробуйте еще раз. ')
            attempt = attempt + 1
          
    if attempt == 2:
        print('Правильный ответ: ' + answer)

score = 0
print('тест эрудит')
guess1 = input('Год на Руси называется: \n \
1) лето\n 2) зима\n 3) осень\n 4) весна\n \
Введите 1, 2, 3 или 4. ')
check_guess(guess1, '1')
guess2 = input('Кланяется, кланяется, придет домой - растянется: \n \
1) пила\n 2) человек\n 3) топор\n \
Введите 1, 2 или 3. ')
check_guess(guess2, '3')
guess3 = input('Символ русских муз. инструментов: \n \
1) гусли\n 2) бубен\n 3) балалайка\n \
Введите 1, 2 или 3. ')
check_guess(guess3, '3')
guess4 = input('Сидит девица в темнице, а коса на улице: \n \
1) морковь\n 2) капуста\n 3) пшеница\n \
Введите 1, 2 или 3. ')
check_guess(guess4, '1')
guess5 = input('Старинное название торговца: \n \
1) купец\n 2) городничий\n 3) гость\n \
Введите 1, 2 или 3. ')
check_guess(guess5, '3')
guess6 = input('Число 10.000 в старинном русском счете называлось: \n \
1) куча\n 2) тьма\n 3) много\n \
Введите 1, 2 или 3. ')
check_guess(guess6, '2')
guess7 = input('Какое из этих животных рыба? \n \
1) Кит\n 2) Дельфин\n 3) Акула\n 4) Кальмар\n \
Введите 1, 2, 3 или 4. ')
check_guess(guess7, '3')


print('Вы набрали очков: ' +str(score))
