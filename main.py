from queue import Queue


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
    if j < 0 or j >= 4:
        return 'Invalid number. Choose a number 1 and 3'
    else:
        temp = list()
        found = 0
        for element in range(len(vector_puzzle)):
            temp.append(vector_puzzle[j])

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
    temp_vector = list()

    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            # create the sub grid rows
            sub_grid_row_top = vector_as_puzzle[i]
            sub_grid_row_bottom = vector_as_puzzle[j]

            # create the sub grid columns
            temp_vector.append(sub_grid_row_top[i + 1])
            temp_vector.append(sub_grid_row_bottom[j + 1])
            temp_vector.append(sub_grid_row_bottom[i + 1])
            temp_vector.append(sub_grid_row_bottom[j + 1])

            # create the columns
            vector_as_puzzle.append(temp_vector[0])
            vector_as_puzzle.append(temp_vector[1])
            vector_as_puzzle.append(temp_vector[2])
            vector_as_puzzle.append(temp_vector[3])

    return vector_as_puzzle


def make_solution(vector_row):
    puzzle_input = make_vector(vector_row)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                permuted_puzzle = permute_rows(puzzle_input, x, y, z)
                columns = create_col_from_grids(permuted_puzzle)
                if check_col(columns):
                    return True
    return False


# test

output = [2, 4, 1, 3]
puzzle = make_vector(output)
permuted = permute_vector(output, 1)

permuted_row = permute_rows(puzzle, 2, 3, 1)
check = check_column(puzzle, 4)
check_columns = check_col(puzzle)

cols_from_grids = create_col_from_grids(puzzle)
solution = make_solution(permuted_row)

print(solution)
