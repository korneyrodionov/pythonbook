#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


lives = 10
words = ['генерал', 'десант', 'солдат', 'пуля',
         'пулемет', 'граната', 'танк', 'война',
         'командир','рота','батальон','блокада',
         'винтовка','бомба','адмирал','бункер']
secret_word = random.choice(words)
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index + 1
heart_symbol = u'\u2764'
guessed_word_correctly = False

unknown_letters = len(secret_word)

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1
        
    return unknown_letters
        
difficulty = input('Выберите уровень сложности:\n 1 Легкий\n 2 Средний\n 3 Трудный\n')
difficulty = int(difficulty)

if difficulty == 1:
    lives =12
elif difficulty == 2:
    lives = 9
else:
    lives =6
        
        
while lives > 0:
    print(clue)
    print('Осталось жизней: ' + heart_symbol * lives)
    guess = input ('Угадай букву или слово целиком: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('Неправильно. Вы теряете жизнь')
        lives = lives - 1
    
    if unknown_letters == 0:
        guessed_word_correctly = True
        break
        
if guessed_word_correctly:
    print('Победа! Было загадано слово ' + secret_word)
else:
    print('Проигрыш! Было загадано слово ' + secret_word)