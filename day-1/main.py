def read_file(input_path):
    with open(input_path) as f:
        data = f.readlines()
    return data

def rotations(inputs, start_point=50):
    point = start_point
    counter = 0
    for move in inputs:
        if move[0] == "L":
            point = point - int(move[1:])
        else:
            point = point + int(move[1:])
        point = point % 100
        # print(point)

        if point == 0:
            counter += 1
    
    print("password is", counter)

def main():
    input_path = "input.txt"
    inputs = read_file(input_path)
    rotations(inputs)
    
if __name__ == '__main__':
    main()
