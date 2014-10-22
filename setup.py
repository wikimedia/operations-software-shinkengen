from setuptools import setup

setup(
    name="shinkengen",
    version='0.1',
    author="Yuvi Panda",
    author_email="yuvipanda@gmail.com",
    description=("A shinken config generator for Wikimedia Labs"),
    license="Apache2",
    url="https://gerrit.wikimedia.org/r/#/admin/projects/operations/software/shinkengen",
    packages=['shingen'],
    scripts=['scripts/shingen'],
    install_requires=[
        'jinja2',
        'pyyaml',
    ],
)
