N = int(input())

s_1 = []
s_2 = []
cnt = 0
dict = {}

for itr in range(N):
    ptr = str(input())
    for item in ptr.split():
        if cnt == 0:
            s_1.append(item)
        if cnt == 1:
            s_2.append(item)
        cnt += 1
    cnt = 0

for itr in range(N):
    dict[s_1[itr]] = s_2[itr]

word = str(input())

print(dict[word])