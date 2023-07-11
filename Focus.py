import time
from tkinter import *
window=Tk()
window.title('Focus Timer')
window.geometry("350x200")
lbl = Label(window, text="Start focusing!", font=("Arial Bold", 35))
lbl.grid(column=10, row=0)
def clicked():
  tite = Label(window, text="How many minutes do you want to focus?", font=("Arial", 20))
  spin = Spinbox(window, from_=1, to=240, width=10)
  spin.grid(column=0, row=0)
  focustime=spin.get()
  start = Button(window, text="Start focusing!", command=clicked)
  start.grid(column=2, row=0)

btn = Button(window, text="Start!", bg='green', fg='white', command=clicked)
btn.grid(column=10, row=10)
window.mainloop()
while True:
  focussec=focustime*60
  while focussec:
    mins,secs = divmod(focussec,60)
    timer='{:02d}:{:02d}'.format(mins,secs)
    print(timer, end='\n')
    time.sleep(1)
    focussec-=1

  print("Times up! Congrats! You can rest for a while.")
  continuee=input('Continue focusing?')
  if continuee=='yes' or 'Yes':
    continue
  if continuee=='No' or 'no':
    break

input()
  
