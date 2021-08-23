# login-django

configurações a serem feitas no arquivo settings.py

SECRET_KEY = 'insira sua secret key aqui'



# PARA UTILIZAR COM GMAIL.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu email'
EMAIL_HOST_PASSWORD = 'sua senha'



# PARA UTILIZAR COM MAILGUN
# LEMBRE-SE DE INSTALAR O DJANGO-ANYMAIL

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'email que ira aparecer na mensagem'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ANYMAIL = {
    "MAILGUN_API_KEY":" sua api_key aqui ",
    "MAILGUN_SENDER_DOMAIN":" seu sender domain aqui ",
} 