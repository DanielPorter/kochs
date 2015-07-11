import xlrd
import datetime
from tentacles.models import Affiliation, Person, Institution, AffiliationType, InstitutionType
from django.db import transaction
book = xlrd.open_workbook('affiliations1.xlsx')
sheet = book.sheet_by_name('Sheet1')
#[text:u'POI', text:u'Institution', text:u'Affiliation Type', text:u'Title', text:u'Start Date', text:u'End Date', text:u'Primary (True/False)', text:u'Note', text:u'Source']
print "okay!"
with transaction.atomic():
    for i in xrange(2, sheet.nrows):
        row = sheet.row(i)
        fname, lname = row[0].value.split(',')
        person, created = Person.objects.get_or_create(first_name=fname, last_name=lname)
        institution, created = Institution.objects.get_or_create(name=row[1].value)
        if row[2].value != '':
            inst_type, created = InstitutionType.objects.get_or_create(name=row[2].value)
            institution.institution_type = inst_type
            institution.save()
        affiliation_type = AffiliationType.objects.get_or_create(name=row[3].value)
        
        if row[6].value != '':
            start_date = datetime.datetime.strptime(str(int(row[5].value)), '%Y')
        else:
            start_date = None

        if row[6].value != '':
            end_date=datetime.datetime.strptime(str(int(row[6].value)), '%Y')
        else:
            end_date = None
        affiliation = Affiliation.objects.create(
                person=person, 
                institution=institution, 
                title=row[6].value,
                start_date=start_date,
                end_date=end_date,
                primary=bool(row[7].value)
                )
