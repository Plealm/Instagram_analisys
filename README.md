# Instagram Business Account Analysis

Social networks are means to promote business, therefore, it is of utmost importance to learn as they are constantly changing, for this reason, it is essential to perform analysis like this on Instagram publications taking the data from [here](https://statso.io/instagram-reach-analysis-case-study/) where is composed for 13 differents columns:

<p align="justify">
  <ul>
<li>Impressions: Number of impressions in a post
<li>From Home: Reach from home
<li>From Hashtags: Reach from Hashtags
<li>From Explore: Reach from Explore
<li>From Other: Reach from other sources
<li>Saves: Number of saves
<li>Comments: Number of comments
<li>Shares: Number of shares
<li>Likes: Number of Likes
<li>Profile Visits: Numer of profile visits from the post
<li>Follows: Number of Follows from the post
<li>Caption: Caption of the post
<li>Hashtags: Hashtags used in the post
    </ul>
</p>


The process in order to analise this data was inspired in the study made by [AMAN KHARWAL](https://thecleverprogrammer.com/2022/03/22/instagram-reach-analysis-using-python/).

This analysis is divided into 5 parts:

## 1. Visuallization of the Data

Using the free seaborn and matplotlib libraries, bar plots were made on the impressions of the variables, where it was plotted the mean and median and adjusted the normal distribution parameters: 

### From Home
<p float="left">
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Home.png" width="400" height="300" />
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Home1.png" width="400" height="300" />
</p>
From the home section on Instagram has a mean of 2475.8 impressions, with a meadian of 2207 and a standard deviation of 1483.2.
  
### From Hashtags
<p float="left">
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Hashtags.png" width="400" height="300" />
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Hashtags1.png" width="400" height="300" />
</p>
  From this graphs we can see how the mean values is: 1887, median 1278 and std 1876, It is lower than home, but it is a considerable quantitive of impressions reached using Hashtags, seeing that is a good way to atract new followers.
  
### From Explore
<p float="left">
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Explore.png" width="400" height="300" />
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Explore1.png" width="400" height="300" />
</p>
In the case of explore the stadistics parameters are: mean 1078, median 326 and std 2602. In this case as the std is bigger than the mean, it means a high variation between values, and abnormal distribution for data suggesting that as a central parameter is better the median and variation parameter is prefer the range. But, It also means that the suggestion algortim from Instagram do not help to much in order to crear more impressions and followers.
  
### From Other
<p float="left">
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Other.png" width="400" height="300" />
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/From%20Other1.png" width="400" height="300" />
</p>

In other sources ways to reach new followers, the stadistical parameters have the same behaviour than explore where mean = 171 < std = 288 leaving as central parameter median = 74 and the range. It can be see it that this is the lowest contribution.

### Comparation 3
  <img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/visualization.png" width="900" height="360" />
  
  Plotting the 3 with the best contribution explore shows how the majority of its impressions are in the range from 0 to 2500 describing that it is important to improve in this section.
  
### Pie Chart
<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/pie.png" width="500" height="350" />

Tha above pie chart demostrates that 44% of the impresions are from Home, 33% from Hashtags, 19.2% from Explore and only 3% from Other sources.
  
## 2. Wordcloud Caption and Hashtags

### Caption
<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/Caption.png" width="600" height="350" />

Cerating a wordcloud of the words more used in captions we can check that: "Machine Learning", "Using Python", "Data Science", "Time Series" among others are the most used.

### Hashtags
<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/Hashtags.png" width="600" height="350" />

the most populars Hashtags used in the Instagrams publications are: "#pythonprogramming", "#pyhtonproject", "theclaverprogrammer" between others Hashtags.

## 3. Relation between Impressions and other variables

Trying to discorver some relationships between variables It can be done a regresion of likes, comments, shares and saves with their respect impressions.

### Likes
<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/RelationLikes.png" width="600" height="450" />

It can be a linear realationship between the number of likes and the number of impressions, but there are some outliners that decrease the correlation factor.

### Comments
<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/RelationComments.png" width="600" height="450" />

There is not a linear relationship at all. Therefore the number of comments do NOT affect the number of people reach. This can be explanied checking the bar plot on the right for comments.

### Shares
<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/RelationShares.png" width="600" height="450" />

There is a linear realationship between the number of shares and the number of impressions.

### Saves
<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/RelationSaves.png" width="600" height="450" />
Shares also shows a linear realtionship saying: A more number of saves will result in a higher reach.


## 4. Correlation

<img src="https://github.com/Plealm/Instagram_analisys/blob/64f1a12e3df0c48f301e1b9c8283ef1b97362203/images/Correlation.png" width="600" height="450" />

From this heat map it can be seen that the parameters that are more correlated with impresions are: From explore, Likes, From Hashtags  and Follows.

![Screenshot from 2023-03-03 16-56-00](https://user-images.githubusercontent.com/84750731/222837317-fe9da5f3-412a-434c-9e49-ca4035d9eb33.png)

Checking numerically the correlationship where nearest of 1 or -1 is a good correlationship and near from 0 is not correlationship the more important values are the mention before where all of them have a pearson correlationship more than 0.8, this means that it can be a correlation even if it is not a strong one. 

## 5. Machine Learning Prediction

![Screenshot from 2023-03-03 16-56-14](https://user-images.githubusercontent.com/84750731/222837392-42e71656-de93-49a8-b57d-d4757037abd8.png)

Using the PassiveAggressive Model one of the few online learning algoritms where it is used primarilly in problems where data is streaming in a continuous flow, also when is a huge amount of data and it is computationally infeasible to train the entire dataset because of the sheer size of the data. The name of this method is because:

<li>Passive: If the prediction is correct, keep the model and do not make any changes. i.e., the data in the example is not enough to cause any changes in the model. 
<li>Aggressive: If the prediction is incorrect, make changes to the model. i.e., some change to the model may correct it.

Information taken from: [geeksforgeeks](https://www.geeksforgeeks.org/passive-aggressive-classifiers/) and [AMAN KHARWAL](https://thecleverprogrammer.com/2021/07/04/passive-aggressive-regression-in-machine-learning/)
