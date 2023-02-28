from census.pipeline.pipeline import Pipeline
from census.logger import logging
from census.exception import CensusException
from census.config.configuration import Configuration
from census.component.data_transformation import DataTransformation
from census.util.util import read_yaml_file
import os, sys
def main():
    try:

        config_path = os.path.join("config","config.yaml")

        pipeline = Pipeline(Configuration(config_file_path=config_path))
        
        pipeline.start()
        logging.info(f"Main function execution completed.")
        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)
        #m  = read_yaml_file(file_path="E:\Machine_Learning_Project\config\schema.yaml")
        #print(m)
    
    except Exception as e:
        logging.error(f"{e}")
        raise CensusException(e,sys) from e
        print(e)

        
if __name__=="__main__":
    main()