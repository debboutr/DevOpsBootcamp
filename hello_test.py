import unittest
from app import app

class TestHello(unittest.TestCase):
    
    def setUp(self):
	self.client = app.test_client()

    def test_hello(self):
	test_url = '/hello/bob'
	expected_response = 'Hello, bob!'
	
	actual_response = self.client.get(test_url).data	

	assert expected_response == actual_response

if __name__=="__main__":
    unittest.main()
