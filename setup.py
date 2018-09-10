import os.path
from setuptools import setup, find_packages

package_dir = os.path.abspath(os.path.dirname(__file__))
setup(
    name = "rubick",
    version = "0.0.1",
    author = "Orvis Venture",
    author_email = "oscar.sanchez@orbis.com.pe",
    description = "Herramienta para la creación de proyectos base",
    package_data={'': ['config.yaml']},
    packages = find_packages(),
    include_package_data=True,
    install_requires = ["click==6.7",
                        "Jinja2==2.10",
                        "GitPython==2.1.11",
                        "PyYAML==3.12"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts = ['bin/rubick'],
)