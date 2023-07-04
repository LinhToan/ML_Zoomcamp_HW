#!/usr/bin/env python
# coding: utf-8

import pickle

# You can use the following to save your model:
# output_file = f'model_C={C}.bin'
# with open(output_file, 'wb') as f_out:
#     pickle.dump((dv, model), f_out)

def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

def solution(model_file, dv_file, client):

    model = load(model_file)
    dv = load(dv_file)

    X = dv.transform([client])

    return round(model.predict_proba(X)[0,1], 3)

# client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
# model_file = 'model1.bin'
# dv_file = 'dv.bin'
# print(solution(model_file, dv_file, client))