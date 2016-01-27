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
        if row[3] != '':
            root, created = Institution.objects.get_or_create(name=row[3].value)
        else:
            root = None
        country = row[4].value
        state = row[5].value
        public_or_private = row[6].value
        notes = row[7].value
        print i

        inst, created = Institution.objects.get_or_create(name=name)
        inst.name=name
        inst.institution_type=inst_type
        inst.parent = parent
        inst.root_institution = root
        inst.country = country
        inst.state = state
        inst.notes = notes
        inst.public_or_private = public_or_private
        inst.save()
