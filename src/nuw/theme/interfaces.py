from zope.interface import Interface

class IThemeSpecific(Interface):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "NVP Theme" theme, this interface must be its layer
       (in skin/viewlets/configure.zcml).
    """
