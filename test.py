import skyapi
import unittest

configuration = skyapi.Configuration()
configuration.host = 'http://localhost:6420'
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))

class TestSum(unittest.TestCase):
    def test_version(self):
        """
        Test /api/v1/version
        """
        result = api_instance.version()
        
        self.assertEqual(result['branch'], 'v0.26.0')
        self.assertEqual(result['commit'], 'ff754084df0912bc0d151529e2893ca86618fb3f')
        self.assertEqual(result['version'], '0.26.0')

if __name__ == '__main__':
    unittest.main()

