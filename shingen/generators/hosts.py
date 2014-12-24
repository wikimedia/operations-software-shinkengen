from ..shinkenconfig import ConfigObject

def generate_host_config(config, project_name, instance):
    co = ConfigObject('host')
    co.properties['use'] = 'generic-host'
    co.properties['host_name'] = instance['name']
    co.properties['address'] = instance['ip']
    hostgroups = [project_name] + instance['puppetClasses']
    co.properties['hostgroups'] = ','.join(hostgroups)
    co.properties['contact_groups'] = project_name
    co.properties['notes'] = project_name  # Used for auto deriving graphite path
    return co
