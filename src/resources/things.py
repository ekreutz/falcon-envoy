import json

from falcon import Request, Response
from falcon.status_codes import *

class ThingsResource:
    def on_get(self, req: Request, resp: Response, field):
        print(f"Received request! {field}")
        resp.status = HTTP_200
        resp.body = json.dumps({
            "magic": 500,
            "message": "Lorem ipsum, eigh?"
        })
