import math
from timeit import default_timer

def is_close(chair, other_chair):
    """Computes the distance between two points (x1, y1) and (x2, y2) using the 
    formula (x1-x2)^2 + (y1-y2)^2 and returning the square root of this.""" 
    distance = (chair[0] - other_chair[0])**2 + (chair[1] - other_chair[1])**2
    distance = math.sqrt(distance)
    return distance <= 1.5

def has_close_seats(chair_list):
    """Given a list of chairs with their positions [x, y], returns True if there 
    is a pair of close chairs, and False otherwise."""
    for i in range(len(chair_list)):
        for j in range(i+1, len(chair_list)):
            if is_close(chair_list[i], chair_list[j]):
                return True
    return False

chair_list1 = [[0, 0], [10, 0], [20, 0]] # no close pair, should return False 
print(has_close_seats(chair_list1))

chair_list2 = [[1, 1], [3, 2], [0, 1]] # has a close pair, should return True 
print(has_close_seats(chair_list2))

chair_list3 = []

for i in range(5000):
    chair_list3.append([0,i*5])

start = default_timer()
has_close_seats(chair_list3)
print(default_timer() - start)