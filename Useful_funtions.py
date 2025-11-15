import pandas as pd
import pm4py
from fontTools.misc.cython import returns


def import_xes(file_path):
    event_log = pm4py.read_xes(file_path)
    print(event_log)
    for t in event_log:
        print(t)
    trace_list = list(filter(lambda t : len(t) > 5, event_log))
    print(trace_list)
    print(type(trace_list))

    trace_log = functools.filter(lambda t : len(t) > 5, event_log)
    print(type(trace_log))
    print(len(trace_log))

if __name__ == '__main__':
    i = 0