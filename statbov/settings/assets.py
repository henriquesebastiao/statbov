from .environment import BASE_DIR, DATA_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'statbov' / 'static']
STATIC_ROOT = DATA_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = DATA_DIR / 'media'
