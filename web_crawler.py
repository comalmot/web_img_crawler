from bs4 import BeautifulSoup
import requests
import os

def take_file_list(url):
    global headers
    r = requests.get(url, headers=headers)
    source = r.text

    print(source)
    soup = BeautifulSoup(r.text, 'html.parser')

    a_list = soup.find_all('a')


    for i in a_list[5:]:
        print(i.attrs['href'])
        temp_url = url + i.attrs['href']
        print(temp_url)
        if '/' in i.attrs['href']:
            take_file_list(temp_url)
        
        with open(path + i.attrs['href'], 'wb') as file:
            r_  = requests.get(temp_url, headers=headers)
            file.write(r_.content)

path = './Down/'

if not os.path.exists(path):
    os.mkdir(path)

url = "http://www.mavericktheater.com/assets/images/"

headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}


r = requests.get(url, headers=headers)
source = r.text

print(source)
soup = BeautifulSoup(r.text, 'html.parser')

a_list = soup.find_all('a')


for i in a_list[5:]:
    print(i.attrs['href'])
    temp_url = url + i.attrs['href']
    print(temp_url)
    if '/' in i.attrs['href']:
        take_file_list(temp_url)
        continue
        
    with open(path + i.attrs['href'], 'wb') as file:
        r_  = requests.get(temp_url, headers=headers)
        file.write(r_.content)
