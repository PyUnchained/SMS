from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import unittest, timezone
from office.models import*

# Create your tests here.
class ModelsTestCase(TestCase):
	"""Tests that the custom methods on all of the models are working"""

	fixtures = ['testdata1.json']

	def test_id_generator(self):

		#Find current year, since the id is always linked to the year the
		#student is entered into the system.
		year = str(datetime.date.today().year)
		year = year[2:]

		#Correct id details
		resp = generateid('Percy','Nyoka','Musango')
		expected_answer = 'PNM'+ year + '23'
		self.assertEqual(resp, expected_answer)