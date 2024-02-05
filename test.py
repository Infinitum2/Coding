## test.py file ##############
def LetterColor():
  while True:  
    colorLetters = ["r","y","g","b","p"]
    print("RAINBOW-IZER Thingy")
    print("")
    myString = input("Put in any sentence.")
    print(myString)
    for letter in myString:
    
      if letter.lower() == colorLetters[0]:
        print("\033[0;31m", end='') #red
      elif letter.lower() == colorLetters[1]:
        print("\033[1;33m", end='') #yellow
      elif letter.lower() == colorLetters[2]:
        print("\033[0;32m", end='') #green
      elif letter.lower() == colorLetters[3]:
        print("\033[0;34m", end='') #blue
      elif letter.lower() == colorLetters[4]:
        print("\033[0;35m", end='') #purple
      print(letter, end="")
      print('\033[0m', end='') #back to default