import c4d
from material_strategies import collect_material_info
import json
from os import path


MATERIAL_CHANNELS = {
    "color": c4d.CHANNEL_COLOR,                  # +
    "luminance": c4d.CHANNEL_LUMINANCE,          # +
    "transparency": c4d.CHANNEL_TRANSPARENCY,    # +
    "reflection": c4d.CHANNEL_REFLECTION,        # ~
    "environment": c4d.CHANNEL_ENVIRONMENT,      # -
    "fog": c4d.CHANNEL_FOG,                      # - 
    "bump": c4d.CHANNEL_BUMP,                    # +
    "alpha": c4d.CHANNEL_ALPHA,                  # +
    "specular": c4d.CHANNEL_SPECULAR,            # +
    "specular_color": c4d.CHANNEL_SPECULARCOLOR, # +
    "glow": c4d.CHANNEL_GLOW,                    # ~
    "displacement": c4d.CHANNEL_DISPLACEMENT,    # ~
    "diffusion": c4d.CHANNEL_DIFFUSION,          # ~
    "normal": c4d.CHANNEL_NORMAL,                # +
    "any": c4d.CHANNEL_ANY                       # - 
}

SHADER_CHANNELS = {
    "color": c4d.MATERIAL_COLOR_SHADER,
    "luminance": c4d.MATERIAL_LUMINANCE_SHADER,
    "transparency": c4d.MATERIAL_TRANSPARENCY_SHADER,
    "reflection": c4d.MATERIAL_REFLECTION_SHADER,
    "environment": c4d.MATERIAL_ENVIRONMENT_SHADER,
    "bump": c4d.MATERIAL_BUMP_SHADER,
    "alpha": c4d.MATERIAL_ALPHA_SHADER,
    "specular": c4d.MATERIAL_SPECULAR_SHADER,
    "displacement": c4d.MATERIAL_DISPLACEMENT_SHADER,
    "diffusion": c4d.MATERIAL_DIFFUSION_SHADER,
    "normal": c4d.MATERIAL_NORMAL_SHADER
}

SHADER_CONSTANTS = {
    "blackpoint": c4d.BITMAPSHADER_BLACKPOINT,
    "color_profile": c4d.BITMAPSHADER_COLORPROFILE,
    "exposure": c4d.BITMAPSHADER_EXPOSURE,
    "filename": c4d.BITMAPSHADER_FILENAME,
    "gamma": c4d.BITMAPSHADER_GAMMA,
    "interpolation": c4d.BITMAPSHADER_INTERPOLATION,
    "white_point": c4d.BITMAPSHADER_WHITEPOINT
}

MATERIAL_NEEDED_CHANNELS = [
    "color", "luminance", "transparency", "bump", "alpha",
    "specular", "specular_color", "normal"
]

MATERIAL_OPTIONAL_CHANNELS = [
    "reflection", "glow", "displacement", "diffusion"
]


def get_all_children(obj):
    all_seen = [obj]
    f_child = obj.GetDown()
    if not f_child:
        return all_seen
    all_seen.extend(get_all_children(f_child))
    n_child = f_child.GetNext()
    while n_child:
        all_seen.extend(get_all_children(n_child))
        n_child = n_child.GetNext()
    return all_seen

def collect_all_objects(objects):
    data = []
    for obj in objects:
        data.extend(get_all_children(obj))
    return data


def collect_data(doc):
    document = c4d.documents.GetActiveDocument()
    objects = collect_all_objects(document.GetObjects())
    materials = doc.GetMaterials()
    
    data = []
    for obj in objects:
        sourceTags = obj.GetTags()
        for tag in sourceTags:
            if not isinstance(tag, c4d.TextureTag):
                continue
            mat = tag.GetMaterial()
            if not mat in data:
                data.append(mat)
    return objects, data

def collect_shader_data(doc, shader):
    if shader is None:
        return
    data = {}
    for name, constant in SHADER_CONSTANTS.iteritems():
        data[name] = shader[constant]
        
    tex_path = c4d.GenerateTexturePath(doc[c4d.DOCUMENT_PATH], data["filename"], "")
    if tex_path is None:
        tex_path = "INVALID PATH"
        print("ERR:  Texture {} not found in project folder.".format(data["filename"]))
    data["filename"] = tex_path
    return data

def probe_channel(doc, mat, chan, chan_name):
    if not chan_name in MATERIAL_NEEDED_CHANNELS:
        return (None, None)
    if not chan_name in SHADER_CHANNELS: # ignores specular_color - mby mistake
        return (None, None)
    has_state = mat.GetChannelState(chan)
    if not has_state:
        return (None, None)
    channel_data = collect_material_info(mat, chan_name)
    shader_data = collect_shader_data(doc, channel_data["shader"])
    # serialize vector - might need patching
    for name, data_point in channel_data.iteritems():
        if isinstance(data_point, c4d.Vector):
            channel_data[name] = {'x': data_point[0], 'y': data_point[1], 'z': data_point[2]}
    return (channel_data, shader_data)

def serialize_materials(doc, materials):
    data = []
    unique_materials = []
    for material in materials:
        tag_data = {}
        if material in unique_materials:
            continue
        unique_materials.append(material)
        for name, channel in MATERIAL_CHANNELS.iteritems():
            channel_data, shader_data = probe_channel(doc, material, channel, name)
            if not channel_data is None:
                tag_data[name] = channel_data
                if not shader_data is None:
                    tag_data[name]["shader"] = shader_data
        data.append({
            "id": id(material),
            "tag_data": tag_data,
            "name": material.GetName()
        })
    if len(unique_materials) < len(materials):
        print("WARN: Materials showed up twice and have been truncated.")
    return data

