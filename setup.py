from setuptools import find_packages, setup
from typing import List

_e_dot = '-e .'
def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [req.strip() for req in requirements]
    if _e_dot in requirements:
        requirements.remove(_e_dot)

    return requirements
setup( 
    name='MLProject',
    version='0.0.1',
    author='GaneshTodkari',
    author_email='ganesh697todkari@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)