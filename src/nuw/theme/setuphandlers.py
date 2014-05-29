import zope.interface

def install( context ):
    if context.readDataFile('marker.txt') is None:
        return

    portal = context.getSite()

    if 'members-area' not in portal:
        # Add members area folder
        portal.invokeFactory( 'Folder', 'members-area', title = 'My NUW Online' )

    if 'campaigns' not in portal:
        # Add campaigns folder
        portal.invokeFactory( 'Folder', 'campaigns', title = 'Campaigns' )
        f = portal.campaigns
        
        # Limit what can be created in folder to Campaigns only
        f.setConstrainTypesMode( 1 )
        f.setImmediatelyAddableTypes( ['nuw.types.campaign' ] )
        f.setLocallyAllowedTypes( [ 'nuw.types.campaign' ] )
