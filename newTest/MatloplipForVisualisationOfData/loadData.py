# Importing libraries
import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import auc, accuracy_score, confusion_matrix
import pandas as pd
import category_encoders as ce

# set a seed for reproducability
random.seed(42)
# read in our data
df_2018 = pd.read_csv("data_jobs_info_2018.csv")
df_2019 = pd.read_csv("data_jobs_info_2019.csv")

X = df_2018.drop("job_title", axis=1)
y = df_2018["job_title"]

# Splitting data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, test_size=0.20)
# save out the split training data to use with Cloud AutoML
with open("train_data_2018.csv", "+w") as file:
    pd.concat([X_train, y_train], axis=1).to_csv(file, index=False)
with open("test_data_2018.csv", "+w") as file:
    pd.concat([X_test, y_test], axis=1).to_csv(file, index=False)

# encode all features using ordinal encoding
encoder_x = ce.OrdinalEncoder()
X_encoded = encoder_x.fit_transform(X)
# you'll need to use a different encoder for each dataframe
encoder_y = ce.OrdinalEncoder()
y_encoded = encoder_y.fit_transform(y)
# split encoded dataset
X_train_encoded, X_test_encoded, y_train_encoded, y_test_encoded = train_test_split(X_encoded, y_encoded,
                                                    train_size=0.80, test_size=0.20)

from xgboost import XGBClassifier

# train XGBoost model with default parameters
my_model = XGBClassifier()
my_model.fit(X_train_encoded, y_train_encoded, verbose=False)

# and save our model
my_model.save_model("xgboost_baseline.model")