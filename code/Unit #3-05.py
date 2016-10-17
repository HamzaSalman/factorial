# coding: utf-8

import ui

counter = 1
print ('enter a number')
number = raw_input()
answer = 1

number = int(number) + 1
while (number != counter):
    answer = answer * counter
    counter = counter + 1
print ('the factorial is') + str(answer)
