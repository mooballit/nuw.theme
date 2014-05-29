from zope.interface import Interface
from five import grok
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.interfaces import IPortalFooter

from nuw.theme.interfaces import IThemeSpecific
from nuw.theme.layout import DummyViewletManager

grok.templatedir('templates')
grok.layer( IThemeSpecific )

class QuickLinksViewlet( grok.Viewlet ):
    grok.context( Interface )
    grok.viewletmanager( DummyViewletManager )

    def __of__( self, context ):
        # This is defined cause plone.portlet.viewlet requires it.
        return self
