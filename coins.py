class Coin:
  def __init__(self):
    self.dime=0.10
    self.quarter=0.25
    self.nickel=0.50
    self.penny=0.75
    self.total_value=0
    
  def for_cal(self):
    self.type1=int(input("no. of dimes  "))*self.dime
    self.type2=int(input("how many quarters  "))*self.quarter
    self.type3=int(input("how many nickel  "))*self.nickel
    self.type4=int(input("how many penny  "))*self.penny
  
  def input_coin_cal(self):
    return(self.type1+self.type2+self.type3+self.type4)
    