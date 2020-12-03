#%%
def check_chars(txt):
    result = 0
    for letter in txt:
        result += 1    
    print("\'" + txt + "\'" + "," + str(result))

def solution1(pws_list):
    counter_valid = 0
    for i in range(0,len(pws_list)):
        act_dict = pws_list[i]
        if act_dict['password'].count(act_dict['letter']) >= act_dict['lower'] and act_dict['password'].count(act_dict['letter']) <= act_dict['upper']:
            counter_valid += 1
        i += 1
        
    return counter_valid

def solution2(pws_list):
    counter_valid = 0
    for i in range(0,len(pws_list)):
        act_dict = pws_list[i]
        if act_dict['password'][act_dict['lower']-1] == (act_dict['letter']) or act_dict['password'][act_dict['upper']-1] == (act_dict['letter']):
            print( act_dict['password'])
            print(act_dict['password'][act_dict['lower']-1])
            print(act_dict['lower']-1)
            print(act_dict['password'][act_dict['upper']-1])
            print(act_dict['upper']-1)
            counter_valid += 1
        i += 1
        
    return counter_valid
    
#%%
pws_list = []
   
with open('input.txt','r') as input:
    for line in input:
        splited_input = line.strip().split(':')
        policy = splited_input[0].strip()
        password = splited_input[1].strip()
        policy_num, policy_letter = policy.split(' ')
        policy_min, policy_max = policy_num.split('-')
        policy_min = int(policy_min.strip())
        policy_max = int(policy_max.strip())
        
        pws_list.append({
            'password': password,
            'letter': policy_letter,
            'lower':  policy_min,
            'upper': policy_max
            })
        
    
print("AOC Tag 2 Lösung 1:", solution1(pws_list))
print("AOC Tag 2 Lösung 2:", solution2(pws_list))
         
            
