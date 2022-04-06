from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial


# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"
'''
@pytest.mark.django_db #this decorator is used to allow the test access to the connected database, wchih is required in this particular view
def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"
    BUT we will want to create more integration tests that require creating tutorial object, so we can convert the function
   above into a fixture as follows:
    '''
@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial
def test_search_tutorials(new_tutorial): #checks that the object created by fixture exists
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial): #updates title of new_tutorial object, saves update, asserts tutorial with updated name exists in db
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()
#having new_tutorial as a parameter causes the fixture to run before the tests
#In side the 2nd F(x) body, new_tutorial doesn't refer to fixture F(x), but to object returned from that fixture F(x)
      
