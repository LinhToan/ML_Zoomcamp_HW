# Question 4: Compute the F1 score for all thresholds in [0, 1] with increment 0.01 using the validation set.
# At which threshold is F1 maximal?
# - 0.1
# - 0.4
# - 0.6
# - 0.7

from prepare_data import prepare
from split_data import split_dataset
from log_reg import log_reg_model
from confusion_mat import confusion_matrix
import numpy as np

def solution(df, cols):
    '''Computes the F1 score and returns the threshold with maximum F1'''

    df_prepared = prepare(df)
    df_train, df_val, df_test, y_train, y_val, y_test = split_dataset(df_prepared)
    y_pred = log_reg_model(cols, df_train, df_val, y_train, y_val)

    thresholds = np.linspace(0, 1, 101)
    df_scores = confusion_matrix(cols, thresholds, y_val, y_pred)

    def calculate_F1(df):
        F1_scores = {}
        for row in df.itertuples():
            F1 = (2 * row[2] * row[3]) / (row[2] + row[3])
            F1_scores[row[1]] = F1
        max_tol = np.round(max(F1_scores, key=F1_scores.get), 1)
        max_F1 = np.round(F1_scores[max_tol], 3)
        ans = 'A threshold of {} yields the highest F1 score with {}'.format(max_tol, max_F1)
        return ans

    F1_df = df_scores[['threshold', 'precision', 'recall']]
    return calculate_F1(F1_df)