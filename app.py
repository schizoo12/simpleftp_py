import json
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

with open("config.json") as f:
    config = json.load(f)

authorizer = DummyAuthorizer()

for user in config["users"]:
    authorizer.add_user(
        user["user"],
        user["password"],
        user["homedir"],
        perm=user["permissions"]
    )

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", config["port"]), handler)
print(f"Serwer FTP działa na porcie {config['port']}")
server.serve_forever()
