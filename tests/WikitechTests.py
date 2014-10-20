import unittest
from shingen.wikitech import Wikitech


class WikitechTests(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.wikitech = Wikitech()

    def test_projects(self):
        projects = self.wikitech.fetch_projects()
        self.assertNotEqual(len(projects), 0)
        self.assertIn('tools', projects)

    def test_instances(self):
        tools_instances = self.wikitech.fetch_instances('tools', 'eqiad')
        self.assertNotEqual(len(tools_instances), 0)

if __name__ == '__main__':
    unittest.main()
