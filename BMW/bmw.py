from bs4 import BeautifulSoup
import requests


def write_options_to_file(soup_object):
    progress = 0
    for link in soup_object.find_all(attrs={"class": "cblt-button  conversion"}):
        progress += 1
        print(progress)
        new_link = "http://www.bramanmotorsbmw.com/" + link.get('href')
        new_r = requests.get(new_link)
        new_soup = BeautifulSoup(new_r.content, "lxml")
        grand_parent = new_soup.find(attrs={"class": "cblt-panel no-chrome", "id": "optionsFolder"})
        parent = grand_parent.contents[1]
        for child in parent.children:
            options_file.write(child.string)
    options_file.close()


def find_popular_options(list, n):
    dict = {}
    newdict = {}
    for list_item in list:
        dict[list_item] = 0
    for list_item in list:
        dict[list_item] += 1
    for key in dict:
        if dict[key] >= float(n/3):
            newdict[key] = dict[key]
    for key in newdict:
        popular_file.write(key)


def create_list(file_to_read_from):
    options_list = []
    for line in file_to_read_from:
        options_list.append(line)
    return options_list


num_items = 25
site_name = "http://www.bramanmotorsbmw.com/VehicleSearchResults?search=new&make=BMW&model=328i&bodyType=ALL&trim=Sedan&series=&minYear=&maxYear=&minPrice=&maxPrice=&vehicleType="
r = requests.get(site_name)
soup = BeautifulSoup(r.content, "lxml")
options_file = open("BMW_options.txt", 'w')
write_options_to_file(soup)
popular_file = open("popular_options.txt", 'w')
options_file = open("BMW_options.txt", 'r')
find_popular_options(create_list(options_file), num_items)
popular_file.close()