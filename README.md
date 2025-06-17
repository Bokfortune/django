# start
```
가상환경 생성
git clone https://github.com/sknetworks20250226/django.git .
pip install django
pyton manage.py migrate
django-admin createsuperuser  --> id / psw 설정
pyton manage.py runserver
localhost:8000/admin  --> 테스트용 question 데이터 생성
```

# 마이그레이션
```
model이 새로 생성되거나 변경된 경우 DB를 갱신해야 하는데,
makemigration -> migration 해서 반영한다.
```


