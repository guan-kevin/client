import sys

from distutils.core import setup


if sys.version_info[0] < 3:
    raise Exception('Sorry, Python 2 and earlier is not supported. Please install with Python 3 (using pip3).')


setup(
    name='bugswarm',
    packages=['client'],
    version='0.1',
    description='The BugSwarm CLI',
    author='Naji Dmeiri',
    author_email='nddmeiri@ucdavis.edu',
    maintainer='',
    maintainer_email='',
    url='https://github.com/BugSwarm/client',
    download_url='https://github.com/BugSwarm/client/archive/0.1.tar.gz',
    keywords=['bugswarm', 'client', 'cli', 'dataset', ],

    install_requires=[
        'Click==6.7',
        'requests==2.18.4',
    ],
    entry_points='''
        [console_scripts]
        bugswarm=bugswarm:cli
    ''',
)
