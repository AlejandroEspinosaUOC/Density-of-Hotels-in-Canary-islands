import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import contextily as ctx

data = pd.read_csv('alojatur_2024.csv')

# GeoDataFrame a partir de les coordenades
geometry = [Point(xy) for xy in zip(data.utm_x, data.utm_y)]
geo_data = gpd.GeoDataFrame(data, geometry=geometry)

# Referència per a les canàries
geo_data.crs = "EPSG:25828"

fig, ax = plt.subplots(figsize=(20, 22))
#Plot
geo_data.plot(ax=ax, color='blue', markersize=10, alpha=0.5)

# Mapa base de les canàries
geo_data = geo_data.to_crs(epsg=25828)
ctx.add_basemap(ax, crs=geo_data.crs)

# Extra
plt.title('Dot Density Map allotjaments a les canàries')
plt.xlabel('UTM X')
plt.ylabel('UTM Y')
plt.grid()

plt.savefig('allotjaments_canaries.png')
plt.savefig('allotjaments_canaries.pdf')
plt.show()
