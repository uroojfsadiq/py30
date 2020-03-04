from django.contrib import admin
from .models import Achievement, Testimonial

class AchievementAdmin(admin.ModelAdmin):
   list_display = ('caption', 'count')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'testi')


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Testimonial, TestimonialAdmin)