from django.contrib import admin
from .models import News
from .models import Category
from .models import Country

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Country)
# Register your models here.
