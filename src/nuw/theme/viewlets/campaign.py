# Campaign specific viewlets (used as portlets through the magic of the viewlet portlet)
from five import grok

from nuw.theme.interfaces import IThemeSpecific
from nuw.theme.layout import DummyViewletManager
from zope.interface import Interface

grok.templatedir('templates')
grok.layer( IThemeSpecific )

class CampaignActions( grok.Viewlet ):
    grok.viewletmanager( DummyViewletManager )
    grok.context( Interface )
    
    def __of__( self, context ):
        # This is defined cause plone.portlet.viewlet requires it.
        return self
