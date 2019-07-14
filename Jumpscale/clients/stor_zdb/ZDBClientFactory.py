import os
import uuid
from pprint import pprint

from Jumpscale import j

from .ZDBAdminClientBase import ZDBAdminClientBase
from .clients_impl import ZDBClientDirectMode, ZDBClientSeqMode, ZDBClientUserMode
from .clients_impl import ZDBClientDirectModeAdmin, ZDBClientSeqModeAdmin, ZDBClientUserModeAdmin

JSBASE = j.application.JSBaseClass


class ZDBClientFactory(j.application.JSFactoryConfigsBaseClass):
    """

    different modes: seq,user,direct

    """

    __jslocation__ = "j.clients.zdb"
    _CHILDCLASS = None  # because we use _childclass_selector
    _SCHEMATEXT = """
    @url = jumpscale.zdb.client.1
    name* = "test" (S)
    addr = "localhost" (S)
    port = 9900 (I)
    secret_ = "" (S)
    nsname = "test" (S)
    admin = false (B)
    mode = "seq,user,direct" (E)
    
    """

    def _childclass_selector(self, jsxobject, **kwargs):
        """
        allow custom implementation of which child class to use
        :return:
        """
        if jsxobject.mode == "seq":
            if jsxobject.admin:
                return ZDBClientSeqModeAdmin
            else:
                return ZDBClientSeqMode
        elif jsxobject.mode == "user":
            if jsxobject.admin:
                return ZDBClientUserModeAdmin
            else:
                return ZDBClientUserMode
        elif jsxobject.mode == "direct":
            if jsxobject.admin:
                return ZDBClientDirectModeAdmin
            else:
                return ZDBClientDirectMode
        else:
            raise RuntimeError("childclass cannot be defined")

    def client_admin_get(self, name="admin", addr="localhost", port=9900, secret="123456", mode="seq"):
        if self.exists(name=name):
            cl = self.get(name=name)
        else:
            cl = self.new(name=name, addr=addr, port=port, secret_=secret, mode=mode, admin=True)
        assert cl.admin == True
        return cl

    def client_get(self, name="main", nsname="test", addr="localhost", port=9900, secret="1234", mode="seq"):
        """
        :param nsname: namespace name
        :param addr:
        :param port:
        :param secret:
        :return:
        """
        if self.exists(name=name):
            cl = self.get(name=name)
        else:
            cl = self.new(name=name, nsname=nsname, addr=addr, port=port, secret_=secret, mode=mode, admin=False)
        return cl

    def test(self):
        """
        kosmos 'j.clients.zdb.test()'

        """

        j.servers.zdb.test_instance_start()

        self.delete("admin")

        cl = self.client_admin_get(port=9901)
        assert cl.ping()

        self._test_run(name="base")
        self._test_run(name="admin")

        self.delete("admin")
        self.delete("test")
        self.delete("newnamespace")

        j.servers.zdb.test_instance_stop()