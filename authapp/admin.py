from django.contrib import admin
from authapp.models import Contact
from authapp.models import Enrollment, MembershipPlan, Trainer ,Attendance,Gallery


admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Attendance)
admin.site.register(Gallery)



# Register your models here.
