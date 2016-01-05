from django.contrib import admin
# Register your models here.
from models import Person, Institution, InstitutionType, Paper, PaymentType, Payment, Affiliation, RelationshipTypes, Relationship, AffiliationType
from models import ResearchDiscipline

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)


class InstitutionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Institution, InstitutionAdmin)


class InstitutionTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(InstitutionType, InstitutionTypeAdmin)


class PaperAdmin(admin.ModelAdmin):
    pass
admin.site.register(Paper, PaperAdmin)


class PaymentTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(PaymentType, PaymentTypeAdmin)


class PaymentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Payment, PaymentAdmin)


class AffiliationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Affiliation, AffiliationAdmin)

class RelationshipTypesAdmin(admin.ModelAdmin):
    pass
admin.site.register(RelationshipTypes, RelationshipTypesAdmin)
class RelationshipAdmin(admin.ModelAdmin):
    pass
admin.site.register(Relationship, RelationshipAdmin)

admin.site.register(AffiliationType)

admin.site.register(ResearchDiscipline)