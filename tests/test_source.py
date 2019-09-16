import unittest
from app.models import Source,Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1234,'igihe','graduation at moringa','https://igihe.com','entertainment','English','Rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

