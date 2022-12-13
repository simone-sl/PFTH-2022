# Title: Assignment 6: Regression and Data Visualization
# Author: Simone Lewis 
# Date: 12-12-2022

# This script contains my individual assignment. 


#importing dependencies and libraries

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

def regression():
        df = pd.read_csv('adm_data.csv')
        #reading csv file
        df.drop(df.columns[0], axis=1, inplace=True)
        X = df.loc[:,['Chance of Admit', 'CGPA']].values

        scaler = StandardScaler()
        scaler.fit(X)
        X_sd = scaler.transform(X)
        x = X_sd[:,1].reshape(-1, 1)
        y = X_sd[:,0].reshape(-1, 1)

        X_train, X_test, y_train, y_test = train_test_split(
        #split array into train and test subjects
                x, y, 
                test_size=0.20, 
                random_state=20
                )   

        reg = linear_model.LinearRegression()
        reg.fit(X_train, y_train)
        #regression matrix

        y_pred = reg.predict(X_test)
        print(f'Coefficients: {reg.coef_}')
        print(f'Average Squared Error: {mean_squared_error(y_test, y_pred)}')
        print(f'Coefficient of Determination: {r2_score(y_test, y_pred)}')

        fig, axs = plt.subplots(1, 2, figsize=(9,9), sharex=True)
        fig.text(0.5, 0.04, 'Chance of Admision', ha='center',size=15)
        fig.text(0.05, 0.5, 'Undergraduate GPA', va='center', rotation='vertical',size=15)
        fig.suptitle('Chance of Admission vs. Undergraduate GPA (Training & Testing Set)')
        axs[0].plot(X_train, reg.predict(X_train), linewidth=3, color ='palevioletred')
        axs[0].scatter(X_train, y_train, color = 'pink')
        axs[0].set_title('Training Set')
        axs[0].legend(['Regression Line', 'Original Observations'], numpoints=1, loc='lower right')
        axs[1].plot(X_train, reg.predict(X_train), linewidth=3, color ="thistle")
        axs[1].scatter(X_test, y_test, color ='orchid')
        axs[1].legend(['Regression Line', 'Original Observations'], numpoints=1, loc='lower right')
        axs[1].set_title('Test Set')     
        
        plt.show()
        plt.close()
regression()



""" 

This script uses machine learning to predict continuous 
values from administrative data. 
The data I chose to analyze are the 'Chance of Admit' & 
'CGPA' values. Which are the chance of admission into the university
and the undergraduate GPA.  

The mean squared error is smaller and preferred, meaning that there are few errors.  
The coefficient of determination returned indicates a weak 
to medium correlation betweeen the selected variables.  

After the data is analyzed, it is visualized using matplotlib,
where the testing and training are plotted. 

"""






