A collection of python scripts for scraping digital camera specs from dpreview.com for statistical analysis using the pandas library

![3 plot figure](/multiplot.JPG?raw=true "Density plots")

# Usage
1. Run specparser.py to fetch the links for camera spec pages of all vendors listed at https://www.dpreview.com/products/. This will create a cameras.txt file which will be used as input for the scrapy crawler
2. Run `scrapy crawl cameradb`, which will fetch all pages, saving them to /cameradata, and extracting relevant info into individual JSON files under /camera_specs
3. Run madstats.py to aggregate all individual JSON files into a single all.json which will be used by pandas and matplotlib to generate plots.
