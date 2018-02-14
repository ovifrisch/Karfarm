sf_file = open("sf_ops.txt", 'r')
kf_file = open("karfarm_ops.txt", 'r')
sf_dic = {}
kf_dic = {}

for line in sf_file:
    line = line.lower()
    for i, char in enumerate(line):
        if char == "\t" or char == " ":
            sf_dic[line[i+1:i+4]] = line[i+5:len(line) - 1]
            break
print(sf_dic)

for line in kf_file:
    line = line.lower()
    for i, char in enumerate(line):
        if line[i] == 'c' and line[i+1] == 'o' and line[i+2] == 'd' and line[i+3] == 'e':
            kf_dic[line[i+5:i+8]] = line[0:i-2]
            break
print(kf_dic)
for sf_key in sf_dic:
    all_good = False
    for kf_key in kf_dic:
        if sf_key == kf_key and sf_dic[sf_key] == kf_dic[kf_key]:
            print(sf_dic[sf_key] + " +++++++++")
            all_good = True
            break
    if all_good == False:
        print(sf_dic[sf_key] + " -------")