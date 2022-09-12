DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangotest',  # database name
        'USER': 'dsem',     # 로그인-유저 명
        'PASSWORD': 'dsem',  # 로그인-비밀번호
        'HOST': '220.68.27.113',
        'PORT': '23307',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

SECRET_KEY = 'django-insecure-x2ld4+w+fx^+l-56md5%rn-ctj8-p%b2u)i66+9#l43u_5n$l2'
