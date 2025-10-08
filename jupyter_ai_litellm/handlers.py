import json

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado

from .chat_models_rest_api import ChatModelsRestAPI

class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({
            "data": "This is /jupyter-ai-litellm/get-example endpoint!"
        }))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    print(f"Base url is {base_url}")
    route_pattern = url_path_join(base_url, "jupyter-ai-litellm", "get-example")
    handlers = [
        (route_pattern, RouteHandler),
        (url_path_join(base_url, "api/ai/models/chat") + r"(?:\?.*)?", ChatModelsRestAPI)
    ]
    web_app.add_handlers(host_pattern, handlers)
