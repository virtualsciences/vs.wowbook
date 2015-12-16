from Acquisition import aq_parent, aq_inner
from plone.app.workflow.browser.sharing import SharingView
from Products.PluggableAuthService.plugins.ZODBRoleManager import (
    ZODBRoleManager, ManageUsers)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
