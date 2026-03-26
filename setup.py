from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:

    """
    This function will return list of requirements

    """
    requirements_list:List[str] = []

    try:
        # Open and read requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the files
            lines =  file.readlines()
            # Process each line
            for line in lines:
                # Stripe whitespaces and newline characters
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print(" requirements.txt not found")

    return requirements_list
print(get_requirements())

# setup is main function
setup(
    name="AI-TRIP-PLANNER",
    version="0.0.1",
    author="Himanshu",
    author_email="himanshu.waghmare78@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements(),
)