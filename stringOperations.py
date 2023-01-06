txt = str(input("Put here any text and see the results! "))
word = str(input("Put here any word to see operations on the text! "))

class stringPunch:
  def __init__(self, text, word):
    self.text = text
    self.word = word

  #is looking for the word inside of the text
  def checkTheWord(self):
    if self.word.casefold() in self.text.casefold():
      print("The word [or set of characters] is inside the text, or at least as a part of a bigger one")
    else:
      print("The word [or set of characters] is not inside the text")

  #is showing the first 5 letters
  def showFirst5Letters(self):
    print("If they exist, the first 5 letters/characters of the text are - " + self.text[0:5])
    print("If they exist, the first 5 letters/characters of the word are - " + self.word[0:5])

  #gets word letters to upper case
  def wordUpperCase(self):
    print("Word in upper case looks like this - " + self.word.upper())

  #replaces word in string with @
  def replaceWord(self):
    print("Text with word replaced by @ looks like this(works only if letters are same size) - " + self.text.replace(word, "@"))
  


ppSmall = stringPunch(txt, word)

ppSmall.checkTheWord()
ppSmall.showFirst5Letters()
ppSmall.wordUpperCase()
ppSmall.replaceWord()