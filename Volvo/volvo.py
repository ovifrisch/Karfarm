from bs4 import BeautifulSoup
import requests


def clean_string(str):
    previous_position = 0
    list_of_options = []
    actual_list_of_options = []
    for i, char in enumerate(str):
        if char == ":" or char == ",":
            current_position = i
            list_of_options.append(str[previous_position:current_position])
            previous_position = i + 2
    for option in list_of_options:
        if option[0].isupper() and option[1].isupper() and option[2].isupper():
            actual_list_of_options.append(option)
    return actual_list_of_options


def find_popular_options(list, n):
    dict = {}
    newdict = {}
    for list_item in list:
        dict[list_item] = 0
    for list_item in list:
        dict[list_item] += 1
    for key in dict:
        if dict[key] >= float(n/2):
            newdict[key] = dict[key]
    for key in newdict:
        popular_file.write(key + "\n")

sample_size = 1
url = "http://www.volvosandiego.com/new-2016-volvo-s60-4dr-sdn-t6-drive-e-fwd-san-diego-ca?_gmod[]=Dfe_Modules_VehiclePrice_Module&direction=asc&t=n&year[]=2016&make[]=Volvo&model[]=XC90&trim[]=AWD%204dr%20T6%20Inscription&sf=sf_model,sf_trim"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
options_file = open("all_options.txt", 'w')
all_options = []
for link in soup.find_all(attrs={'class': 'v-image'}):
    new_url = "http://www.volvosandiego.com" + link.get("href")
    r2 = requests.get(new_url)
    new_soup = BeautifulSoup(r2.content, "lxml")
    options_string = new_soup.find(attrs= {"class": "comment-text-inner"}).contents[5]
    for op in clean_string(options_string):
        all_options.append(op)
print(all_options)
popular_file = open("popular_options.txt", 'w')
find_popular_options(all_options, sample_size)
popular_file.close()





