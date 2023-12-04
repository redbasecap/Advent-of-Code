with open('input_small.in', 'r') as f:
    parts = f.read()[:-1].split('\n\n')
    drawings = parts[0].split('\n')
    print(drawings)
    stacks = [[] for _ in range(len(drawings[0])/2)]
    print(stacks)









