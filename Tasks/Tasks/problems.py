import numpy as np
import pandas as pd
import jax
import jax.numpy as jnp
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns


def problem_A(plot_range=(0,100)):
    def fn(x):
        y = np.power((x - 50), 2) / 2500
        return y
        
    def d_fn(x):
        dy_dx = 2 * (x - 50) / 2500
        return dy_dx
    
    # Plot problems
    plot_df = pd.DataFrame(range(plot_range[0], plot_range[1], 1), columns=['x']).reset_index()
    plot_df['y'] = plot_df['x'].map(fn)
    plot_df['dy/dx'] = plot_df['x'].map(d_fn)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,5))
    plot_df.plot(x='x', y='y', c='b', ax=ax1)
    ax1.set_title('Function')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    
    plot_df.plot(x='x', y='dy/dx', c='b', ax=ax2)
    plt.plot(plot_range, [0, 0])
    ax2.set_title('Derivative of function')
    ax2.set_xlabel('x')
    ax2.set_ylabel('dy')
    
    fig.suptitle('Problem A')
    
    return fn, d_fn

def problem_B(plot_range=(0,100)):
    def fn(x):
        y = (x-20) * (x - 40) * (x-50) * (x-95) / 1000000
        return y
        
    def d_fn(x):
        dy_dx = (4 * np.power(x,3) - 615 * np.power(x, 2) + 28500 * x - 401000) / 1000000
        return dy_dx
    
    # Plot problems
    plot_df = pd.DataFrame(range(plot_range[0], plot_range[1], 1), columns=['x']).reset_index()
    plot_df['y'] = plot_df['x'].map(fn)
    plot_df['dy/dx'] = plot_df['x'].map(d_fn)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,5))
    plot_df.plot(x='x', y='y', c='b', ax=ax1)
    ax1.set_title('Function')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    
    plot_df.plot(x='x', y='dy/dx', c='b', ax=ax2)
    plt.plot(plot_range, [0, 0])
    ax2.set_title('Derivative of function')
    ax2.set_xlabel('x')
    ax2.set_ylabel('dy')
    
    fig.suptitle('Problem B')
    
    return fn, d_fn

def problem_C(plot_range=(0,100)):
    def fn(x):
        y = (x-20) * (x - 40) * (x-50) * (x-95) / 1000000
        y = np.sin(x) / 20 + y
        return y
        
    def d_fn(x):
        dy_dx = np.cos(x) / 20 + (4 * np.power(x,3) - 615 * np.power(x, 2) + 28500 * x - 401000) / 1000000
        return dy_dx
    
    # Plot problems
    plot_df = pd.DataFrame(range(plot_range[0], plot_range[1], 1), columns=['x']).reset_index()
    plot_df['y'] = plot_df['x'].map(fn)
    plot_df['dy/dx'] = plot_df['x'].map(d_fn)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,5))
    plot_df.plot(x='x', y='y', c='b', ax=ax1)
    ax1.set_title('Function')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    
    plot_df.plot(x='x', y='dy/dx', c='b', ax=ax2)
    plt.plot(plot_range, [0, 0])
    ax2.set_title('Derivative of function')
    ax2.set_xlabel('x')
    ax2.set_ylabel('dy')
    
    fig.suptitle('Problem C')
    
    return fn, d_fn

def solution_plotter_1D(fn, history, plot_range=(0,100)):
    plot_df = pd.DataFrame(range(plot_range[0], plot_range[1], 1), columns=['x'])
    plot_df['y'] = plot_df['x'].map(fn)
    
    ax = plot_df.plot(x='x', y='y', c='b', figsize=(12,6))
    plt.plot(history, [fn(i) for i in history], c='r')
    ax.set_title('Your solution')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

