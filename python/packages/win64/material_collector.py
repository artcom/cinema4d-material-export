from os import path
from materialexport.serializer_classes import Material
import json
import c4d


def get_all_children(obj):
    '''Recursive function searching all children AND sibling objects in a scene
    (depth first search)

    Args:
        obj (c4d.BaseObject): The object to search from

    Returns:
        list: object itself, accompanied by all children AND siblings
    '''
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
    '''Entry function to start a recursive object search for the objects in a
    scene

    Args:
        objects (list): A list of objectes, ie. from doc.GetObjects()
    
    Returns:
        list: Containing all objects, including input objects, found as
              childrens and siblings
    '''
    data = []
    for obj in objects:
        data.extend(get_all_children(obj))
    return data


def collect_data(doc):
    ''' Collects all objects and materials inside the given document
    Args:
        doc (c4d.document): The document 

    Returns:
        tuple (list(c4d.BaseObject), list(c4d.TextureTag)): All found objects
        and associated materials to those objects (unused materials are ignored)
    '''
    objects = collect_all_objects(doc.GetObjects())    
    mat_data = []
    for obj in objects:
        source_tags = obj.GetTags()
        for tag in source_tags:
            # filter all non-material tags - we still keep objects without
            # materials, so any other software can look it up if it contains
            # any material
            if not isinstance(tag, c4d.TextureTag):
                continue
            mat = tag.GetMaterial()
            name = mat.GetName()
            if not mat in mat_data:
                mat_data.append(mat)
                
    return objects, mat_data


def serialize_materials(materials, doc):
    '''Serializes all materials given to a json format.abs

    Args:
        materials (list(c4d.TextureTag)): All materials to serialize
    
    Returns:
        list: JSON strings of materials
    '''
    data = []
    unique_materials = []
    # convert all c4d.TextureTag elements to serializer_classes.Material
    # which then does the heavy lifting
    for material in materials:
        mat = Material(material, doc)
        if mat in data:
            continue
        unique_materials.append(material)
        data.append(mat)
    if len(data) < len(materials):
        print("WARN: Materials showed up twice and have been truncated.")
    # throw it out into the void
    return [mat.to_json() for mat in data]