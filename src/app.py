import falcon

from resources.things import ThingsResource

def create_app():
    """Adds all app resources and makes Falcon WSGI app, and returns it.

    Returns:
        (falcon.API): the Falcon app instance
    """
    # falcon.API instances are callable WSGI apps
    app = falcon.API()

    # Add all routes
    app.add_route("/{field}", ThingsResource())

    return app
