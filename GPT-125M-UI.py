import tkinter
from transformers import pipeline
import time
import linecache

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

  
# Top level window

master=tkinter.Tk()
master.title("GPT-Neo Ui")
master.geometry("1920x1080")
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    tempe = temperature.get(1.0, "end-1c")
    gen_text = generator(inp, do_sample=True, min_length=50, max_length=300, temperature=float(tempe))
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
printButton.place(x=860, y=930)

clearButton = tkinter.Button(master,text = "Clear", height=4, width=15, command = clearInput, bg='dimgray', activebackground="red")
clearButton.place(x=700, y=930)

copyButton = tkinter.Button(master,text = "Copy", height=2, width=15, command = save_text, bg='dimgray', activebackground="green")
copyButton.place(x=1060, y=925)

pasteButton = tkinter.Button(master,text = "Paste", height=2, width=15, command = open_text, bg='dimgray', activebackground="red")
pasteButton.place(x=1060, y=970)


  
# Label Creation
lbl = tkinter.Label(master, text = "Temperature:")
lbl.place(x=70, y=0)

temperature = tkinter.Text(master,height = 1, width = 10, font=('Fredoka One',17,''))
temperature.place(x=40, y=30)

temperature.insert('1.0', ("1.2"))

master.mainloop()