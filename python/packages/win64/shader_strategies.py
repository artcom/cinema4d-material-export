import c4d
from pprint import pprint


def collect_shader_info(shader):
    pprint(dir(shader))
    pprint(type(shader))
