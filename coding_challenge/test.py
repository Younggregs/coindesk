## Tests can be run from the root directory using the command below:
## ./manage.py test coding_challenge.test

from django.test import TestCase
from challenge.schema import Query

class CoindDeskTestCase(TestCase):
    def setUp(self):
       pass

    def test_calculate_price(self):
        """Testing calculatePrice without Test Cases"""
        ## Test if result returned by test case is Valid
        self.assertIsNotNone(Query.resolve_calculatePrice('request', 'info', 'buy', 0.2, 350.0))
        
        ##Test if result returned by test case is True
        self.assertTrue(Query.resolve_calculatePrice('request', 'info', 'buy', 0.2, 350.0))


    def tearDown(self):
        pass