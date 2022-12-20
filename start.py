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
    
neighboursOfPoland()
