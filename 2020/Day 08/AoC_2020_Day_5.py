            

# %%
    part1 = 0
    part2 = 0

    instructions = [s.strip().split(' ') for s in open('input.txt','r').read().strip().split('\n')]
    visited_inst = []
    accumulator = 0
    position = 0

    while True:
        type = instructions[position][0]
        value = int(instructions[position][1])
        #print(value)
        #print(instructions[position][1])
        #print(position)

        if position not in visited_inst: 
        
            if type == "nop":
                visited_inst.append(position)
                position += 1
                continue

            if type == "acc":
                accumulator += value
                visited_inst.append(position)
                position += 1
                continue

            if type == "jmp":
                visited_inst.append(position)
                position += value
                continue

        else: 

            print(position)
            print(visited_inst)
            break
        

print("AOC Tag 8 Lösung 1:", accumulator)
           

# %%
import copy

instructions_orig = [s.strip().split(' ') for s in open('input.txt','r').read().strip().split('\n')]

for i in range(len(instructions_orig)):
    visited_inst = []
    accumulator = 0
    position = 0
        
    #Copy the array with deepcopy
    instructions = copy.deepcopy(instructions_orig)
    
    if instructions[i][0] == "nop":
        #print(instructions[i][1])
        instructions[i][0] = "jmp"

    elif instructions[i][0] == "jmp":
        instructions[i][0] = "nop"

    while position not in visited_inst and position < len(instructions):
        type_inst = instructions[position][0]
        value = int(instructions[position][1])
        visited_inst.append(position)

        if type_inst == "nop":
            position += 1
          
        elif type_inst == "acc":
            accumulator += value
            position += 1
          
        elif type_inst == "jmp":
            position += value
        #print(visited_inst)
          
    if position == len(instructions):
        print("AOC Tag 8 Lösung 2:", accumulator)

        break


# %%
