#%%

def solution1(line_list):
    count_trees = 0
    position_x = 0
    position_y = 0

    for i in range(0,len(line_list)):
        print(line_list[i])

        if position_x >= len(line_list[i]):
            position_x  -= len(line_list[i])
            continue
        if line_list[i][position_x] == '#':
            count_trees += 1
            continue
        print(position_x)
        position_x += 1
        position_y += 1

    return count_trees
   
slopeline_list = []
   
with open('input.txt','r') as input:
    for line in input:
        splited_input = line.strip().split('\n')
        slopeline_list.append(splited_input)
        
    
print("AOC Tag 2 Lösung 1:", solution1(slopeline_list))
#print("AOC Tag 2 Lösung 2:", solution2(pws_list))
         
            

# %%
