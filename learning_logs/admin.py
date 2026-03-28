from django.contrib import admin

from .models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)

from .models import Topic

# Register your models here.

# admin.site.register(Topic)

