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

## What it does
The Measurer application measures the following parameters and outputs them to a `csv` file:
- Data size (MB): data consumed or freed up on disk (by creation or deletion of files)
- Data size in grid points
- Main memory available (GB): available RAM memory 
- Main memory consumed (GB): used RAM memory during processing
- Description of CPU/GPU
- Wall time in seconds: how many seconds took the processing to complete
- Energy consumed (kW)
- Programming language
- Essential libraries: main libraries loaded by the process
