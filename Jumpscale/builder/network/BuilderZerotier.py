from Jumpscale import j
import json

builder_method = j.builder.system.builder_method



class BuilderZerotier(j.builder.system._BaseClass):

    def _init(self):
        self.DIR_BUILD = j.core.tools.text_replace("{DIR_VAR}/build/zerotier/")
        self.CLI = j.sal.fs.joinPaths('{DIR_BIN}', 'zerotier-cli')


    def clean(self):
        super().reset()
        j.sal.fs.remove(self.DIR_BUILD)
        self._init()

    @builder_method()
    def build(self,reset=False):
        """
        kosmos 'j.builder.network.zerotier.build()'
        :return: 
        """


        if j.core.platformtype.myplatform.isMac:
            raise RuntimeError("not supported yet")

            # j.sal.process.execute("xcode-select --install", die=False, showout=True)
        # elif j.core.platformtype.myplatform.isUbuntu:

        j.builder.system.package.ensure("gcc")
        j.builder.system.package.ensure("g++")
        j.builder.system.package.ensure('make')

        self.DIR_CODEL = j.clients.git.pullGitRepo(
            "https://github.com/zerotier/ZeroTierOne", reset=reset, depth=1, branch='master')

        S = """
            cd {DIR_CODEL}
            export DESTDIR={DIR_BUILD}
            make one
            make install        
            """
        self._execute(S)

        # cmd = "cd {code} &&  make one".format(code=codedir, build=self.DIR_BUILD)
        # j.sal.process.execute(cmd)
        # if j.core.platformtype.myplatform.isMac:
        #     cmd = "cd {code} && make install-mac-tap".format(code=codedir, build=self.DIR_BUILD)
        #     bindir = '{DIR_BIN}'
        #     j.core.tools.dir_ensure(bindir)
        #     for item in ['zerotier-cli', 'zerotier-idtool', 'zerotier-one']:
        #         j.builder.tools.file_copy('{code}/{item}'.format(code=codedir, item=item), bindir+'/')
        #     return
        # j.core.tools.dir_ensure(self.DIR_BUILD)
        # cmd = "cd {code} && DESTDIR={build} make install".format(code=codedir, build=self.DIR_BUILD)
        # j.sal.process.execute(cmd)


    @builder_method()
    def install(self):
        """
        kosmos 'j.builder.network.zerotier.install()'
        :return:
        """
        self.build()
        self._copy("{DIR_BUILD}/usr/sbin/","/sandbox/bin/")


    @property
    def startup_cmds(self):
        cmd = j.tools.startupcmd.get("zerotier", "zerotier-one", path="/tmp", timeout=10,ports=[9993])
        return [cmd]
