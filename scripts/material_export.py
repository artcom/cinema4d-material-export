import c4d
from shutil import copyfile
from materialexport.material_collector import collect_data, serialize_materials, Material
from materialexport.material_strategies import collect_material_info
import json
from os import path, makedirs
from pprint import pprint

EXPORT_FBX = 1026370  # magic number - not documented


def spawn_save_dialog():
    '''Creates a save dialoge that only accepts JSON.'''
    path = c4d.storage.SaveDialog(
        c4d.FILESELECTTYPE_ANYTHING,
        "Material Export",
        "json",
        doc[c4d.DOCUMENT_FILEPATH],
        (doc[c4d.DOCUMENT_NAME] + "_Materials")
    )
    return path


def copy_texture_files(serialized_materials, to_path):
    '''By basically moving manually through the data structure, we copy all
    textures to the location where the JSON + FBX will be and change all
    filepaths to a local reference since all files are now findable in relative
    '''
    s = serialized_materials
    for mat in s:
        tag_data = mat["tag_data"]
        for key, value in tag_data.iteritems():
            shader = value["shader"]
            if shader is None or not "filename" in shader:
                continue
            filename = shader["filename"]
            real_filename = path.basename(filename)
            to_folder_path = path.join(to_path, "textures")
            to_file_path = path.join(to_folder_path, real_filename)
            if not path.exists(to_folder_path):
                makedirs(to_folder_path)
            copyfile(filename, to_file_path)
            shader["filename"] = path.join("texture", real_filename)


def serialize_object_w_materials(objects, materials):
    '''Re-link all objects with material references.'''
    objs = []
    for obj in objects:
        source_tags = obj.GetTags()
        mats = []
        for tag in source_tags:
            if not isinstance(tag, c4d.TextureTag):
                continue
            c4d_mat = tag.GetMaterial()
            mat = [mat for mat in materials if mat == c4d_mat][0]
            mats.append(mat)
        objs.append({"id": id(obj), "name": obj.GetName(),
                     "materials": [mat.id for mat in mats]})
    return objs


def main():
    '''Main procedure for exporting:
    - Generate a data structure that is serializable (and serialize)
    - Copy all referenced textures in the scene
    - Write out an FBX + JSON
    '''
    # collect everything
    objects, materials = collect_data(doc)
    # serialize materials
    mats = serialize_materials(materials)
    # based on that, we relink what materials are used on which objects
    objs = serialize_object_w_materials(
        objects, [Material(m, doc) for m in materials])

    # figure out the filepath
    filepath = spawn_save_dialog()
    if filepath is None:
        print("No filepath given - aborting.")
        return
    # and then copy textures
    copy_texture_files(mats, path.dirname(filepath))
    # write out the json for material reconstruction
    with open(filepath, "w") as f:
        f.write(json.dumps({"materials": mats, "objects": objs}, indent=4))
        print("INFO: Exported material JSON.")
    # write out an FBX into the same folder
    if c4d.documents.SaveDocument(doc, path.splitext(filepath)[0] + ".fbx", c4d.SAVEDOCUMENTFLAGS_EXPORTDIALOG, 1026370):
        print("INFO: Exported FBX")
    else:
        print("ERR:  FBX not exported.")
    print("Done.")


if __name__ == '__main__':
    main()
