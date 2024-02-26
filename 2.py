N = int(input())

s_rus = []
s_eng = []
cnt = 0
dict = {}
new_ptr = ''

for itr in range(N):
    ptr = str(input())
    for item in ptr.split():
        if cnt == 0:
            s_rus.append(item)
        if cnt == 1:
            s_eng.append(item)
        cnt += 1
    cnt = 0

for itr in range(N):
    dict[s_rus[itr]] = s_eng[itr]

ptr = str(input())

for item in ptr.split():
    for key in dict.keys():
        if item == key:
            new_ptr += dict[key]
    if item not in dict:
        new_ptr += item
    new_ptr += ' '

print(new_ptr)