from ..shinkenconfig import ConfigObject

def generate_host_config(project_name, instance):
    co = ConfigObject('host')
    co.properties['use'] = 'generic-host'
    co.properties['host_name'] = instance['name']
    co.properties['address'] = instance['ip'][0]
    co.properties['hostgroups'] = project_name
    co.properties['contact_groups'] = project_name
    return co
