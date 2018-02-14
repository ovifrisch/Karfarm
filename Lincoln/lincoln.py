import pdfquery
from pdfquery.cache import FileCache


def add_all_options_of_one_trim_to_file(range_begin, range_end):
    decrement = 9.1
    options_deviation = 9
    for x in range(range_begin, range_end):
        print(x)
        pdf = pdfquery.PDFQuery('windowsticker (%d).pdf' % x, parse_tree_cacher=FileCache("/tmp/"))
        pdf.load()
        equipment_group_label = pdf.pq('LTTextLineHorizontal:contains("EQUIPMENT GROUP")')
        options_label = pdf.pq('LTTextLineHorizontal:contains("OPTIONAL EQUIPMENT")')
        bottom_corner_equip_group = float(equipment_group_label.attr('y0'))
        left_corner = float(options_label.attr('x0'))
        bottom_corner_options = float(options_label.attr('y0'))
        position1 = 0
        while True:
            options = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner,
                    bottom_corner_options - options_deviation - position1,left_corner + 300,
                    bottom_corner_options - position1)).text()
            #only reads 6
            if options == "":
                break
            options_file.write(options + '\n')
            position1 += decrement
        equipment = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner,
        bottom_corner_equip_group,left_corner + 300, bottom_corner_equip_group + 9)).text()
        options_file.write(equipment + '\n')
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

trim_name_list = ["MKC Select", "MKS Sedan", "MKS Sedan Ecoboost", "MKT Wagon Ecoboost",
                  "MKX Select", "MKX Reserve", "Navigator L Reserve", "Navigator Reserve",
                  "Navigator L Select", "Navigator Select"]
num_pdfs_per_trim = [16, 6, 2, 18, 18, 16, 2, 11, 10, 13]
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