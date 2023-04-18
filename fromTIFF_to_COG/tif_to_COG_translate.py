# from GeoTIFF to COG

# input_file is the file (including path) .tif to be transformed e.g. "C:/Users/name/folder/input_file.tif".
# output_file is the file (including path) .tif transformed e.g. "C:/Users/name/folder/output_file.tif".
# Compression method. Typically, no compression, DEFLATE or LZW can be used for lossless, or JPEG for lossy. (Note that DEFLATE while more efficient than LZW can cause compatibility issues with some software packages). default=LZW
# include_internal_overivews default=True

def tif_to_COG_translate(input_file, output_file, include_internal_overivews = True, compress="LZW"):
    import os
    if include_internal_overivews:
        cmd = 'gdaladdo -r average "' + str(input_file) + '" 2 4 8 16'
        out = os.popen(cmd).read()
        print(out)
    cmd = 'gdal_translate "' + str(input_file) + '" "' + str(output_file) + '" -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=' + str(compress)
    out = os.popen(cmd).read()
    print(out)
    cmd = 'gdalinfo "' + str(output_file) + '"'
    out = os.popen(cmd).read()
    print(out)