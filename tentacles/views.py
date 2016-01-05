from django.shortcuts import render, render_to_response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from models import Person, Institution, InstitutionType, Affiliation, Relationship
from serializers import PersonSerializer, InstitutionSerializer, AffiliationSerializer, RelationshipSerializer

def d3(request):
    return render_to_response('d3.html')


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