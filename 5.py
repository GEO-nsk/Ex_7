N = int(input())


temp_s = []
s = []
s_parent = []
s_child = []
dict ={}
cnt = 0
count = 0

for itr in range(N):
    ptr = str(input())
    for item in ptr.split():
        temp_s.append(item)
    s.append(temp_s)
    temp_s = []

fist_name = s[0][0]
for itr in range(N):
    if s[itr][0] == fist_name:
        temp_s.append(s[itr][1])
    else:
        dict[s[itr-1][0]] = temp_s
        temp_s = []
        temp_s.append(s[itr][1])
        fist_name = s[itr][0]
dict[fist_name] = temp_s
name = str(input())
name1 = name

def num_child(dict,name,name1):
    count = 0
    if name == name1 and name not in dict.keys():
        return 0
    else:
        for item in dict[name]:
            new_name = item
            if item not in dict.keys():
                #print(item)
                count += 1
            else:
                #print(item)
                count += 1
                count += num_child(dict,new_name,name1)
        return count



print(num_child(dict,name,name1))

