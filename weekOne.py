class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __contain__(self, checkName):
      if checkName in self.__myTeam:
          print("Yes, {} does exist.".format(checkName))
      else:
          print("Nope, {} does not exist.".format(checkName))
          
  def __iter__(self):
      for member in self.__myTeam:
          print(member)

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print (len(classmates))
  
  classmates.__contain__('Tim')
  
  classmates.__contain__('Sam')
  
  classmates.__iter__()

main()