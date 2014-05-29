from zope.interface import Interface
from five import grok
from nuw.theme.interfaces import IThemeSpecific

grok.templatedir('templates')
grok.layer( IThemeSpecific )
grok.context( Interface )

class Quicklinks( grok.View ):
    pass

class SocialIconsBig( grok.View ):
    pass

class SocialIconsSmall( grok.View ):
    pass
