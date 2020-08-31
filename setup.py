"""a Python software that gets basic information about an MCPE server

setup.py

Copyright (c) 2016 w-gao
"""

from setuptools import setup, find_packages

setup(name='py_mcpe_stats',
      version='0.1.3',
      description='a Python software that gets basic information about an MCPE server',
      long_description='a Python software that allows you to ping a Minecraft Pocket:Edition (MCPE) server for basic '
                       'information.',
      url='https://github.com/w-gao/py-mcpe-stats',
      author='w-gao',
      author_email='w-gao@users.noreply.github.com',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Networking'
      ],
      keywords='MCPE minecraft mcpeserver raknet',
      packages=find_packages('.')
      )
