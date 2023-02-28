import os
import sys

from census.exception import CensusException
from census.util.util import load_object

import pandas as pd


class CensusData:

    def __init__(self,
                workclass : str,
                education : str,
                marital_status : str, 
                occupation  : str,
                relationship : str,
                race : str,
                sex : str,  
                country : str, 
                age : int,
                education_num : int, 
                hours_per_week : float,
                salary : str = None
                ):
        try:
            self.workclass = workclass
            self.education = education
            self.marital_status = marital_status
            self.occupation  = occupation
            self.relationship = relationship
            self.race = race
            self.sex = sex
            self.country = country 
            self.age = age
            self.education_num = education_num  
            self.hours_per_week = hours_per_week
            self.salary = salary        
        except Exception as e:
            raise CensusException(e, sys) from e

    def get_census_input_data_frame(self):

        try:
            census_input_dict = self.get_census_data_as_dict()
            return pd.DataFrame(census_input_dict)
        except Exception as e:
            raise CensusException(e, sys) from e

    def get_census_data_as_dict(self):
        try:
            input_data = {
                "workclass" : [self.workclass],
                "education" : [self.education],  
                "marital-status" : [self.marital_status],  
                "occupation"  : [self.occupation],
                "relationship" : [self.relationship],
                "race" : [self.race],
                "sex" : [self.sex],
                "country" : [self.country],
                "age" : [self.age],
                "education-num" : [self.education_num],  
                "hours-per-week" : [self.hours_per_week],
            }
            return input_data
        except Exception as e:
            raise CensusException(e, sys)


class CensusPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise CensusException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise CensusException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            census_income_class = model.predict(X)
            return census_income_class
        except Exception as e:
            raise CensusException(e, sys) from e