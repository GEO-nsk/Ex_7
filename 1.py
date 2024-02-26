ptr = str(input())

unique_words = []
dict = {}
new_dict = {}
cnt = 0

for item in ptr.split():
    if item not in unique_words:
        unique_words.append(item)

for item in unique_words:
    for itr in ptr.split():
        if item == itr:
            cnt += 1
    dict[item] = cnt
    cnt = 0

sort_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

for itr in range(len(sort_dict)):
    new_dict[sort_dict[itr][0]] = sort_dict[itr][1]

for item in new_dict.keys():
    print(item)