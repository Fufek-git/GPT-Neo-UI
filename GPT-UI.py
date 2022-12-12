import tkinter
from transformers import pipeline
import time
import linecache
from ttkthemes import ThemedStyle

master=tkinter.Tk()
master.title("GPT-Neo Ui")
master.geometry("1920x1080")
style = ThemedStyle(master)
master.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

options_list = ['EleutherAI/gpt-neo-1.3B', 'EleutherAI/gpt-neo-125M']
  
# Variable to keep track of the option
# selected in OptionMenu
model = tkinter.StringVar(master)
  
# Set the default value of the variable
model.set('EleutherAI/gpt-neo-125M')
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu = tkinter.OptionMenu(master, model, *options_list)
question_menu.place(x=10, y=160)
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    tempe = temperature.get(1.0, "end-1c")
    lenght = maxlenght.get(1.0, "end-1c")
    generator = pipeline('text-generation', model=format(model.get()))
    gen_text = generator(inp, do_sample=True, min_length=1, max_length=int(lenght), temperature=float(tempe))
    inputtxt.delete("1.0",tkinter.END)
    inputtxt.insert('1.0', (gen_text[0]['generated_text']) )

def clearInput():
    inputtxt.delete("1.0",tkinter.END)

# Copy an Paste Functions
def open_text():
   inputtxt.delete("1.0",tkinter.END)
   text_file = open("saved.txt", "r")
   content = text_file.read()
   inputtxt.insert("end-1c", content)
   text_file.close()

def save_text():
   text_file = open("saved.txt", "w")
   text_file.write(inputtxt.get(1.0, "end-1c"))
   text_file.close()



  
# TextBox Creation
inputtxt = tkinter.Text(master,height = 30, width = 100, font=('Fredoka One',17,''))
inputtxt.pack()
  
# Button Creation
printButton = tkinter.Button(master, text = "Generate", height=4, width=20, command = printInput, bg='orange', activebackground="green")
printButton.place(x=860, y=860)

clearButton = tkinter.Button(master,text = "Clear", height=4, width=15, command = clearInput, bg='dimgray', activebackground="red")
clearButton.place(x=700, y=860)

copyButton = tkinter.Button(master,text = "Copy", height=2, width=15, command = save_text, bg='dimgray', activebackground="green")
copyButton.place(x=1060, y=850)

pasteButton = tkinter.Button(master,text = "Paste", height=2, width=15, command = open_text, bg='dimgray', activebackground="red")
pasteButton.place(x=1060, y=905)


  
# Label Creation
lbl = tkinter.Label(master, text = "Temperature:")
lbl.place(x=70, y=0)

temperature = tkinter.Text(master,height = 1, width = 10, font=('Fredoka One',17,''))
temperature.place(x=40, y=30)

lbl = tkinter.Label(master, text = "Max lenght:")
lbl.place(x=70, y=90)

maxlenght = tkinter.Text(master,height = 1, width = 10, font=('Fredoka One',17,''))
maxlenght.place(x=40, y=120)

temperature.insert('1.0', ("1.2"))
maxlenght.insert('1.0', ("150"))

master.mainloop()