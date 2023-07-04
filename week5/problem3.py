#!/usr/bin/env python
# coding: utf-8

import pickle

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

def solution(model_file, dv_file, client):

    model = load(model_file)
    dv = load(dv_file)

    X = dv.transform([client])
    y_pred = round(model.predict_proba(X)[0,1], 3)
    return y_pred