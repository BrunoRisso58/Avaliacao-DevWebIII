from django.test import TestCase
from django.urls import reverse
from .models import PresenceModel
from .forms import PresenceForm
from .views import presentStudents

class PresenceTestCase(TestCase):
    def test_presence_creation(self):
        student_name = 'Bruno R.'
        professor_name = 'Orlando'
        presence = PresenceModel.objects.create(student_name=student_name, professor_name=professor_name)
        self.assertEqual(presence.student_name, student_name)
        self.assertEqual(presence.professor_name, professor_name)

    def test_presence_list_view(self):
        student1 = PresenceModel.objects.create(student_name='Bruno R.', professor_name='Orlando')
        student2 = PresenceModel.objects.create(student_name='R. Bruno', professor_name='Thiago')

        url = reverse(presentStudents)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, student1.student_name)
        self.assertContains(response, student2.student_name)

    def test_presence_form_valid(self):
        form_data = {'student_name': 'Bruno R', 'professor_name': 'Orlando'}
        form = PresenceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_presence_form_invalid(self):
        form_data = {'student_name': '', 'professor_name': ''}
        form = PresenceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('student_name', form.errors)
        self.assertIn('professor_name', form.errors)
