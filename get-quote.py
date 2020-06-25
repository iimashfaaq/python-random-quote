import random

def printQuote():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd], end=" ")

def writeQuote():
  quote = input("Write your quote: :")
  f = open("quotes.txt", "a")
  f.writelines(quote)
  f.close()

if __name__== "__main__":
  writeQuote()
  printQuote()
