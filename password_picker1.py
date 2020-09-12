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
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    
    password = adjective + noun + str(number) + special_char
    print('Новый пароль: %s' % password)

    response = input('Сгенерировать другой пароль? Введите д или н: ')
    if response == 'н':
        break