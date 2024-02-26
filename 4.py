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
        if cnt > 0:
            s_2.append(item)
        cnt += 1
    cnt = 0
    dict[s_1[0]] = s_2
    s_1 = []
    s_2 = []

word = str(input())

for k, v in dict.items():
    if word in v:
        print(k)