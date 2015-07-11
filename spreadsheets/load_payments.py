import xlrd
import datetime
from tentacles.models import Affiliation, Person, Institution, AffiliationType, InstitutionType, Payment, PaymentType
from django.db import transaction
book = xlrd.open_workbook('spreadsheets/PAYMENTS.xlsx')
sheet = book.sheet_by_name('Sheet1')
with transaction.atomic():
    for i in xrange(2, sheet.nrows):
        row = sheet.row(i)
        if row[0].value != '':
            payment_type, created = PaymentType.objects.get_or_create(name=row[0].value)
        else:
            payment_type = None
        donor, created = Institution.objects.get_or_create(name=row[1].value)
        recipient, created = Institution.objects.get_or_create(name=row[2].value)
        amount = row[3].value
        if row[4].value != '':
            date = datetime.datetime.strptime(str(int(row[4].value)), '%Y')
        else:
            date = None
        notes = row[5].value
        source = row[6].value
        print i
        Payment.objects.create(
                donor=donor,
                recipient=recipient,
                amount=amount,
                payment_type=payment_type,
                note=notes,
                source=source,
                year=date
        )

