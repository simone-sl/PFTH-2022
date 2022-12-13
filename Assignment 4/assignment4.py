import numpy as np
import matplotlib.pyplot as plt 
#data visualization
import matplotlib as mpl
#data processing 
import pandas as pd
import os
#file finding

def visualization():
    input_file_name = input("Please enter a file name to analyze: ")
    #prompts user to enter a file name to find and analyze
    output_file_name = input("Please enter your desired file name: ")
    #prompts user to enter a file name to save the analyzed data into
    if os.path.exists(input_file_name):
        #if the user entered file exists the file will be opened, 
        # analyzed, then inputted into the output file as an average value plot
        f = open(input_file_name, "r")
        data=np.loadtxt(input_file_name, delimiter=',')
        #data from a csv value is loaded
        ave_value = np.mean(data, axis = 0)
        ave_plot = plt.plot(ave_value, linewidth=5, color='pink', )
        #constructs a plot of the average from the received data
        #plot is customizable (linewidth and color)
    plt.title('Average of ' + input_file_name)
    plt.xlabel('Your label here')
    plt.ylabel('Your label here')
    #customizable title and axis
    #plt.show()
    #optional to show to the figure before saving 
    plt.show()
    #shows the fig before saving
    plt.savefig(output_file_name)
    #saves the fig under the desired file name
    plt.close()
    f.close()
visualization()
#shows the average values in a singular line, fully customizable

def subplot():
    input_file_name = input('Please enter a file name to analyze: ')
    output_file_name = input('Please enter a desired file name: ')
    if os.path.exists(input_file_name):
        f = open(input_file_name, "r")
        data=np.loadtxt(input_file_name, delimiter=',')
        df = data
        df = pd.read_csv(input_file_name, nrows = 8)
        arr = df.to_numpy()
        x = arr
        nrows = x.shape[0]
        fig, axes = plt.subplots(8, 1)
        for i in range(0, 8):
            axes[i].plot(x[:][i], linewidth=1, color = 'pink')
    plt.show()
    plt.savefig(output_file_name)
    plt.close()
    f.close()
#subplot()

def stack():
    input_file_name = input("Please enter a file name to analyze: ")
    output_file_name = input("Please enter a file name to output: ")
    if os.path.exists(input_file_name):
        f = open(input_file_name, "r")
        data=np.loadtxt(input_file_name, delimiter=',')
        image = plt.plot(data)
    plt.title('Stacking of ' + input_file_name)
    plt.xlabel('Your label here')
    plt.ylabel('Your label here')
    plt.show()
    plt.savefig(output_file_name)
    plt.close()
#stack() 
#shows all data within one plot