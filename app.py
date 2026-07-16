from fastapi import FastAPI
import pickle
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated


with open('model.pkl','rb') as f:
    pickle.load(f)

app=FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

class userinput(BaseModel):
      age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
      weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
      height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
      income_lpa: Annotated[float, Field(..., gt=0, description='Annual salary of the user in lpa')]
      smoker: Annotated[bool, Field(..., description='Is user a smoker')]
      city: Annotated[str, Field(..., description='The city that the user belongs to')]
      occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
      
      @computed_field
      @property
      def bmi(self)->float:
           return self.weight/(self.height)**2
      

      @computed_field
      @property
      def lifestyle_risk(self)->str:
           if self.bmi and self.smoker >30:
                return 'high'
           elif self.bmi and self.smoker >27:
                return 'medium'
           else:
                return 'low'
      @computed_field
      @property
      def age_group(self)->str:
           if self.age < 25:
                return 'young'
           elif self.age < 45:
                return 'adult'
           elif self.age < 65:
                return 'middle aged'
           return 'senior'
      @computed_field
      @property
      def 
           
                
                


            
      
    


     

