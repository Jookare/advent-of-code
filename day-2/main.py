def read_file(input_path):
    with open(input_path) as f:
        data = f.readlines()
    return data

def silver(inputs):
    
    sum_invalid = 0
    for r in inputs:
        start = r.split("-")[0]
        end = r.split("-")[1]
        
        # Remove odd numbers
        if len(start) % 2:
            start = "1"+len(start)*"0"
        if len(end) % 2:
            end = "9"*(len(end)-1)
        # print(start, end)
        for value in range(int(start), int(end)+1):
            value = str(value)
            midpoint = len(str(value))//2
            flag = True
            for i in range(midpoint):
                if value[i] != value[midpoint+i]:
                    flag = False
                    break
            if flag:
                print(value)
                sum_invalid += int(value)

            
    print("\nSilver answer", sum_invalid)

def gold(inputs):
    print("\Gold answer", None)
            
    
def main():
    input_path = "input"
    inputs = read_file(input_path)[0]
    inputs = inputs.replace("\n", "")
    inputs = inputs.split(",")
    silver(inputs)
    gold(inputs)
    
if __name__ == '__main__':
    main()
