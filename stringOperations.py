txt = str(input("Put here any text and see the results!"))
word = str(input("Put here any word to see operations on the text!"))

class stringPunch:
  def __init__(self, text, word):
    self.text = text
    self.word = word

  #is looking for the word inside of the text
  def checkTheWord(self):
    if self.word in self.text:
      print("The word is inside the text")
    else:
      print("The word is not inside the text")

ppSmall = stringPunch(txt, word)

ppSmall.checkTheWord()