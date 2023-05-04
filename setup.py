"""
Flask-Session
-------------

Flask-Session is an extension for Flask that adds support for
Server-side Session to your application.

"""
from setuptools import setup
from flask_sessionstore import __version__

setup(
    name='Flask-Sessionstore',
    version=__version__,
    description='Adds session support to your Flask application',
    long_description=__doc__,
    author='Matthew Crowson',
    author_email='matthew.d.crowson@gmail.com',
    maintainer='Ulrich Berthold',
    maintainer_email='ub@artfacts.net',
    url='https://github.com/Artfacts/flask-sessionstore',
    license='BSD',
    packages=['flask_sessionstore'],
    platforms='any',
    install_requires=[
        'Flask>=2.3.2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
