'''Exports material attributes to json as well as generating some python code
for assigning and exporting a materials channel data
'''
import json
import c4d

# 'smart' meta python: string formats and concats
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
# functions and constants, actually, but only constants are left over
CONSTANTS = dir(c4d)

# attribute -> friendly names
attribute_dict = {}
# list with fully defined functions
assembled_functions = []
# all attributes used once
named_attr_pairs = []

# run through all (manually identified) channels
for channel_name, channel in CHANNELS.iteritems():
    # ie. MATERIAL_BUMP_*
    channel_prefix = "MATERIAL_{}".format(channel)
    # query all constants associated with a channel
    c4d_constants = [x for x in CONSTANTS if x.startswith(channel_prefix)]
    named_attributes = []
    for constant in c4d_constants:
        attribute = constant.split(channel_prefix + "_")
        if len(attribute) < 2 or len(attribute[1]) < 1:
            print("Bad attribute name: {}".format(constant))
            continue
        attribute = attribute[1]
        # if we're lacking a friendly name for an attribute, query the user
        if not attribute in attribute_dict:
            attribute_name = raw_input("Name for {}: ".format(attribute))
            # ... and store it to the friendly names
            attribute_dict[attribute] = attribute_name
        attribute_name = attribute_dict[attribute]
        # good ol' string fmt
        named_attributes.append(CONTENT.format(
            name=attribute_name, channel_attribute=constant
        ))
        named_attr_pairs.append(constant)
    string = PREFACE.format(channel=channel_name) + \
        "".join(named_attributes) + END
    assembled_functions.append(string)

# dump all that content into a json
with open('material_names.json', 'w') as f:
    f.write(
        json.dumps({
            'attribute_names': attribute_dict,
            'channels': CHANNELS,
            'attributes': named_attr_pairs
        }, indent=4)
    )

# write a simple python script
with open('material_strategies.py', 'w') as f:
    f.write("import c4d\n\n\n" + "\n\n".join(assembled_functions))
