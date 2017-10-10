import c4d
from shutil import copyfile 
from material_collector import collect_data, serialize_materials, Material
from material_strategies import collect_material_info
import json
from os import path, makedirs
from pprint import pprint

EXPORT_FBX = 1026370 # magic number - not documented

def spawn_save_dialog():
    print(c4d.FILESELECTTYPE_ANYTHING)
    print(type(c4d.FILESELECTTYPE_ANYTHING))
    path = c4d.storage.SaveDialog(
        c4d.FILESELECTTYPE_ANYTHING,
        "Material Export",
        "json",
        doc[c4d.DOCUMENT_FILEPATH],
        (doc[c4d.DOCUMENT_NAME] + "_Materials")
    )
    print(path)
    return path

def copy_texture_files(serialized_materials, to_path):
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
        objs.append({"id": id(obj), "name": obj.GetName(), "materials": [mat.id for mat in mats]})
    return objs

def main():
    # here are only active materials
    objects, materials = collect_data(doc)
    mats = serialize_materials(doc, materials)
    objs = serialize_object_w_materials(objects, [Material(m, doc) for m in materials])
    
    filepath = spawn_save_dialog()
    if filepath is None:
        print("No filepath given - aborting.")
        return

    copy_texture_files(mats, path.dirname(filepath))
    with open(filepath, "w") as f:
        f.write(json.dumps({"materials": mats, "objects": objs}, indent=4))
    if c4d.documents.SaveDocument(doc, path.splitext(filepath)[0] + ".fbx", c4d.SAVEDOCUMENTFLAGS_EXPORTDIALOG, 1026370):
        print("INFO: Exported FBX")
    else:
        print("ERR:  FBX not exported.")
    
    print("Done.")
    
    
    if False:
        # here are ALL materials
        materials = doc.GetMaterials()
        cmaterials = doc.GetMaterials()
        
        conv_materials = [Material(mat, doc) for mat in materials]
        conv_cmaterials = [Material(mat, doc) for mat in cmaterials]
        
        for m in conv_materials:
            for cm in cmaterials:
                print(m == cm)
            print("-----------------------")
            
        mats = serialize_materials(doc, materials)

if __name__ == '__main__':
    main()
 