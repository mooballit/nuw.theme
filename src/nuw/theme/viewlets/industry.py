from five import grok
from nuw.theme.interfaces import IThemeSpecific
from nuw.theme.layout import get_parent_content_type
from plone.app.layout.viewlets.interfaces import IPortalHeader
from Products.CMFCore.utils import getToolByName
from zope.interface import Interface

from nuw.types.industry import IIndustry
from nuw.types.base import get_parent_content_type

grok.templatedir( 'templates' )
grok.layer( IThemeSpecific )

class IndustryMenuViewlet( grok.Viewlet ):
    grok.viewletmanager( IPortalHeader )
    grok.context( Interface )

    def update( self ):
        # Get the parent industry object
        industry = get_parent_content_type( self.context, IIndustry )

        if industry:
            catalog = getToolByName( self.context, 'portal_catalog' )
            
            industry_path = '/'.join( industry.getPhysicalPath() )
            
            tabs = catalog.searchResults( path = { "query": industry_path, 'depth': 1 } )
            
            # Hack to workaround mybrains.__cmp__(x,y) error at for loop below
            [ str( tab ) for tab in tabs ]

            def_page = industry.getDefaultPage()
            
            self.tabs = [ { 'url': industry.absolute_url(), 'title': 'Home', 'active': False } ]

            # Determine what tab is selected
            active = None
            for tab in tabs:
                if tab.id == def_page:
                    # Do not list the context's default page!
                    continue
                if self.context.absolute_url().startswith( tab.getURL() ):
                    active = tab
                self.tabs.append( {
                    'url': tab.getURL(),
                    'title': tab.Title,
                    'active': tab == active
                } )

            if not active:
                self.tabs[0]['active'] = True
        else:
            self.tabs = None

class IndustryLogoViewlet( grok.Viewlet ):
    grok.viewletmanager( IPortalHeader )
    grok.context( Interface )

    def update( self ):
        industry = get_parent_content_type( self.context, IIndustry )

        if industry:
            self.industry_id = industry.id
            self.industry_title = industry.Title
        else:
            self.industry_id = None
            self.industry_title = None
