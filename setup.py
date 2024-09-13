from setuptools import find_packages,setup
from typing import List
HYPEN_DOT_E="-e ."

def get_requirements(file_path:str)->List[str]:
    """"
        this function returns the requirements list of package to install
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E) 


setup(
    name="mlproject",
    version="0.0.1",
    author="vivek",
    author_email="vivekkumarknow@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')

)
