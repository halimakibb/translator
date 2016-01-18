from django.contrib import admin
from models import User, OriginalArticle, TranslatedArticle

admin.site.register(User)
admin.site.register(OriginalArticle)
admin.site.register(TranslatedArticle)

# Register your models here.
