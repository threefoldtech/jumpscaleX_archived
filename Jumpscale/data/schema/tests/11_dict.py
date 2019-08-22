# Copyright (C) July 2018:  TF TECH NV in Belgium see https://www.threefold.tech/
# In case TF TECH NV ceases to exist (e.g. because of bankruptcy)
#   then Incubaid NV also in Belgium will get the Copyright & Authorship for all changes made since July 2018
#   and the license will automatically become Apache v2 for all code related to Jumpscale & DigitalMe
# This file is part of jumpscale at <https://github.com/threefoldtech>.
# jumpscale is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# jumpscale is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License v3 for more details.
#
# You should have received a copy of the GNU General Public License
# along with jumpscale or jumpscale derived works.  If not, see <http://www.gnu.org/licenses/>.
# LICENSE END


from Jumpscale import j


def main(self):
    """
    to run:

    kosmos 'j.data.schema.test(name="dict")'
    """

    schema0 = """
        @url = despiegk.test.dict
        dd = {} (DICT)
        """

    schema_object = j.data.schema.get_from_text(schema_text=schema0)

    o = schema_object.new()

    o.dd["a"] = 1
    o.dd["b"] = "a"

    assert o.dd == {"a": 1, "b": "a"}

    data = o._data

    o3 = schema_object.new(serializeddata=data)

    assert o3.dd == {"a": 1, "b": "a"}

    self._log_info("test for dict ok")

    return "OK"