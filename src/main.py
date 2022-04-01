# Import

import turtle as trtl

words = open("wordlist.txt")
wordlist = []
matches = []

wordCount = 0
currentWord = ""
listOfWords = []

currentInput = ""
currentInputLetter = ""

wn = trtl.Screen()
wn.title("Typing Corrector")
wn.tracer(False)

# Setup

text = trtl.Turtle()
text.hideturtle()




# Functions

def writeInput():
  text.clear()
  text.write(currentInput, align="center", font=("Segoe UI", 20, "normal"))
  

def listify():
  wordlist = []
  for line in words:
    individualWord = line.strip()
    wordlist.append(individualWord)

def sift():
  matches = []
  for item in wordlist:
    if currentInput in wordlist[item]:
      matches.append(wordlist[item])

def wordBreakup():
  currentWord = ""
  wordCount = 1
  listOfWords = []
  for letter in currentInput:
    currentWord =  " ".join([currentWord, letter])
    #currentWord = str(currentWord) + str(currentInput[letter])
    if letter == " ":
      listOfWords.append(currentWord)
      currentWord = ""
      wordCount += 1
  print(listOfWords)



def printInput():
  #for i in range(10):
  #  print("")
  #print(currentInput)
  wordBreakup()
  sift()
  writeInput()


# Key Inputs

wn.listen()

def aPressed():
  global currentInput
  currentInput = currentInput + "a"
  printInput()

def bPressed():
  global currentInput
  currentInput = currentInput + "b"
  printInput()

def cPressed():
  global currentInput
  currentInput = currentInput + "c"
  printInput()

def dPressed():
  global currentInput
  currentInput = currentInput + "d"
  printInput()

def ePressed():
  global currentInput
  currentInput = currentInput + "e"
  printInput()

def fPressed():
  global currentInput
  currentInput = currentInput + "f"
  printInput()

def gPressed():
  global currentInput
  currentInput = currentInput + "g"
  printInput()

def hPressed():
  global currentInput
  currentInput = currentInput + "h"
  printInput()

def iPressed():
  global currentInput
  currentInput = currentInput + "i"
  printInput()

def jPressed():
  global currentInput
  currentInput = currentInput + "j"
  printInput()

def kPressed():
  global currentInput
  currentInput = currentInput + "k"
  printInput()

def lPressed():
  global currentInput
  currentInput = currentInput + "l"
  printInput()

def mPressed():
  global currentInput
  currentInput = currentInput + "m"
  printInput()

def nPressed():
  global currentInput
  currentInput = currentInput + "n"
  printInput()

def oPressed():
  global currentInput
  currentInput = currentInput + "o"
  printInput()

def pPressed():
  global currentInput
  currentInput = currentInput + "p"
  printInput()

def qPressed():
  global currentInput
  currentInput = currentInput + "q"
  printInput()

def rPressed():
  global currentInput
  currentInput = currentInput + "r"
  printInput()

def sPressed():
  global currentInput
  currentInput = currentInput + "s"
  printInput()

def tPressed():
  global currentInput
  currentInput = currentInput + "t"
  printInput()

def uPressed():
  global currentInput
  currentInput = currentInput + "u"
  printInput()

def vPressed():
  global currentInput
  currentInput = currentInput + "v"
  printInput()

def wPressed():
  global currentInput
  currentInput = currentInput + "w"
  printInput()

def xPressed():
  global currentInput
  currentInput = currentInput + "x"
  printInput()

def yPressed():
  global currentInput
  currentInput = currentInput + "y"
  printInput()

def zPressed():
  global currentInput
  currentInput = currentInput + "z"
  printInput()

def spacePressed():
  global currentInput
  currentInput = currentInput + " "
  printInput()

def bkspcPressed():
  global currentInput
  tempInput = ""
  for ltr in range(len(currentInput)-1):
    tempInput = tempInput + currentInput[ltr]
  currentInput = tempInput
  printInput()



wn.onkeypress(aPressed, "a")

wn.onkeypress(bPressed, "b")

wn.onkeypress(cPressed, "c")

wn.onkeypress(dPressed, "d")

wn.onkeypress(ePressed, "e")

wn.onkeypress(fPressed, "f")

wn.onkeypress(gPressed, "g")

wn.onkeypress(hPressed, "h")

wn.onkeypress(iPressed, "i")

wn.onkeypress(jPressed, "j")

wn.onkeypress(kPressed, "k")

wn.onkeypress(lPressed, "l")

wn.onkeypress(mPressed, "m")

wn.onkeypress(nPressed, "n")

wn.onkeypress(oPressed, "o")

wn.onkeypress(pPressed, "p")

wn.onkeypress(qPressed, "q")

wn.onkeypress(rPressed, "r")

wn.onkeypress(sPressed, "s")

wn.onkeypress(tPressed, "t")

wn.onkeypress(uPressed, "u")

wn.onkeypress(vPressed, "v")

wn.onkeypress(wPressed, "w")

wn.onkeypress(xPressed, "x")

wn.onkeypress(yPressed, "y")

wn.onkeypress(zPressed, "z")

wn.onkeypress(spacePressed, "space")

wn.onkeypress(bkspcPressed, "Left")


wn.mainloop()



