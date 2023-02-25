#!/usr/bin/env python

from distutils.core import setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='GeetControl',
      version='1.0',
      description='Control Your Desktop Remotely',
      author='Itay Bachar',
      author_email='itay.bachar01@gmail.com',
      url='https://github.com/itaybachar',
      packages=["backend","backend.response", "backend.router","backend.controller","frontend.public"],
      package_data={"frontend.public":["pages/*.html","res/*.png","scripts/*.js","styles/*.css"]},
      include_package_data=True,
        entry_points={
        'console_scripts': ['geetControl = backend.main:main']
        },
        install_requires=required,
     )