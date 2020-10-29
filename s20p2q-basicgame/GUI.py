'''Graphical User Interface Menu File
Implemented by Jacob Lussier
March 2,2020'''

from tkinter import *
from PIL import Image
from PIL import ImageTk
import webbrowser

def setupMenu():
    # Create a new Tkinter window called menu
    menu = Tk()
    # Sets the menu to fullscreen at startup
    menu.attributes("-fullscreen", True)
    # Sets the size of the menu window
    menu.geometry("6000x6000")
    # Sets the background of the menu window
    menu.configure(background = "green")
    # Blackjack logo label    
    bjLogo = Image.open("images\textfx.png")
    #The (550, 100) is (height, width)
    bjLogo = bjLogo.resize((550,100), Image.ANTIALIAS) 
    # Convert the PIL images to a general TK photo image
    bjLogo = ImageTk.PhotoImage(bjLogo) 
    
    suitsImage = ImageTk.PhotoImage(Image.open("images\suits.png").resize((150,150), Image.ANTIALIAS))
    suitsLabel = Label(menu, image = suitsImage)
    suitsLabel.place(x = 250, y = 50)
    suitsLabel.configure(background = "green")
    suitsLabel2 = Label(menu, image = suitsImage)
    suitsLabel2.place(x = 1075, y = 50)
    suitsLabel2.configure(background = "green")
    
    cardsImage = ImageTk.PhotoImage(Image.open("images\cards.png").resize((100,100), Image.ANTIALIAS))
    cardsLabel = Label(menu, image = cardsImage)
    cardsLabel.place(x = 675, y = 0)
    cardsLabel.configure(background = "green")
    
    titleLabel = Label(menu, image = bjLogo)
    titleLabel.place(x = 460, y = 110)
    titleLabel.configure(background = "green")
    
    playImage = ImageTk.PhotoImage(Image.open("images\play.png"))
    playButton = Button(menu, image=playImage,borderwidth = 0,command = playClick)
    playButton.configure(background = "green")
    playButton.place(x = 615,y=300)
    
    rulesImage = ImageTk.PhotoImage(Image.open("images\rules.png"))
    rulesButton = Button(menu, image=rulesImage,borderwidth = 0)
    rulesButton.configure(background = "green",command = rulesClick)
    rulesButton.place(x = 615,y=400)
    
    
    exitImage = ImageTk.PhotoImage(Image.open("images\exit.png"))
    exitButton = Button(menu, image=exitImage,borderwidth = 0,command = exitClick)
    exitButton.configure(background = "green")
    exitButton.place(x = 615,y=500)
    
    return menu

'''
# Function to open a web url using webrowser module
def callback(url):
    webbrowser.open_new(url)
'''
# Function to handle rules button click
def rulesClick():
    # calls the callback function passing the black rules web address
    #callback("https://www.888casino.com/blog/blackjack-strategy-guide/how-to-play-blackjack")
    pass

# Function for the exit button
def exitClick():
    # destroys the window so it closes
    menu.destroy()

def changeToMan():
    global manLabel
    manLabel = Label(mainGame, image = manImage)
    manLabel.place(x = 390, y = 520)
    manLabel.configure(background = "green")
    girlLabel.destroy()
def changeToGirl():
    global girlLabel
    girlLabel = Label(mainGame, image = girlImage)
    girlLabel.place(x = 410, y = 520)
    girlLabel.configure(background = "green")
    manLabel.destroy()


