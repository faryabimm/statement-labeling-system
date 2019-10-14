# statement-labeling-system
A responsive dataset crowd-labeling system

#### installation

```bash
sudo apt install sudo apt install libpq-dev python3-dev
virtualenv .venv --python=python3.7
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

# create a superuser interactively
python manage.py createsuperuser

# import dataset in .TXT format
python manage.py import_statements dataset.txt

# run the server
python manage.py runserver
```

#### current functionality
+ multi-level dataset labeling (user, label, time it took the user to label)
+ create account, login, logout functionality
+ responsive design

####\#TODO
+ ~~gain feedback and apply necessary changes~~
+ ~~add postgresql database compatibility~~
+ ~~deliver production settings~~
+ ~~admin command to~~ `export_labeled_dataset` 
