from collections import OrderedDict

from django.shortcuts import render, render_to_response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from models import Person, Institution, InstitutionType, Affiliation, Relationship, Payment
from serializers import PersonSerializer, InstitutionSerializer, AffiliationSerializer, RelationshipSerializer
from itertools import groupby
import itertools
from django.db.models import Q

def d3(request):
    return render_to_response('d3cd .html')


def Table(request, table_name):
    c = {'table_name': table_name}
    return render_to_response('people_table.html', c)

class ListPeople(APIView):
    """
    View to list all people.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        people = [person for person in Person.objects.all()]
        serializer = PersonSerializer(people, many=True)
        s = PersonSerializer()
        return Response({'columns':s.get_slick_columns(), 'rows':serializer.data})

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print serializer.error_messages
            print serializer.errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        person = Person.objects.get(id=request.data['id'])
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print serializer.error_messages
            print serializer.errors
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class ListInstitutions(APIView):
    """
    View to list all institutions.
    """
    def get(self, request, format=None):
        """
        Return a list of all institutions.
        """
        institutions = [institution for institution in Institution.objects.all()]
        serializer = InstitutionSerializer(institutions, many=True)
        s = InstitutionSerializer()
        return Response({'columns':s.get_slick_columns(), 'rows':serializer.data})

    def post(self, request):
        serializer = InstitutionSerializer(data=request.data)
        print request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print serializer.error_messages
            print serializer.errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        institution = Institution.objects.get(id=request.data['id'])
        serializer = InstitutionSerializer(institution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print serializer.error_messages
            print serializer.errors
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class ListAffiliations(APIView):
    """
    View to list all institutions.
    """
    def get(self, request, format=None):
        """
        Return a list of all institutions.
        """
        affiliations = [affiliation for affiliation in Affiliation.objects.all()]
        serializer = AffiliationSerializer(affiliations, many=True)
        s = AffiliationSerializer()
        return Response({'columns':s.get_slick_columns(), 'rows':serializer.data})


class ListRelationship(APIView):
    """
    View to list all institutions.
    """
    def get(self, request, format=None):
        """
        Return a list of all institutions.
        """

        relationships = [relationship for relationship in Relationship.objects.all()]
        serializer = AffiliationSerializer(relationships, many=True)
        s = RelationshipSerializer()
        return Response({'columns':s.get_slick_columns(), 'rows':serializer.data})


def InstitutionReport(request, id):
    print id
    root_institutions = list(Institution.objects.filter(root_institution__id=1)) + list(Institution.objects.filter(root_institution=None))
    Q(recipient__root_parent__id=id) | Q(recipient_id=id)

    ids = [x.id for x in Institution.objects.filter(root_institution=id)]
    ids.append(id)
    payments = Payment.objects.filter(recipient_id__in=ids).order_by('year', 'donor__name', 'recipient__name').\
        prefetch_related('donor', 'recipient')
    groupfunc = lambda x: x.year.strftime('%Y') + x.donor.name + x.recipient.name
    groups = []
    unique_keys = []
    a = sorted(payments, key=groupfunc)

    print type(id)
    for k, g in groupby(a, groupfunc):
        groups.append(list(g))
        unique_keys.append(k)
    results = [(sum([payment.amount for payment in g]), g[0].year.strftime('%Y'), g[0].recipient, g[0].donor) for g in groups]
    return render_to_response('institution_report.html', {'results':results, 'root_institutions':root_institutions, 'selected':int(id)})

def InstitutionDonorsAndPeopleByYear(request, id):
    root_institutions = list(Institution.objects.filter(Q(root_institution__id=1) | Q(root_institution=None)).order_by("name"))

    ids = [x.id for x in Institution.objects.filter(root_institution=id)]
    ids.append(id)
    payments = Payment.objects.filter(recipient_id__in=ids).order_by('year', 'donor__name', 'recipient__name').\
        prefetch_related('donor', 'recipient')
    groupfunc = lambda x: x.year.strftime('%Y') + x.donor.name
    groups = []
    unique_keys = []
    a = sorted(payments, key=groupfunc)

    for k, g in groupby(a, groupfunc):
        groups.append(list(g))
        unique_keys.append(k)
    results = [(len(g), sum([payment.amount for payment in g]), g[0].year.year, g[0].recipient, g[0].donor) for g in groups]
    years = {}
    payment_years = list(set([x.year.year for x in payments]))
    affiliations = Affiliation.objects.filter(institution_id__in=ids).prefetch_related('institution', 'person')
    affiliation_years = list(itertools.chain.from_iterable([(a.start_date.year, a.end_date.year) for a in affiliations]))
    years_list = payment_years + affiliation_years
    for x in xrange(min(years_list), max(years_list) + 1):
        years[x] = {"payments":[], "affiliations":[]}
    for payment in results:
        years[payment[2]]["payments"].append(payment)
    for a in affiliations:
        for x in xrange(a.start_date.year, a.end_date.year + 1):
            years[x]["affiliations"].append(a)
    return render_to_response('institution_report_2.html', {'years':years, 'root_institutions':root_institutions, 'selected':int(id)})

def PersonReport(request, id):
    person = Person.objects.get(id=id)
    affiliations = Affiliation.objects.filter(person=person).exclude(start_date=None).exclude(end_date=None).order_by("start_date", "primary")

    start_year = min([x.start_date.year for x in affiliations])
    end_year = max([x.end_date.year for x in affiliations])

    yearlyAffiliations = OrderedDict()
    for x in xrange(start_year, end_year + 1):
        yearlyAffiliations[x] = [aff for aff in affiliations if x >= aff.start_date.year and x <= aff.end_date.year]

    return render_to_response('person_report.html', {'yearlyAffiliations':yearlyAffiliations.iteritems()})