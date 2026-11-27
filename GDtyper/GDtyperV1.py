import pyautogui as pa
import time as ti
import random
writing = input("Paste Text Here")
mistake_chance = int(input("whats the chance of a mistake?(only affects speed) 1/x <--- min 2: "))
if mistake_chance <=1:
    mistake_chance = 2
typing_speed = float(input("what is the SPEED of typing LETTERS?  "))
deleting_speed = float(input("what is the SPEED of deleting? "))
hesitation_speed_words = float(input("how long do you HESITATE between WORDS? "))
hesitation_speed_sentences = float(input("how long do you HESITATE between SENTENCES? "))

pa.PAUSE = 0

# sentences_writing = []
# sentence = ''
current_word = ''
# writing = writing.replace('#','   ')
# for char in writing:
#     if char =='.':
#         sentence+=char
#         sentences_writing.append(sentence)
#         sentence = ''
#     else:
#         sentence +=char


text = []
for i,letter in enumerate(writing):
    if letter != ' ' and letter != '':
        current_word += letter
        if i == len(writing)-1:
            text.append(current_word)        
    else:
        current_word+=' '
        text.append(str(current_word))
        current_word = ''
periods = 0
for letters in writing:
    if letters == '.':
        periods +=1
estimated_time = (periods*4 + len(writing)*0.005+ len(writing)*hesitation_speed_words)* (float(2/ mistake_chance))
print("estimated time "+str(estimated_time))
print(text)
ti.sleep(2)
pa.leftClick(2590,414)
ti.sleep(0.1)
pa.leftClick(2590,414)
ti.sleep(0.1)
pa.leftClick(2590,414)
ti.sleep(0.1)
pa.press('backspace')
print(text)

for i,word in enumerate(text):
    delete = random.randrange(1,mistake_chance)
    if delete == 1:
        fake_word = random.choice(text)
        pa.typewrite(fake_word,random.uniform(0,hesitation_speed_words*2))
        for y in range(0,len(fake_word)):
            pa.press('backspace')
            pa.PAUSE = 0
            ti.sleep(((random.uniform(0,deleting_speed*2))))
        pa.typewrite(word,random.uniform(0,hesitation_speed_words*2))
    else:
        pa.typewrite(word,random.uniform(0,hesitation_speed_words*2))
    if '.' in word:
        ti.sleep(random.uniform(0,hesitation_speed_sentences*2))
    ti.sleep(random.uniform(0,hesitation_speed_words*2))



#THIS IS V1

"""things it does well :
    types out the words at different speeds
    deletes and retypes some of the words
    splits up the sentences and splits up the words"""

"""things that are missing :
    we need it to write entire phrases then delete them then rewrite the correct phrase
    we need to add random pauses like 2-3 that just completely pause writing for like 5m(can be changed)
    so it looks like you took a little break and then kept writing"""