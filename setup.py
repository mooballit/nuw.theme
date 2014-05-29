from setuptools import setup, find_packages
import os

version = '0.3.2'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='nuw.theme',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['nuw', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'mooball.theme.bootstrap',
          'collective.lesscss',
          'collective.uploadify',
          'nuw.types',
          'plone.portlet.viewlet',
          'mooball.portlets.latestcontent',
          'mooball.analyticsviewlet',
          'zope.tal>=3.6.1',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
