import json
import requests
from bs4 import BeautifulSoup as bsp
import gzip
import zlib
from io import BytesIO
import brotli

#OSCAR DATA
def oscar_data():
    url = 'https://www.scrapethissite.com/pages/ajax-javascript/' 
    response = requests.get(url) 
    data = bsp(response.text,'html.parser')
    yrs = data.find_all('a',{'class':'year-link'})
    urls = []
    year = []
    for yr in yrs:
        next_url=url+'#'+yr.string
        year.append(yr.string)
        urls.append(next_url)
    

    actual_oscar_urls=[]
    oscar_base_url = 'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year='
    
    for i in year:
        oscar_actual_url = oscar_base_url+i
        actual_oscar_urls.append(oscar_actual_url)

    full_info=[]
    for actual_url in actual_oscar_urls:
        oscar_response = requests.get(actual_url)
        movies = json.loads(oscar_response.text)
        full_info.append(movies)

    best_pictures = []

    for info in full_info:
        for i in info:
            if(i.get('best_picture') is not None):
                best_pictures.append({'year':i['year'],'title':i['title']})

    return full_info,best_pictures

# HOCKEY DATA
def hockey_data():
    # Step 1: Define the URL
    hockey_url = 'https://www.scrapethissite.com/pages/forms/?page_num=1'

    # Step 2: Send a request to the URL
    response = requests.get(hockey_url)

    # Step 3: Parse the HTML content
    soup = bsp(response.text, 'html.parser')

    # Step 4: Find the 'ul' with the class 'pagination'
    pagination_ul = soup.find('ul', {'class': 'pagination'})

    # Step 5: Extract all 'a' tags within the 'ul' and get their 'href' attributes
    hrefs = []
    if pagination_ul:
        a_tags = pagination_ul.find_all('a')
        for a in a_tags:
            href = a.get('href')
            if href:
                hrefs.append(href)

    # Print the extracted hrefs
    #print(hrefs)
    #last href is same as page 2, so remove it
    hrefs = hrefs[:-1]

    # for h in hrefs:
    #   print('https://www.scrapethissite.com'+h)

    teams=[] # array of dict --> each dict in this array denotes a team
    for url in hrefs:
        hockey_url='https://www.scrapethissite.com'+url
        #hockey_url = 'https://www.scrapethissite.com/pages/forms/?page_num=1' ---> for page 1
        h=requests.get(hockey_url)
        h_d=bsp(h.text,'html.parser')
        t=h_d.find_all(class_='team')
        for i in t:
            dic={}
            # name, year, wins, losses, ot-losses, pct, gf, ga, diff

            name=i.find('td',{'class':'name'}) 
            #print(name.string.strip())
            dic['name']=name.string.strip()

            year=i.find('td',{'class':'year'}) 
            dic['year']=year.string.strip()

            wins=i.find('td',{'class':'wins'}) 
            dic['wins']=year.string.strip()

            losses=i.find('td',{'class':'losses'}) 
            dic['losses']=year.string.strip()

            ot_losses=i.find('td',{'class':'ot-losses'}) 
            dic['ot_losses']=year.string.strip()

            pct=i.find('td',{'class':'pct'}) 
            dic['pct']=year.string.strip()

            gf=i.find('td',{'class':'gf'}) 
            dic['gf']=year.string.strip()

            ga=i.find('td',{'class':'ga'}) 
            dic['ga']=year.string.strip()

            diff=i.find('td',{'class':'diff'}) 
            dic['diff']=year.string.strip()

            teams.append(dic)

        return teams

def get_adv_urls():
    adv_url='https://www.scrapethissite.com/pages/advanced/'
    adv_base_url='https://www.scrapethissite.com/'
    adv_res=requests.get(adv_url)
    adv_data=bsp(adv_res.text,'html.parser')
    adv_data_h4=adv_data.find_all('h4')
    adv_urls=[]
    for i in adv_data_h4:
        adv_urls.append(adv_base_url+i.a['href'])
        print(adv_base_url+i.a['href'])
    return adv_urls

def failed_req_spoofing_headers():
    #SPOOFING THE HEADERS --> ADVANCED TOPICS REAL WORLD CHALLENGE - 1
    import requests
    from bs4 import BeautifulSoup as bsp

    # URL to scrape
    url = 'https://www.scrapethissite.com/pages/advanced/?gotcha=headers'

    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = bsp(response.content, 'html.parser')
        print(soup.prettify())  # Print the formatted HTML
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

def spoof_headers():

    # Define the headers
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Content-Type': 'text/plain',
        'Cookie': 'ar_debug=1',
        'Origin': 'https://www.scrapethissite.com',
        'Referer': 'https://www.scrapethissite.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    # Perform the request
    url = 'https://www.scrapethissite.com/pages/advanced/?gotcha=headers'
    response = requests.get(url, headers=headers)

    # Check the encoding
    encoding = response.headers.get('Content-Encoding')
    print("Content-Encoding:", encoding)

    # Handle different encodings
    if encoding == 'gzip':
        with gzip.GzipFile(fileobj=BytesIO(response.content)) as f:
            content = f.read().decode('utf-8')
    elif encoding == 'deflate':
        content = zlib.decompress(response.content, -zlib.MAX_WBITS).decode('utf-8')
    elif encoding == 'br':
        content = brotli.decompress(response.content).decode('utf-8')
    else:
        content = response.text

    # Print the response text
    print(content)
    return content