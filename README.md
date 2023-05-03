### Adult Census Income Prediction
The Adult Census Income Prediction project is a machine learning project that predicts an individual's income level based on their demographic and socioeconomic characteristics. The goal of this project is to develop a machine learning model that can accurately predict an individual's income level, i.e., whether they make less than or equal to $50,000 per year or more than $50,000 per year.

## Dataset
The project uses the Adult Census Income dataset, which contains demographic and socioeconomic characteristics of individuals, including age, education, occupation, marital status, and more. The dataset can be obtained from the UCI Machine Learning Repository or Kaggle.

## Solution
The proposed solution involves building a binary classification algorithm to predict an individual's income level. The solution includes the following steps:

1. Data preprocessing
2. Feature engineering
3. Model selection
4. Model training
5. Model evaluation
6. Model deployment
7. CI/CD pipelines
8. Requirements

## The project requires the following dependencies:
1. Python 3.x
2. Scikit-learn
3. Pandas
4. NumPy
5. Flask

## Usage
To run the project, follow these steps:

1. Clone the repository to your local machine
2. Install the required dependencies using pip install -r requirements.txt
3. Run the main.py file to preprocess the data, engineer features, select the best model train the model, and evaluate the model on the test set.
5. Deploy the model in a production environment.

## License
The project is licensed under the [Apache license](http://www.apache.org/licenses/).




### Software and account requirement:
1. [Github Account](https://github.com/Rajendra9997/Machine_Learning_Project.git)
2. [Railway account]
3. VS Code IDE
4. GIT Cli


## Useful Commands for extra knowledge
Create virtual environment
```
conda create -p venv python==3.7 -y
```

To activate virtuak environment
```
conda activate venv
```
or
```
conda activate venv/
```
To install all requirements from the requirements.txt file 
```
pip install requirements.txt
```
To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To check the version/commit alll changes by git
```
git commit -m " message"
```
To send or push version changes to git 
```
git push origin main
```

To check remote url
```
git remote -v
```

Requirements for app deployment on cloud flatform(Railway)
1. RAILWAY_TOKEN:

To build docker image
```
docker build -t <image_name>:<tag_name> location  # can use . as location for current location
```
Note : Image name should be lower case

To list docker images
```
docker images
```
To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_ID>
```
To check running container in docker
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```

To install all requirements and created packages using setup file
```
python setup.py install
```

To install ipykernal
'''
pip install ipykernal
'''
