import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)
## load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scaler=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict((new_data))
    print(output[0])
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)
"""{
	"data": {
		"CRIM": 0.07832,
		"ZN": 31.0,
		"INDUS": 1.31,
		"CHAS": 0.0,
		"NOX": 0.538,
		"RM": 6.575,
		"AGE": 65.2,
		"DIS": 4.0900,
		"RAD": 1.0,
		"TAX": 296,
		"PTRATIO": 15.3,
		"B": 396.90,
		"LSTAT": 4.98
	}
}"""