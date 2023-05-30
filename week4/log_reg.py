from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

def log_reg_model(columns, df_train, df_val, y_train, y_val):

    dv = DictVectorizer(sparse=False)

    train_dict = df_train[columns].to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)

    model = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000)
    model.fit(X_train, y_train)

    val_dict = df_val[columns].to_dict(orient='records')
    X_val = dv.transform(val_dict)

    y_pred = model.predict_proba(X_val)[:, 1]

    return y_pred