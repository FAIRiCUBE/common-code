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
- ___Data size (MB)___: data consumed or freed up on disk (by creation or deletion of files)
- ___Data size in grid points___
- ___Largest allocated array in grid points___: the variable, instance of np.ndarray or pandas.DataFrame, with the highest size value. In NumPy and pandas size is the number of elements in the array.
- ___Main memory available (GB)___: available RAM memory 
- ___Main memory consumed (GB)___: used RAM memory during processing
- ___Sum of allocated variable sizes (GB)___: the sum of all variables allocated by the script (in GB)
- ___Description of CPU/GPU___
- ___Wall time in seconds___: how many seconds took the processing to complete
- ___Energy consumed (kW)___
- ___Network traffic (MB)___
- ___CO₂-equivalents [CO₂eq] (kg)___
- ___Programming language___
- ___Essential libraries___: main libraries loaded by the process
