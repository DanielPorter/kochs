__author__ = 'daniel'
from rest_framework import serializers
from models import Person, InstitutionType, Institution, Affiliation, Relationship


class BaseSlickSerializer(serializers.ModelSerializer):
    def get_slick_columns(self):
        fields = self.get_fields()
        cols = []
        for key in fields:
            field_type = fields[key].__repr__().split('Field')[0]
            cols.append({'name':key, 'id':key, 'field':key, 'type':field_type})
        return cols


class PersonSerializer(BaseSlickSerializer):
    birthday = serializers.DateField(format="%m/%d/%Y", required=False)
    class Meta:
        model = Person


class InstitutionTypeSerializer(BaseSlickSerializer):
    class Meta:
        model = InstitutionType


class InstitutionSerializer(BaseSlickSerializer):
    institution_type = serializers.CharField(required=False)
    class Meta:
        model = Institution

    def create(self, validated_data):
        try:
            inst_type, created = InstitutionType.objects.get_or_create(name=validated_data["institution_type"])
            validated_data["institution_type"] = inst_type
        except KeyError:
            pass
        return Institution.objects.create(**validated_data)

    def update(self, instance, validated_data):
        try:
            inst_type, created = InstitutionType.objects.get_or_create(name=validated_data["institution_type"])
            validated_data["institution_type"] = inst_type
        except KeyError:
            pass
        return super(InstitutionSerializer, self).update(instance, validated_data)

class AffiliationSerializer(BaseSlickSerializer):
    class Meta:
        model = Affiliation

class RelationshipSerializer(BaseSlickSerializer):
    class Meta:
        model = Relationship