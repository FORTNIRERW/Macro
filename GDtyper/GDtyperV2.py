import pyautogui as pa
import time as ti
import random
writing = input("Paste Text Here")
mistake_chance_word = int(input("whats the chance of a mistake word: "))
mistake_chance_sentence = int(input("whats the chance of a mistake sentence: "))
if mistake_chance_word <=1:
    mistake_chance_word = 2
if mistake_chance_sentence <=1:
    mistake_chance_sentence = 2
typing_speed = float(input("what is the SPEED of typing LETTERS?  "))
deleting_speed = float(input("what is the SPEED of deleting? "))
hesitation_speed_words = float(input("how long do you HESITATE between WORDS? "))
hesitation_speed_sentences = float(input("how long do you HESITATE between SENTENCES? "))

pa.PAUSE = 0
current_word = ''
text = []
for i,letter in enumerate(writing):       
    if letter == ' ': #------------------------new word
        current_word+=' '
        text.append(str(current_word))
        current_word = ''
    elif letter =='.':#--------------------------new sentence
        text.append(str(current_word))
        current_word ='.'
    else: # -------------------------------- current word 
        current_word += letter
        if i == len(writing)-1:
            text.append(str(current_word)) 
sentences_correct = []
sentence = []
for i,word in enumerate(text):
    if word == '. ':
        sentence.append(str(word))
        sentences_correct.append(sentence)
        sentence = []
    elif i == len(text)-1:
        sentence.append(str(word))
        sentences_correct.append(sentence)
        sentence = []
    else:
        sentence.append(str(word))
ti.sleep(2)
pa.leftClick(2590,414)
ti.sleep(0.1)
pa.leftClick(2590,414)
ti.sleep(0.1)
pa.leftClick(2590,414)
ti.sleep(0.1)
pa.press('backspace')
for sent in sentences_correct:
    delete_sent = random.randrange(0,mistake_chance_sentence)
    if delete_sent == 1:
        fake_sent = random.choice(sentences_correct)
        print(fake_sent)
        for word in fake_sent:
            delete_word = random.randrange(0,mistake_chance_word)
            if delete_word == 1:
                pass
                # print(random.choice(fake_sent))
            pa.typewrite(word,random.uniform(0,hesitation_speed_words*2))
        for word in fake_sent:
            print(word)
            for char in word:
                pa.press('backspace')
                ti.sleep(deleting_speed)

    for word in sent:
        delete_word = random.randrange(0,mistake_chance_word)
        if delete_word == 1:
            print(random.choice(sent))
        pa.typewrite(word,random.uniform(0,hesitation_speed_words*2))












#THIS IS V1

"""things it does well :
    types out the words at different speeds
    deletes and retypes some of the words
    splits up the sentences and splits up the words"""

"""things that are missing :
    we need it to write entire phrases then delete them then rewrite the correct phrase
    we need to add random pauses like 2-3 that just completely pause writing for like 5m(can be changed)
    so it looks like you took a little break and then kept writing"""