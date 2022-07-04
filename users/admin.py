#django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
#admin.site.register(Profile) #Se puede registrar de esta manera

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = ('pk','user','phone','website','picture')
    list_display_links = ('pk','user')
    #list_editable=('phone','website','picture')
    search_fields = ('user__email','user__first_name','user__last_name','phone')
    list_filter = ('created','modified','user__is_active','user__is_staff')
    fieldsets = (
        ('Profile',{
            'fields':('user','picture')

        }),
        ('Extra info',{
            'fields':(
             ('website','phone'),
             ('biography'),
            )
        }),
        ('Fechas',{
            'fields':('created','modified'),
        }),
        )
    
    readonly_fields = ('created','modified')

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for Users."""
    model = Profile
    can_delete = False
    verbose_name = "Profiles"

class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display=(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)