from django.contrib import admin
from .models import Member
from .models import Certification
from .models import Book

admin.site.register(Certification)
admin.site.register(Member)
admin.site.register(Book)
