from django.contrib.messages import constants

# Adiciona classes do Bootstrap nas mensagens do Django
MESSAGE_TAGS = {
    constants.DEBUG: 'alert alert-primary user-select-none',
    constants.ERROR: 'alert alert-danger user-select-none',
    constants.INFO: 'alert alert-info user-select-none',
    constants.SUCCESS: 'alert alert-success user-select-none',
    constants.WARNING: 'alert alert-warning user-select-none',
}