def problem_D():
    def fn(x, a=1, b=100):
        y = np.power(a - x[0], 2) + b * np.power(x[1] - np.power(x[0], 2), 2)
        y = np.log1p(y)
        return y
        
    def d_fn(x, a=1, b=100):
        k = np.power(a - x[0], 2) + b * np.power(x[1] - np.power(x[0], 2), 2)
        k = np.log1p(k)
        dy_dx0 = 1 / (k + 1) * (-2 * (a - x[0]) - 4 * b * x[0] * (x[1] - np.power(x[0], 2)))
        dy_dx1 = 1 / (k + 1) * 2 * b * (x[1] - np.power(x[0], 2))
        return np.asarray([dy_dx0, dy_dx1])
    
    # Plot problems
    linspace = np.arange(-2, 2, 0.1)
    y = []
    dy_dx0 = []
    dy_dx1 = []
    for x0 in linspace:
        for x1 in linspace:
            y.append(fn([x0, x1]))
            
            [a, b] = d_fn([x0, x1])
            dy_dx0.append(a)
            dy_dx1.append(b)
            
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,5))
    ax1.contourf(linspace,
                 linspace,
                 np.asarray(y).reshape((40, 40)).T,
                 levels=10)
    ax1.set_title('Function')
    ax1.set_xlabel('x0')
    ax1.set_ylabel('x1')
    
    ax2.contourf(linspace,
                 linspace,
                 np.asarray(dy_dx0).reshape((40, 40)).T,
                 levels=10)
    ax2.set_title('Partial derivative (x0) of function')
    ax2.set_xlabel('x0')
    ax2.set_ylabel('x1')
    
    ax3.contourf(linspace,
                 linspace,
                 np.asarray(dy_dx1).reshape((40, 40)).T,
                 levels=10)
    ax3.set_title('Partial derivative (x1) of function')
    ax3.set_xlabel('x0')
    ax3.set_ylabel('x1')
    
    fig.suptitle('Problem D (Rosenbrook function variant)')
    
    return fn, d_fn

def solution_plotter_2D(fn, history):
    linspace = np.arange(-2, 2, 0.1)
    y = []
    for x0 in linspace:
        for x1 in linspace:
            y.append(fn([x0, x1]))
    
    fig, ax = plt.subplots(1, 1, figsize=(12,6))
    cs = ax.contourf(linspace,
                     linspace,
                     np.asarray(y).reshape((40, 40)).T,
                     levels=10)
    ax.plot([i[0] for i in history], [i[1] for i in history], c='r')
    ax.plot([1], [1], c='r', marker='x')
    ax.set_title('Your solution')
    ax.set_xlabel('x0')
    ax.set_ylabel('x1')
    cbar = fig.colorbar(cs)

def problem_subway():
    def fn(x):
        # Use floats for jax
        x = jnp.array(x, dtype='float')
        
        # Route and train parameters
        s = 4200 # [m]
        v_abs_max = 24 # [m/s]
        m = 10 * 38600 # [kg]
        k = 18 # drag coeff. [kg/m]

        a1_abs_max = 1 # [m/s^2] hardware limit
        a3_abs_max = 2 # [m/s^2] safety limit

        energy_price = 0.2 # [EUR / kWh]
        energy_price = energy_price / 1000 / 3600 # [EUR / Ws]

        tax_loss = 1 / 3600 # [EUR / s / people]

        passenger_mean = 100 # [pcs]

        # Cost model
        v_max = x[0] # [m/s]
        a1 = x[1] # [m/s^2]
        a3 = x[2] # [m/s^2]
        
        # Time and length 
        t1 = v_max / a1
        s1 = a1 / 2 * t1 * t1
        
        t3 = v_max / a3
        s3 = a3 / 2 * t3 * t3

        s2 = s - s1 - s3
        t2 = s2 / v_max
        
        t = t1 + t2 + t3

        # Energy balance
        E_drag_1 = k * pow(a1, 3) * pow(t1, 5) / 5
        E_drag_2 = (k * v_max * v_max) * v_max * t2
        E_drag_3 = k * pow(a3, 3) * pow(t3, 5) / 5
        E_drag = E_drag_1 + E_drag_2 + E_drag_3

        E_kinetic = (m /2 * v_max * v_max)

        E_regen_3 = (1 - jnp.exp(-a3)) / a3 * E_kinetic
        
        E_overall = E_kinetic - E_regen_3 + E_drag
        
        # Maintanance
        m_a1 = 3 * a1
        m_a3 = 6 * a3
        
        # Price components
        cost_energy = E_overall * energy_price
        cost_tax = passenger_mean  * t * tax_loss
        cost_maintanance = m_a1 + m_a3
        
        cost = cost_energy + cost_tax + cost_maintanance

        return cost
        
    def d_fn(x):
        # Use floats for jax
        x = jnp.array(x, dtype='float')
        
        # Gradient
        result = jax.grad(fn)(x)
        
        return np.asarray(result)
     
    return fn, d_fn