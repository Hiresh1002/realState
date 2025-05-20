from django.apps import AppConfig

class SuperadminConfig(AppConfig):  # Class name can be CamelCase
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'superadmin'  # ✅ Must match the folder/module name
