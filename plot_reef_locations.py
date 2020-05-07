import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import pandas 

def plot_reefs(lon, lat):
    fig = plt.figure(figsize=(12,4))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.LAND)

    # parallels/meridiens
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='gray', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabel_style = {'size': 18, 'color': 'black'}
    gl.ylabel_style = {'size': 18, 'color': 'black'}

    plt.plot(lon, lat, 'ro',markersize=2)
    return fig

csv_fil = '/Users/lizdrenkard/TOOLS/Hollings_2020/ReefLocations.csv'
df = pandas.read_csv(csv_fil,encoding= 'unicode_escape')

print(df)

fig = plot_reefs(df['LON'],df['LAT'])

plt.show()


