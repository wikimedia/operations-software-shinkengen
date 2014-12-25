"""
Generator script that generates hosts and service configuration.

1. Checks config to figure out which projects to monitor
2. Fetches instance information from ldap
3. Generates hosts info and hostgroups info for the instances
"""
from ..ldapsource import LDAPSource


class GeneratorRunner():
    def __init__(self, config, instances_generator=None, hostgroups_generator=None):
        self.config = config
        self.instance_generator = instances_generator
        self.hostgroups_generator = hostgroups_generator

    def generate(self):
        ldapsource = LDAPSource(self.config['ldap']['server'],
                                self.config['ldap']['bindas'],
                                self.config['ldap']['password'])
        all_host_configs = []
        for project in self.config['projects']:
            instances = ldapsource.get_hostsinfo(project)
            host_configs = []
            for instance in instances:
                hostconfig = self.instance_generator(self.config, project, instance)
                host_configs.append(hostconfig)
            hosts_config_path = '%s/%s.cfg' % (
                self.config['base_path'], project
            )
            with open(hosts_config_path, 'w') as hostsfile:
                hostsfile.write('\n'.join([str(co) for co in host_configs]))
            all_host_configs += host_configs

        hostgroup_configs = self.hostgroups_generator(all_host_configs)
        hostgroups_config_path = '%s/hostgroups.cfg' % self.config['base_path']
        with open(hostgroups_config_path, 'w') as hostgroupsfile:
            hostgroupsfile.write('\n'.join([str(co) for co in hostgroup_configs]))
