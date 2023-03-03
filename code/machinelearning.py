# Code to analyze the Instagram business account
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, ImageColorGenerator
from scipy.stats import norm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

# Read Data using the path
data = pd.read_csv('../data/Instagram.csv',  encoding='latin1')

fe = ['Likes', 'Saves', 'Comments', 'Shares',
      'Profile Visits', 'Follows']

x = np.array(data[fe])
y = np.array(data["Impressions"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.2,
                                                random_state=2)
model = PassiveAggressiveRegressor()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)

features = []
print("Please Select:")
for i in range(len(fe)):
    val = input(f"How many {fe[i]}?: ")
    features.append(int(val))

results = model.predict(np.array([features]))
print(
    f"With the given parameters the expect impression for the post is: {float(results):.2f}")
