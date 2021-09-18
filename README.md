# Dice-Rolling-Python
## What is Tkinter?
Python offers various packages to design the GUI (Graphical User Interface). Tkinter is the most common, fast, and easy to use Python package used to build Graphical User Interface applications. It provides a powerful Object-Oriented Interface and is easy to use. Also, you develop an application; you can use it on any platform, which reduces the need of amendments required to use an app on Windows, Mac, or Linux.

## Dice Rolling in Python
We all know about dice. It’s a simple cube with numbers from 1 to 6 written on its face. But what is simulation? It is making a computer model. Thus, a dice simulator is a simple computer model that can roll a dice for us.

We aim to build a dice simulator which looks like:
![dice](https://user-images.githubusercontent.com/87347502/133890385-6d0b05f2-7b59-4e52-bf61-a8d43dbbe2ee.png)

## Build Dice Rolling Simulator by Python

### 1. Import libraries
+ Tkinter: Imported to use Tkinter and make GUI applications.
+ Image, Imagetk: Imported from PIL, Python Imaging Library. We use it to perform operations involving images in our UI. ***pip install Pillow***
+ Random: Imported to generate random numbers.
#### Start:
    import tkinter
    from PIL import Image, ImageTk
    import random
    
### 2. Building a top-level widget to make the main window for our application
    #top-level widget which represents the main window of an application
    root = tkinter.Tk()
    root.geometry('400x400')
    root.title('Roll Dice By SON BK')
    
### 3. Add Label into the frame
    BlankLine = tkinter.Label(root, text="")
    BlankLine.pack()

    #adding label with different font and formatting
    HeadingLabel = tkinter.Label(root, text="Hello from SON BK!", fg="light green", bg= "dark green", font="Helvetica 16 bold italic")
    HeadingLabel.pack()
#### Explanation:
Here, we use *pack()* to arrange our widgets in row and column form. The 'BlankLine' label is to skip a line, whereas we use 'HeadingLabel' label to give a heading.
+ ***root*** – the name by which we refer to the main window of the application
+ ***text*** – text to be displayed in the HeadingLabel
+ ***fg*** – the colour of the font used in HeadingLabel
+ ***bg*** – background colour of the HeadingLabel
+ ***font*** – used to give customised fonts to the HeadingLabel text
+ ***.pack()*** – Used to pack the widget onto the root window

### 4. Forming a list of images to be randomly displayed
    #images
    dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
    #simulating the dice with random numbers between 0 to 6 and generating image
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
#### Explanation:
+ ***dice*** is the list of names of images kept in same folder, which are chosen randomly according to the random number generated.
+ ***DiceImage*** is used to store an image of dice which is chosen by randomly generated numbers.

### 5. Constructing a label for image
    #construct a label widget for image
    ImageLabel = tkinter.Label(root, image=DiceImage)
    ImageLabel.image = DiceImage

    #packing a widget in the parent widget
    ImageLabel.pack(expand=True)
#### Explanation:
+ ***ImageLabel*** is to place an image in the window. The parameter expands declared as True so that even if we resize the window, image remains in the center.

### 6. Button and function
    #Design Button
    def roll_dice():
        DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        ImageLabel.configure(image=DiceImage)  #update image
        ImageLabel.image = DiceImage
    button = tkinter.Button(root, text="Roll Dice", fg="pink", command=roll_dice)
    button.pack(expand=True)

### 7. Forming a list of images to be randomly displayed
    root.mainloop()
#### Explanation:
+ ***root.mainloop()*** is used to open the main window. It acts as the main function of our program.
