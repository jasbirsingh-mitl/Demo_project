from setuptools import setup, find_packages
from typing import List


def Require_get(filepath:str) -> List[str]:
    
    require=[]
    Navigation_char="-e ."
    with open(filepath) as obj:
        
        require=obj.readlines()
        require=[ line.replace("\n","")for line in require ]
        
        if Navigation_char in require:
            require.remove(Navigation_char)
    
        
    return require    
    
    
    
setup(
    name="ml_project",                 # Package name
    version="0.1.0",                   # Version
    description="A sample ML project", # Short description
    author="Your Name",
    author_email="your.email@example.com",

    packages=find_packages(), # Automatically find modules in src/
    # package_dir={"": "src"},             # Root directory for source code
    # install_requires=[                   # Dependencies
    #     "numpy>=1.21.0",
    #     "pandas>=1.3.0",
    #     "scikit-learn>=1.0.0",
    #     "matplotlib"
    # ]
    
    install_requires=Require_get("requirements.txt")
)

# print(Require_get("requirements.txt"))