from flask import Flask,render_template,request,jsonify
import pickle
from model_files.ml_model import predict_val

app = Flask('function')
model = pickle.load(open(".\model_files\model.pkl", 'rb'))

@app.route('/',methods=['GET'])
def Home(): 
  return render_template('gui.html')  

@app.route('/predict',methods = ['POST'])
def predict():
    
    if request.method == 'POST':
        val = float(request.form['Input'])
        
        
        predictions = predict_val(val, model)
        
        
        return jsonify(predictions[0])

    else:
        return render_template('gui.html')
    


    
    
    
if __name__ == '__main__':
    app.run(debug=True)