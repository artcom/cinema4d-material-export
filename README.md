# Cinema4D Material Export plugin

While working with Cinema4D and integrating it into Unity, it was apperant that
it takes a lot of manual overhead to import Cinema4D projects into the engine.
The biggest issue faced is reconstructing materials that a designer created.

This plugin exports an FBX and a JSON-file containing all object to material
links inside a scene graph aswell as all material properties for used materials
inside a scene.

An example JSON can look like this: 

```JSON
{
    "materials": [
        {
            "tag_data": {
                "bump": {
                    "parallax_samples": 8, 
                    "strength": -0.76, 
                    "parallax_height": 0.0, 
                    "mip_falloff": 1, 
                    "shader": {
                        "blackpoint": 0.0, 
                        "filename": "texture\\bump.png", 
                        "color_profile": 0, 
                        "white_point": 1.0, 
                        "interpolation": 6, 
                        "gamma": 1.0, 
                        "exposure": 0.0
                    }
                }, 
                "color": {
                    "color": {
                        "y": 0.0, 
                        "x": 0.8, 
                        "z": 0.0
                    }, 
                    "texture_strength": 1.0, 
                    "diffuse_falloff": 0.0, 
                    "model_lambertian": null, 
                    "diffuse_level": 1.0, 
                    "model_orennayar": null, 
                    "brightness": 1.0, 
                    "shader": null, 
                    "roughness": 0.5, 
                    "texture_mixing": 0, 
                    "model": 0
                }
            }, 
            "id": 2347778699888, 
            "name": "bump"
        }, 
        {
            "tag_data": {
                "bump": {
                    "parallax_samples": 8, 
                    "strength": 0.2, 
                    "parallax_height": 0.0, 
                    "mip_falloff": 1, 
                    "shader": {
                        "blackpoint": 0.0, 
                        "filename": "texture\\bump.png", 
                        "color_profile": 0, 
                        "white_point": 1.0, 
                        "interpolation": 6, 
                        "gamma": 1.0, 
                        "exposure": 0.0
                    }
                }, 
                "color": {
                    "color": {
                        "y": 0.0, 
                        "x": 0.0, 
                        "z": 0.0
                    }, 
                    "texture_strength": 1.0, 
                    "diffuse_falloff": 0.0, 
                    "model_lambertian": null, 
                    "diffuse_level": 1.0, 
                    "model_orennayar": null, 
                    "brightness": 1.0, 
                    "shader": {
                        "blackpoint": 0.0, 
                        "filename": "texture\\tex.png", 
                        "color_profile": 0, 
                        "white_point": 1.0, 
                        "interpolation": 6, 
                        "gamma": 1.0, 
                        "exposure": 0.0
                    }, 
                    "roughness": 0.5, 
                    "texture_mixing": 0, 
                    "model": 0
                }
            }, 
            "id": 2347778700048, 
            "name": "tex"
        }
    ], 
    "objects": [
        {
            "materials": [
                2347778699888, 
                2347778700048
            ], 
            "id": 2347778699664, 
            "name": "cube_bump.1"
        }, 
        {
            "materials": [], 
            "id": 2347778699696, 
            "name": "Cone"
        }, 
        {
            "materials": [], 
            "id": 2347778699728, 
            "name": "Square_renamed"
        }, 
        {
            "materials": [
                2347778700048
            ], 
            "id": 2347778699632, 
            "name": "cube_tex"
        }, 
        {
            "materials": [
                2347778699888
            ], 
            "id": 2347778699600, 
            "name": "cube_bump"
        }
    ]
}
```

See LICENSE file for license details. 