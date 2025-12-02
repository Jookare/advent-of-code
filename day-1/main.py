def read_file(input_path):
    with open(input_path) as f:
        data = f.readlines()
    return data

def silver(inputs, start_point=50):
    point = start_point
    counter = 0
    for move in inputs:
        side = move[0]
        rot = int(move[1:])
        
        if side == "L":
            end_raw = point - rot
        else:
            end_raw = point + rot

        point = end_raw % 100
        if point == 0:
            counter += 1
            
    print("\nSilver answer", counter)

def gold(inputs, start_point=50):
    point = start_point
    counter = 0
    for move in inputs:
        side = move[0]
        rot = int(move[1:])
        
        if side == "L":
            end_raw = point - rot
            if point == 0:
                counter += rot // 100
            else:
                counter += (100 - end_raw) // 100
        else:
            # Counter = (sp + rot) // 100
            end_raw = point + rot
            if point == 0:
                counter += rot // 100
            else:
                counter += end_raw // 100

        point = end_raw % 100
            
    print("\nGold answer", counter)
    
def main():
    input_path = "input"
    inputs = read_file(input_path)
    silver(inputs)
    gold(inputs)
    
if __name__ == '__main__':
    main()
