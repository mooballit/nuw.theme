from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class NuwTheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import nuw.theme
        xmlconfig.file('configure.zcml',
                       nuw.theme,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nuw.theme:default')

NUW_THEME_FIXTURE = NuwTheme()
NUW_THEME_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(NUW_THEME_FIXTURE, ),
                       name="NuwTheme:Integration")