from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.userinput import UserInput
from model.predict import predict_output,model
from model.predict import MODEL_VERSION
from schema.prediction_response import PredictionResponse
app = FastAPI()


@app.get('/')
def welcome():
    return{'messsage':'Welcome to Insurance premium prediction API'}

@app.get('/healthcheck')
def health():
    return{
        'status':'Ok',
        'model version':MODEL_VERSION
    }
@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):
    user_input= {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    # 1. Get prediction
    try:
        prediction=predict_output(user_input)
        return JSONResponse(status_code=200, content=prediction)
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
   


   