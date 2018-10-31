"""
Setup script for the ``rotate-backups`` package.
"""

# Standard library modules.
import codecs
import os
import re

from setuptools import find_packages, setup


def get_contents(*args):
    with codecs.open(get_absolute_path(*args), 'r', 'UTF-8') as handle:
        return handle.read()


def get_requirements(*args):
    """Get requirements from pip requirement files."""
    requirements = set()
    with open(get_absolute_path(*args)) as handle:
        for line in handle:
            # Strip comments.
            line = re.sub(r'^#.*|\s#.*', '', line)
            # Ignore empty lines
            if line and not line.isspace():
                requirements.add(re.sub(r'\s+', '', line))
    return sorted(requirements)


def get_absolute_path(*args):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)


setup(name="py-backup",
      version="0.0.1",
      description="Backup Tool",
      long_description=get_contents('README.rst'),
      url='https://github.com/',
      author="tamutamu",
      author_email='tamu.0.0.tamu@gmail.com',
      license='MIT',
      packages=find_packages(),
      entry_points=dict(console_scripts=[
          'py-backup = pybackup.pybackup:hoge'
      ]),
      install_requires=get_requirements('requirements.txt'),
      test_suite='',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development',
          'Topic :: System :: Archiving :: Backup',
          'Topic :: System :: Systems Administration',
      ])
