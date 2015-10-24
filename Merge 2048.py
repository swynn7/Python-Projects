"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    # make local list the same length as parameter list 
    new_line = [0]*len(line)
    # run through parameter list, if not 0 insert into local list, 
    # starting from first 0 encountered 
    for num in line:
        if num != 0 :
            new_line[new_line.index(0)] = num
    for num in range(len(new_line)):
        # if index is greater than 0 and the value is not 0
        if num > 0:
            #print new_line[num]
            # compare current value with the one before it, 
            # if they are the same, double the current value and eliminate the one before it,
            # append a new 0 to the list
            if new_line[num] == new_line[num-1]:
                new_line[num-1] = new_line[num]*2
                new_line.pop(num)
                new_line.append(0)

    return new_line

print merge([4, 8, 4, 4, 8])