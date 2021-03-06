#!/usr/bin/env python

from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
install_requires = open(path.join(this_directory, 'requirements.txt'), encoding='utf-8').read().strip().split('\n')
print(install_requires)

# This setup is suitable for "python setup.py develop".

setup(name='BiblioMeter',
      version='0.0.0',
      description='An application for bibliometry',
      long_description=long_description,
      long_description_content_type='text/markdown',
      include_package_data = True,
      license = 'MIT',
      classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Information Analysis :: Visualization',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research'
        ],
      keywords = 'Bibliography, Corpus parsing, Corpuses merging, WOS, SCOPUS',
      install_requires = install_requires,
      author= 'BiblioAnalysis team',
      author_email= 'francois.bertin7@wanadoo.fr, amal.chabli@orange.fr, ludovic.desmeuzes@yahoo.com',
      url= 'https://github.com/LuDesmeuzes/BiblioMeter_Utils',
      packages=["BiblioMeter_GUI", "BiblioMeter_FUNCTS"],
      package_dir={
        "": ".",
        "BiblioMeter_GUI": "./BiblioMeter_Utils/BiblioMeter_GUI",
        "BiblioMeter_FUNCTS": "./BiblioMeter_Utils/BiblioMeter_FUNCTS",
                  },
     )
