# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:04:29 2018

@author: S
"""
#
q = 'What can you answer?'
q1 = 'What is your name?'
q2 = 'What is your quest?'
q3 = 'What do you do in your free time?'
q4 = 'What else would you like to tell us that you haven\'t already expressed through the application?'
q5 = 'What are you most excited to learn about this quarter?'
#输入问题
question = input("Ask me a question: ")
if question == q:
    print(q1+'\n'+q2+'\n'+q3+'\n'+q4+'\n'+q5)
elif question == q1:
    print ('It is Vickey, soulmate of Salamander Fire')
elif question == q2:
    print('To be the one you are to be')
elif question == q3:
    print('To muse, to relax')
elif question == q4:
    print('emmm time for you to guess')
elif question == q5:
    print('Frankly,to learn how to write a love letter in python')
else :
    print('Error: unknown question')