def playClick():
    global dealerImage
    global manImage
    global girlImage
    global manHeadImage
    global girlHeadImage
    global playerLabel
    global mainGame
    global bankValue
    global fiftyImage
    global hundredImage
    global thousandImage
    global deckImage
    global hitImage
    global standImage
    global doubleImage
    global welcomeImage
    global welcomeLabel
    
    # create a new window for the main game
    mainGame = Toplevel()
    # Withdram hides the menu window
    menu.withdraw()
    mainGame.attributes("-fullscreen", True)
    mainGame.geometry("6000x6000")
    mainGame.configure(background = "green")
    
    dealerImage = ImageTk.PhotoImage(Image.open("images\dealer.png").resize((275,275), Image.ANTIALIAS))
    dealerLabel = Label(mainGame, image = dealerImage)
    dealerLabel.place(x = 367, y = 100)
    dealerLabel.configure(background = "green")
    dealerTagLabel = Label(mainGame, text = "Dealer", fg = "black",bg = "green", font = 16)
    dealerTagLabel.place(x = 470, y = 75)

    girlImage = ImageTk.PhotoImage(Image.open("images\girl.png").resize((150,200), Image.ANTIALIAS))
    girlHeadImage = ImageTk.PhotoImage(Image.open("images\girlHead.png").resize((85,85), Image.ANTIALIAS))
    manImage = ImageTk.PhotoImage(Image.open("images\man.png").resize((200,200), Image.ANTIALIAS))
    manHeadImage = ImageTk.PhotoImage(Image.open("images\manHead.png").resize((85,85), Image.ANTIALIAS))
    selectImage = ImageTk.PhotoImage(Image.open("images\select.png").resize((200,200), Image.ANTIALIAS))
    playerTagLabel = Label(mainGame,text = "Player", fg = "black", bg = "green", font = 16)
    playerTagLabel.place(x = 460, y = 475)

    manSelectButton = Button(mainGame, image=manHeadImage,borderwidth = 0,command = lambda: changeToMan())
    manSelectButton.configure(background = "green")
    manSelectButton.place(x = 1,y=778)

    girlSelectButton = Button(mainGame, image=girlHeadImage,borderwidth = 0,command = lambda: changeToGirl())
    girlSelectButton.configure(background = "green")
    girlSelectButton.place(x = 100,y=778)

    playerSelectLabel = Label(mainGame, text = "Character Select", fg = "black",bg = "green", font = 16)
    playerSelectLabel.place(x = 15, y = 740)

    bankValue = 0

    bankLabel = Label(mainGame, text = "Player Bank = " + str(bankValue), fg = "black",bg = "green", font = 18)
    bankLabel.place(x = 410,y = 725)

    fiftyImage = ImageTk.PhotoImage(Image.open("images\50.png").resize((165,125), Image.ANTIALIAS))
    
    fiftySelectButton = Button(mainGame, image=fiftyImage,borderwidth = 0)
    fiftySelectButton.configure(background = "green")
    fiftySelectButton.place(x = 55,y=500)

    hundredImage = ImageTk.PhotoImage(Image.open("images\100.png").resize((115,115), Image.ANTIALIAS))
    
    hundredSelectButton = Button(mainGame, image= hundredImage,borderwidth = 0)
    hundredSelectButton.configure(background = "green")
    hundredSelectButton.place(x = 80,y=370)

    thousandImage = ImageTk.PhotoImage(Image.open("images\500.png").resize((115,115), Image.ANTIALIAS))
    
    thousandSelectButton = Button(mainGame, image= thousandImage,borderwidth = 0)
    thousandSelectButton.configure(background = "green")
    thousandSelectButton.place(x = 80,y=225)

    betAmountLabel =  Label(mainGame, text = "Select Bet Amount", fg = "black",bg = "green", font = 18)
    betAmountLabel.place(x = 55, y = 170)

    deckImage = ImageTk.PhotoImage(Image.open("images\deck.png").resize((110,145), Image.ANTIALIAS))

    deckButton = Button(mainGame, image = deckImage,borderwidth = 0)
    deckButton.place(x = 280, y = 150)
    deckButton.configure(background = "green")

    hitImage = ImageTk.PhotoImage(Image.open("images\hit.png").resize((200,50), Image.ANTIALIAS))

    hitButton = Button(mainGame, image = hitImage,borderwidth = 0)
    hitButton.place(x = 660, y = 420)
    hitButton.configure(background = "green")

    standImage =  ImageTk.PhotoImage(Image.open("images\stand.png").resize((215,50), Image.ANTIALIAS))

    standButton = Button(mainGame, image = standImage,borderwidth = 0)
    standButton.place(x = 900, y = 420)
    standButton.configure(background = "green")

    doubleImage = ImageTk.PhotoImage(Image.open("images\double.png").resize((220,50), Image.ANTIALIAS))

    doubleButton = Button(mainGame, image = doubleImage,borderwidth = 0)
    doubleButton.place(x = 1155, y = 420)
    doubleButton.configure(background = "green")

    welcomeImage = ImageTk.PhotoImage(Image.open("images\welcome.png").resize((1400,80), Image.ANTIALIAS))

    welcomeLabel = Label(mainGame, image = welcomeImage, bg = "green")
    welcomeLabel.place(x = 40, y = 20 )





