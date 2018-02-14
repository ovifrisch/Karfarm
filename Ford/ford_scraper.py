import pdfquery
from pdfquery.cache import FileCache
# import os


def add_all_options_of_one_trim_to_file(range_begin, range_end):
    decrement = 9.35
    for x in range(range_begin, range_end):
        no_equipment_group = False
        pdf = pdfquery.PDFQuery('windowsticker (%d).pdf' % x, parse_tree_cacher=FileCache("/tmp/"))
        pdf.load()
        print(x)
        equipment_group_label = pdf.pq('LTTextLineHorizontal:contains("EQUIPMENT GROUP")')
        options_label = pdf.pq('LTTextLineHorizontal:contains("OPTIONAL EQUIPMENT")')
        if "EQUIPMENT GROUP" not in equipment_group_label:
            print("hi")
            no_equipment_group = True
        else:
            bottom_corner_equip_group = float(equipment_group_label.attr('y0'))
        bottom_corner_options = float(options_label.attr('y0'))
        left_corner = float(options_label.attr('x0'))
        position1 = 0
        position2 = 0
        while True:
            if position1 >= decrement*29:
                while True:
                    options = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (248.4, 447.64 - position2, 540, 460.8 - position2)).text()
                    if options == "":
                        break
                    options_file.write(options + '\n')
                    position2 += decrement
                break
            else:
                options = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner_options - 9 - position1, left_corner + 300, bottom_corner_options - position1)).text()
                if options == "":
                    break
                options_file.write(options + '\n')
                position1 += decrement
        if not no_equipment_group:
            equipment = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner_equip_group, left_corner + 300, bottom_corner_equip_group + 9)).text()
            options_file.write(equipment + '\n')
    # os.remove('windowsticker (%d).pdf' % x)
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


def find_start(trim_list, index):
    if index == 0:
        return 1
    else:
        sum = 0
        for x in range(0, index):
            sum += trim_list[x]
        return sum + 1


def find_stop(trim_list, index):
    if index == 0:
        return trim_list[0] + 1
    else:
        sum = 0
        for x in range(0, index + 1):
            sum += trim_list[x]
        return sum + 1


trim_name_list = ["Taurus SEL", "Taurus Lim", "Taurus SHO", "Shelby G350R", "Shelby G350 BASE",
                  "Wagon XLT LWB", "Wagon XL LWB", "Wagon Titanium LWB", "Cargo Van XL LWB",
                                                                         "Cargo Van XLT LWB"]
num_pdfs_per_trim = [20, 2, 3, 3, 20, 19, 4, 2, 20, 19]
popular_file = open("popular_options.txt", 'w')
for x in range(0, len(num_pdfs_per_trim)):
    options_file = open("cars.txt", 'w')
    number_of_files_to_read = num_pdfs_per_trim[x]
    add_all_options_of_one_trim_to_file(find_start(num_pdfs_per_trim, x), find_stop(num_pdfs_per_trim, x))
    options_file = open("cars.txt", 'r')
    popular_file.write('\n' + '\n' + trim_name_list[x] + '\n' + '\n')
    find_popular_options(create_list(options_file), number_of_files_to_read)
    options_file.close()
    if x == len(num_pdfs_per_trim) - 1:
        options_file = open("cars.txt", 'w')
popular_file.close()