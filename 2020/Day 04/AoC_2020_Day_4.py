            

# %%
    part1 = 0
    part2 = 0

    forms = [s.rstrip().split('\n') for s in open('input.txt','r').read().strip().split('\n\n')]

    for f in forms:
        part1 += len(set(''.join(f)))

        print(f)
        first = set(f[0]) 
        
        for i in range(1,len(f)):
            
            for letter in first.copy():
                if letter not in f[i]:
                    first.remove(letter)

        part2 += len(first)   

    print(part1)
    print(part2)
#with open('input.txt','r') as input:


# count_dict[]
# if key not in d:
#     d[key] = value

# print(splited_input)
   
    
#print("AOC Tag 2 Lösung 1:", solution1(slopeline_list))
#print("AOC Tag 2 Lösung 2:", solution2(pws_list))
         

# %%
