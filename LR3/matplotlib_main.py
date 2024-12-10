import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def taylor_series(x, epsilon):
    """
    Calculate the first function using the Taylor series expansion with the given accuracy.
    
    Parameters:
    x (float): The input value for the function.
    epsilon (float): The desired accuracy for the Taylor series expansion.
    
    Returns:
    float: The value of the first function.
    """
    y = 0
    term = 1
    n = 0
    
    while abs(term) > epsilon:
        term = (-1)**n * x**(n) / np.math.factorial(n)
        y += term
        n += 1
    
    return 1 - x + x**2/2 - x**3/6 + x**4/24 + y

def plot_functions(xstart, xend, dx, epsilon,  b, color1, style1, marker1, color2, style2, marker2, legend_location, filename):
    """
    Plot the two functions on the given interval.
    
    Parameters:
    xstart (float): The start of the x-axis interval.
    xend (float): The end of the x-axis interval.
    dx (float): The step size for the x-axis.
    b (float): The value of the parameter 'b' for the second function.
    color1 (str): The color for the first function.
    style1 (str): The line style for the first function.
    marker1 (str): The marker style for the first function.
    color2 (str): The color for the second function.
    style2 (str): The line style for the second function.
    marker2 (str): The marker style for the second function.
    legend_location (str): The location for the legend.
    filename (str): The name of the file to save the plot.
    """
    x = np.arange(xstart, xend, dx)
    
    y1 = [taylor_series(xi, epsilon) for xi in x]
    y2 = np.exp(-x) + b
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y1, color=color1, linestyle=style1, marker=marker1, label='First Function')
    ax.plot(x, y2, color=color2, linestyle=style2, marker=marker2, label='Second Function')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plot of Two Functions')
    ax.legend(loc=legend_location)
    
    plt.savefig(filename)
    plt.show()

def main():
    root = tk.Tk()
    root.title("Function Plotter")

    # User input fields
    xstart_label = ttk.Label(root, text="X start:")
    xstart_label.grid(row=0, column=0, padx=5, pady=5)
    xstart_entry = ttk.Entry(root)
    xstart_entry.grid(row=0, column=1, padx=5, pady=5)

    xend_label = ttk.Label(root, text="X end:")
    xend_label.grid(row=1, column=0, padx=5, pady=5)
    xend_entry = ttk.Entry(root)
    xend_entry.grid(row=1, column=1, padx=5, pady=5)

    dx_label = ttk.Label(root, text="Step size (dx):")
    dx_label.grid(row=2, column=0, padx=5, pady=5)
    dx_entry = ttk.Entry(root)
    dx_entry.grid(row=2, column=1, padx=5, pady=5)

    epsilon_label = ttk.Label(root, text="Accuracy (epsilon):")
    epsilon_label.grid(row=3, column=0, padx=5, pady=5)
    epsilon_entry = ttk.Entry(root)
    epsilon_entry.grid(row=3, column=1, padx=5, pady=5)

    b_label = ttk.Label(root, text="Value of b:")
    b_label.grid(row=4, column=0, padx=5, pady=5)
    b_entry = ttk.Entry(root)
    b_entry.grid(row=4, column=1, padx=5, pady=5)

    # Customization options
    color1_label = ttk.Label(root, text="Color (First Function):")
    color1_label.grid(row=5, column=0, padx=5, pady=5)
    color1_entry = ttk.Entry(root)
    color1_entry.grid(row=5, column=1, padx=5, pady=5)

    style1_label = ttk.Label(root, text="Line Style (First Function):")
    style1_label.grid(row=6, column=0, padx=5, pady=5)
    style1_entry = ttk.Entry(root)
    style1_entry.grid(row=6, column=1, padx=5, pady=5)

    marker1_label = ttk.Label(root, text="Marker (First Function):")
    marker1_label.grid(row=7, column=0, padx=5, pady=5)
    marker1_entry = ttk.Entry(root)
    marker1_entry.grid(row=7, column=1, padx=5, pady=5)

    color2_label = ttk.Label(root, text="Color (Second Function):")
    color2_label.grid(row=8, column=0, padx=5, pady=5)
    color2_entry = ttk.Entry(root)
    color2_entry.grid(row=8, column=1, padx=5, pady=5)

    style2_label = ttk.Label(root, text="Line Style (Second Function):")
    style2_label.grid(row=9, column=0, padx=5, pady=5)
    style2_entry = ttk.Entry(root)
    style2_entry.grid(row=9, column=1, padx=5, pady=5)

    marker2_label = ttk.Label(root, text="Marker (Second Function):")
    marker2_label.grid(row=10, column=0, padx=5, pady=5)
    marker2_entry = ttk.Entry(root)
    marker2_entry.grid(row=10, column=1, padx=5, pady=5)

    legend_label = ttk.Label(root, text="Legend Location:")
    legend_label.grid(row=11, column=0, padx=5, pady=5)
    legend_entry = ttk.Entry(root)
    legend_entry.grid(row=11, column=1, padx=5, pady=5)

    filename_label = ttk.Label(root, text="Filename:")
    filename_label.grid(row=12, column=0, padx=5, pady=5)
    filename_entry = ttk.Entry(root)
    filename_entry.grid(row=12, column=1, padx=5, pady=5)

    plot_button = ttk.Button(root, text="Plot Functions", command=lambda: plot_functions(
        float(xstart_entry.get()),
        float(xend_entry.get()),
        float(dx_entry.get()),
        float(b_entry.get()),
        float(epsilon_entry.get()),
        color1_entry.get(),
        style1_entry.get(),
        marker1_entry.get(),
        color2_entry.get(),
        style2_entry.get(),
        marker2_entry.get(),
        legend_entry.get(),
        filename_entry.get()
    ))
    plot_button.grid(row=13, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()