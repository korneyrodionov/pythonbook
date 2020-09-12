#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

adjectives = ['perfect', 'fast', 'old',
              'young', 'fat', 'blue',
              'cold', 'hot', 'small',
              'big', 'tall', 'cool',
              'sleepy', 'kind', 'angry']

nouns = ['dragon', 'goal', 'goalkeeper', 
         'world', 'forward', 'coach', 
         'referee', 'number', 'password', 
         'billiard', 'snooker', 'balley']

print ('Добро пожаловать!')

while True:
    
    for num in range(3):
        adjective1 = random.choice(adjectives)
        adjective2 = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
    
        password = adjective1 + adjective2 + noun + str(number) + special_char
        print('Новый пароль: %s' % password)

    response = input('Сгенерировать другие пароли? Введите д или н: ')
    if response == 'н':
        break