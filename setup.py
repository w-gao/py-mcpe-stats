#
# Copyright (c) 2016-2021 w-gao
#
from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='mcstats',
      version='0.0.1',
      description='A tool to get basic information from Minecraft: Bedrock Edition servers.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/w-gao/py-mcpe-stats',
      author='w-gao',
      author_email='me@wlgao.com',
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      python_requires=">=3.6",
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Networking'
      ],
      keywords='minecraft bedrock mcpe mcbe mcpeserver mcbeserver raknet',
      entry_points={
          'console_scripts': [
              'mcstats = mcstats.main:main',
          ]
      })
