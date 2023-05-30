# Question 3: Compute the precision and recall for our model. Evaluate the model on
# the validation dataset on all thresholds from 0.0 to 1.0 with step 0.01.
# For each threshold, compute precision and recall. At which threshold do precision and recall intersect?
# - 0.1
# - 0.3
# - 0.6
# - 0.8

from prepare_data import prepare
from split_data import split_dataset
from log_reg import log_reg_model
from confusion_mat import confusion_matrix
import numpy as np

def solution(df, cols):
    '''Computes the precision and recall of our logistic regression model, then determines point of intersection'''
    df_prepared = prepare(df)
    df_train, df_val, df_test, y_train, y_val, y_test = split_dataset(df_prepared)
    y_pred = log_reg_model(cols, df_train, df_val, y_train, y_val)


    thresholds = np.linspace(0, 1, 101)
    df_scores = confusion_matrix(cols, thresholds, y_val, y_pred)

    # The graph shows precision and recall intersect only once
    # plt.plot(df_scores.threshold, df_scores.precision, label='precision')
    # plt.plot(df_scores.threshold, df_scores.recall, label='recall')
    # plt.legend()

    # Rounds the largest value of threshold where precision and recall intersect
    ans = np.round(max(df_scores[df_scores.loc[:, 'precision'] == df_scores['recall']]['threshold']), 1)
    
    return ans