# Import
import turtle as trtl

words = open("wordlist.txt") # Imports the .txt file

# Variables Setup

wordlist = []
matches = []

wordCount = 0
currentWord = ""
listOfTypedWords = []

currentInput = ""
currentInputLetter = ""
correctedWord = ""

lastTypedWord = ""
listOfFrequencies = []

# Turtle Setup

wn = trtl.Screen()
wn.title("Typing Corrector")
wn.tracer(False) # Keeps screen updates instant

text = trtl.Turtle()
text.hideturtle()

# Functions

def writeInput(): # Displays any necessary information on the screen.
  text.clear()
  text.goto(0,0)
  text.write(currentInput, align="center", font=("Segoe UI", 25, "normal"))
  if correctedWord != lastTypedWord:
    text.goto(0,-50)
    message = "Correct " + lastTypedWord + " to " + correctedWord + "?"
    text.write(message, align="center", font=("Segoe UI", 17, "normal"))
    text.goto(0, -80)
    text.write("Click anywhere to accept.", align="center", font=("Segoe UI", 14, "normal"))

def listify(): # Imports the .txt file and converts it to a list, from which it can pull values.
  global wordlist
  wordlist = []
  for line in words:
    individualWord = line.strip()
    wordlist.append(individualWord) # This function was taken with permission from github user Ethan-Francolla

def generateFrequencies(): # Creates a parallel list with weights for every word in the wordlist
  global lastTypedWord, perLengthScore, listOfTypedWords, wordlist, listOfFrequencies, letterInWord
  lastTypedWord = listOfTypedWords[len(listOfTypedWords) - 1]
  perLengthScore = 0
  listOfFrequencies = []
  for item in wordlist: # Loops through every word in the wordlist
    letterInWord = 0
    wordScore = 0
    perLengthScore = 0
    if abs(len(item) - len(lastTypedWord)) < 2: # Allows word corrections to be a maximum length of 1 letter off above or below
      if len(item) == len(lastTypedWord):
        wordScore += 4 # Even though other lengths are allowed, same length corrections are favored
      for letter in item: # Loops through every letter in the item
        if letterInWord < len(lastTypedWord):
          if letter in lastTypedWord: # Checks if the letter is also in the user-typed word
            if lastTypedWord[letterInWord] == item[letterInWord]: # If above is true, checks if the letter is in the same spot
              wordScore += 3 # If in the same spot, the word is weighted more
            else:
              wordScore += 1 # If not in the same spot, the word is weighted less
        letterInWord += 1
      perLengthScore = wordScore / len(item)       
    else:
      perLengthScore = 0
    listOfFrequencies.append(perLengthScore) # Appends the weight to the list of weights

def findHighestWord(): # Runs through the weight list to find the item with the highest weight, finds the corresponding word
  global wordlist, listOfFrequencies, highestScore, correctedWord
  highestScore = 0
  for item in listOfFrequencies:
    if item > highestScore:
      highestScore = item
  correctedWord = wordlist[listOfFrequencies.index(highestScore)]


def wordBreakup(): # Breaks up the user input string into a list of words
  global currentWord, listOfTypedWords
  currentWord = ""
  wordCount = 1
  listOfTypedWords = []
  for letter in currentInput:
    if letter == " ": # Creates a new word if the current letter is a space
      listOfTypedWords.append(currentWord)
      currentWord = ""
      wordCount += 1
    else:
      currentWord =  "".join([currentWord, letter])

def changeWord(x,y): # Changes the wrong word to the correct one
  global listOfTypedWords, correctedWord, lastTypedWord, currentInput
  lastTypedWord = listOfTypedWords.pop()
  listOfTypedWords.append(correctedWord)
  lastTypedWord = correctedWord
  currentInput = " ".join(listOfTypedWords)
  currentInput = currentInput + " "
  writeInput()

def printInput(): # Master function that controls the calling of other functions
  global correctedWord, lastTypedWord
  wordBreakup()
  if len(listOfTypedWords) > 0 and currentInput[len(currentInput) - 1] == " ": # Only calls these if a word has just been completed
    if lastTypedWord in wordlist:
      correctedWord = lastTypedWord
    else:
      generateFrequencies()
      findHighestWord()
  writeInput()

listify()

# Key Input Functions

wn.listen() # Allows the program to check for key inputs

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

# Raw Key Inputs

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

trtl.onscreenclick(changeWord)


# Mainloop

wn.mainloop() # Keeps the screen persistent