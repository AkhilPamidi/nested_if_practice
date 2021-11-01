from coins import Coin
coin=Coin()
print("welcome to the joy ride")
height=int(input("what is your height in cm? \n"))
bill=0
if height<=120:
  print("sorry you cant have the ride!")
else:
  age=int(input("what is your age? \n"))
  if age<=8:
    print("sorry you cant have the ride")
  else:
    if age>8 and age<=12:
      print("your ticket price for a ride is 5$")
      bill+=5
    elif age>12 and age<=18:
      print("your ticket price for a ride is 7$")
      bill+=7
    elif age>18:
      print("your ticket price for a ride is 10$ ")
      bill+=10
    photo=input("do you like to have photo? type y or n \n").lower()
    if photo=="y":
      bill+=2
      print(f"your photo bill is 2$ and your total bill is {bill}$")
    mode_of_payment=int(input("for coin payment mode type '1'\n for card method type '2'"))
    if mode_of_payment==1:
      coin.for_cal()
      coin.input_coin_cal()
      if bill>coin.input_coin_cal():
        print("you haven't given sufficient amount of coins refresh the payment mode and try again ")
      if bill<coin.input_coin_cal():
        change=coin.input_coin_cal()-bill
        print(f"here is your change amount:{round(change,2)}$, thanks for paying")
    if mode_of_payment==2:
      print("thanks for paying the bill ")
