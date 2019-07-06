from Jumpscale import j

from .RedisConfig import RedisConfig


class RedisConfigFactory(j.application.JSBaseConfigsClass):
    __jslocation__ = "j.clients.redis_config"
    _CHILDCLASS = RedisConfig

    def get_client(self, name):
        """
        get redis client
        :param name:
        :return:
        """
        if name.lower() == "core":
            return j.clients.redis.core_get()
        cl = self.get(name=name)
        return cl.redis

    def test(self):
        """
        kosmos 'j.clients.redis_config.test()'
        :return:
        """
        cl0 = j.clients.redis.core_get()
        unixsocket = cl0.connection_pool.connection_kwargs["path"]

        cl1 = self.get(name="test_config", addr="localhost", port=6379).redis
        assert cl1.ping()

        cl2 = self.get(name="test_config2", unixsocket=unixsocket).redis
        assert cl2.ping()

        cl3 = self.get(name="test_config3", unixsocket=unixsocket, addr=None, port=None).redis
        assert cl3.ping()

        cl4 = self.get_client(name="test_config3")
        assert cl4.ping()
