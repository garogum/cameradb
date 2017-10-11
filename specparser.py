# BeautifulSoup tutorial:
# http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/

from bs4 import BeautifulSoup
import requests
import re

#r = requests.get("https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications")
#r = requests.get("https://www.dpreview.com/products/olympus/cameras?subcategoryId=cameras")
#data = r.text

companies = ["agfa","canon","casio","contax","dxo_labs","fujifilm","hartblei","kodak","konicaminolta","kyocera","leica","nikon","olympus","panasonic","pentax","ricoh","samsung","samyang","schneider","sigma","sony","tamron","tokina","voigtlander","zeiss"]

for company in companies:
    r = requests.get("https://www.dpreview.com/products/"+company+"/cameras?subcategoryId=cameras")
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    for link in soup.find_all('a'):
        camera = re.findall('.*buy', link.get('href'))
        if camera and 'products' in camera[0]:
            camera = camera[0].replace('buy', 'specifications')
            print(camera)

    #for link in soup.find_all(re.compile()):
    #    print(link)