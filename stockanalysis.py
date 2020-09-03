#%%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import math
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime
style.use('ggplot')
dataset = pd.read_csv("AMD.csv",header=0,
index_col='Date',
parse_dates=True)
dataset['h2l']= (dataset['High']-dataset['Low'])/dataset['Adj Close']*100
dataset['daily']=(dataset['Adj Close']-dataset['Open'])/dataset['Open']*100
dataset.dropna(inplace=True)


forecast_col = 'Adj Close'
dataset.fillna('-999999',inplace=True)
forecast_out = int(math.ceil(0.01*len(dataset)))
dataset['label']=dataset['Adj Close'].shift(-forecast_out)
print(forecast_out)
dataset.dropna(inplace=True)

X=np.array(dataset.drop(['label'],1))
y=np.array(dataset['label'])
X=preprocessing.scale(X)

y=np.array(dataset['label'])
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)
clf = LinearRegression()
clf.fit(X_train,y_train)
y_predict=clf.predict(X_test)
accuracy=clf.score(X_test,y_test)
X=X[:-forecast_out]
X_lately=X[-forecast_out:]
print("Accuracy is ",accuracy*100)
forecast_set = clf.predict(X_lately)
print(forecast_set)
dataset['forecast']=np.nan
last_date=dataset.iloc[-1].name
last_unix=last_date.timestamp()
one_day=86400
next_unix=last_unix + one_day
for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    dataset.loc[next_date] = [np.nan for _ in range(len(dataset.columns)-1)] + [i]
dataset['Adj Close'].plot()
dataset['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('price')
plt.show()
y_test.shape

#%%
