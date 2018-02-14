sample_size = 15
def find_ops(list,n):
    dict = {}
    newdict = {}
    for list_item in list:
        dict[list_item] = 0
    for list_item in list:
        dict[list_item] += 1
    print(dict)
    for key in dict:
        if dict[key] >= float(n/3):
            newdict[key] = dict[key]
    for key in newdict:
        print(key)

file_name = "cars.txt"
file = open(file_name)
options_list = []
for line in file:
    options_list.append(line)
print(find_ops(options_list, sample_size))
file.close()









