from django.db import models
from django.utils.translation import ugettext as _


class Patient(models.Model):
    '''
    Information on a patient
    '''
    patient_id = models.CharField(max_length=40)

    gender = models.CharField(max_length=40)

    date_of_birth = models.DateTimeField('Date of Birth')

    patient_race = models.CharField(max_length=40)

    patient_language = models.CharField(max_length=40)

    # def __str__(self):
    #     return "Patient " + str(patient_id)

class PatientVisit(models.Model):
    '''
    Class details the results of a patient visit
    '''
    patient = models.CharField(max_length=40)

    admission_id = models.IntegerField()

    admission_start_date = models.DateTimeField('Date patient entered medical facility')

    admission_end_date = models.DateTimeField('Date patient left medical facility')

    # def __str__(self):
    #     return "Patient " + str(patient_id) + " visit on " + str(admission_start_date)
