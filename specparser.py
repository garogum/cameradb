# BeautifulSoup tutorial:
# http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/

'''
https://www.dpreview.com/products/agfa
https://www.dpreview.com/products/canon
https://www.dpreview.com/products/casio
https://www.dpreview.com/products/contax
https://www.dpreview.com/products/dxo_labs
https://www.dpreview.com/products/fujifilm
https://www.dpreview.com/products/hartblei
https://www.dpreview.com/products/kodak
https://www.dpreview.com/products/konicaminolta
https://www.dpreview.com/products/kyocera
https://www.dpreview.com/products/leica
https://www.dpreview.com/products/nikon
https://www.dpreview.com/products/olympus
https://www.dpreview.com/products/panasonic
https://www.dpreview.com/products/pentax
https://www.dpreview.com/products/ricoh
https://www.dpreview.com/products/samsung
https://www.dpreview.com/products/samyang
https://www.dpreview.com/products/schneider
https://www.dpreview.com/products/sigma
https://www.dpreview.com/products/sony
https://www.dpreview.com/products/tamron
https://www.dpreview.com/products/tokina
https://www.dpreview.com/products/voigtlander
https://www.dpreview.com/products/zeiss
'''

from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications")

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
    

'''
<div class="specificationsPage">
    <table cellpadding="0" cellspacing="0" class="specsTable compact" style="margin-bottom: 15px;">
            <thead>
                <tr>
                    <th colspan="3" class="large groupLabel">Price</th>
                </tr>
            </thead>
            <tbody>
                            <tr>
                                <th class="label">
                                    MSRP
                                </th>
                                <td class="value">
                                    $699.99 / &#163;529.99 / &#8364;599 (body only), $799.99 / &#163;699.99 / &#8364;799 (with 14-42mm F3.5-5.6 lens (standard in US, EZ in Europe)
                                </td>
                                
                            </tr>
            </tbody>
            <thead>
                <tr>
                    <th colspan="3" class="large groupLabel">Body type</th>
                </tr>
            </thead>
            <tbody>
                            <tr>
                                <th class="label">
                                    Body type
                                </th>
                                <td class="value">
                                    SLR-style mirrorless
                                </td>
                                
                            </tr>
            </tbody>
'''