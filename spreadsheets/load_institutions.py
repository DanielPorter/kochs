import xlrd
import datetime
from tentacles.models import Affiliation, Person, Institution, AffiliationType, InstitutionType, Payment, PaymentType
from django.db import transaction
book = xlrd.open_workbook('spreadsheets/institutions.xlsx')
sheet = book.sheet_by_name('Sheet1')
with transaction.atomic():
    for i in xrange(2, sheet.nrows):
        row = sheet.row(i)
        name = row[0].value
        inst_type, created = InstitutionType.objects.get_or_create(name=row[1].value)
        print row[2].value
        if row[2] != '':
            parent, created = Institution.objects.get_or_create(name=row[2].value)
        else:
            parent = None
        country = row[3].value
        state = row[4].value
        public_or_private = row[5].value
        notes = row[6].value
        print i

        inst, created = Institution.objects.get_or_create(name=name)
        inst.name=name
        inst.institution_type=inst_type
        inst.parent = parent
        inst.country = country
        inst.state = state
        inst.notes = notes
        inst.public_or_private = public_or_private
        inst.save()
