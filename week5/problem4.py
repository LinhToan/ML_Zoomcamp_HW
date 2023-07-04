import pickle
from flask import Flask
from flask import request
from flask import jsonify

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

app = Flask('problem4')

def predict(model_file, dv_file, client):
    model = load(model_file)
    dv = load(dv_file)

    X = dv.transform([client])
    y_pred = round(model.predict_proba(X)[0,1], 3)

    return y_pred

@app.route('/problem4', methods=['POST'])
def solution(model_file, dv_file, client):

    client = request.get_json()

    y_pred = predict(model_file, dv_file, client)

    result = {
        "credit approval probability": float(y_pred)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)