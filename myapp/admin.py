from django.contrib import admin
from .models import Author, Book, Publisher, Library, Member

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Library)
admin.site.register(Member)

