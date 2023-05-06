from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str) -> list:
    # This function will return the list of requirments
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[x.replace("/n","") for x in requirments]

        if "-e ." in requirments:
            requirments.remove("-e .") 
        
    return requirments


setup(
    name='mlproject',
    version='0.0.1',
    author='Koushik',
    author_email='saikoushik.gsk@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
)

