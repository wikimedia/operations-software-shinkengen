from ..shinkenconfig import ConfigObject

def generate_hostgroups_config(config_objects):
    hostgroup_names = set()
    hostgroups = set()

    for cob in config_objects:
        hostgroup_names = hostgroup_names.union(set(cob.properties.get('hostgroups', '').split(',')))

    for hostgroup_name in hostgroup_names:
        hostgroup = ConfigObject('hostgroup')
        hostgroup.properties['hostgroup_name'] = hostgroup_name
        hostgroup.properties['alias'] = hostgroup_name
        hostgroups.add(hostgroup)
    return hostgroups
