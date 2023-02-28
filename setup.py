from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup function
PROJECT_NAME="Income-predictor"
PROJECT_VERSION="0.0.4"
PROJECT_AUTHOR="Rushikesh"
DESCRIPTION="This is end-to-end Machine Learning project \
    for Adult Census Income Prediction."
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_install_requirements()->List[str]:
    """
    Description :This is function returns requirements 
    given in requirement.txt file as list

    return: This function is going to return a list which
     contain name of libraries mentioned in requirement.txt
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
name= PROJECT_NAME,
version=PROJECT_VERSION,
author=PROJECT_AUTHOR,
description=DESCRIPTION,
packages=find_packages(), 
install_requires=get_install_requirements() 
)

