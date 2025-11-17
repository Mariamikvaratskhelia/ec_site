from django.contrib import admin
from .models import Profile, Product, ProductHistory, Cart, CartItem, Payment, Comment, Rating

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(ProductHistory)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(Comment)
admin.site.register(Rating)