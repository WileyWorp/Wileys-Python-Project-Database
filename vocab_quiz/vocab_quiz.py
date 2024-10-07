import random as rand
import time
import vocab_quiz.list as list

words = list.vwords
defs = list.vdefs

mode = str(input("Would you like to input your own words? (y/n)"))

if mode == 'y':
    count = int(input("How many words do you have? "))
    for n in range(count):
        ask_word = input("What is the word? ")
        ask_def = input("What is the definition? ")
        words.append(ask_word)
        defs.append(ask_def)
elif mode == 'n':
    print("Okay! ")


print('''---------------------------------------------
''' * 100, "Time for your test")
time.sleep(1)

for t in range(len(words)):
  rw = rand.choice(words)
  index = words.index(rw)
  pdef = input('What is the definition of  ' + rw)
  while pdef != defs[words.index(rw)]:
    print("Incorrect")
    time.sleep(2)
    pdef = defs[words.index(rw)]
    print("The correct answer is ", pdef)
  words.pop(index)
  defs.pop(index)

print("Congratulations! You have completed the test!")