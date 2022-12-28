#Tuples example
def neighboursOfPoland():
  polishNeighbours = ("Germany", "Czechia", "Slovakia", "Ukraine", "Belarus", "Russia", "Lithuania")
  allTexts = ("Type one of the following words - amount, biggest, smallest, wealthiest...", "nope")

  print(allTexts[0])
  x = input()

  match x:
    case "amount":
      print("There is " + str(len(polishNeighbours)) + " neighbours of Poland... and that is my lucky number!")
    case "biggest":
      print("The biggest neighbour of Poland is " + polishNeighbours[5] + "... Unfortunately.")
    case "smallest":
      print("Smallest neighbouring country of Poland is " + polishNeighbours[2] + " or " + polishNeighbours[6] + " but idk because I am bad at math and too lazy to check on Google lol.")
    case "wealthiest":
      print("The wealthiest neighbouring country of Poland is " + polishNeighbours[0] + " but I really think that it is propably from someone elses gold!")
    case _:
      print("Unknown Command!")

#Sets example
def randomOrderEuropeCountries():
  randCountries = {"Russia", "Germany", "Poland", "Netherlands", "Denmark", "Sweden", "United Kingdom"}
  print("Some of the european countries in random order:")
  print(randCountries)
  
  randCountries.add("Hungary")
  
  print("+1 more country in random place:")
  print(randCountries)

  randCountries.remove("Germany")
  
  print("Random countries without Germany:")
  print(randCountries)


#Dictionaries example
def germanyInfo():
  germany = {
  "Name": "Germany",
  "Size": "540,854 km²",
  "Year": 1939
  }

  print(germany)

  germany["Year"] = 2022
  germany["Size"] = "357,588 km²"

  print(germany)
    
def polandInfo():
  poland = {
  "Name": "Germany",
  "Size": "389,000 km²",
  "Year": 1939
  }

  print(poland)

  poland["Year"] = 2022
  poland["Size"] = "322,575 km²"

  print(poland)
    
neighboursOfPoland()
randomOrderEuropeCountries()
germanyInfo()
polandInfo()
