import yaml
from census.exception import CensusException
from census.constant import *
import os, sys
import pandas as pd
import numpy as np
import dill

def read_yaml_file(file_path:str)->str:
    """
    Read a YAML file and returns the content as dictionary 
    file path: str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CensusException(e,sys) from e

def write_yaml_file(file_path:str,data:dict=None):
    """
    Create yaml file 
    file_path: str
    data: dict
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path,"w") as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
    except Exception as e:
        raise CensusException(e,sys)

def load_data( data_file_path:str, schema_file_path:str) -> pd.DataFrame:
        try:
            dataset_schema = read_yaml_file(schema_file_path)

            schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]

            dataframe = pd.read_csv(data_file_path)

            error_message = ""

            for column in dataframe.columns:
                if column in list(schema.keys()):
                    dataframe[column].astype(schema[column])
                else:
                    error_message = (f"{error_message} \nColumn: {column} not present in schema")
            
            if len(error_message) > 0:
                raise Exception(error_message)
            return dataframe
        except Exception as e:
            raise CensusException(e, sys) from e
            
def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise CensusException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to loa
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj, allow_pickle=True)
    except Exception as e:
        raise CensusException(e, sys) from e

def save_object(file_path:str,obj):
    """
    file_path: str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CensusException(e,sys) from e


def load_object(file_path:str):
    """
    file_path: str
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CensusException(e,sys) from e
    
 
def replace_column_categories(data):
    try:
                    
        
        # replace categories in the marital-status column
        data['marital-status'] = data['marital-status'].replace([' Divorced',' Married-spouse-absent',' Never-married',' Separated',' Widowed'],' single')
        data['marital-status'] = data['marital-status'].replace([' Married-AF-spouse',' Married-civ-spouse'],' couple')

        # replace categories in the country column
        data.loc[data['country'] != ' United-States', 'country'] = ' Non-US'
        data.loc[data['country'] == ' United-States', 'country'] = ' US'
        
        # replace categories in the workclass column
        def replace_workclass_cat(data):
            if data['workclass'] == ' Federal-gov' or data['workclass']== ' Local-gov' or data['workclass']==' State-gov': return ' govt'
            elif data['workclass'] == ' Private':return ' private'
            elif data['workclass'] == ' Self-emp-inc' or data['workclass'] == ' Self-emp-not-inc': return ' self_employed'
            else: return 'without_pay'
        # replace categories in education column
        def replace_education_cat(data):
            if data['education'] == ' 10th' or data['education'] == ' 9th' or data['education'] == ' 7th-8th'  or data['education'] == ' 5th-6th'  or data['education'] == ' 1st-4th' or data['education'] == ' Preschool' or data['education'] == ' Prof-school' : return ' 10th_or_below'
            elif data['education'] == ' HS-grad' or data['education'] == ' 12th' or data['education'] == ' 11th':return ' HS-grad'
            elif data['education'] == ' Some-college' or data['education'] == ' Bachelors' :return ' Bachelors'
            elif data['education'] == ' Assoc-voc' or data['education'] == ' Assoc-acdm' :return ' Assoc-acdm_or_voc'
            elif data['education'] == ' Masters' or data['education'] == ' Doctorate' :return ' Masters_or_higher'
            else: pass

        data['workclass'] = data.apply(replace_workclass_cat, axis = 1)
        data['education'] = data.apply(replace_education_cat, axis = 1)

        data.drop(["fnlwgt","capital-gain","capital-loss"], axis = 1, inplace = True, errors = "raise")
        return data
        
    except Exception as e:
        raise CensusException(e,sys) from e


