## 프로젝트 실행하기(Windows)

> 가상환경 설치하기

    $ python -m venv venv

> 가상환경 실행하기

    $ source venv/bin/activate

> Django 설치하기

    $ pip install django

> 데이터베이스 적용하기 (manage.py 파일이 있는 곳에서 명령어 치기)

    $ python manage.py makemigrations
    $ python manage.py migrate

> admin에 접속했을때 사용할 슈퍼유저 만들기

    $ python manage.py createsuperuser

> 프로젝트 실행해보기

    $ python3 manage.py runserver

> 가상환경 종료하기

    $deactivate
