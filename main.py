import math
import random
from queue import Queue
from numpy import zeros


# function to create a new
# vector from a given input row
def make_vector(row):
    vector = list()
    for element in range(4):
        vector.append(row)
    return vector


# permute vector
def permute_vector(row, p):
    queue = Queue(maxsize=4)
    if p == 0 or p > 3:
        return row
    else:

        # place all vector rows into the empty
        # queue
        for element in row:
            queue.put(element)

        # get the head of the queue
        # put the head into the queue
        for item in range(p):
            head = queue.get()
            queue.put(head)

        # copying queue into row
        row = list(queue.queue)
        return row


def permute_rows(vector_input, x, y, z):
    # permute all the rows in the vector, save for the first
    vector_input[1] = permute_vector(vector_input[1], x)
    vector_input[2] = permute_vector(vector_input[2], y)
    vector_input[3] = permute_vector(vector_input[3], z)
    return vector_input


def linear_search(list_to_search, item):
    for element in range(len(list_to_search)):
        if element == item:
            return True

    return False


def check_column(vector_puzzle, j):
    # if the number is invalid, throw an error message
    if j < 0 or j >= 4:
        return 'Invalid number. Choose a number 1 and 3'
    else:
        temp = list()
        found = 0
        for i in range(4):
            temp.append(vector_puzzle[i][j])

        for item in range(4):
            if linear_search(temp, j):
                found += 1

        if found == 4:
            return True
        else:
            return False


def check_col(input_puzzle_vector):
    for element in range(len(input_puzzle_vector)):
        if check_column(input_puzzle_vector, element):
            return True
        else:
            return False


def create_col_from_grids(vector_as_puzzle):
    if (len(vector_as_puzzle)) >= 0 or vector_as_puzzle is not None:
        # create a temporary two dimensional vector of type int and length 4
        temp = zeros([4, 4], int)
        for i in range(4):
            row = math.floor(i / 2)
            temp[i] = vector_as_puzzle[i][row]
            for j in range(4):
                col = j % 2
                temp[j] = vector_as_puzzle[j][col]

        return temp
    return 'Please enter a valid vector'


def make_solution(vector_row):
    # make the vector
    puzzle_input = make_vector(vector_row)
    # cyclic permutations
    cyclic_permutation_x = [2, 1]
    cyclic_permutation_y = [1, 2]
    cyclic_permutation_z = [3, 3]
    for i in range(len(cyclic_permutation_x)):
        puzzle_input = permute_rows(puzzle_input,
                                    cyclic_permutation_x[i],
                                    cyclic_permutation_y[i],
                                    cyclic_permutation_z[i]
                                    )
        columns = create_col_from_grids(puzzle_input)
        if check_col(columns):
            return puzzle_input
        return False


def make_blanks(vector_to_make_blank, n):
    if n > len(vector_to_make_blank) or n < 0:
        return "Please enter a valid number, which is either smaller than " \
               "the length of the vector or bigger than zero."
    for item in range(n):
        # generate a number between 0 and 3
        random_number_row = random.randint(0, 3)
        random_number_col = random.randint(0, 3)

        # replace the selected row and column with None
        vector_to_make_blank[random_number_row][random_number_col] = None
    return vector_to_make_blank


def print_array(vector):
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            print(vector[i][j], end=' ')
        print()


# test
output = [2, 3, 4, 1]
solution = make_solution(output)
print_array(solution)

blank_vector = make_blanks(solution, 1)
print_array(blank_vector)
