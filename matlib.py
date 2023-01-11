import matplotlib.pyplot as myGraph

n = int(input("Type the number of data you want to create a graph with - "))

x = list(map(int,input("Now type in every data for X axis: ").strip().split()))[:n]

y = list(map(int,input("Now type in every data for Y axis: ").strip().split()))[:n]

myGraph.plot(x, y)

myGraph.title(input("Add title for the graph - "))

myGraph.xlabel(input("Add name for X axis - "))
myGraph.ylabel(input("Add name for Y axis - "))
myGraph.savefig("images/graph.png")

print("Graph got saved at images/graph.png")