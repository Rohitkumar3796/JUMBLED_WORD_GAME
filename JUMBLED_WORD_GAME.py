# JUMBLED WORD GAME
import tkinter as tk
from tkinter import  messagebox
import random as rdm

window=tk.Tk()
window.title('JUMBLED WORD GAME')
window.geometry('250x200')
# list
fruits=['Apple','Mango','Cherry','Pomegrenate','Kiwi','Banana','Apricot','Avocado','Papaya','Watermelon','Pineapple']
# blank list
word_list=[]
num=rdm.randint(0,len(fruits)-1)
# here is for loop to append shuffle words 
for i in fruits:
    word=list(i)
    rdm.shuffle(word)
    word_list.append(word)

 
def random_words():
    global word_list, num
    label3.config(text=word_list[num])

# user input and then check it is correct or not 
def check_ans():
    global word_list,num,fruits
    user_input1=entry1.get()
    user_input=str(user_input1)
    user_input=user_input.capitalize()
    if user_input==fruits[num]:
        messagebox.showinfo("WON","Hurray!!!!!! You Are Correct ",)
        reset()
    else:
        messagebox.showinfo("LOOSE","So Sad!!!!!!!!!!!! Try Again ")
        entry1.delete(0, 'end')

def reset():
    global word_list,num,fruits
    num=rdm.randint(0,len(fruits)-1)
    label3.config(text=word_list[num])
    entry1.delete(0,'end')

label3=tk.Label(window,font=("Helvetica", "12"), borderwidth=2, relief="sunken")
label3.grid(pady=10,ipadx=15)

# fruits=tk.StringVar()
entry1=tk.Entry(window)
# entry1=tk.Entry(window)
entry1.grid()

btn1=tk.Button(window,text='Click',command=check_ans,)
btn1.grid(padx=100)

btn2=tk.Button(window,text='Reset',command=reset)
btn2.grid()

random_words()
window.mainloop()

