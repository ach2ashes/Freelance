import random
import numpy as np
from scipy.stats import binom
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def uniform(data_dict, sample_nbr, plot=False):
    # Sample from uniform distribution
    data_dict['A_' + str(sample_nbr)] = np.random.uniform(0, 1, sample_nbr)

    # Plot samples and their distribution
    if plot:
        plot_df = pd.DataFrame(data_dict['A_' + str(sample_nbr)], columns=['value']).reset_index()

        fig, (ax1, ax2) = plt.subplots(1, 2)
        plot_df.plot.scatter(x='index', y='value', c='b', ax=ax1)
        ax2.set_title('Scatter plot')

        plot_df['value'].plot.hist(bins=25, ax=ax2)
        ax2.set_title('Value distribution')

        fig.suptitle('A dataset')
    
    return data_dict

def sorted_data(data_dict, sample_nbr, plot=False):
    # Sorted data
    data_dict['A2_' + str(sample_nbr)] = sorted(np.random.uniform(0, 1, sample_nbr).tolist())

    # Plot samples and their distribution
    if plot:
        plot_df = pd.DataFrame(data_dict['A2_' + str(sample_nbr)], columns=['value']).reset_index()

        fig, (ax1, ax2) = plt.subplots(1, 2)
        plot_df.plot.scatter(x='index', y='value', c='b', ax=ax1)
        ax2.set_title('Scatter plot')

        plot_df['value'].plot.hist(bins=25, ax=ax2)
        ax2.set_title('Value distribution')

        fig.suptitle('A2 dataset')
    
    return data_dict

def sorted_reversed_data(data_dict, sample_nbr, plot=False):
    # Sorted and reversed data
    data_dict['A3_' + str(sample_nbr)] = sorted(np.random.uniform(0, 1, sample_nbr).tolist())[::-1]

    # Plot samples and their distribution
    if plot:
        plot_df = pd.DataFrame(data_dict['A3_' + str(sample_nbr)], columns=['value']).reset_index()

        fig, (ax1, ax2) = plt.subplots(1, 2)
        plot_df.plot.scatter(x='index', y='value', c='b', ax=ax1)
        ax2.set_title('Scatter plot')

        plot_df['value'].plot.hist(bins=25, ax=ax2)
        ax2.set_title('Value distribution')

        fig.suptitle('A3 dataset')
    
    return data_dict

def sorted_few_unique(data_dict, sample_nbr, plot=False):
    # Sorted few unique data
    steps = [3 * i for i in range(4)]

    data_dict['A4_' + str(sample_nbr)] = sorted([random.choice(steps) for i in range(sample_nbr)])

    # Plot samples and their distribution
    if plot:
        plot_df = pd.DataFrame(data_dict['A4_' + str(sample_nbr)], columns=['value']).reset_index()

        fig, (ax1, ax2) = plt.subplots(1, 2)
        plot_df.plot.scatter(x='index', y='value', c='b', ax=ax1)
        ax2.set_title('Scatter plot')

        plot_df['value'].plot.hist(bins=50, ax=ax2)
        ax2.set_title('Value distribution')

        fig.suptitle('A4 dataset')
    
    return data_dict

def standard_normal(data_dict, sample_nbr, plot=False):
    # Sample from standard normal distribution
    data_dict['B_' + str(sample_nbr)] = np.random.randn(sample_nbr)

    # Plot samples and their distribution
    if plot:
        plot_df = pd.DataFrame(data_dict['B_' + str(sample_nbr)], columns=['value']).reset_index()

        fig, (ax1, ax2) = plt.subplots(1, 2)
        plot_df.plot.scatter(x='index', y='value', c='b', ax=ax1)
        ax2.set_title('Scatter plot')

        plot_df['value'].plot.hist(bins=25, ax=ax2)
        ax2.set_title('Value distribution')

        fig.suptitle('B dataset')
    
    return data_dict

def binomial(data_dict, sample_nbr, plot=False):
    # Sample from binomial distribution
    data_dict['C_' + str(sample_nbr)] = binom.rvs(n=100, p=0.01, size=sample_nbr)

    # Plot samples and their distribution
    if plot:
        plot_df = pd.DataFrame(data_dict['C_' + str(sample_nbr)], columns=['value']).reset_index()

        fig, (ax1, ax2) = plt.subplots(1, 2)
        plot_df.plot.scatter(x='index', y='value', c='b', ax=ax1)
        ax2.set_title('Scatter plot')

        plot_df['value'].plot.hist(bins=25, ax=ax2)
        ax2.set_title('Value distribution')

        fig.suptitle('C dataset')
    
    return data_dict

def step_and_noise(data_dict, sample_nbr, plot=False):
    # Sample from step+noise distribution
    steps = [3 * i for i in range(8)]

    data_dict['D_' + str(sample_nbr)] = [value + random.choice(steps) for value in data_dict['A_' + str(sample_nbr)]]

    # Plot samples and their distribution
    if plot:
        plot_df = pd.DataFrame(data_dict['D_' + str(sample_nbr)], columns=['value']).reset_index()

        fig, (ax1, ax2) = plt.subplots(1, 2)
        plot_df.plot.scatter(x='index', y='value', c='b', ax=ax1)
        ax2.set_title('Scatter plot')

        plot_df['value'].plot.hist(bins=50, ax=ax2)
        ax2.set_title('Value distribution')

        fig.suptitle('D dataset')
    
    return data_dict