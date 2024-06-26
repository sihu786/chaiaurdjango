from django.contrib import admin
from .models import chaiVarity,ChaiReview,Store,ChaiCertificate
from .models import About,Skill,Resume,Socalmedia
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display=('name','type','date_add')
    inlines=[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varietes',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    
    list_display=('chai', 'certificate_number')










admin.site.register(chaiVarity,ChaiVarityAdmin)

admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Resume)
admin.site.register(Socalmedia)