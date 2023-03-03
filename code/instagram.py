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
columns_graph = ['From Home', 'From Hashtags', 'From Explore', "From Other"]
palette = ['deep', 'muted', 'pastel', 'bright', 'dark']

print('Finish loading data')
# --------------------------------- 1. Visualization ---------------------------


def Graph(col, p):
    """Function to graph the data"""
    mu, std = norm.fit(data[col])
    fig, ax = plt.subplots()
    sns.set_palette(p)
    sns.histplot(data[col], kde=True, ax=ax, bins=30)
    ax.set(xlabel=col,
           ylabel="Density",
           title="Impressions " + col)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2,
             label="Fit Values: {:.2f} and {:.2f}".format(mu, std))

    ax.legend()
    # plt.savefig("../images/"+col+"1.png")


for col, p in zip(columns_graph, palette):
    Graph(col, p)


# Visualize the data (3 Columns in 1 Fig)
fig, axs = plt.subplots(1, 3, sharey=True, figsize=(15, 10))
for ax, colums in zip(axs, columns_graph):
    sns.histplot(data[colums], kde=True, ax=ax, bins=30)
    ax.set(xlabel=colums,
           ylabel="Density", xlim=(0, 15000),
           title="Impressions " + colums)
# plt.savefig("../images/visualization.png")


# Pie Chart
values = [data[i].sum() for i in columns_graph]
fig = px.pie(data, values=values, names=columns_graph,
             title='Impressions on Instagram Posts From Various Sources', hole=0.5)
# fig.write_image("../images/pie.png")

print('Finish 1')
# -------------------------------- 2. Kind of content -----------------------------------
for word in ['Caption', 'Hashtags']:
    text = " ".join(i for i in data[word])
    wordcloud = WordCloud(width=1600, height=800,
                          background_color='white').generate(text)
    plt.figure(figsize=(20, 10), facecolor='k')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    # wordcloud.to_file(f"../images/{word}.png")
print('Finish 2')
# -------------------------------- 3. Checking Relationships -----------------------------
for i in ["Likes", "Comments", "Shares", "Saves"]:
    sns.jointplot(data=data, x="Impressions", y=i, kind="reg", x_ci=None)
    # plt.savefig("../images/Relation"+i+".png")
print('Finish 3\n')
# ----------------------------------- 4. Correlation Process --------------------------------
cols = ["Impressions", "Likes", "From Hashtags", "Follows", "Profile Visits", "Saves", "From Home", "From Explore", "Shares",
        "From Other", "Comments"]
fig, axs = plt.subplots(figsize=(10, 10))
sns.heatmap(data[cols].corr(), cmap='YlGnBu')
# plt.savefig("../images/Correlation.png")

correlation = data.corr(numeric_only=True)
print(correlation["Impressions"].sort_values(ascending=False))
print('\n Finish 4')
# ---------------------------------- 5. Instagram Reach Prediction Model --------------------------------

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
