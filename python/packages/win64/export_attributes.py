import c4d
import json


PREFACE = "def collect_{channel}_info(mat):\n    return {{"
END = "\n    }"
CONTENT = "\n        \"{name}\": mat[c4d.{channel_attribute}],"
CHANNELS = {
    "color": "COLOR",
    "luminance": "LUMINANCE",
    "transparency": "TRANSPARENCY",
    "reflection": "REFLECTION",
    "environment": "ENVIRONMENT",
    "fog": "FOG",
    "bump": "BUMP",
    "alpha": "ALPHA",
    "specular": "SPECULAR",
    "specular_color": "SPECULARCOLOR",
    "glow": "GLOW",
    "displacement": "DISPLACEMENT",
    "diffusion": "DIFFUSION",
    "normal": "NORMAL",
    "any": "ANY"
}
CONSTANTS = dir(c4d)

type_names = {}
function_strings = []
attrs = []

for channel_name, channel in CHANNELS.iteritems():
    channel_prefix = "MATERIAL_{}".format(channel)
    attributes = [attr for attr in CONSTANTS if attr.startswith(channel_prefix)]
    attr_list = []
    for attr in attributes:
        attribute = attr.split(channel_prefix + "_")
        if len(attribute) < 2 or len(attribute[1]) < 1:
            print("Bad attribute name: {}".format(attr))
            continue
        attribute = attribute[1]
        if not attribute in type_names:
            attribute_name = raw_input("Name for {}: ".format(attribute))
            type_names[attribute] = attribute_name
        attribute_name = type_names[attribute]
        attr_list.append(CONTENT.format(name=attribute_name, channel_attribute=attr))
        attrs.append(attr)
    string = PREFACE.format(channel=channel_name) + "".join(attr_list) + END
    function_strings.append(string)


with open('material_names.json', 'w') as f:
    f.write(
        json.dumps({
            'attribute_names': type_names,
            'channels': CHANNELS,
            'attributes': attrs
            },indent=4)
        )

with open('material_strategies.py', 'w') as f:
    f.write("import c4d\n\n\n" + "\n\n".join(function_strings))