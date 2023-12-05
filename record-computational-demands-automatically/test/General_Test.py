from measurer import Measurer
from types import ModuleType
import numpy as np
import time
import os


def your_function():
    # Path where the data are stored (the use of the disk in this path is measured).
    # Use '/' to measure the entire disk.
    data_path = '/'
    measurer = Measurer()
    tracker = measurer.start(data_path=data_path)
    # example -> shape = [5490, 2170]
    shape = []

    #Start
    size_mb = 10
    artificial_data = np.zeros((size_mb * 1024 * 1024 // 8,), dtype=np.float64)

    seconds = 2
    time.sleep(seconds)

    csv_filename = "artificial_data.csv"
    np.savetxt(csv_filename, artificial_data, delimiter=",")
    file_size_bytes = os.path.getsize(csv_filename)
    print("Largest allocated array in grid points: ", artificial_data.shape)
    print("Memory consumption (Gb): ", size_mb/1024)
    print("Wall time in seconds: ", seconds)
    print("Data (MB): ", file_size_bytes/ (1024*1024))



    #End

    # it is very important to use program_path = __file__
    measurer.end(tracker=tracker,
                 shape=shape,
                 libraries=[v.__name__ for k, v in globals().items() if type(v) is ModuleType and not k.startswith('__')],
                 data_path=data_path,
                 program_path=__file__,
                 variables=locals(),
                 csv_file='benchmarks.csv')

if __name__ == "__main__":
    your_function()
