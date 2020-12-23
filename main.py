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


# test
output = [2, 4, 1, 3]
puzzle = make_vector(output)
permuted = permute_vector(output, 1)

permuted_row = permute_rows(puzzle, 2, 3, 1)
check = check_column(puzzle, 4)
check_columns = check_col(puzzle)


