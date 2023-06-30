from measurer import Measurer
from types import ModuleType


def your_function():
    # Path where the data are stored (the use of the disk in this path is measured).
    # Leave '/' to measure the entire disk.
    data_path = '/'
    measurer = Measurer()
    tracker = measurer.start(data_path=data_path)
    # example -> shape = [5490, 2170]
    shape = []

  '''
    # write here your code...
  '''

    measurer.end(tracker=tracker,
                 shape=shape,
                 libraries=[k for k, v in globals().items() if type(v) is ModuleType and not k.startswith('__')],
                 data_path=data_path,
                 csv_file='benchmarks.csv')
