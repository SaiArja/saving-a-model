import pandas as pd
import numpy as np
from sklearn import model_selection
import pickle
from sklearn.linear_model import LogisticRegression

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
names = ['Preg','plas','pers','skin','test','mass','pedi','age','class']
df = pd.read_csv(url, names = names)
# print(df)
#splitting train and test
X = df.iloc[:, :8]
y = df.iloc[:,8]

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2, random_state = 101)

# train the model
model = LogisticRegression()
model.fit(X_train, y_train)

result = model.score(X_test, y_test)

print(result)

#save the model

pickle.dump(model, open('dib_23.pkl','wb'))
