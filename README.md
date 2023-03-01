## Machine_Learning_Project
This is my first end to end Machine Learning project

### Software and account requirement:
1. [Github Account](https://github.com/Rajendra9997/Machine_Learning_Project.git)
2. [Cloud Platform account](https://github.com/Rajendra9997/Machine_Learning_Project.git)
3. VS Code IDE
4. GIT Cli

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
1. RAILWAY_EMAIL:
2. RAILWAY_API_KEY:
3. RAILWAY_APP_NAME:

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
