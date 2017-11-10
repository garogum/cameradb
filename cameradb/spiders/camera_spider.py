import scrapy
import os
import subprocess
import json

class CameraSpider(scrapy.Spider):
    name = "cameradb"

    def start_requests(self):
        # specparser.py will make a "cameras" file listing all url's to all cameras to be parsed
        file = 'cameras.txt'
        with open(file) as f:
            urls = [url.strip() for url in f.readlines()]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        camera={}
        values=[]
        labels=[]
        os.makedirs("cameradata", exist_ok=True)
        os.makedirs("camera_specs", exist_ok=True)
        page = response.url.split("/")[-2]
        # Write the HTML response to a file
        # These can be used later without having to bombard dpreview.com again
        filename = os.getcwd()+'/cameradata/'+'cameras-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        camera_name = response.xpath('//h1[@itemprop="name"]/text()').extract()[0]
        self.log('##### Processing camera %s #####' % camera_name)
        camera['Model'] = camera_name

        # get the field keys
        for i in response.xpath('//div[@class="specificationsPage"]/table[contains(@class,"specsTable")]/tbody/tr/th/text()').extract():
            labels.append(i.strip())
            
        # get the values for the previously fetched keys in the specs table
        fieldvaluess=[]
        for item in response.xpath('//div[@class="specificationsPage"]/table[contains(@class,"specsTable")]/tbody/tr/td'):
            fieldvaluess.append(item.xpath('.//text()').extract())
        for fieldvalue in fieldvaluess:
            values.append(' '.join(fieldvalue).strip())
        
        for label, value in zip(labels, values):
            #print(label,"-",value)
            camera[label] = value
            
        specs_file = os.getcwd()+'/camera_specs/'+'%s_specs.json' % page
        with open(specs_file, 'w') as file:
            json.dump(camera, file)
            print("##### Wrote "+ camera_name +" specs to "+ specs_file +" #####")