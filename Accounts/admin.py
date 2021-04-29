from django.contrib import admin
from .models import CustomUser,Feedback,Subscription
admin.site.register(CustomUser)

class AdminFeedback(admin.ModelAdmin):
    list_display=['Name','Email','Phone','Message']

class AdminSubscription(admin.ModelAdmin):
    list_display=['Email']


admin.site.register(Feedback,AdminFeedback)


admin.site.register(Subscription,AdminSubscription)