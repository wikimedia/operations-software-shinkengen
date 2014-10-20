from urllib.request import urlopen
import json
import codecs


class Wikitech():
    '''
    Represents a wikitech instance against which we can perform API queries
    '''
    def __init__(self):
        self.api_url = 'https://wikitech.wikimedia.org/w/api.php'

    def _fetch_json(self, url):
        '''
        Helper function to fetch JSON from a given URL

        :param url: URL to fetch. Must return JSON data in utf-8
        :return: The returned JSON parsed into appropriate python structures
        '''
        reader = codecs.getreader('utf-8')
        data = json.load(reader(urlopen(url)))
        return data

    def fetch_projects(self):
        '''
        Fetch all projects defined in Wikitech

        :return: List of project names defined in Wikitech
        '''
        url = '%s?action=query&list=novaprojects&format=json' % self.api_url
        data = self._fetch_json(url)
        return data['query']['novaprojects']

    def fetch_instances(self, project, region):
        '''
        Fetch all instances for a particular project in a particular region

        :param project: Name of project to fetch instances for
        :param region: Region to fetch instances of the project for. Eg. eqiad, codfw
        :return: A list of dicts containing instance info
        '''
        url = '%s?action=query&list=novainstances&niproject=%s&niregion=%s&format=json' % (
            self.api_url, project, region
        )
        data = self._fetch_json(url)
        return data['query']['novainstances']
