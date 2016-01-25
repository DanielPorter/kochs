from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    middle_name = models.CharField(blank=True,max_length=100)
    birthday = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.last_name + ", " + self.first_name


class ResearchDiscipline(models.Model):
    name = models.CharField(max_length=200)
    people = models.ManyToManyField(Person)

    def __unicode__(self):
        return self.name

class InstitutionType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=200, null=True)
    institution_type = models.ForeignKey(InstitutionType, null=True)
    parent = models.ForeignKey("Institution", related_name='inst_parent', null=True, blank=True)
    root_institution = models.ForeignKey("Institution", related_name="root_inst", null=True, blank=True)
    country = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    public_or_private = models.TextField(blank=True)
    site = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class AffiliationType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Affiliation(models.Model):
    person = models.ForeignKey(Person, related_name='person')
    institution = models.ForeignKey(Institution)
    affiliation_type = models.ForeignKey(AffiliationType, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    salary = models.FloatField(default=0)
    title = models.CharField(max_length=100)
    primary = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    source = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.title) + ", " + str(self.person) + " at " + str(self.institution)


class PaymentType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Payment(models.Model):
    donor = models.ForeignKey(Institution, related_name='donor')
    recipient = models.ForeignKey(Institution, related_name='recipient')
    amount = models.FloatField()
    payment_type = models.ForeignKey(PaymentType, blank=True, null=True)
    year = models.DateField(null=True)
    note = models.TextField(blank=True)
    source = models.TextField(blank=True)

    def __unicode__(self):
        return "%s to %s from %s" % (self.amount, self.recipient, self.donor)




class Paper(models.Model):
    title = models.CharField(default="",max_length=100)
    author = models.ForeignKey(Person, related_name='primary_author')
    secondary_authors = models.ManyToManyField(Person)

    def __unicode__(self):
        return str(self.title) + " by " + str(self.author)


class RelationshipTypes(models.Model):
    name = models.CharField(max_length=200)


class Relationship(models.Model):
    person_a = models.ForeignKey(Person, related_name='person_a')
    person_b = models.ForeignKey(Person, related_name='person_b')
    relationship_type = models.ForeignKey(RelationshipTypes)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __unicode__(self):
        return str(self.person_a) + " is " + self.relationship_type.name + " to " + str(self.person_b)
