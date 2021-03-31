def probability_of_collision(car_1, car_2):
    # car_1 and car_2 will each be strings whose value will either be 
    # "L" for left, "S" for straight, or "R" for right.
    probability = 0.0 # you should change this value based on the directions.
    
    #indices initialize
    i = 0
    j = 0
    
    #probabilities data
    data = [[0]*3 for i in range (3)]
    data[0][0] = 0.5
    data[1][0] = 0.25
    data[2][0] = 0.1
    data[0][1] = 0.25
    data[1][1] = 0.02
    data[2][1] = 0.1
    data[0][2] = 0.1
    data[1][2] = 0.1
    data[2][2] = 0.01
    
    if car_1 == "L":
        # your code here for when car 1 turns left
       i = 0
    elif car_1 == "S":
        # your code here for when car 1 goes straight
        i = 1
    else:
        # your code here for when car 1 turns right
        i = 2
    
    if car_2 == "L":
        # your code here for when car 1 turns left
       j = 0
    elif car_2 == "S":
        # your code here for when car 1 goes straight
        j = 1
    else:
        # your code here for when car 1 turns right
        j = 2    
    
    probability = data[i][j]
    
    return probability


# This function is used to test the correctness of your code. You shouldn't
# touch any of the code below here (but feel free to look through it to
# understand what "correct" looks like).
def test():
    num_correct = 0
    
    p1 = probability_of_collision("L", "L")
    if p1 == 0.5:
        num_correct += 1
    
    p2 = probability_of_collision("L", "R")
    if p2 == 0.1:
        num_correct += 1
    
    p3 = probability_of_collision("L", "S")
    if p3 == 0.25:
        num_correct += 1
    
    p4 = probability_of_collision("S", "R")
    if p4 == 0.1:
        num_correct += 1
    
    print("You got", num_correct, "out of 4 correct")
    
test()
