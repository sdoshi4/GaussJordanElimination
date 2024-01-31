# Shaan Doshi 1/30/24

# This is a Python implementation of Gauss-Jordan Elimination. 
# In my math class (UIUC's Math 416: Abstract Linear Algebra, taught my Professor Dunfield), 
# we went over the 6 steps of Gauss Jordan elimination (notes attached),
# and proved using induction that it always outputs a row-equivalent matrix to the input that is in RREF.
# I thought this was really cool, and decided to implement this using vanilla python to work for matrices stored in 2D arrays.

# Our three row operations - Scalar Mutiplication, Swapping Rows, and Adding a Row to Another
def scalarMult(row, scalar):
    return [scalar * i for i in row]

def rowSwap(inp, a, b):
    tmp = inp[a]
    inp[a] = inp[b]
    inp[b] = tmp
    return inp

def rowAdd(inp, row1_ind, row2): # we change the first row passed in, which is why we need it's index in inp
    inp[row1_ind] = [inp[row1_ind][i] + row2[i] for i in range(len(row2))]
    return inp

# checks if all the entries in a specified column below a certain row are zero
def isColZero(inp, row_ind, col_ind):
    if col_ind >= len(inp[0]): # edge case of the column being out of bounds
        return True
    for i in range(row_ind + 1, len(inp)):
        if (inp[i][col_ind] != 0):
            return False
    return True
        
# Sample Inputs (From my Homework)
inp = [[2, 1, 0],
       [1, 1, 1],
       [3, 4, 5],
       [3, 5, 7]]

inp2 = [[0, 4, 6, 8],
       [2, 0, -2, 4],
       [-3, 0, 3, 5]]

inp3 = [[1, 2, -1, 1],
        [1, 1, 2, 0],
        [5, 8, 1, 1]]

inp4 = [[2, 4, 5, 7, 18],
        [1, 2, 1, -1, 3],
        [4, 8, 7, 5, 24]]

def gaussJordan(inp):
    print(inp)
    # Step 0 (I set them to negative one because we are working with indices starting at 0, as opposed to 1 like in math)
    r = -1
    j = -1
    while (j < len(inp[0])):
        j+= 1  # Step 1 encompasses the while loop and this increment 
        colIsZero = isColZero(inp, r, j) 
        if (not colIsZero): # Step 2 encompasses this if statement and the above call to isColZero
            # Step 3 is this increment and the row swap if necessary
            r+= 1 
            if (inp[r][j] == 0): # ensure inp[i][j] is not zero by swapping rows
                for i in range(r+1, len(inp)):
                    if (inp[i][j] != 0):
                        print(f"Swap row {r} with {i}")
                        inp = rowSwap(inp, r, i)
                        print(inp)
            # Step 4 is this scalar multiplaction to create a leading 1 in the column
            print(f"Scalar multiply row {r} by {1.0/inp[r][j]}")
            inp[r] = scalarMult(inp[r], 1.0/inp[r][j])
            print(inp)
            # Step 5 is the below loop to make zeroes in the column
            for i in range(len(inp)):
                if (i != r):
                    print(f"Add {-inp[i][j]} * row {r} to row {i}")
                    inp = rowAdd(inp, i, scalarMult(inp[r], -inp[i][j]))
                    print(inp)
        # Step 6 is going to the next iteration of the loop
    return inp

gaussJordan(inp)