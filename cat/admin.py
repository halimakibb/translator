from django.contrib import admin
from models import User, OriginalArticle, TranslatedArticle, Language

admin.site.register(User)
admin.site.register(OriginalArticle)
admin.site.register(TranslatedArticle)
admin.site.register(Language)

# Register your models here.
