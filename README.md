

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

pip install django-mathfilters

pip install pandas

​ 

python manage.py makemigrations

python manage.py migrate

python manage.py runserver $IP:$PORT

​ 

push시 충돌이 날 경우

git pull  https://github.com/McDeepBook/DeepBook

git pull  https://github.com/ash92kr/likelion-team-project


git checkout -b about

git push origin about

git checkout master   # 입력 후 동일하게 add, commit, push를 입력한 다음, GUI로 merge 요청을 수락한다

​ 

git add .

git commim -m "  "

git remote add origin2  https://github.com/ash92kr/likelion-team-project

git push origin2 master

