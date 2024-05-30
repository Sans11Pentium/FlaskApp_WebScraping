import requests
from bs4 import BeautifulSoup as bsp
import json


response = requests.get('http://quotes.toscrape.com/')
print(response.status_code)
data = bsp(response.text,'html.parser')
base_url = 'http://quotes.toscrape.com/'
li=[]
while True:
  temp = data.find_all('div',{'class':'quote'})
  for ele in temp:
    auth = ele.find('small',{'class':'author'}).string
    if(auth == 'Albert Einstein'):
      li.append(ele.span.string)
  url=data.find('li',{'class':'next'})
  if url is None:
    break
  url = base_url + url.a['href']
  response = requests.get(url)
  data = bsp(response.text,'html.parser')
for i in li:
  print(i)




# 'https://quotes.toscrape.com/page/1/'
base_url = 'https://quotes.toscrape.com/'

curr_page_url = 'https://quotes.toscrape.com/page/1/'
all_url = [curr_page_url]
# response = requests.get(curr_page_url)

# data = bsp(response.text, 'html.parser')

# q = temp = data.find_all('div',{'class':'quote'})
# for quote in q:
#   print(quote.span.string)

li=[]
while True:
  # fetch quotes from current page
  response = requests.get(curr_page_url)
  data = bsp(response.text, 'html.parser')
  q = data.find_all('div',{'class':'quote'})
  for quote in q:
    li.append(quote.span.string)

  nxt = data.find('li',{'class':'next'})
  if(nxt is None):
    break
  next = nxt.a['href']
  next_page_url = base_url + next
  all_url.append(next_page_url)
  curr_page_url = next_page_url

for i in li:
  print(i)