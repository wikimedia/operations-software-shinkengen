"""
Generator script that generates hosts and service configuration.

1. Checks config to figure out which projects to monitor
2. Fetches instance information from wikitech
3. Runs the instance info through a series of functions, which generate
   config objects for shinken
"""
from ..wikitech import Wikitech


class GeneratorRunner():
    def __init__(self, config):
        self.config = config
        self.instance_generators = []
        self.project_generators = []

    def register_instance_generator(self, func):
        self.instance_generators.append(func)

    def register_project_generator(self, func):
        self.project_generators.append(func)

    def generate(self):
        wikitech = Wikitech()
        for project in self.config['projects']:
            instances = wikitech.fetch_instances(project, 'eqiad')
            config_objects = []
            for instance in instances:
                for generator in self.instance_generators:
                    co = generator(project, instance)
                    config_objects.append(co)
            hosts_config_path = '%s/%s.cfg' % (
                self.config['base_path'], project
            )
            open(hosts_config_path, 'w').write('\n'.join([str(co) for co in config_objects]))

            project_cos = []
            for generator in self.project_generators:
                co = generator(project, instances, config_objects)
                project_cos.append(co)
            projects_config_path = '%s/project-%s.cfg' % (
                self.config['base_path'], project
            )
            open(projects_config_path, 'w').write('\n'.join([str(co) for co in project_cos]))



