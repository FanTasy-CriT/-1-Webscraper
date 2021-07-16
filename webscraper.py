import requests
from bs4 import BeautifulSoup
import csv
page = requests.get('https://www.sbsinformatique.com/pcs-gamers-tunisie/').text
soup = BeautifulSoup(page,'lxml')
sbs_file = open('Sbs.csv','w+')
csv_writer= csv.writer(sbs_file)
csv_writer.writerow(['PC Title','Description','price'])
for article in soup.find_all('article'):
    article_name = article.h4.a.text
    article_price = article.find('span',class_='price').text
    apm=str(article_price[0:article_price.find(",")])
    apm = int(apm[:1]+apm[2:])
    link = article.find('div',class_='img_block').a['href']
    page = requests.get(link).text
    soup = BeautifulSoup(page,'lxml')
    description = soup.find('div',class_='product-desc').text
    csv_writer.writerow([article_name,description,article_price])
page = requests.get('https://www.sbsinformatique.com/pcs-gamers-tunisie/?page=2').text
soup = BeautifulSoup(page,'lxml')
for article in soup.find_all('article'):
    article_name = article.h4.a.text
    article_price = article.find('span',class_='price').text
    apm=str(article_price[0:article_price.find(",")])
    apm = int(apm[:1]+apm[2:])
    #take out summer vibes articles or replace them by something else
    link = article.find('div',class_='img_block').a['href']
    page = requests.get(link).text
    soup = BeautifulSoup(page,'lxml')
    description = soup.find('div',class_='product-desc').text
    csv_writer.writerow([article_name,description,article_price])