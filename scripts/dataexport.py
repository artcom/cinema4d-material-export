import c4d
from shutil import copyfile 
from material_collector import collect_data, serialize_materials
import json
from os import path, makedirs

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
            if shader is None:
                continue
            filename = shader["filename"]
            real_filename = path.basename(filename)
            to_folder_path = path.join(to_path, "textures")
            to_file_path = path.join(to_folder_path, real_filename)
            if not path.exists(to_folder_path):
                makedirs(to_folder_path)
            copyfile(filename, to_file_path)
            shader["filename"] = path.join("texture", real_filename)
    

def main():
    objects, materials = collect_data(doc)
    mats = serialize_materials(doc, materials)
    filepath = spawn_save_dialog()
    copy_texture_files(mats, path.dirname(filepath))
    with open(filepath, "w") as f:
        f.write(json.dumps({"materials": mats}, indent=4))
    print("Done.")
    # spawn_save_dialog()
    # with open("C:/Users/artcom/Desktop/C4D-Export/test1.json", "w") as f:
    #     f.write(json.dumps({"materials": mats}, indent=4))
    # print("Done.")

if __name__ == '__main__':
    main()
 