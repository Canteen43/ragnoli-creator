# python 3

def print_rangoli(size: int) -> None:

    # Protect against impossible sizes
    if size < 1 or size > 26:
        print("Size has to be between 1 and 26!")
        return

    # Alphabet-String that the program can use to look up what letter to print
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Calculating the length of the edges. X is horizontal. It is longer because of the hypens
    x_length = size * 4 - 3
    y_length = size * 2 - 1

    # Calculating the position of the center 'a'
    center = {'x': 2 * size - 2, 'y': size - 1}

    # Setting up a coordinates-dictionary that keeps track of the current position
    coordinates = {'x': 0, 'y': 0}

    # for-logic that goes row by row and inside of that character by character
    for row in range(y_length):
        for character in range(x_length):

            # Calculating the distance between the current position and the position of center 'a'. X has to be halved because of inbetween hyphens
            distance = abs(coordinates['x'] - center['x']) / \
                2 + abs(coordinates['y'] - center['y'])

            # only whole numbers are allowed to get letters since half numbers correspond to dashes. Distance has to be within size
            if distance % 1 == 0 and distance < size:
                print(alphabet[int(distance)], end="")
            else:
                print("-", end="")

            # logic to keep updating coordinates during iteration
            coordinates['x'] += 1
        coordinates['x'] = 0
        coordinates['y'] += 1
        print("")


if __name__ == '__main__':
    n = input("Enter the size of the rangoli: ")
    if n.isdigit():
        print_rangoli(int(n))
    else:
        print("We need a valid integer!")
