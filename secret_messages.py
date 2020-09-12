#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even (len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def encrypt(message):
     swapped_message = swap_letters(message)
     encrypted_message = ''.join(reversed(swapped_message))
     return encrypted_message

def decrypt(message):
    unreversed_message = ''.join(reversed(message))
    decrypted_message = swap_letters(unreversed_message)
    return decrypted_message

def get_task():
    task = simpledialog.askstring('Задание', 'Что сделать: зашифровать или расшифровать?')
    return task

def get_message():
    message = simpledialog.askstring('Сообщение', 'Введите секретное сообщение: ')
    return message

root = Tk()
root.withdraw()

while True:
    task = get_task()
    if task == 'зашифровать':
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo('Зашифрованное сообщение:', encrypted)
    elif task == 'расшифровать':
        message = get_message()
        decrypted = decrypt(message)
        messagebox.showinfo('Расшифрованное сообщение:', decrypted)
    else:
        break