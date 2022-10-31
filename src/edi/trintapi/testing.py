# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import edi.trintapi


class EdiTrintapiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.trintapi)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.trintapi:default')


EDI_TRINTAPI_FIXTURE = EdiTrintapiLayer()


EDI_TRINTAPI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_TRINTAPI_FIXTURE,),
    name='EdiTrintapiLayer:IntegrationTesting',
)


EDI_TRINTAPI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_TRINTAPI_FIXTURE,),
    name='EdiTrintapiLayer:FunctionalTesting',
)


EDI_TRINTAPI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_TRINTAPI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiTrintapiLayer:AcceptanceTesting',
)
