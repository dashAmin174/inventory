''' Developer : #ABS '''

from django.contrib import admin
from .models import user_accounts
'''
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_title', 'quantity', 'price', 'image', 'color')
    list_filter = ('user',)
    search_fields = ('user', 'product_title')
'''

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_login', 'phoneNumber', 'is_staff',)
    list_filter = ( 'email', 'is_superuser',  'is_staff',  'first_name',)
    search_fields = ('all',)


admin.site.register(user_accounts, AccountsAdmin)
