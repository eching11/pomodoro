from django.contrib import admin

# Register your models here.
from .models import Category, Pomodoro

#admin.site.register(User)
#admin.site.register(Category)
#admin.site.register(Pomodoro)

# Define the admin class
# Django tutorial: 
#    Book === Category
#    BookInstance === Pomodoro

#class UserAdmin(admin.ModelAdmin):
#    list_display = ('username', 'verified', 'userID') 

# Register the admin class with the associated model
#admin.site.register(User, UserAdmin)


# Register the Admin classes for Category using the decorator
#@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'categoryID') # 'userID', 'categoryURL')
    exclude = ['categoryID']
# Register the admin class with the associated model
admin.site.register(Category, CategoryAdmin)

# Register the Admin classes for Pomodoro using the decorator
@admin.register(Pomodoro)
class PomodoroAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'minutes', 'id', 'categoryID') #'categoryID', 'minutes')
    list_filter = ('day_of_week', 'time_of_day')
    
    fieldsets = (
        (None, {
            'fields': ['task_name']
            }),
        ('Date Stats', {
            'fields': ('time_of_day', 'day_of_week')
            }),
    )
    exclude = ['categoryID', 'id']