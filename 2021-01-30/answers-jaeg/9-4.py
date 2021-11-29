import math

#I create a list to store all close pairs in the chair list
close_pair = []

def is_close(chair, other_chair):
    """Computes the distance between two points (x1, y1) and (x2, y2) using the 
    formula (x1-x2)^2 + (y1-y2)^2 and returning the square root of this.""" 
    distance = (chair[0] - other_chair[0])**2 + (chair[1] - other_chair[1])**2
    distance = math.sqrt(distance)
    return distance <= 1.5

#I use the has_close_seats function from 9.1 to determine which seats are too close
def has_close_seats(chair_list):
    """Given a list of chairs with their positions [x, y], returns True if there 
    is a pair of close chairs, and False otherwise."""
    for i in range(len(chair_list)):
        for j in range(i+1, len(chair_list)):
            if is_close(chair_list[i], chair_list[j]):
                #i append the close chairs to the close_pair list to determine which chairs should be removed
                close_pair.append(chair_list[i])
                close_pair.append(chair_list[j])
                return True
    return False

def ensure_proximity(chair_list):
    #the function removes a chair (determined by my close_pair list) from chair_list as long as has_close_seats evaluates to True
    while has_close_seats(chair_list) == True:
        chair_list.remove(close_pair[0])


chair_list = [[1, 1], [3, 2], [0, 1]] # has a close pair, so something must be removed 
print(has_close_seats(chair_list))
print(close_pair)
print(ensure_proximity(chair_list))
print(has_close_seats(chair_list))
