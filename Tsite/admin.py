from django.contrib import admin
from .models import Student, Submissions, AnswersKey
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AcountAdmin(UserAdmin):
    list_display = ('email', 'username', 'usn', 'year', 'branch', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('usn',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(Student, AcountAdmin)
admin.site.register(Submissions)
admin.site.register(AnswersKey)
