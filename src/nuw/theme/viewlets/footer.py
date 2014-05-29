from zope.interface import Interface
from five import grok
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.interfaces import IPortalFooter

from nuw.theme.interfaces import IThemeSpecific

from Acquisition import aq_inner
from plone.app.layout.viewlets.common import SiteActionsViewlet

import datetime

grok.templatedir('templates')
grok.layer( IThemeSpecific )

def render_viewlet(factory, context, request):
    """ Helper method to render a viewlet """

    context = aq_inner(context)
    viewlet = factory(context, request, None, None).__of__(context)
    viewlet.update()
    return viewlet.render()

class FooterViewlet( grok.Viewlet ):
    grok.context( Interface )
    grok.viewletmanager( IPortalFooter )

    def get_industries( self ):
        catalog = getToolByName( self.context, 'portal_catalog' )

        return catalog( { 'portal_type': 'nuw.types.industry' } )

    def get_campaigns( self ):
        catalog = getToolByName( self.context, 'portal_catalog' )
        return catalog( { 'portal_type': 'nuw.types.campaign',
            'sort_on': 'effective', 'sort_order': 'descending' } )[:5]

    def site_actions( self ):
        return render_viewlet(SiteActionsViewlet, self.context, self.request)
        
    def get_year( self ):
        return datetime.date.today().year
