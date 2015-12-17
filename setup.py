import os.path
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djasmine',
    version='0.2.2',
    packages=['djasmine'],
    url='https://github.com/tjwalch/djasmine',
    license='MIT',
    author='Tomas Walch',
    author_email='tomaswalch@gmail.com',
    description='Integrates Jasmine JavaScript tests with the Django test framework in a simple but effective DRY way.',
    long_description=README,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django',
        'jasmine_core',
        'selenium',
        'glob2',
    ],
)
