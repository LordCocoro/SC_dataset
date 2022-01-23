# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib inline
from matplotlib import patches

# read the csv file using read_csv function of pandas
train = pd.read_csv('train.csv')
train.head()