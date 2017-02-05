from django.db import models
from django.utils.translation import ugettext as _


class Patient(models.Model):
	'''
        Information on a patient
	'''

	first_name = models.CharField(
        _('First Name'),
        max_length=255,
        blank=False,
        help_text=_('First Name of the patient (including middle name)'))

	last_name = models.CharField(
        _('Last Name'),
        max_length=255,
        blank=True,
        help_text=_('Last name of the patient'))

	birth_date = models.DateField(
		_('Date of Birth'),
		blank=False,
		null=True,
		help_text=_('Patient Date of birth'))

	full_address = models.CharField(
        _('First Address'),
        max_length=255,
        blank=False,
        help_text=_('Full Address of the patient'))

	city = models.CharField(
        _('City'),
        max_length=255,
        blank=False,
        help_text=_('City of the patient'))

	province = models.CharField(
        _('Province of residence'),
        max_length=255,
        blank=False,
        help_text=_('Province where the patient resides'))

	mobile_no = models.CharField(
        _('Mobile No'),
        max_length=10,
        blank=False,
        help_text=_('Mobile No of the patient'))

	landline_no = models.CharField(
        _('Landline No'),
        max_length=255,
        blank=True,
        help_text=_('Landline no of the patient'))

	email = models.EmailField(
		_('Email ID'),
		max_length=70,
		blank=True,
		null=True,
		help_text=_('Email ID of the patient'),)

	referred_by = models.CharField(
        _('Reffered By'),
        max_length=255,
        blank=True,
        help_text=_('Name of the Doctor who referred the patient, if applicable'))

	patient_since = models.DateTimeField(
        _("Date of patient's first visit"),
        help_text=_('When did the patient first visit the hospital'))

        # TODO
	def __str__(self):
		return

class PatientVisit
