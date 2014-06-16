DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hireapp_db',
        'USER': 'hireapp',
        'PASSWORD': '9ijnnji9!3',
        'HOST': '',
        'PORT': '',
    }
}


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_port = 25
EMAIL_HOST_USER = 'info.hire.app@gmail.com'
EMAIL_HOST_PASSWORD = '9ijnnji9!3'
EMAIL_USE_TLS = True

ALLOWED_HOSTS = ['hireapp.co', 'www.hireapp.co']