from setuptools import find_packages,setup
from typing import List
REMOVE_CONSTANT='-e .'
def get_requirements(file_path:str) -> List[str]:
    
    '''
    This function will return list of requirements.
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n" , " ") for req in requirements]

        if REMOVE_CONSTANT in requirements :
            requirements.remove(REMOVE_CONSTANT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Rajini',
author_email='ganjirajini277@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)