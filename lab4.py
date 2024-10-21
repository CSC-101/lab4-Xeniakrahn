from operator import truediv
import math
import data


# Write your functions for each part in the space below.

# Part 1
def first_element(list:list[list[int]])->list:
    return [x[0] for x in list]


# Part 2
def x_coordinates(list: [data.Point]) ->float:
    return [list[0]]


# Part 3
def are_in_positive_quadrant(list: [data.Point]) -> bool:
    if list[0]>0 and list[1]>0:
        print (list, "is in the first quadrant")
        return (list, "is in the first quadrant")
    else:
        print (list, "is not in the first quadrant")
        return(list, "is not in the first quadrant")
# Part 4
def distance(list:list[list[data.Point]])->float:
    z=((([0,0]-[1,0])**2)+(([0,1] - [1,1])**2))
    g= math.sqrt(z)
    return(g)
# Part 5


# Part 6


