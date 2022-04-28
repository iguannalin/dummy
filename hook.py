from app.utility.base_world import BaseWorld
from plugins.dummy.app.dummy_gui import DummyGUI
from plugins.dummy.app.dummy_api import DummyAPI

name = 'Dummy'
description = 'dummy plugin to test vue app'
address = '/plugin/dummy/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    dummy_gui = DummyGUI(services, name=name, description=description)
    app.router.add_static('/dummy', 'plugins/dummy/static/', append_version=True)
    app.router.add_route('GET', '/plugin/dummy/gui', dummy_gui.splash)

    dummy_api = DummyAPI(services)
    # Add API routes here
    app.router.add_route('POST', '/plugin/dummy/mirror', dummy_api.mirror)

