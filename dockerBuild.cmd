cd ..
cd GeoSoftII_DataServer
docker build -t felixgi1516/geosoft2_dataserver .
cd ..
cd GeoSoftII_Frontend
docker build -t felixgi1516/geosoft2_frontend .
cd ..
cd GeoSoftII_JobManagement
docker build -t felixgi1516/geosoft2_jobmanagement .
cd ..
cd GeoSoftII_NDVI_Process
docker build -t felixgi1516/geosoft2_ndvi_process .
cd ..
cd GeoSoftII_SST_Process
docker build -t felixgi1516/geosoft2_sst_process .