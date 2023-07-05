import pickle
from flask import Flask
from flask import request
from flask import jsonify

def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

dv = load('./dv.bin')
model = load('./model2.bin')

def predict(dv, model, client):
    X = dv.transform([client])
    y_pred = round(model.predict_proba(X)[0, 1], 3)

    return y_pred

app = Flask('problem6')

@app.route('/problem6', methods=['POST'])
def solution():
    client = request.get_json()
 
    y_pred = predict(dv, model, client)

    result = {
        'credit_approval_probability': float(y_pred)
    }

    return jsonify(result)
    # should return a probability of 0.928

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)