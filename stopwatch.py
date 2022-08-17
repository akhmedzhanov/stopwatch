import tkinter as tk
from datetime import datetime


temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(100, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id)

def continue_tick():
    tick()
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()

def reset_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()


root = tk.Tk()
root.title('Секундомер')
root.resizable(height=False, width=False)
root.geometry('300x160+50+50')

label1 = tk.Label(root, width=20, font=('Times New Roman', 20), text='00:00')
label1.pack()

btnStart = tk.Button(root, text='Start', font=('Times New Roman', 20), width = 20, command=start_tick)
btnStop = tk.Button(root, text='Stop', font=('Times New Roman', 20), width = 20, command=stop_tick)
btnContinue = tk.Button(root, text='Continue', font=('Times New Roman', 20), width = 20, command=continue_tick)
btnReset = tk.Button(root, text='Reset', font=('Times New Roman', 20), width = 20, command=reset_tick)

btnStart.pack()


root.mainloop()
