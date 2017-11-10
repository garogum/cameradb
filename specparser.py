from bs4 import BeautifulSoup
import requests
import re
import os

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