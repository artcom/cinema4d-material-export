import c4d
from materialexport.constants import (
    MATERIAL_CHANNELS, MATERIAL_NEEDED_CHANNELS, SHADER_CHANNELS, SHADER_CONSTANTS)
from materialexport.material_strategies import collect_material_info


class Material:
    '''Material class is basically the same as 'c4d.TextureTag', but stores
    a serializable string. Allows for comparison with other 'Material's and
    'c4d.TextureTag's
    '''
    id, doc, name, c4d_material, tag_data = (None, None, None, None, None)

    def __init__(self, c4d_material, doc=None):
        '''Is currently a "serialize first, then never again" strategy, which
        could be - in hindsight - be a mistake. Can be re-serialized with
        obj.serialize()

        Args:
            c4d_material (c4d.TextureTag): Original material
        '''
        if not isinstance(c4d_material, c4d.BaseMaterial):
            raise ValueError(
                "1st parameter is of invalid type: {}".format(type(c4d_material)))
        self.c4d_material = c4d_material
        self.name = c4d_material.GetName()
        self.id = id(c4d_material)
        self.tag_data = {}
        self.doc = doc
        # serialize on object creating
        self.serialize()

    def serialize(self):
        '''Serializes a c4d.TextureTag with all associated channels'''
        for name, channel in MATERIAL_CHANNELS.iteritems():
            # probe a channel
            channel_data, shader_data = self.probe_channel(
                self.c4d_material, channel, name)
            # which could be empty and therefore irrelevant
            if channel_data is None:
                continue
            self.tag_data[name] = channel_data
            if not shader_data is None:
                self.tag_data[name]["shader"] = shader_data

    def probe_channel(self, mat, chan, chan_name):
        '''Retrieves all channel and shader data
        
        Returns:
            tuple(dict(channel), dict(shader)): channel and shader attributes
        '''
        # Filter out irrelevant channels
        if not chan_name in MATERIAL_NEEDED_CHANNELS:
            return (None, None)
        # filter out shader-less channels (ie. global raytracer attributes)
        if not chan_name in SHADER_CHANNELS:  # ignores specular_color - mby mistake
            return (None, None)
        # or if the channel is just empty
        if not mat.GetChannelState(chan):
            return (None, None)
        # collect all attributes and shader data
        channel_data = collect_material_info(mat, chan_name)
        shader_data = self.collect_shader_data(channel_data["shader"])
        # serialize vector - might need patching
        for name, data_point in channel_data.iteritems():
            if isinstance(data_point, c4d.Vector):
                channel_data[name] = {'x': data_point[0],
                                      'y': data_point[1], 'z': data_point[2]}
        return (channel_data, shader_data)

    def collect_shader_data(self, shader):
        '''Retrieves all shader data for a given c4d.BaseShder. Needs associated
        document to find a real path to associated textures (because obv. that's
        a mess, too)
        
        Returns:
            dict: containing all shader attributes
        '''
        if shader is None:
            return
        data = {}
        for name, constant in SHADER_CONSTANTS.iteritems():
            value = shader[constant]
            if isinstance(value, c4d.Vector):
                value = {'x': value[0], 'y': value[1], 'z': value[2]}
            data[name] = value
        # The tex-path can be: empty, not findable, missing or fine
        # the filename is just a filename - no path or anything
        tex_path = None
        # when we don't have a document, we can't find the file anyway
        if not self.doc is None:
            tex_path = c4d.GenerateTexturePath(
                self.doc[c4d.DOCUMENT_PATH], data["filename"], "")
        # if it's None by not finding or not being able to search, then
        # we remove the filename, because it has no data value
        if tex_path is None:
            tex_path = "INVALID PATH"
            print("ERR:  Texture {} not found in project folder.".format(
                data["filename"]))
            del data["filename"]
        else:
            data["filename"] = tex_path
        return data

    def to_json(self):
        '''Outputs a friendly json-ready dictionary

        Returns:
            dict: Containing all material info ready to be serialized
        '''
        return {"id": self.id, "name": self.name, "tag_data": self.tag_data}

    def __str__(self):
        return "Material: name: [{}] - id: [{}]".format(self.name, self.id)

    def __eq__(self, other):
        if isinstance(other, Material):
            return self.c4d_material.Compare(other.c4d_material)
        if isinstance(other, c4d.Material):
            return self.c4d_material.Compare(other)
        else:
            return False

    def __hash__(self):
        return hash([self.name, self.tag_data])