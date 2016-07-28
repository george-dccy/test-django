# test-django
test-driven web development with django

# 步骤记录
## first init test
- add functional_test.py
```python
from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:8000')

assert 'Django' in browser.title
```
- git
1. create new git repo: test-django
2. git clone in my workspace
```git
git clone https://github.com/george-dccy/test-django.git
```
- init django:
```python
cd test-django
django-admin.py startproject superlists
```
- run test
```python
cd superlists
python manage.py runserver
(another cmd window:)
python functional_test.py
```
3. git again
```git
git checkout -b textinit
mv functional_test.py test-django\superlists
echo db.sqlite3 >> .gitignore
echo __pycache__ >> .gitignore
echo *.pyc* >> .gitignore
git add .
git commit -m 'init django project and config, run the functional_test'
```