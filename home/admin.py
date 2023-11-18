from django.contrib import admin
from .models import SignUp,FoodTips,Bmi,BloodPresure,Sugar,Update,FoodBlog,HealthBlog

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    list_display=('fname','uname','umail','pass1')
admin.site.register(SignUp,SignUpAdmin)

class FoodTipsAdmin(admin.ModelAdmin):
    list_display=('foodname','fooddescriptions')
admin.site.register(FoodTips,FoodTipsAdmin)

class BmiAdmin(admin.ModelAdmin):
    list_display=('bmitype','bmidescription')
admin.site.register(Bmi,BmiAdmin)

class BloodPresureAdmin(admin.ModelAdmin):
    list_display=('presuretype','presuredescription')
admin.site.register(BloodPresure,BloodPresureAdmin)

class SugarAdmin(admin.ModelAdmin):
    list_display=('sugartype','sugardescription')
admin.site.register(Sugar,SugarAdmin)

class UpdateAdmin(admin.ModelAdmin):
    list_display=('unamep','bmi','bp','bs')
admin.site.register(Update,UpdateAdmin)

class FoodBlogAdmin(admin.ModelAdmin):
    list_display=('title','description')
admin.site.register(FoodBlog,FoodBlogAdmin)

class HealthBlogAdmin(admin.ModelAdmin):
    list_display=('title','description')
admin.site.register(HealthBlog,HealthBlogAdmin)


