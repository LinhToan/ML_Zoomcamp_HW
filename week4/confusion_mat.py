import pandas as pd

def confusion_matrix(cols, tols, y_val, y_pred):
    scores = []

    for t in tols:
        actual_pos = (y_val == 1)
        actual_neg = (y_val == 0)

        predict_pos = (y_pred >= t)
        predict_neg = (y_pred < t)

        tp = (predict_pos & actual_pos).sum()
        tn = (predict_neg & actual_neg).sum()

        fp = (predict_pos & actual_neg).sum()
        fn = (predict_neg & actual_pos).sum()

        scores.append((t, tp, fp, fn, tn))
        
    cols = ['threshold', 'tp', 'fp', 'fn', 'tn']
    df_scores = pd.DataFrame(scores, columns=cols)

    df_scores['precision'] = df_scores.tp / (df_scores.tp + df_scores.fp)
    df_scores['recall'] = df_scores.tp / (df_scores.tp + df_scores.fn)
        
    return df_scores
