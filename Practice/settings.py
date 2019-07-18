"""
Django settings for Practice project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '905@jd(r2&=r5d!8*um7or9&m(2xf&%s=$xr@p&+b^jogj#=vn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [          #ordering matters as django looks for files line by line. So if we put registration above new the files which we want to override from registration will never get priority. Files having same name will get priority as per order of installed apps
    # 'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',    #for social registration
    'New',  #we need to add entry for each app we created here
    'registration',      #it will activate registration redux app within django
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #for social registration
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Practice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #for social registration
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'Practice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#Registration
ACCOUNT_ACTIVATION_DAYS = 15        #No of days account activation will last. After that they wont be able to use their account
REGISTRATION_AUTO_LOGIN = True      #After registration, automatically login to account
INCLUDE_REGISTER_URL = True
LOGIN_REDIRECT_URL = '/New' #this defines where to redirect after user logged in
ACCOUNT_AUTHENTICATED_REGISTRATION_REDIRECTS = True       #if you dont put this line then we will get error page not found. but if you open same site in private mode then it will work fine


#Email Settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"   #address of gmail(smtp) server
EMAIL_HOST_USER = "bhupali.maheshwari@gmail.com"    #username used to connect with smtp account with
EMAIL_HOST_PASSWORD = "pakoda@22"
EMAIL_PORT = 587    #TLS port no
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "books@mysterybooks.com"     #this is email address from which it will show that email is send

#authentication backends:
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Add the Facebook app credentials.
SOCIAL_AUTH_GITHUB_KEY = '257b5dc305935ac9d940'
SOCIAL_AUTH_GITHUB_SECRET = '3ce5f736113d94d39779bf458841d8fd321ad205'


