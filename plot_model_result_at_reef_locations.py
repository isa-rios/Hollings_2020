import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import pandas 
import numpy as np
import xarray as xr
import xesmf


# Open Zooplankton Dataset
ds = xr.open_dataset('/Users/lizdrenkard/external_data/Hollings_2020/zooplankton_data_luo.nc')#, decode_times=False)
#print(ds)

# Open Reef Site CSV file
csv_fil = '/Users/lizdrenkard/TOOLS/Hollings_2020/ReefLocations.csv'
df = pandas.read_csv(csv_fil,encoding= 'unicode_escape')

# Create CSV xarray
rf_locs = xr.Dataset()
rf_locs['lon'] = xr.DataArray(data=df['LON'], dims=('reef_sites'))
rf_locs['lat'] = xr.DataArray(data=df['LAT'], dims=('reef_sites'))

#print(rf_locs)

# Call xesmf locStream
regridder = xesmf.Regridder(ds.rename({'GEOLON_T': 'lon', 'GEOLAT_T': 'lat'}), rf_locs, 'bilinear', locstream_out=True)
zpb_rf_locs = regridder((ds['SMALLZOO_BIOMASS']+ds['MEDZOO_BIOMASS']+ds['LARGEZOO_BIOMASS']))

# Pick a month index
nm = 6

fid, ax =  plt.subplots() 
zpb_rf_locs.isel(TIME=nm).plot.hist(ax=ax,edgecolor='black') 
ax.set_title('Total Zooplankton Biomass at Tropical Reef Sites')
ax.set_ylabel('Number of Reef Sites')
ax.set_xlabel('Zooplankton Biomass (units mass Carbon)')
ax.text(ax.get_xlim()[1]-.4*(np.diff(ax.get_xlim())), ax.get_ylim()[1]-.1*(np.diff(ax.get_ylim())), zpb_rf_locs['TIME'].isel(TIME=nm).values, fontsize=12)

plt.show()


