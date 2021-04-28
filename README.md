# MDM_dev
Mobile Device Management (MDM)
a web application to help manage, track and administer mobile devices in a corporate environment.
The Web app is built using  the django framework.
00

# How to set up Django
1. Create a virtual(Pipenv, virtualenv) environment to host the project.
2. From the root directory run `pip install -r requirements.txt` to install all dependencies.
    - django
    - pillow
    - django-crispy-forms
     
3. After installation of *requirements.txt* run `django-admin createproject`, register **admin** by filling in the needed details. 
4. From the terminal cd into **MDMproject** and run the follow command : `python manage.py makemigrations` press enter after
5. Run this command: `python manage.py migrate` and press enter

after performing the steps above run this command: `python manage.py runserver` to start the local built-in django webserver

# GitHub info

### How to clone the project
1. Form the pycharm new project window select **get from VCS**
2. Make sure you are logged into GitHub (check settings)
3. There several methods you can use to get the project:
- Git (CLI)
- Github Desktop app
- download zipped folder from GitHub
- Use Pycharm VCS options

### Commit, Pull, Push
1. The initial *pull* should be performed from the **main** branch
   - *never pull from dev_code*
2. *commit* and *push* new work to the **dev_code** branch
3. sign your code when you make commits
4. add clear comments to ur commits

# Task List
### Mncedisi
1. - [ ] Design logo
2. - [ ] Theme and color scheme
3. - [ ] Design bg img for landing page
4. - [ ] Design main bg of site

### Refilwe
1. - [ ] Fix profile page
2. - [ ] Fix text on login and register page

### Letlaka
1. - [x] Code forms to enroll devices
2. - [ ] Code Dashboard view
3. - [ ] Code dropdown for Dept, Phone Manu, Phone model
4. - [ ] Code inventory tab/page

### Tshepiso
1. - [ ] Find platform to host application

### Palesa
1. - [ ] Create project plan

# Helpful links

### Download / Install
If there is a need to manually install any of the dependencies links are below:
1. [Python](https://www.python.org/)
2. [Django](https://www.djangoproject.com/download/)
3. [Pillow](https://pypi.org/project/Pillow/)
4. [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
5. [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

### Documentation
1. [Python](https://docs.python.org/3/)
2. [Django](https://docs.djangoproject.com/en/3.2/)
3. [Pillow](https://pillow.readthedocs.io/en/stable/?badge=latest)
4. [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
5. [Pycharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)
