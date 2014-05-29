""" Override the default Plone layout utility.

Based of: http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/css.html#adding-new-css-body-classes
"""

from zope.component import queryUtility
from zope.component import getMultiAdapter
from five import grok
from zope.interface import Interface

from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.app.layout.globals import layout as base
from plone.app.layout.navigation.interfaces import INavigationRoot

from nuw.types.industry import IIndustry
from nuw.types.campaign import ICampaign
from nuw.types.base import get_parent_content_type

class LayoutPolicy(base.LayoutPolicy):
    """
    Enhanched layout policy helper.

    Extend the Plone standard class to have some more <body> CSS classes
    based on the current context.
    """

    def bodyClass(self, template, view):
        """Returns the CSS class to be used on the body tag.
        """

        # Get contet parent
        body_class = super( LayoutPolicy, self ).bodyClass( template, view )

        normalizer = queryUtility( IIDNormalizer )

        # Add industry-$industry$ if context is under an industry object
        industry = get_parent_content_type( self.context, IIndustry )
        if industry:
            body_class += ' industry industry-%s' % normalizer.normalize(industry.id)
        
        campaign = get_parent_content_type( self.context, ICampaign )
        if campaign:
          body_class += ' campaign campaign-%s' % normalizer.normalize(campaign.id)

        # Add siteroot-default-page if context is default page of siteroot
        context_state = getMultiAdapter((self.context, self.request), name="plone_context_state")
        
        if context_state.is_portal_root() and context_state.is_default_page():
            body_class += ' siteroot-default-page'

        return body_class

class DummyViewletManager(grok.ViewletManager):
    grok.context( Interface )
    grok.name( 'nuw.theme.dummyviewletmanager' )
