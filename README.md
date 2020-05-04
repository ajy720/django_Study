# django_Study

### 다른 로컬에서 작업 할 때 설정

1. 가상환경 생성

   > python3 -m venv {가상환경 이름}

2. 패키지 설치

   > pip install {패키지 이름}

   1. django
   2. Pillow

3. DB 테이블 테이블 생성

   > python manage.py makemigrations **{앱 이름}**<br/>
   > python manage.py migrate

4. 어드민 계정 생성

   > python managy.py createsuperuser
