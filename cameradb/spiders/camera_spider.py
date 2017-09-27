import scrapy


class CameraSpider(scrapy.Spider):
    name = "cameradb"

    def start_requests(self):
        urls = [
            'https://www.dpreview.com/products/olympus/slrs/oly_epl1/specifications',
            'https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'cameras-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
'''
tested on view-source:https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications
scrapy shell https://www.dpreview.com/products/olympus/slrs/oly_em10/specifications
camera = response.css("div.specificationsPage")[0]
table = camera.css("table.specsTable.compact")[0]
table.css("thead")[0].css("tr").css("th::text")[0].extract()
'Price'
table.css("tbody")[0].css("tr").css("td.value::text")[0].extract()
'\r\n                                    $699.99 / £529.99 / €599 (body only), $799.99 / £699.99 / €799 (with 14-42mm F3.5-5.6 lens (standard in US, EZ in Europe)\r\n                                '
'''

# So I could build it up like:
# - per camera
#  - thead -> tbody
#   just like a key -> value thing

for i in table.css("thead"):
    print(i.css("tr").css("th::text")[0].extract(), )
    
'''
Price
Body type
Sensor
Image
Optics & Focus
Screen / viewfinder
Photography features
Videography features
Storage
Connectivity
Physical
Other features
'''

# this is actually pretty decent
for i in table.css("tbody"):
    for j,k in zip(i.css("tr").css("th.label::text").extract(), i.css("tr").css("td.value::text").extract()):
        if (j.strip() and k.strip()) != '':
            print(j.strip(), "-", k.strip())
    #print(i.css("tr").css("th.label::text")[0].extract().strip() , "-", i.css("tr").css("td.value::text")[0].extract().strip())

for i in table.css("tbody"):
    for j in i.css("tr").css("th.label::text").extract():
        print(j.strip())
table.css("tbody").css("tr").css("th.label::text").extract()

for i in table.css("tbody"):
    for j in i.css("tr").css("td.value::text").extract():
        print(j.strip())
table.css("tbody").css("tr").css("td.value::text").extract()

# one Dict per camera...?
# ....list of dicts aka of cameras...?