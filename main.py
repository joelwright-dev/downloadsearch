import mysql.connector
from bs4 import BeautifulSoup
import requests
import lxml
import random

blacklist = open("C:/Users/Owner/Desktop/downloaderprogram/python/block.txt", "r")
blockedsites = blacklist.read().split('\n')

useragentlist = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

useragent = random.choice(useragentlist)

headers = {
    'User-Agent': useragent
}

running = True

while running:
    query = str(input("Search term: "))
    returncount = input("Desired result count: ")
    if returncount.isnumeric():
        returncount = int(returncount)
        if returncount<=10:
            if query == "exit":
                running = False
            else:
                url = f'https://www.google.com/search?q={query}'
                for site in blockedsites:
                    url = url + f" -site:{site}"
                response = requests.get(url, headers=headers).text

                soup = BeautifulSoup(response, 'lxml')

                descs = []

                c=0

                for snip in soup.find_all('div', class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc'):
                    descs.append(snip.getText())

                print("Here is everything that your query returned:")
                print(" ")

                count = 0

                for item in soup.find_all('div', class_='tF2Cxc'):
                    if count<returncount:
                        if not item.table:
                            link = item.a['href']
                            title = item.h3.getText().encode('ascii','ignore')
                            title = title.replace(b"  ", b" - ")
                            print("Title:", title.decode())
                            print("Link:", link)
                            print("Description:", descs[c])
                            print(" ")
                            c+=1
                            count+=1
        else:
            print("Desired result count must be smaller than or equal to 10!")
    else:
        print("Desired result count must be a number!")

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="download")
# if(mydb):
#     print("Successfully connected to the database")
# else:
#     print("Failed to connect to the database")
# mycursor = mydb.cursor()

# #mycursor.execute("insert into tbldownloads(name,description,websitelink,downloadlink) values('testname', 'testdesc', 'testweblink', 'testdownlink')")
# mycursor.execute("select * from tbldownloads")

# myresult = mycursor.fetchone()

# if(myresult):
#     for row in myresult:
#         print(row)
