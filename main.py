# import libraries
import tkinter
from PIL import Image, ImageTk
import random

# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll Dice By SON BK')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello from SON BK!", fg="light green", bg= "dark green", font="Helvetica 16 bold italic")
HeadingLabel.pack()

# images
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget
ImageLabel.pack(expand=True)

# Design Button
def roll_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)  #update image
    ImageLabel.image = DiceImage
button = tkinter.Button(root, text="Roll Dice", fg="blue", command=roll_dice)
button.pack(expand=True)

root.mainloop()