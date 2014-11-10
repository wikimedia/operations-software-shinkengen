from ..shinkenconfig import ConfigObject

def generate_host_config(config, project_name, instance):
    co = ConfigObject('host')
    co.properties['use'] = 'generic-host'
    co.properties['host_name'] = instance['name']
    co.properties['address'] = instance['ip'][0]
    projects = [project_name, config.get('default-hostgroup', 'labshost')]
    co.properties['hostgroups'] = ','.join(projects)
    co.properties['contact_groups'] = project_name
    return co
