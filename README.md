# Shipment Dashboard


## Setting up the project
### Create virtualenv with python3
- `python3.9 -m venv <virtual env path>`
- `source <virtual env path>/bin/activate`

### Install Requirements
- `cd <project_root_directory>`
- `pip install -r requirements/base.txt`


### Database table creations\
- `cd <project_root_directory>`
- `./manage.py migrate`

### Running Backend
- Once the above steps are done, then server can be started anytime by running
- `./manage.py runserver`

