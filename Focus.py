import time
while True:
  focustime=int(input("How long do you want to focus? Please enter minutes."))
  focussec=focustime*60
  while focussec:
    mins,secs = divmod(seconds,60)
    timer='{:02d}:{:02d}'.format(mins,secs)
    print(timer, end='/n')
    time.sleep(1)
    seconds-=1

  print("Times up! Congrats! You can rest for a while.")
  continuee=input('Continue focusing?')
  if continuee=='yes' or 'Yes':
    continue
  if continuee=='No' or 'no':
    break

input()
  
