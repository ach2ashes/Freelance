import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_generator import *

def benchmark(data_dist, sample_nbr=500, sort_functions=[], runs=3):
    # Generate data
    data = {}
    for dist in data_dist:
        if dist == 'A' or dist == 'uniform':
            data = uniform(data, sample_nbr=sample_nbr)
        elif dist == 'A2' or dist == 'sorted_data':
            data = sorted_data(data, sample_nbr=sample_nbr)
        elif dist == 'A3' or dist == 'sorted_reversed_data':
            data = sorted_reversed_data(data, sample_nbr=sample_nbr)
        elif dist == 'A4' or dist == 'sorted_few_unique':
            data = sorted_few_unique(data, sample_nbr=sample_nbr)
        elif dist == 'B' or dist == 'standard_normal':
            data = standard_normal(data, sample_nbr=sample_nbr)
        elif dist == 'C' or dist == 'binomial':
            data = binomial(data, sample_nbr=sample_nbr)
        elif dist == 'D' or dist == 'step_and_noise':
            data = step_and_noise(data, sample_nbr=sample_nbr)
        else:
            print('Unknown distribution:', dist)
    
    # Saving performance info in this dataframe
    performance_df = pd.DataFrame()

    # Check all sorting algorithm
    for fn in sort_functions:
        print('Testing function: ', fn.__name__ )

        # Check all data type
        for key in data.keys():
            print('Data type: ', key)
            test_data = data[key]

            # For multiple time for better timing accuracy
            for i in range(runs):
                # Time a sorting with given input
                start_time = time.perf_counter_ns()
                result = fn(test_data)
                execution_time = time.perf_counter_ns() - start_time

                # Save results
                stat = {'sort type': fn.__name__,
                        'data type': key.split('_')[0],
                        'data amount': sample_nbr,
                        'run': i, 'time [ms]': execution_time / 1000 / 1000}
                stat_df = pd.DataFrame(stat, index=[0])
                performance_df = pd.concat([performance_df, stat_df], ignore_index=True)
    
    # Plot settings
    sns.set(rc={'figure.figsize':(16,5)})
    sns.set_style("whitegrid")

    # Performance on different amount of data
    temp_df = performance_df[performance_df['data amount'] == sample_nbr]
    ax = sns.barplot(x="data type", y="time [ms]", hue="sort type", data=temp_df)
    ax.set_yscale('log')
    ax.set_title('Sorting algorithm performance on ' + str(sample_nbr) + ' data point')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
      
    