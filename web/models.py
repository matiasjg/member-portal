from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'joined_on', )

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'fee', )

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'member', 'created_at', )
