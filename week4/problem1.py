# Question 1: For each numerical variable, use it as score and compute the AUC with the 'card' variable.
# Use the training dataset. If your AUC < 0.5, negate it. Which numerical variable has the highest AUC?
# - reports
# - dependents
# - active
# - share

from prepare_data import prepare
from split_data import split_dataset
from sklearn.metrics import roc_auc_score

def solution(df, tol):
    ''' Computes AUC with the 'card' variable for each numerical variable.'''

    df_prepared = prepare(df)
    df_train, df_val, df_test, y_train, y_val, y_test = split_dataset(df_prepared)
    numerical_columns = list(df_train.dtypes[df_train.dtypes != 'object'].index)

    def compare_auc(tol, cols):
        auc_dict = {}
        choices = ['reports', 'dependents', 'active', 'share']
        for c in cols:
            auc = roc_auc_score(y_train, df_train[c])
            if auc < tol:
                auc = roc_auc_score(y_train, -df_train[c])
            # print(f'The feature {c} yields an AUC of {auc.round(3)}')
            if c in choices:
                auc_dict[c] = auc
        
        max_key = max(auc_dict, key=auc_dict.get)
        max_value = auc_dict[max_key].round(3)
        ans = 'Out of the choices given, {} yields the highest AUC score with {}'.format(max_key, max_value)
        # Out of the choices given, share yields the highest AUC score with 0.989
        return ans

    return compare_auc(tol, numerical_columns)