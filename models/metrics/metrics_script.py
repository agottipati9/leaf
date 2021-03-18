#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import visualization_utils


# Constants
SHOW_WEIGHTED = True
PLOT_CLIENTS = True
stat_file = 'metrics_stat.csv'
sys_file = 'metrics_sys.csv'

# Retrieve Metrics
stat_metrics, sys_metrics = visualization_utils.load_data(stat_file, sys_file)

# Plots accuracy vs. round number.
if stat_metrics is not None:
    visualization_utils.plot_accuracy_vs_round_number(stat_metrics, True, plot_stds=False)

# Plots accuracy per client
if PLOT_CLIENTS and stat_metrics is not None:
    visualization_utils.plot_accuracy_vs_round_number_per_client(stat_metrics, sys_metrics, max_num_clients=20)

# Plots the cumulative sum of the bytes written and read by the server in
# the past rolling_window rounds versus the round number
if stat_metrics is not None:
    visualization_utils.plot_bytes_written_and_read(sys_metrics, rolling_window=10)

# Plot server computation per round
visualization_utils.plot_client_computations_vs_round_number(sys_metrics, aggregate_window=1, max_num_clients=20, range_rounds=(1, 4))

# Longest FLOP Path
print('Longest FLOPs path: %s' % visualization_utils.get_longest_flops_path(sys_metrics))