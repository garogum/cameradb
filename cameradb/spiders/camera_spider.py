import scrapy
import os
import subprocess
import json
import pandas as pd

class CameraSpider(scrapy.Spider):
    name = "cameradb"

    def start_requests(self):
        file = 'cameras'
        #urls = ['https://www.dpreview.com/products/agfa/compacts/agfa_dc600uw/specifications']

        with open(file) as f:
            urls = [url.strip() for url in f.readlines()]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        camera={}
        values=[]
        labels=[]
        page = response.url.split("/")[-2]
        filename = os.getcwd()+'/cameradata/'+'cameras-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        camera_name = response.xpath('//h1[@itemprop="name"]/text()').extract()[0]
        self.log('##### Processing camera %s #####' % camera_name)
        camera['Model'] = camera_name

        for i in response.xpath('//div[@class="specificationsPage"]/table[contains(@class,"specsTable")]/tbody/tr/th/text()').extract():
            labels.append(i.strip())
            
        shits=[]
        for item in response.xpath('//div[@class="specificationsPage"]/table[contains(@class,"specsTable")]/tbody/tr/td'):
            shits.append(item.xpath('.//text()').extract())
        for shit in shits:
            values.append(' '.join(shit).strip())
            
        #print(labels)
        #print(values)      
        #print("length of labels", len(labels))
        #print("length of values", len(values))
        
        for label, value in zip(labels, values):
            #print(label,"-",value)
            camera[label] = value
            
        specs_file = os.getcwd()+'/camera_specs/'+'%s_specs' % page
        with open(specs_file, 'w') as file:
            json.dump(camera, file)
            print("##### Wrote "+ camera_name +" specs to "+ specs_file +" #####")

# https://stackoverflow.com/questions/7100125/storing-python-dictionaries
# https://pythontips.com/2013/08/08/storing-and-loading-data-with-json/
# https://www.slideshare.net/wesm/data-structures-for-statistical-computing-in-python
# https://stackoverflow.com/questions/24722923/trying-to-extract-data-from-tables-using-scrapy
# https://stackoverflow.com/questions/21105492/python-scrapy-for-grabbing-table-columns-and-rows
# https://stackoverflow.com/questions/18609267/scrapy-how-to-separate-text-within-a-html-tag-element

#### For plotting the data ####
# https://stackoverflow.com/questions/21913007/matplotlib-with-json-files
# aka get it into a pandas dataframe and then plot that with matplotlib
# http://pandas.pydata.org/pandas-docs/stable/visualization.html

# jq -s '.' * > all.json
# with open('camera_specs/all.json') as data_file:
#   data = json.load(data_file)
# pd.DataFrame(data)
# pd.DataFrame(data, columns=['Model','Dimensions','Sensor type','Max resolution','Flash modes','Sensor size'])
# https://seaborn.pydata.org/



'''
tested on view-source:https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications
scrapy shell https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications
camera = response.css("div.specificationsPage")[0]
table = camera.css("table.specsTable.compact")[0]

        #subprocess.call("sed -i -e 's/<span[^>]*>//g' "+filename,shell=True)
        #subprocess.call("sed -i -e 's/<\/span[^>]*>//g' "+filename, shell=True)
'''

# So I could build it up like:
# - per camera
#  - thead -> tbody
#   just like a key -> value thing
'''

# this is actually pretty decent
for i in table.css("tbody"):
    for j,k in zip(i.css("tr").css("th.label::text").extract(), i.css("tr").css("td.value::text").extract()):
        if (j.strip() and k.strip()) != '':
            print(j.strip(), "-", k.strip())
    #print(i.css("tr").css("th.label::text")[0].extract().strip() , "-", i.css("tr").css("td.value::text")[0].extract().strip())

for i in table.css("tbody"):
    for j in i.css("tr>th.label::text").extract():
        print(j.strip())
table.css("tbody").css("tr").css("th.label::text").extract()

for i in table.css("tbody"):
    for j in i.css("tr>td.value::text").extract():
        print(j.strip())
table.css("tbody").css("tr").css("td.value::text").extract()

# one Dict per camera...?
# ....list of dicts aka of cameras...?
'''