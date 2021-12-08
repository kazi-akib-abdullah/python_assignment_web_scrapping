from typing import Counter
from html.parser import HTMLParser
import urllib as urllib
import mysql.connector
import urllib.request as urllib2
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

mydict = {}
url = "https://www.vrbo.com/vacation-rentals/usa/north-carolina/blue-ridge-mountains/boone"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozila'})
with urllib.request.urlopen(req) as html:
    page = html.read()
    names = []



class MyHTMLParser(HTMLParser):

    def __init__(self, wanted_tag, wanted_attrs):
        super().__init__()
        self.wanted_tag = wanted_tag
        self.wanted_attrs = wanted_attrs
        self.flag = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == self.wanted_tag and all(attr in attrs for attr in self.wanted_attrs.items()):
            self.flag = True

    def handle_data(self, data):
        if self.flag == True:
            names.append(data)
            self.data.append(data)

    def handle_endtag(self, tag):
        if tag == self.wanted_tag:
            self.flag = False


# class ParseStartTag(HTMLParser):
#    def __init__(self, wanted_tag, wanted_attrs_key):
#       super().__init__()
#       self.wanted_tag = wanted_tag
#       self.wanted_attrs_key = wanted_attrs_key
#       #self.flag = False
#       self.data = []
#    def handle_starttag(self, tag, attrs):
#      if tag == self.wanted_tag:
#        for key, value in attrs:
#          if key == self.wanted_attrs_key:
#            image.append(value)
parser = MyHTMLParser('div', {'class': 'CommonRatioCard__description'})
parser.feed(str(page))


parser = MyHTMLParser(
    'a', {'class': 'SingleImageCarousel SingleImageCarousel--cover'})
parser.feed(str(page))


parser = MyHTMLParser('div', {'class': 'CommonRatioCard__subcaption'})
parser.feed(str(page))


parser = MyHTMLParser('span', {'class': 'CommonRatioCard__price'})
parser.feed(str(page))

title = names[:6]
facilities = names[6:12]
for i in range(len(facilities)):
    facilities[i] = facilities[i].split(" \\xc2\\xb7 ")
price = names[12:18]


image = []
class MyHTMLParser(HTMLParser):
    query = []
    result = {}
    def handle_starttag(self, tag, attrs):
        self.result['name'] = tag
        self.result['attr'] = attrs

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        tag = self.query[0]
        attr = self.query[1]
        text = self.query[-1]
        if not len(attr):
            try:
                if self.result['name'] == tag:
                    image.append(data)
            except:
                pass
        else:
            pass


parser = MyHTMLParser()
html_page = urllib2.urlopen(
    "https://www.vrbo.com/vacation-rentals/usa/north-carolina/blue-ridge-mountains/boone")
parser.query = ['script', (), 'text']
parser.feed(str(html_page.read()))

pic = ''

image_list_1 = []
image_list_2 = []
image_list_3 = []
for im in image:
    x = re.search("^window.__PRELOADED_STATE__", im)
    if x:
        pic = im
        x = ''

        li = re.findall(
            r'"tripleId":(.*?),"thumbnailUrl":(.*?),', im)
        for i in li[-6:]:
            image_list_1.append(i[1])

        li2 = re.findall(
            r'"tripleId":(.*?),"thumbnailUrl2":(.*?),', im)
        for i in li2[-6:]:
            image_list_2.append(i[1])

        li3 = re.findall(
            r'"tripleId":(.*?),"thumbnailUrl3":(.*?),', im)
        for i in li3[-6:]:
            image_list_3.append(i[1])


for i in range(len(title)):
    mydict[i] = [title[i], facilities[i], price[i],
                 image_list_1[i], image_list_2[i], image_list_3[i]]

# Create Table


# mycursor = mydb.cursor()
# create_table='''CREATE TABLE Villa(
#                     Name varchar(250) NOT NULL,
#                     Sleeps varchar(30),
#                     Bedroom varchar(30),
#                     Bathroom varchar(30),
#                     Price varchar(10),
#                     Image1 varchar(500),
#                     Image2 varchar(500),
#                     Image3 varchar(500),
#                     PRIMARY KEY (Name))
#                     '''
# mycursor.execute(create_table)


def insert_mysql(name, sleeps, bedroom, bathroom, price, img1, img2, img3):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='parsingData',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Villa (Name, Sleeps, Bedroom, Bathroom, Price, Image1, Image2, Image3) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        record = (name, sleeps, bedroom, bathroom, price, img1,  img2, img3)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Villa")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Database Insertion
for info in mydict.values():
    insert_mysql(info[0],
                 info[1][0],
                 info[1][1],
                 info[1][2],
                 info[2],
                 info[3],
                 info[4],
                 info[5]
                 )
