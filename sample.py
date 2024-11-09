sudo apt-get install Docker

mkdir fapp2
touch app.py 

app.py
from flask import Flask
app=Flask(__name__)
@app.route('/')
def run():
    return "vicky punda"
app.run('0.0.0.0',5000)

touch Dockerfile

Dockerfile
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3","app.py"]


touch requirements.txt

requirements.txt
Flask==2.0.1
Werkzeug==2.0.1

docker build -t fapp2 .

docker run -p 5000:5000 fapp2


  SSH

ssh username@hostname_or_ip_address

If key pair not generated already

ssh-keygen 
ssh-copy-id username@hostname_or_ip_address
ssh username@hostname_or_ip_address
 


JENKINS

sudo apt-get install jenkins
sudo apt-get install fontconfig openjdk-17-jre (if Java doesnt exist)
