# output_path -> disk path where GeoTIFF will be saved
# data_array -> NumPy array
# crs_input -> CRS
# data_type -> Byte or Float32
# compression_method -> compression method. Typically, no compression, DEFLATE or LZW can be used for lossless, or JPEG for lossy.
# block_x_size -> x dimension of block size (must be multiples of 16)
# block_y_size -> y dimension of block size (must be multiples of 16)
# pm -> photometric

def geotiff_builder(output_path, data_array, crs_input, data_type = "Byte", compression_method = "LZW", block_x_size = 64, block_y_size = 64, pm = 'RGB'):
    # checking if block_x_size and block_y_size are multiples of 16
    if not block_x_size%16 == 0 or not block_y_size%16==0:
        exit()
    
    # used for data type
    arr = []
    # default value for tiled field
    tile = True
    # default value for photometric field
    p = pm
    
    # data type transformation
    if data_type == "Float32":
        arr = np.float32(data_array)
    else:
        arr = np.byte(data_array)
    
    # single band
    if arr.shape[0] == 1:
        tile = False
        p = 'Gray'
    
    # geotiff building
    with rio.open(
        output_path,
        'w',
        driver = 'GTiff',
        height = arr.shape[1],
        width = arr.shape[2],
        count = arr.shape[0],
        dtype = arr.dtype,
        crs = rio.CRS.from_string(crs_input),
        photometric = p,
        compress = compression_method,
        blockxsize = block_x_size,
        blockysize = block_y_size,
        tiled = tile
    ) as dst:
        dst.write(arr)
    dst.close()