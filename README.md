# An openEO back-end driver for geospatial data science using the Pangeo software stack
### Geosoftware II Project WiSe 2020/21
---

## Table of contents
[1. Overview](#overview) \
[2. Installation](#install) \
[3. Scope of functionalities](#functionalities)


\
<a name="overview"><h3>Overview</h3></a>
The goal of this project is to implement a backend that can process Copernicus Sentinel and SST data using pangeo-packages (primarily xarray and dask).
All Code of the used Microservices can be found here: [GeoSoftII2020-21 Github](https://github.com/GeoSoftII2020-21)


\
<a name="install"><h3>Installation</h3></a>
1. Download [docker-compose.yml](https://github.com/GeoSoftII2020-21/GeoSoftII_Projekt/blob/main/docker-compose.yml)
2. Configure your composefile by editing the  `database` item:  
	- Enter your username and password for accessing Copernicus Open Acess Hub to download Sentinel2 data 
	- select datasets and their time periods to download
	-  further information can be seen in the  [GeoSoftII_DataServer](https://github.com/GeoSoftII2020-21/GeoSoftII_DataServer#functionalities) GitHub repository.
3. Start the docker composefile, in step 2. selected datasets will be downloaded now
4. Get an [example.JSON](https://github.com/GeoSoftII2020-21/GeoSoftII_Projekt/tree/main/Examples) and configure it to your desired output:
	- `"loadcollection1"` with time period and datatype (SST or Sentinel2)
	- `"process_id"` with time period and boundingbox
	- `"process_id":"safe_result"` with time period and boundingbox
5. create a batchjob using the Python scripts for SST or Sentinel found in the [example folder](https://github.com/GeoSoftII2020-21/GeoSoftII_Projekt/tree/main/Examples)
6. Do an api-get-Request   `POST /jobs/` to create a new batch job with the posted JSON
7. Do an api-post-request   `POST /jobs/{job_id}/results` to start your specified Job
8. Do an api-get-Request `GET /jobs/{job_id}/results` to get a download link for the specified job

\
<a name="functionalities"><h3>Scope of functionalities</h3></a>

#### Central Functionality
Can be seen best by looking into the central functionalities of [SST](https://github.com/GeoSoftII2020-21/GeoSoftII_SST_Process#functionalities), [NDVI](https://github.com/GeoSoftII2020-21/GeoSoftII_NDVI_Process#functionalities) and [Demos](https://github.com/GeoSoftII2020-21/Demos)
