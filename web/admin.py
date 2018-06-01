from django.contrib import admin
from core.models import Plan, Member, Payment
from web.models import MemberAdmin, PlanAdmin, PaymentAdmin

admin.site.register(Plan, PlanAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Payment, PaymentAdmin)

admin.site.site_header = "Membership Administrator";
admin.site.site_title = "Membership Administrator";
admin.site.empty_value_display = '(N/A)'
