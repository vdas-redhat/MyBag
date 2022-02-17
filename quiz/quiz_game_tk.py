import Tkinter
from Tkinter import *
import yaml
# This is just for the jpg image in pop up box
#from PIL import ImageTk, Image

"""
root = tk
labeltext = txt_label
"""
grey = "#808080"
offwhite = "#e3e3e3"

filepath = "quiz.yaml"

tk = Tkinter.Tk()
tk.title("Kaun Banega Gamer")
tk.geometry("800x600")

x = ''
tk.config(background=offwhite)
tk.resizable(0,0)
q_count = 0
v_list = []

def yaml_loader(filepath):
    with open (filepath, "r") as fileread:
        data = yaml.load(fileread)
        return data

def popup(msg):
    global pop,happy
    pop = Tkinter.Tk()
    pop.geometry("200x200")
    #pop.config(background='red')
    pop.title("Data")
    if msg == 'CORRECT':
        pop.config(background="goldenrod2")
        pop_lbl = Label(pop, text = msg, font = ("Times New Roman", 14), background = 'spring green')
        pop_lbl.pack(pady = (30,0))
        pop_button = Button(pop, text = "Next Question", font = ("default", 10, "bold"), bg='cyan', fg = 'black', border=2, height = 2, width = 12, command = lambda: cleaner('popup'))
        pop_button.pack(pady = (60,0))
    elif msg == "TRY AGAIN":
        msg_new = "WRONG ANSWER"
        pop.config(background="magenta2")
        pop_lbl = Label(pop, text = msg_new, font = ("Times New Roman", 14), background = 'red')
        pop_lbl.pack(pady = (30,0))
        pop_button = Button(pop, text = msg, font = ("default", 10, "bold"), bg='cyan2', fg = 'black', border=2, height = 2, width = 8, command = pop.destroy)
        pop_button.pack(pady = (60,0))

def selected():
    # when you click you get the index of the radio button
    global radio_default
    global x, data,q_count
    x = radio_default.get()
    if q_count <= len(data):
        q = data.keys()[q_count]
        a = data[q]  #second dictionary
        v = a.keys() #second dictionary keys
        if a[v[x]][0]:
            msg = "CORRECT"
            popup(msg)
        else:
            msg = "TRY AGAIN"
            popup(msg)
    else:
        print "Mid way"

def start():
    labelimage.destroy()
    txt_label.destroy()
    abt_label.destroy()
    button_start.destroy()
    game_loop()

def cleaner(hint):
    global rbutton
    global q_count
    global quest_label
    global radio1
    global button_game
    quest_label.destroy()
    radio1.destroy()
    for b in rbutton:
        b.destroy()
    button_game.destroy()
    if hint == "popup":
        pop.destroy()
    #q_count += 1
    q_count += 1
    game_loop()



def display_question(questions, qc):
    global quest_label
    q = questions.keys()[qc]
    a = questions[q]
    v = a.keys()
    quest_label = Label(tk, text = q, font = ("Consolas", 16), width = 500, justify = "center", wraplength = 400)
    quest_label.pack(pady = (50,0))
    return v

def display_answer(ans):
    global radio1, rbutton
    global x
    global radio_default
    radio_default = IntVar()
    rbutton = []
    val_count = 0
    #radio_default.set(0)
    for i in ans:
        radio1 = Radiobutton(tk, text = i, font = ("times", 14, "bold"), value = val_count, variable = radio_default, command = selected, background = 'NavajoWhite3')
        rbutton.append(radio1)
        val_count += 1
        radio1.pack(pady = (30,0))
        radio_default.set(-1)

def press_button():
    global button_game
    global radio1
    button_game = Button(tk, text = 'SUBMIT', font = ("default", 15, "bold"), bg='orange', fg = 'white', border=2, height = 2, width = 8, command = lambda: cleaner('normal'))
    button_game.pack(pady = (30,0))
    return True

def game_loop():
    global q_count
    global x, data
    #global radio_default
    global quest_label, button_game
    global radio1
    #radio_default = IntVar()
    #radio_default.set(-1)
    action = True
    data = yaml_loader(filepath)
    #data = {'What is the full name of Sachin Tendulkar ?': {' Sachin 10dulkar': [False], 'Sachin Ramesh Tendulkar': [True], 'Sachin Tendehar': [False], 'Sachin Ramya Tendulkar': [False]}, "What is Sachin Tendulkar's birth place ?": {'Chennai': [False], 'Gurgaon': [False], 'Delhi': [False], 'Bombay': [True]}}
    """
    if x != '':
        if q_count <= len(data)-1:
            q = data.keys()[q_count]
            a = data[q]
            v = a.keys()
            for i in v:
                print a[i]
    """
    if q_count <= len(data)-1:
        l_ans = display_question(data, q_count)
        display_answer(l_ans)
        action = press_button()
        #q_count += 1
    else:
        txt_label = Label(tk, text = "CONGRATULATIONS ON COMPLETING SACHIN SAGA", font = ("Comicsans", 24, "bold"), background = offwhite, wraplength = 700)
        txt_label.pack(pady = (100,0))


        button_end = Button(tk, text = 'THANK YOU !', font = ("default", 15, "bold"), bg='saddle brown', fg = 'white', border=2, height = 3, width = 10, command = tk.destroy)
        button_end.pack(pady = (50,0))


my_img = PhotoImage(file="sachin_cartoon.png")
labelimage = Label(tk, image = my_img, background = offwhite)
labelimage.pack(pady = (50,0))

txt_label = Label(tk, text = "SACHIN SAGA", font = ("Comicsans", 24, "bold"), background = offwhite)
txt_label.pack()


button_start = Button(tk, text = 'START', font = ("default", 15, "bold"), bg='orange', fg = 'white', border=2, height = 2, width = 8, command = start)
button_start.pack(pady = (30,0))

abt_label = Label(tk, text = "Let's see how much you know about the god of cricket.", font = ("Times New Roman", 15), background = offwhite)
abt_label.pack(pady = (30,0))


tk.mainloop()
