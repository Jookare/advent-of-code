def read_file(input_path):
    with open(input_path) as f:
        data = f.readlines()
    return data

def rotations(inputs, start_point=50):
    point = start_point
    counter = 0
    for move in inputs:
        rot = int(move[1:])
        sp = point
        if move[0] == "L":
            point = point - rot
            print("start", sp)
            if sp < rot and sp != 0:
                counter += abs(point // 100)
        else:
            point = point + rot
            if point > 100:
                counter += abs(point // 100)
        
        if point % 100 == 0:
            counter += 1
            print("zero point")
        
        point = point % 100
    
    print("password is", counter)

def main():
    input_path = "input.txt"
    inputs = read_file(input_path)
    rotations(inputs)
    
if __name__ == '__main__':
    main()
