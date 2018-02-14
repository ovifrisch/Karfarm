from bs4 import BeautifulSoup
import requests

reviews_file = open("reviews.txt", 'w')
rating_dictionary = {}
url_1 = "http://www.dealerrater.com"
r1 = requests.get(url_1)
soup1 = BeautifulSoup(r1.content, 'lxml')
url_2 = soup1.find(attrs={"class": "quick-menu-tab pad-left-none"}).a.get('href')
r2 = requests.get(url_2)
soup2 = BeautifulSoup(r2.content, 'lxml')
for brand in soup2.find_all(attrs={"class": "col-xs-12 font-18 pad-none"}):
    brand_name = brand.a.string
    if brand_name == "Alfa Romeo" or brand_name == "Aston Martin" or brand_name == "Bentley" or brand_name == "CODA" or brand_name == "Daihatsu" or brand_name == "Ferrari" or brand_name == "Fisker" or brand_name == "Isuzu" or brand_name == "Lamborghini" or brand_name == "Maserati" or brand_name == "Maybach" or brand_name == "McLaren" or brand_name == "Mercury" or brand_name == "Opel" or brand_name =="Panoz" or brand_name == "Peugeot" or brand_name == "Pontiac" or brand_name == "Porsche" or brand_name == "Rolls Royce" or brand_name == "Saab" or brand_name == "Saturn" or brand_name == "SRT" or brand_name == "Suzuki" or brand_name == "Yamaha" or brand_name == "Leasing Company" or brand_name == "Recreational Vehicles" or brand_name == "Used Car Dealer":
        pass
    else:
        print(brand_name + '\n' + '\n')
        url_3 = url_1 + brand.a.get('href')
        r3 = requests.get(url_3)
        soup3 = BeautifulSoup(r3.content, 'lxml')
        for location in soup3.find_all(attrs={'class': 'col-md-12 font-18 pad-none tap-target'}):
            if location.a.string == "California":
                url_4 = url_1 + location.a.get('href')
                break
        r4 = requests.get(url_4)
        soup4 = BeautifulSoup(r4.content, 'lxml')
        active_page_list = []
        for active_page in soup4.find_all(attrs={'class': 'page_active page'}):
            active_page_list.append(int(active_page.a.string))
        if active_page_list == []:
            num_pages = 1
        else:
            num_pages = active_page_list[len(active_page_list) - 1]
        for page in range(1, num_pages+1):
            url_5 = url_4 + "?page=%d" % page
            r5 = requests.get(url_5)
            soup5 = BeautifulSoup(r5.content, 'lxml')
            for dealership in soup5.find_all(attrs={'class': 'col-xs-12 pad-none border-all margin-bottom-lg margin-top-md bottom-right-radius-30 search-result mobile-border-none'}):
                print(dealership.a.string + '\n')
                url_6 = url_1 + dealership.a.get('href')
                r6 = requests.get(url_6)
                soup6 = BeautifulSoup(r6.content, 'lxml')
                if soup6.find(attrs={'class': 'col-xs-12 text-center pad-md margin-top-md'}) is None:
                    pass
                else:
                    url_7 = url_1 + soup6.find(attrs={'class': 'col-xs-12 text-center pad-md margin-top-md'}).a.get('href')
                    r7 = requests.get(url_7)
                    soup7 = BeautifulSoup(r7.content, 'lxml')
                    for employee in soup7.find_all(attrs={'class': 'col-lg-3 col-md-3 col-sm-4 col-xs-6 margin-bottom-xl employee-tile'}):

                        reviews_list = []
                        url_8 = url_1 + employee.a.get('href')
                        r8 = requests.get(url_8)
                        soup8 = BeautifulSoup(r8.content, 'lxml')
                        employee_name = soup8.find(attrs={'class': 'no-format font-28 bolder margin-bottom-none line-height-1 hidden-xs'}).string
                        active_page_list_2 = []
                        for active_page_2 in soup8.find_all(attrs={'class': 'page_active page'}):
                            active_page_list_2.append(int(active_page_2.a.string))
                        if active_page_list_2 == []:
                            num_pages_2 = 1
                        else:
                            num_pages_2 = active_page_list_2[len(active_page_list_2) - 1]
                        for page2 in range(1, num_pages_2 + 1):
                            url_9 = url_8 + "page%d/" % page2
                            r9 = requests.get(url_9)
                            soup9 = BeautifulSoup(r9.content, 'lxml')
                            for assessment in soup9.find_all(attrs={'class': 'review-entry col-xs-12 text-left pad-none pad-top-lg  border-bottom-teal-lt'}):
                                date_written = assessment.p.string
                                year_written = date_written[len(date_written) - 4: len(date_written)]
                                if int(year_written) <= 2014:
                                    pass
                                else:
                                    rating = (assessment.div.div.div['class'])[1]
                                    rating_number = rating[len(rating) - 2: len(rating)] + '/50'
                                    comment = assessment.contents[5].p.string
                                    reviews_list.append(rating_number + ', ' + comment)
                        rating_dictionary[employee_name] = reviews_list
                        print(employee_name)
for key in rating_dictionary:
    reviews_file.write(key)
    for review in rating_dictionary[key]:
        reviews_file.write(review)