from setuptools import setup, find_packages

setup(
    name="shinkengen",
    version='0.3',
    author="Yuvi Panda",
    author_email="yuvipanda@gmail.com",
    description=("A shinken config generator for Wikimedia Labs"),
    license="Apache2",
    url="https://gerrit.wikimedia.org/r/#/admin/projects/operations/software/shinkengen",
    packages=find_packages(),
    scripts=['scripts/shingen'],
    install_requires=[
        'jinja2',
        'pyyaml',
        'python3-ldap'
    ],
)
