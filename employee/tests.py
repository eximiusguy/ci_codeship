from django.test import TestCase
from employee.models import Employee
from django.http import HttpRequest
from employee.views import employee_registration, employee_listing
from django.core.urlresolvers import reverse


class EmployeeTestCase(TestCase):
    def setup(self):
        pass

    def test_employee_registration_landing_page(self):
        """Tests registration page is not giving error """
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_reg_page_title(self):
        request = HttpRequest()
        response = employee_registration(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Register employee</title>', response.content)

    def test_register_view_fails_blank(self):
        response = self.client.post(reverse('register'), {}) # blank data dictionary
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')

    def test_register_view_fails_email_blank(self):
        response = self.client.post(reverse('register'),
                                    {'first_name':'test1', 'last_name':'sample1', 'email':'',
                                     'website':'http://www.google.com'}) # blank email field
        self.assertFormError(response, 'form','email','This field is required.')

    def test_register_form_filled_pass(self):
        """If all fields are filled then test should pass and should redirect to user listing page"""
        response = self.client.post(reverse('register'),
            {'first_name':'john','last_name':'smith','email':'john@smith.com','website':'http://google.com'})
        self.assertRedirects(response, reverse('employee_list'))

    def test_employee_listing_page(self):
        """Tests employee list page not giving error"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_employee_list_title(self):
        request = HttpRequest()
        response = employee_listing(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<h2>Employee listing</h2>', response.content)