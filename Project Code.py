#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:43:06 2021

@author: tylervo
"""

import numpy as np
import scipy.stats as stats
import pandas as pd             # this is the main statistical package
import statsmodels.api as sm    # This is the package that does the most "regression stuff"
import seaborn as sns           # Seaborn helps us to make nice plots
import matplotlib.pyplot as plt # Matplotlib helps us with graphs also. 

blm = pd.read_csv(r"/Users/tylervo/Downloads/BLM_Data_ready.csv")
blm.dropna(axis = 0, how = 'any', thresh = None, subset = None, inplace = True)
#%% Linear regression for The number of Black people in the total population
sns.regplot(x="BlackPop", y="AverageTurnout", data=blm, ci=0)
plt.title("Effect of Black Population on Average Turnout")
plt.ylabel("Average Turnout")
plt.xlabel("Total Black Population")
#plt.xlim(0, 300000)
#plt.ylim(0, 150)
#%%
## Define the explanatory and response variables

X = blm["BlackPop"]
# A little Math:
#We want to make an equation that looks like y = a + BX
# In order to do this, Python reads the equation as y = (1)*b0 + (X)* b1
#So, we need a column of just a bunch of "1"s. Thats what the add_constant function does!
X = sm.add_constant(X)
print(X)
y = blm["AverageTurnout"]


# Apply the regression equation
model = sm.OLS(y, X).fit()

b0 = round(model.params[0], 2)
b1 = round(model.params[1], 2)

print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")
#%%
"""""""""""""""""""""""""""""""""""""""
Create residual plot 
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = blm["BlackPop"]
X = sm.add_constant(X)
y = blm["AverageTurnout"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals
m_resid = model.resid

# Create plot 
sns.residplot(x=blm.BlackPop, y=m_resid)
plt.title("Residual plot")
plt.ylabel("Residuals")
plt.xlabel("Total Black Population")
#%% Linear regression for The number of Black/PC deaths
sns.regplot(x="deaths_black_pc", y="AverageTurnout", data=blm, ci=0)
plt.title("Effect of Black/PC deaths on Average Turnout")
plt.ylabel("Average Turnout")
plt.xlabel("Total Black/PC deaths")
#plt.xlim(0, .4)
#plt.ylim(0, 1000)

#%%
## Define the explanatory and response variables

X = blm["deaths_black_pc"]
# A little Math:
#We want to make an equation that looks like y = a + BX
# In order to do this, Python reads the equation as y = (1)*b0 + (X)* b1
#So, we need a column of just a bunch of "1"s. Thats what the add_constant function does!
X = sm.add_constant(X)
print(X)
y = blm["AverageTurnout"]


# Apply the regression equation
model = sm.OLS(y, X).fit()

b0 = round(model.params[0], 2)
b1 = round(model.params[1], 2)

print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")
#%%
"""""""""""""""""""""""""""""""""""""""
Create residual plot 
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = blm["deaths_black_pc"]
X = sm.add_constant(X)
y = blm["AverageTurnout"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals
m_resid = model.resid

# Create plot 
sns.residplot(x=blm.deaths_black_pc, y=m_resid)
plt.title("Residual plot")
plt.ylabel("Residuals")
plt.xlabel("The number of Black/PC deaths")
#%% Linear regression for Percent Bachelors
sns.regplot(x="PercentBachelor.s", y="AverageTurnout", data=blm, ci=0)
plt.title("Effect of percent bachelor on Average Turnout")
plt.ylabel("Average Turnout")
plt.xlabel("Percent Bachelor")
#plt.xlim(0, 300000)
#plt.ylim(0, 1000)
#%%
## Define the explanatory and response variables

X = blm["PercentBachelor.s"]
# A little Math:
#We want to make an equation that looks like y = a + BX
# In order to do this, Python reads the equation as y = (1)*b0 + (X)* b1
#So, we need a column of just a bunch of "1"s. Thats what the add_constant function does!
X = sm.add_constant(X)
print(X)
y = blm["AverageTurnout"]


# Apply the regression equation
model = sm.OLS(y, X).fit()

b0 = round(model.params[0], 2)
b1 = round(model.params[1], 2)

print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")
#%%
"""""""""""""""""""""""""""""""""""""""
Create residual plot 
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = blm["PercentBachelor.s"]
X = sm.add_constant(X)
y = blm["AverageTurnout"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals
m_resid = model.resid

# Create plot 
sns.residplot(x=blm['PercentBachelor.s'], y=m_resid)
plt.title("Residual plot")
plt.ylabel("Residuals")
plt.xlabel("Percent Bachelors")
#%%
sns.regplot( x="BlackPop", x1 = "deaths_black_pc", x2 = "PercentBachelor.s", y="AverageTurnout", data=blm, ci=0)
plt.title("Head and Body length of Crocs")
plt.ylabel("Body Length (cm)")
plt.xlabel("Head Length (cm)")
