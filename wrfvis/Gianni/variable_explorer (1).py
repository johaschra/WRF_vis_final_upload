#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 08:49:08 2024

@author: gianniferribontempi
"""

import netCDF4 as nc
from os import sys
import numpy as np
import tkinter as tk
from tkinter import ttk

def show_variable_info():
    selectable_variable = combox.get()
    if selectable_variable:
        variable = dataset.variables[selectable_variable]
        variable = str(variable)
        variable = variable.splitlines()

        # Join the lines excluding the first one
        variable = '\n'.join(variable[1:])
        
        # Updating text in Tkinter 
        variable_text.delete("2.0", tk.END)
        variable_text.insert(tk.END, variable)
        
    

# Creating displayed window 
window = tk.Tk()

# Giving the file path
file_path = 'WRF_output_project.nc' 

# Reading the Dataset
dataset = nc.Dataset(file_path, 'r')

# Giving title and geometry to the window
window.title("Variable Explorer")
window.geometry("500x500")

# Creating a frame linked to the window and giving it a position
topframe = tk.Frame(window)
topframe.pack(side='top',pady=10)

# Getting variables list from the dataset
list_variables = dataset.variables
keys_list = list(list_variables.keys()) 

# Creating a label and giving to it a position in topframe
label_v = tk.Label(topframe, text="Variables:")
label_v.pack(side='left')

# Creating a Combobox and adding it to topframe
combox = ttk.Combobox(topframe, values=keys_list, style='Black.TCombobox')
combox.pack(side='left')

# setting text color of combobox
text_color = ttk.Style()
text_color.configure('Black.TCombobox',foreground = 'black')

# Display the first value as default
combox.set(keys_list[0])

# Create a button to show variable information
show_button = tk.Button(topframe, text="Show Variable Information", command=show_variable_info)
show_button.pack(side='left')

# Displaying variables information inside the window
variable_text = tk.Text(window, wrap=tk.WORD)

# fill both it's telling the object to expand till the maximum horizontally and vertically
variable_text.pack(fill='both',expand=True)

# Start the Tkinter event loop
window.mainloop()

# Close the NetCDF file when the window is closed
dataset.close()
 



