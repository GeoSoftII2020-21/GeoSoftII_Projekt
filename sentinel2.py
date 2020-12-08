'''user = '' #from Scihub
password = '' #from Scihub
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')'''

from multiprocessing.dummy import freeze_support

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import geopandas as gpd
import folium
import rasterio as rio
import pandas as pd
import xarray as xr
import dask
import timeit
import time
from dask.diagnostics import ProgressBar
from dask.distributed import  Client, LocalCluster
#cluster= LocalCluster()
#client = Client (cluster)
client = Client()

def ndvi():

    '''to download specific sentinelData, choose date and cloudcover, for choosing area please define bounding box in the footprint '''
    ''''
    footprint = geojson_to_wkt(read_geojson('subset.geojson'))
    #footprint=<gml:Polygon srsName="http://www.opengis.net/gml/srs/epsg.xml#4326" xmlns:gml="http://www.opengis.net/gml"> <gml:outerBoundaryIs> <gml:LinearRing> <gml:coordinates>51.92544819931061,9.141955569822006 51.78482171524243,9.067417678030306 51.640839356950416,8.991790773698952 51.496720902135166,8.91665283377979 51.36152846581334,8.845725452997755 51.354432348394134,7.563305120541532 52.34134780285317,7.531528902588295 52.350386283733314,9.143290766756213 51.92544819931061,9.141955569822006</gml:coordinates> </gml:LinearRing> </gml:outerBoundaryIs> </gml:Polygon>
    print(footprint)
    products = api.query(footprint,
                         date = ('20200601', '20200630'),
                         platformname = 'Sentinel-2',
                         processinglevel = 'Level-2A',
                         cloudcoverpercentage = (0,10)
                        )

    print(products)
    products_gdf = api.to_geodataframe(products)
    products_gdf_sorted = products_gdf.sort_values(['cloudcoverpercentage'], ascending=[True])
    print(products_gdf_sorted['title'])
    #saveFile(products_gdf_sorted)

    products_gdf_sorted.to_csv('w')
    api.download_all(products) #downlads all files available files
    '''

    '''define import path and concrete files'''
    R60_a = 'S2B_MSIL2A_20200612T064629_N0214_R020_T39NXJ_20200612T110440.SAFE\GRANULE\L2A_T39NXJ_A017063_20200612T070244\IMG_DATA\R60m'
    R60_b = 'S2A_MSIL2A_20200613T103031_N0214_R108_T32UMC_20200613T111252.SAFE\GRANULE\L2A_T32UMC_A025988_20200613T103506\IMG_DATA\R60m'
    # Open b4 and b8
    b4a = rio.open(R60_a+'/T39NXJ_20200612T064629_B04_60m.jp2')
    b8a = rio.open(R60_a+'/T39NXJ_20200612T064629_B8A_60m.jp2')


    b4b = rio.open(R60_b+'/T32UMC_20200613T103031_B04_60m.jp2')
    b8b = rio.open(R60_b+'/T32UMC_20200613T103031_B8A_60m.jp2')


    # read Red(b4) and NIR(b8) as arrays
    red_a = b4a.read()
    nir_a = b8a.read()

    red_b = b4b.read()
    nir_b = b8b.read()

    #sumRed= (red_a+red_b)/2
    start = timeit.timeit()

    data = {'b4': [b4a, b4b], 'b8': [b8a, b8b]}
    df4 = [red_a, red_b]
    df8 = [nir_a, nir_b]
    combinedData = df4+df8
    datasets = dask.compute(*combinedData)



    end = timeit.timeit()
    print(end - start)


    i = 0
    sumRed = 0
    sumNir = 0

    while i < len(df4):

        sumRed = sumRed + datasets[i]
        sumNir = sumNir+datasets[len(df4)+i]
        i += 1


    sumRed = sumRed/(len(datasets)/2)
    sumNir = sumNir/(len(datasets)/2)


    '''
    sumRed = sumRed+df4[i]
    sumNir = sumNir+df8[i]
    i += 1
    
    sumRed =sumRed/2
    sumNir = sumNir/2
    print (sumNir)
    '''

    #print(sumRed)
    # Calculate ndvi
    ndvi = (sumNir.astype(float)-sumRed.astype(float))/(sumNir+sumRed)

    '''
    # Write the NDVI image
    meta = b4a.meta
    meta.update(driver='GTiff')
    meta.update(dtype=rio.float32)
    
    
    
    with rio.open('NDVIAver.tif', 'w', **meta) as dst:
        dst.write(ndvi.astype(rio.float32))
    '''

if __name__ == '__main__':
    ndvi()