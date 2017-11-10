import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as p
import json
from functools import reduce
import pandas as pd
import glob
import os

# read all the json files into one all.json file and load that data
if os.path.isdir(os.getcwd()+'/camera_specs'):
    read_files = glob.glob("camera_specs/*.json")
else:
    print("[!] /camera_specs doesn't exist so you might have skipped some steps...\nExiting")
    quit()
with open("all.json", "w") as outfile:
    outfile.write('[{}]'.format(','.join([open(f, "r").read() for f in read_files])))
with open("all.json") as data_file:
    data = json.load(data_file)

aux=[]
sensors=['APS-C','Full frame','Four Thirds','Full Frame','1/2.3"']
for camera in data:
    if 'Weight (inc. batteries)' in camera:
        camera['Weight (inc. batteries)'] = int(camera['Weight (inc. batteries)'].split("g")[0].strip())
    if 'Dimensions' in camera:
        for dim in camera['Dimensions'].split("mm")[0].split("x"):
            dim = int(dim)
            aux.append(dim)
        vol = reduce(lambda x,y: x*y, aux) # in mm cube
        camera['Volume'] = round(vol/1000) # in cm cube
        aux = []
    if 'Sensor size' in camera:
        camera['Sensor size'] = camera['Sensor size'].split("(")[0].strip()
    if 'Effective pixels' in camera:
        camera['Effective pixels'] = int(camera['Effective pixels'].split()[0])

df = pd.DataFrame(data)#, columns=['Sensor size','Volume','Weight (inc. batteries)'])
sensordf = df[df['Sensor size'].isin(sensors)]

figure, axes = p.subplots(nrows=3, ncols=1, figsize=(7,10.5))

voldf = sensordf.groupby('Sensor size')['Volume'] # pandas.core.groupby.SeriesGroupBy
volplot = voldf.plot(kind='density', title='Camera size (vol. cm^3) by sensor sinze', legend=True, grid=True, x='Volume (cm^3)', xlim=(0,4000), ax=axes[0])

weightdf = sensordf.groupby('Sensor size')['Weight (inc. batteries)'] # pandas.core.groupby.SeriesGroupBy 
weightplot = weightdf.plot(kind='density', title='Camera weight (g) by sensor sinze', legend=True, grid=True, x='Weight (g)', xlim=(0,2000),ax=axes[1])

resdf = sensordf.groupby('Sensor size')['Effective pixels']
resplot = resdf.plot(kind='density', title='Camera resolution (MP) by sensor size', legend=True, grid=True, xlim=(0,60),ax=axes[2])

p.show()

'''
p.show()
p.cla()   # Clear axis
p.clf()   # Clear figure
p.close() # Close a figure window
'''