from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

#data=pandas.read_csv("data/spanish_words.csv")
#print(data)

window=Tk()
window.title("Flash Card App")
#window.minsize(width=900, height=500)
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
card_front_image=PhotoImage(file="images/card_front.png")
canvas=Canvas(width=800,height=526)
canvas.create_image(400,263,image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.create_text(400,150,text="Español",font=("Times New Roman",40,"italic"))
canvas.create_text(400,256,text="word",font=("Times New Roman",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
#BUTTONS
cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightbackground=BACKGROUND_COLOR)
unknown_button.grid(column=0,row=1)

check_image=PhotoImage(file="images/right.png")
known_button=Button(image=check_image,highlightbackground=BACKGROUND_COLOR)
known_button.grid(column=1,row=1)

window.mainloop()