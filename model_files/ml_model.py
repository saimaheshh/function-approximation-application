
import numpy as np
import pandas as pd



def preprocess(a):
    in_pro = np.array([a]).reshape(-1,1)
    return in_pro


def predict_val(val, model):   
    
    preproc_val = preprocess(val)
   
    y_pred = model.predict(preproc_val)
    return y_pred