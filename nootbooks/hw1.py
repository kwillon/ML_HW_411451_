import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_csv("data/books.csv", sep=',')
df.info()