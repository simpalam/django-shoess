from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from .models import *

# Register your models here.
User = get_user_model()

# user model registered here


@admin.register(User)
class UserInAdmin(UserAdmin):
    """ All User Admin Model (Include Super User) """
    # The forms to add and change user instances
 
    search_fields = ['email']
    list_display = ['email', 'is_admin', 'is_staff', 'is_active']
    list_filter = [ 'is_admin', 'is_staff',
                   'is_active']
    
    # readonly_fields = ('created_at', 'updated_at', 'last_login')
    #inlines = [UserCompanyInline]
 
   
    # ordering = ('email',)
    # filter_horizontal = ()

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    readonly_fields =['view_image']
    
    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.url.url,
            width='350px',
            height='300px',
            )
         )
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    readonly_fields =['view_image']
    
    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width='350px',
            height='300px',
            )
         )
    

@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
