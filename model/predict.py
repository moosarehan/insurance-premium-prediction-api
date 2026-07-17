
import pickle
import pandas as pd

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION='1.0.0'
class_labels = model.classes_.tolist()
def predict_output(userinput:dict):
    input_df=pd.DataFrame([userinput])
    prediction = model.predict(input_df)[0]
    probabilities=model.predict_proba(input_df)[0]
    confidence=max(probabilities)
    class_probs=dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))
    return {
        'predicted_category':prediction,
        'confidence':round(confidence,4),
        'class_probabilities':class_probs
    }
