import matplotlib.pyplot as myGraph

x = []
y = []

n = int(input("Type the number of data you want to create a graph with - "))
n2 = n

print("Now type in every data for X axis: ")
for i in range(0, n):
    ele = int(input())
    
    x.append(ele)

print("Now type in every data for Y axis: ")
for i in range(0, n2):
    ele = int(input())
    
    y.append(ele)


myGraph.plot(x, y)

myGraph.title(input("Add title for the graph - "))

myGraph.xlabel(input("Add name for X axis - "))
myGraph.ylabel(input("Add name for Y axis - "))
myGraph.savefig("images/graph.png")

print("Graph got saved at images/graph.png")