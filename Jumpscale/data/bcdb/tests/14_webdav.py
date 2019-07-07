from Jumpscale import j
import requests


def main(self):
    """
    to run:
    kosmos 'j.data.bcdb.test(name="vfs")'

    """

    # md5 = "cbf134f55d0c7149ef188cf8a52db0eb"
    # sid = "7"
    test_cmd = """
from Jumpscale import j
bcdb = j.data.bcdb.get("test")
bcdb.reset()
vfs = j.data.bcdb._get_vfs()

SCHEMA = \"\"\"
@url = threefoldtoken.wallet.test
name* = "wallet"
addr = ""                   # Address
ipaddr = (ipaddr)           # IP Address
email = "" (S)              # Email address
username = "" (S)           # User name

\"\"\"
m_wallet_test = bcdb.model_get_from_schema(SCHEMA)
for i in range(10):
    o = m_wallet_test.new()
    assert o._model.schema.url == "threefoldtoken.wallet.test"
    o.addr = "something:%s" % i
    o.email = "myemail%s@test.fr" % i
    o.name = "myuser_%s" % i
    o.username = "nothing here_%s" % i
    o.save()

from Jumpscale.data.bcdb.connectors.webdav.BCDBResourceProvider import BCDBResourceProvider
rack = j.servers.rack.get()
rack.webdav_server_add(webdavprovider=BCDBResourceProvider())
rack.start()
    """
    s = j.servers.startupcmd.get(
        name="webdav_test", cmd_start=test_cmd, interpreter="python", executor="tmux", ports=[4443]
    )
    s.start()
    session = requests.session()
    session.auth = requests.auth.HTTPBasicAuth("root", "root")

    # test get schema by url
    schema = session.get("http://0.0.0.0:4443/test/schemas/url/threefoldtoken.wallet.test").json()
    assert schema["url"] == "threefoldtoken.wallet.test"

    # test get schema by sid
    schema = session.get("http://0.0.0.0:4443/test/schemas/sid/7").json()
    assert schema["url"] == "threefoldtoken.wallet.test"

    # test get schema by hash
    schema = session.get("http://0.0.0.0:4443/test/schemas/hash/cbf134f55d0c7149ef188cf8a52db0eb").json()
    assert schema["url"] == "threefoldtoken.wallet.test"

    # test get data by url
    data = session.get("http://0.0.0.0:4443/test/data/1/url/threefoldtoken.wallet.test/1").json()
    assert data["name"] == "myuser_0"

    # test get data by sid
    data = session.get("http://0.0.0.0:4443/test/data/1/sid/7/1").json()
    assert data["name"] == "myuser_0"

    # test get data by hash
    data = session.get("http://0.0.0.0:4443/test/data/1/hash/cbf134f55d0c7149ef188cf8a52db0eb/1").json()
    assert data["name"] == "myuser_0"