# Utilities to transform GeoTiff files into Cloud Optimized GeoTiff (COG)

The folder contains:
  - `tif_to_COG_translate.py` transforms a GeoTIFF to a Cloud-Optimized-GeoTIFF (COG).
  - `tif_to_COG_translate_notebook.ipynb` is the Jupyter Notebook version of the script.
  - `validate_cloud_optimized_geotiff.py` is a Python script to check if a .tif file is a valid  COG.
  - `Transform GeoTIFF file to COG.pdf`, a PDF file with an example and a brief explanation of the Python script.
  - `tif_to_COG_web.py` transforms a GeoTIFF to a Cloud-Optimized-GeoTIFF (COG) optimized for FAIRiCUBE Web maps. Basic usage: `python3 tif_to_COG_web.py input.tif`
  
### REQUIREMENTS:
  - GDAL>= 3.8, download from https://gdal.org/index.html
  - PROJ, download from https://proj.org/about.html

