# Raspberry Works

Software for Think Tank Workspaces LLC

Raspberry Works is comprised of three applications: Members, Staff and Admin

Member is the member facing application. We consider members to be users with
active resources such as dedicated, desk, office, day use.  Staff is the application used by staff members to help with the overall management of the community.

Admin has absolute power to everything.

### Setup for new users

1. make sure you are in the right directory
2. git clone https://github.com/thecount12/thinktank.git
3. virtualenv -p /usr/local/bin/python3.7 ~/.thinktankvenv
4. source ~/.thinktankvenv/bin/activate
5. pip install -r requirements

### First Steps

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations

hopefully no bugs other then getboostrap templates

python manage.py createsuperuser
follow: prompts
### rachel's note
### setup basic project

1. create some test users
2. Go to member section and create resources
    * resources do not need start and stop date
3.  create member packages
4. create memberships.
