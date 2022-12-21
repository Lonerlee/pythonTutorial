#Tuples example
class neighboursOfPoland():
  polishNeighbours = ("Germany", "Czechia", "Slovakia", "Ukraine", "Belarus", "Russia", "Lithuania")
  allTexts = ("Type one of the following words - amount, biggest, smallest, wealthiest...", "nope")

  print(allTexts[0])
  x = input()

  if x == "amount":
    print("There is " + str(len(polishNeighbours)) + " neighbours of Poland... and that is my lucky number!")
  elif x == "biggest":
    print("The biggest neighbour of Poland is " + polishNeighbours[5] + "... Unfortunately.")
  elif x == "smallest":
    print("Smallest neighbouring country of Poland is " + polishNeighbours[2] + " or " + polishNeighbours[6] + " but idk because I am bad at math and to lazy to check on Google lol.")
  elif x == "wealthiest":
    print("The wealthiest neighbouring country of Poland is " + polishNeighbours[0] + " but I really think that it is propably from someone elses gold!")
  else:
    print("Unknown Command!")

#Sets example
class randomOrderEuropeCountries():
  randCountries = {"Russia", "Germany", "Poland", "Netherlands", "Denmark", "Sweden", "United Kingdom"}
  print("Some of the european countries in random order:")
  print(randCountries)

#Dictionaries example
class germanyInfo():
  germany = {
  "Name": "Germany",
  "Size": "540,854 km²",
  "Year": 1939
  }

  print(germany)

  germany["Year"] = 2022
  germany["Size"] = "357,588 km²"

  print(germany)
    
neighboursOfPoland()
randomOrderEuropeCountries()
germanyInfo()
