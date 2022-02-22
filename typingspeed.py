from tkinter import *
import random
from tkinter import messagebox

wordsSet = ['army', 'beautiful', 'became', 'if', 'actually', 'became', 'arrow', 'article', 'therefore',
            'python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone', 'Rock', 'Paper', 'scissor',
            'swot', 'tie', 'saunter', 'market', 'confused', 'close', 'swift', 'ignore', 'brainy', 'governor', 'infect',
            'spray', 'baseball', 'dull', 'kid', 'modern', 'zonked', 'kitten', 'real', 'apparatus', 'carve', 'gusty',
            'impart',
            'slay', 'slow', 'delicious', 'boot', 'crowd', 'rub', 'ten', 'rambunctious', 'ethereal', 'grain', 'previous',
            'hypnotize', 'ducks', 'whip', 'match', 'acceptable', 'exist', 'close', 'amuck', 'broad', 'astonishing',
            'careless', 'idiotic',
            'belong', 'same', 'example', 'cope']


def timer():
    global timeLeft, correctScore, wrongScore
    if timeLeft <= 10:
        timeLabelCount.configure(fg='#B00D23')

    if timeLeft > 0:
        timeLeft = timeLeft - 1
        timeLabelCount.configure(text=timeLeft)
        timeLabelCount.after(1000, timer)
    else:
        gameInfo.configure(
            text='Words Per Minute = {} \n Errors = {} \n Accuracy = {}%'.format(correctScore, wrongScore, (
                    correctScore * 100 / (correctScore + wrongScore))))
        retrymessage = messagebox.askretrycancel('Notice',
                                                 'Words Per Minute = {} \n Errors = {} \n Accuracy = {}%'.format(
                                                     correctScore, wrongScore,
                                                     (correctScore * 100 / (correctScore + wrongScore))))
        if retrymessage:
            correctScore = 0
            wrongScore = 0
            timeLeft = 60
            timeLabelCount.configure(text=timeLeft)
            wordLabel.configure(text='Press Enter to start')
            scoreLabelCount.configure(text=correctScore)
            gameInfo.configure(text='Instructions : \n1.Type the Word and hit Enter\n2.Be Quick!',
                               font=('Helvetica', 15), bg='#28282B', fg='#F8F8FF')
            wordEntry.delete(0, END)
        else:
            window.destroy()


def startGame(event):
    if timeLeft == 60:
        timer()
    global correctScore, wrongScore
    gameInfo.configure(text='')
    if wordEntry.get() == wordLabel['text']:
        correctScore = correctScore + 1
        scoreLabelCount.configure(text=correctScore)

    else:
        wrongScore = wrongScore + 1


    random.shuffle(wordsSet)
    wordLabel.configure(text=wordsSet[0])
    wordEntry.delete(0, END)


#  Windows
window = Tk()
window.geometry('800x600+260+100')
window['background'] = '#28282B'
window.title(' Typing Speed Test')
window.iconbitmap('logo.ico')

# Variables
correctScore = 0
timeLeft = 60
wrongScore = 0

# Labels
fontLabel = Label(window, text='Typing Speed Test', font=('Helvetica', 25), fg='white', bg='#28282B')
fontLabel.place(x=275, y=30)

random.shuffle(wordsSet)

wordLabel = Label(window, text="Press Enter to start", font=('Helvetica', 35), justify='center', anchor=CENTER)
wordLabel.place(x=250, y=200)

scoreLabel = Label(window, text='Your Score : ', font=('Helvetica', 15), bg='#28282B', fg='#FFFFFF')
scoreLabel.place(x=20, y=350)

scoreLabelCount = Label(window, text=correctScore, font=('Helvetica', 15, 'bold'), bg='#28282B', fg='#008080')
scoreLabelCount.place(x=125, y=350)

timerLabel = Label(window, text='Time Left : ', font=('Helvetica', 15), bg='#28282B', fg='#FFFFFF')
timerLabel.place(x=650, y=350)

timeLabelCount = Label(window, text=timeLeft, font=('Helvetica', 17, 'bold'), bg='#28282B', fg='#008080')
timeLabelCount.place(x=743, y=350)

gameInfo = Label(window, text='Instructions : \n1.Type the Word and hit Enter\n2.Be Quick!',
                 font=('Helvetica', 15), bg='#28282B', fg='#F8F8FF')
gameInfo.place(x=250, y=450)

# Entry
wordEntry = Entry(window, font=('Helvetica', 20))
wordEntry.place(x=255, y=280)
wordEntry.focus_set()

#
window.bind('<Return>', startGame)
window.resizable(0, 0)
window.mainloop()
