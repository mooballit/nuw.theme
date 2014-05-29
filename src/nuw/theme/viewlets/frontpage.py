from zope.interface import Interface
from five import grok
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.interfaces import IPortalHeader, IBelowContent

from nuw.theme.interfaces import IThemeSpecific
from nuw.theme.layout import DummyViewletManager

grok.templatedir('templates')
grok.layer( IThemeSpecific )

class FrontPageIndustries( grok.Viewlet ):
    grok.context( Interface )
    grok.viewletmanager( DummyViewletManager )
    
    def __of__( self, context ):
        # This is defined cause plone.portlet.viewlet requires it.
        return self
    
    def get_industries( self ):
        catalog = getToolByName( self.context, 'portal_catalog' )

        return catalog( { 'portal_type': 'nuw.types.industry' } )

class FrontPageCampaignsViewlet( grok.Viewlet ):
    grok.context( Interface )
    grok.viewletmanager( IPortalHeader )

    def available( self ):
        context_state = getMultiAdapter((self.context, self.request),
            name="plone_context_state")
        
        if context_state.is_portal_root() and context_state.is_default_page():
            return True

    def get_campaigns( self, ctype = 'union' ):
        catalog = getToolByName( self.context, 'portal_catalog' )
        return catalog( { 'portal_type': 'nuw.types.campaign', 
            'sort_on': 'effective', 'sort_order': 'descending',
            'campaign_type': ctype } )
    
    def get_union_campaigns( self ):
        return self.get_campaigns( 'union' )

    def get_worksite_campaigns( self ):
        return self.get_campaigns( 'worksite' )

    def get_social_campaigns( self ):
        return self.get_campaigns( 'social' )

class FrontPageSplashViewlet( grok.Viewlet ):
    grok.context( Interface )
    grok.viewletmanager( IBelowContent )

    def available( self ):
        splash_tool = getToolByName( self.context, 'splash_tool' )
        if self.request.cookies.get( "splash_seen", False ) or not splash_tool.splash_filename:
            return False
        
        return True

    def set_cookie( self ):
        if not self.request.cookies.get( "splash_seen", False ):
            self.request.response.setCookie( 'splash_seen', 'true' )

class FrontPageSplash( grok.View ):
    grok.context( Interface )

    def get_splash_url( self ):
        splash_tool = getToolByName( self.context, 'splash_tool' )
        return splash_tool.splash_tool.splash_url
