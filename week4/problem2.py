# Question 2: What's the AUC of the logistic regression model on this validation dataset? Round to 3 digits:
# - 0.615
# - 0.515
# - 0.715
# - 0.995

from prepare_data import prepare
from split_data import split_dataset
from log_reg import log_reg_model
from sklearn.metrics import roc_auc_score

def solution(df):
    '''Calculates AUC of logistic regression model on validation dataset.'''

    cols = ["reports", "age", "income", "share", "expenditure", "dependents", "months", "majorcards", "active", "owner", "selfemp"]
    df_prepared = prepare(df)
    df_train, df_val, df_test, y_train, y_val, y_test = split_dataset(df_prepared)
    y_pred = log_reg_model(cols, df_train, df_val, y_train, y_val)

    return roc_auc_score(y_val, y_pred).round(3)
    # Our logistic regression model yields an ROC AUC score of 0.995
