from random import shuffle
from itertools import chain

def isReadyToPlay():
    isReady = str(input("Are you ready to play? "))
    while isReady.lower() != "yes":
        isReady = str(input("Are you ready now? "))

def playGame(gameFile):
    counter = 1
    score = 0
    i = 0
    j = 1
    questionList = gameFile.readlines()
    questionList = randomizeList(questionList)
    while i < (len(questionList) - 1):
        triviaQuestion = questionList[i]
        triviaQuestion = triviaQuestion.replace("\n", "")
        userAnswer = input("Question " + str(counter) + ": " + triviaQuestion + " ")
        userEndGame(userAnswer, score, questionList)
        counter += 1
        i += 2
        while j < len(questionList):
            triviaAnswer = questionList[j]
            triviaAnswer = triviaAnswer.replace("\n", "")
            j += 2
            if userAnswer == triviaAnswer:
                print("Correct!")
                score += 10
                print("Score: " + str(score))
                print()
                break
            else:
                print("Incorrect. The correct answer is " + triviaAnswer + ".")
                print("Score: " + str(score))
                print()
                break
    endOfGame(score, questionList)

def endOfGame(score, questionList):
    print()
    print("Game over. Your final score is: " + str(score))
    print()

def userEndGame(userAnswer, score, questionList):
    if userAnswer == "END":
        endOfGame(score, questionList)
        exit()

def whichTriviaCategory():
    usersCategory = str(input("Which category of trivia would you like to play? Animals? Geography? Human Anatomy? "))
    print()
    if usersCategory.lower() == "animals":
        gameFile = open("animalTrivia.txt", "r")
        playGame(gameFile)
        gameFile.close()
    elif usersCategory.lower() == "geography":
        gameFile = open("geograpyTrivia.txt")
        playGame(gameFile)
        gameFile.close()
    elif usersCategory.lower() == "human anatomy":
        gameFile = open("humanAnatomyTrivia.txt", "r")
        playGame(gameFile)
        gameFile.close()
    else:
        print("You have entered an invalid category.")
        exit()


def randomizeList(questionList):
    randomizedQuestionList = []
    i = 0
    while i < len(questionList):
        randomizedQuestionList.append(questionList[i:i+2])
        i += 2
    shuffle(randomizedQuestionList)
    return list(chain(*randomizedQuestionList))

def authorNote():
    print()
    print("NOTE: Answers are case sensitive and will be counted wrong if not properly capitalized where needed to. You only need to enter the letter for multiple choice questions. When entering numbers, enter the numerical value instead of the word itself. Enter 'END' to exit the game manually.")
    print()
    print("LET'S BEGIN!")
    print()

def welcomeNote():
    print()
    print("WELCOME TO THE GREATEST TRIVIA GAME ON EARTH!")
    print()


def main():
    #Calls the function to welcome the player to the game
    welcomeNote()
    #Calls the function that checks to see if the user is ready to play the game
    isReadyToPlay()
    #Calls the function that gives the author's notes to the player
    authorNote()
    #Calls the function that allows the player to choose which category of trivia
    #he/she would like to play, and then the game is run from within
    whichTriviaCategory()
main()
