import os
import yaml
from .generators.generator import GeneratorRunner
from .generators.hostgroups import generate_hostgroups_config
from .generators.hosts import generate_host_config

default_config = {
    'projects': ['tools'],
    'base_path': '.'
}
if os.path.exists('/etc/shinkengen.yaml'):
    config = yaml.load(open('/etc/shinkengen.yaml'))
else:
    config = default_config
gr = GeneratorRunner(config)
gr.register_instance_generator(generate_host_config)
gr.register_project_generator(generate_hostgroups_config)
gr.generate()
