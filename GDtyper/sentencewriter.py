import pyautogui as pa
import time as ti
import random
writing = input("Paste Text Here")


current_word = ''
text = []
for i,letter in enumerate(writing):       
    if letter == ' ': #------------------------new word
        current_word+=' '
        text.append(str(current_word))
        current_word = ''
    elif letter =='.':#--------------------------new sentence
        text.append(current_word)
        current_word ='.'
    else: # -------------------------------- current word 
        current_word += letter
        if i == len(writing)-1:
            text.append(current_word) 
print(text)
sentences_correct = []
sentence = ''
for i,word in enumerate(text):
    if word == '. ':
        sentence +=word
        sentences_correct.append(sentence)
        sentence = ''
    elif i == len(text)-1:
        sentence +=word
        sentences_correct.append(sentence)
        sentence = ''
    else:
        sentence += word
print(sentences_correct)


