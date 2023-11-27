# Record computational demands automatically
In this folder there are the Python files for the issue [Record computational demands automatically](https://github.com/FAIRiCUBE/FAIRiCUBE-Hub-issue-tracker/issues/16)
- utils.py contains a function for byte convertions
- example.py contains an example to show how to use the application

### Requirements:
- [codecarbon](https://mlco2.github.io/codecarbon/index.html)
- [psutil](https://psutil.readthedocs.io/en/latest/#)
- [tracemalloc](https://docs.python.org/3/library/tracemalloc.html)
- [torch](https://pypi.org/project/torch/)
- [pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

## What it does
The Measurer application measures the following parameters and outputs them to a `csv` file:
- _Data size (MB)_: data consumed or freed up on disk (by creation or deletion of files)
- _Data size in grid points_
- _Largest allocated array in grid points_: the variable, instance of np.ndarray or pandas.DataFrame, with the highest size value. In NumPy and pandas size is the number of elements in the array.
- _Main memory available (GB)_: available RAM memory 
- _Main memory consumed (GB)_: used RAM memory during processing
- _Sum of allocated variable sizes (GB)_: the sum of all variables allocated by the script (in GB)
- _Description of CPU/GPU_
- _Wall time in seconds_: how many seconds took the processing to complete
- _Energy consumed (kW)_
- _Network traffic (MB)_
- _CO₂-equivalents [CO₂eq] (kg)_
- _Programming language_
- _Essential libraries_: main libraries loaded by the process
