from ..shinkenconfig import ConfigObject

def generate_hostgroups_config(project_name, instances, config_objects):
    co = ConfigObject('hostgroup')
    co.properties['hostgroup_name'] = project_name
    co.properties['alias'] = project_name
    return co
