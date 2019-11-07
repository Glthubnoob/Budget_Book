from django.contrib import admin
from .models import Category, Document, Location, Position, Product, Unit

admin.site.register(Category)
admin.site.register(Document)
admin.site.register(Location)
admin.site.register(Position)
admin.site.register(Product)
admin.site.register(Unit)
