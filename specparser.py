# BeautifulSoup tutorial:
# http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/

from bs4 import BeautifulSoup
import requests
import re
#import urllib
import os

#r = requests.get("https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications")
#r = requests.get("https://www.dpreview.com/products/olympus/cameras?subcategoryId=cameras")
#data = r.text

companies = ["agfa","canon","casio","contax","dxo_labs","fujifilm","hartblei","kodak","konicaminolta","kyocera","leica","nikon","olympus","panasonic","pentax","ricoh","samsung","samyang","schneider","sigma","sony","tamron","tokina","voigtlander","zeiss"]

listoflinks = []

for company in companies:
    r = requests.get("https://www.dpreview.com/products/"+company+"/cameras?subcategoryId=cameras")
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    for link in soup.find_all('a'):
        camera = re.findall('.*buy', link.get('href'))
        if camera and 'products' in camera[0]:
            camera = camera[0].replace('buy', 'specifications')
            listoflinks.append(camera)
            if len(listoflinks) in range(0,5000,100):
                print("[!] Processed",len(listoflinks),"camera links...")

# write the list links to a file for later (scrapy) processing
with open(os.getcwd()+'/cameras.txt', 'w') as f:
    for i in listoflinks:
        f.write(i+'\n')
print("[!] Finished writing",company," cameras to",os.getcwd()+'cameras.txt')
    
'''
def scrape_and_save_pages(folder_path, url_list):
    for i, url in enumerate(url_list[:1], start=0):
        print(i)
        with urllib.request.urlopen(url) as response:
            html = str(response.read())
        with open(f'{folder_path}/{i}.html','w') as f:
            f.write(html)
'''