import unittest
from shingen.shinkenconfig import ConfigObject


class ConfigObjectTests(unittest.TestCase):
    def test_output(self):
        obj = ConfigObject('contact')
        obj.properties['contact_name'] = 'Test Contact'
        obj.properties['alias'] = 'Yuvi Panda'
        output = '''define contact {
contact_name        Test Contact
alias        Yuvi Panda
}'''
        self.assertEqual(str(obj),output)


if __name__ == '__main__':
    unittest.main()
