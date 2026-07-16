from fastapi import FastAPI
import pickle
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated


with open('model.pkl','rb') as f:
    pickle.load(f)

app=FastAPI()

class userinput(BaseModel):
      age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
      weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
      height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
      income_lpa: Annotated[float, Field(..., gt=0, description='Annual salary of the user in lpa')]
      smoker: Annotated[bool, Field(..., description='Is user a smoker')]
      city: Annotated[str, Field(..., description='The city that the user belongs to')]
      occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
     

