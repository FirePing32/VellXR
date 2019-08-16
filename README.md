# VellXR
[VellXR](https://vellxr.herokuapp.com) is a global forum for technology enthusiasts where they can write articles and collaborate with others.<br>
This is the source code of the entire website/web app along with [Sendgrid E-mail](https://github.com/prakhargurunani/VellXR#sendgrid-configuration) and [Cloudinary CDN](https://github.com/prakhargurunani/VellXR#cloudinary-configuration) configurations.<br>

## VirtualENV Setup

This is required to setup the dependencies for the app to start.<br>
Inside the project directory - <br>

* `virtualenv env`
  * `.\env\Scripts\activate` - For Windows users 
  * `source env/bin/activate` - For Linux/MacOS users
* `pip install -r requirements.txt`

## Setup local settings

The settings defined in the `vellxr/settings.py` is configured for _production only_ environments. To use locally - <br>

* Create a file named `local_settings.py` inside the `vellxr/` directory.
* put the following contents in it - 
  * ```python
    DEBUG = True
    SECURE_SSL_REDIRECT = False
    SECURE_PROXY_SSL_HEADER = None
    ```

## Initialize the app

Inside the same directory - <br>

* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py collectstatic`
* `python manage.py runserver 80`

This will start the server locally. Visit [http://localhost:80](http://localhost:80) or [http://127.0.0.1:80](http://127.0.0.1:80) to explore the app.

## Sendgrid E-mail Configuration

This feature will help in error reporting while the app is in production.
<br>
This is not necessary for the app to run properly. If you don't want to use this feature, simply comment out the code lines `42` to `53` in `settings.py`.

* `ADMIN_FULL_NAME` - full name on Sendgrid console
* `ADMIN_EMAIL_ID` - E-mail ID used to signup on Sendgrid
* `SENDGRID_API_KEY` - Sendgrid API key
* `MAILER_LIST` - list of users to send e-mail
* `DEFAULT_FROM_EMAIL` - E-mail ID used to signup on Sendgrid
* `EMAIL_HOST_USER` - Username on Sendgrid console
* `EMAIL_HOST_PASSWORD` - Password of Sendgrid account

## Cloudinary CDN Configuration

This is a necessary configuration as media files are no longer handled by Django. But still, if you want to continue with Django, Comment the lines `15` to `20` in `models.py` and follow [this](https://docs.djangoproject.com/en/2.2/topics/files/). <br>

* `CLOUDINARY_CLOUD_NAME` - Cloud name in Cloudinary console
* `CLOUDINARY_API_KEY` - Cloudinary API key
* `CLOUDINARY_API_SECRET` - Cloudinary API secret

### ___NOTE___

* Feel freely to open issues :smile:.
* The configuration for Heroku is still left to be added in the documentation. Contributing to this will be helpful.