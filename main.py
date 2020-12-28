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
    for element in range(0, len(list_to_search)):
        if list_to_search[element] == item:
            return True
    return False


def contains_integers(array_with_numbers):
    if sum(array_with_numbers) == 10:
        return True
    else:
        return False


def check_column(vector_puzzle, j):
    # if the number is invalid, throw an error message
    if j < 0 or j >= 4:
        return 'Invalid number. Choose a number 1 and 3'
    else:
        temp = list()
        # create an empty vector store all integers of that temp vector
        found = list()
        for i in range(len(vector_puzzle)):
            temp.append(vector_puzzle[i][j])

        for k in temp:
            if linear_search(temp, k):
                found.append(k)

        if contains_integers(found):
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
        # declare the rows
        rows_upper = vector_as_puzzle[0]
        rows_lower = vector_as_puzzle[1]

        # declare the list
        temp = zeros([4, 4], int)

        # declare the columns
        temp[0] = rows_upper[0]
        temp[1] = rows_upper[1]
        temp[2] = rows_lower[0]
        temp[3] = rows_lower[1]
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
        else:
            return False


def make_blanks(vector_to_make_blank, n):
    if isinstance(vector_to_make_blank, list):
        if n > len(vector_to_make_blank) or n < 0:
            return "Please enter a valid number, which is either smaller than " \
                   "the length of the vector or bigger than zero."
        for item in range(n):
            # generate number between 1 and 3
            random_number_row = random.randint(0, 3)
            random_number_col = random.randint(0, 3)

            # replace the selected row and column with None
            vector_to_make_blank[random_number_row][random_number_col] = None
            return vector_to_make_blank
    else:
        return 'This vector is not a proper array.'


def print_array(vector):
    if isinstance(vector, list):
        for i in range(len(vector)):
            for j in range(len(vector[i])):
                print(vector[i][j], end=' ')
            print()
    else:
        print('This vector is not a valid puzzle.')


# switch rows
def switch_rows(puzzle_arr_row, i, j):
    temp_row = puzzle_arr_row[i]
    puzzle_arr_row[i] = puzzle_arr_row[j]
    puzzle_arr_row[j] = temp_row
    return puzzle_arr_row


def make_solution_with_changing_rows(vector_row):
    # swap rows
    for i in range(10):
        vector_row = switch_rows(vector_row, random.randint(0, 3), random.randint(0, 3))

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
        else:
            return False


# tests
valid_output = [1, 2, 3, 4]
solution = make_solution(valid_output)
blank_vector = make_blanks(solution, 1)
print_array(blank_vector)

print()
print('**********')
print()

valid_output_two = [2, 3, 4, 1]
solution = make_solution(valid_output_two)
blank_vector = make_blanks(solution, 2)
print_array(blank_vector)

print()
print('**********')
print()

valid_output_three = [3, 4, 1, 2]
solution = make_solution(valid_output_three)
blank_vector = make_blanks(solution, 3)
print_array(blank_vector)

print()
print('**********')
print()

valid_output_four = [4, 1, 2, 3]
solution = make_solution(valid_output_four)
blank_vector = make_blanks(solution, 2)
print_array(blank_vector)

print()
print('**********')
print()

invalid_output = [4, 4, 4, 3]
solution = make_solution(invalid_output)
blank_vector = make_blanks(solution, 1)
print_array(blank_vector)

print()
print('**********')
print()

invalid_output_two = [1, 1, 1, 3]
solution = make_solution(invalid_output_two)
blank_vector = make_blanks(solution, 1)
print_array(blank_vector)

print()
print('**********')
print()

last_output = [1, 2, 3, 4]
solution = make_solution_with_changing_rows(last_output)
blank_vector = make_blanks(solution, 1)
print_array(blank_vector)

print()
print('******** AND DONE **********')
print()
