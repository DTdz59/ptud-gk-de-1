# ptud-gk-de-1
### Phạm Duy Thông- 22664351
- bước 1 tạo môi trường
+ python version 3.11
+ python -m venv myenv
+ myenv\Scripts\activate
+ django-admin startproject GK_PTUD
+ django-admin startapp app
- bước 2 cài đặt thư viện
+ pip install -r requirements
- bước 3 cài đặt database và đồng bộ với models.py
+ python manage.py migrate
+ python manage.py makemigrations
- tạo admin
+ python manage.py createsuperuser
- chạy 
+ python manage.py runserver
