

# cloud9 백업용 - 다운받고 bash 창에 아래처럼 입력할 것

​ 

​ 

git clone https://github.com/McDeepBook/DeepBook

​ 

pip install keras

pip install tensorflow

pip install django

pip install opencv_python

pip install django-imagekit   -> 문제가 생기면 uninstall하고 다시 설치

​ 

python manage.py makemigrations

python manage.py migrate

​ 

push시 충돌이 날 경우

git pull  https://github.com/McDeepBook/DeepBook

git pull  https://github.com/ash92kr/likelion-team-project

​ 

git add .

git commim -m "  "

git remote add origin2  https://github.com/ash92kr/likelion-team-project

git push origin2 master
