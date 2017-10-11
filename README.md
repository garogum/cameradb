A bunch of python scripts that eventually produce pandas DataFrames for getting statistics and cute plots

- specparser.py fetches all the links for camera spec pages of "relevant" vendors (currently that's all vendors listed at https://www.dpreview.com/products/)
- the actual scrapy scraper is under cameradb/
  - run with scrapy crawl cameradb
  - will use the file created with specparser.py
  - ...these should be merged
  - stores parsed data in JSON format
- madstats.py processes all the data and makes a graph with some density graphs

TODO:
- put everything into one functioning tool
- make the scraper aggregate all JSON data into all.json
  - currently done with "jq -s '.' * > all.json" from camera_specs/ to concatenate everything
- remove file dependencies maybe?


So there's a kind of a collection of all products on dpreview:

https://www.dpreview.com/products
example for Olympus _cameras_, not lenses:
https://www.dpreview.com/products/olympus/cameras?subcategoryId=cameras
example for "full" specs of a camera:
https://www.dpreview.com/products/olympus/slrs/oly_epl1/specifications

Or from here maybe https://www.digicamdb.com/
