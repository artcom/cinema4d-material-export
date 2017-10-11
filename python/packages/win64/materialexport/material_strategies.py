import c4d


def collect_material_info(mat, name):
    '''Collects Cinama4D standard material informations
    - cannot gather data from custom material models

    Args:
        mat (c4d.TextureTag): input material with data attached
        name (str): material channel in which attributes are gathered
    Returns:
        dict: containing all (queryable) attributes of a materials channel
    '''
    name = name.lower()
    if name == 'luminance':
        return collect_luminance_info(mat)
    elif name == 'normal':
        return collect_normal_info(mat)
    elif name == 'bump':
        return collect_bump_info(mat)
    elif name == 'displacement':
        return collect_displacement_info(mat)
    elif name == 'alpha':
        return collect_alpha_info(mat)
    elif name == 'any':
        return collect_any_info(mat)
    elif name == 'glow':
        return collect_glow_info(mat)
    elif name == 'diffusion':
        return collect_diffusion_info(mat)
    elif name == 'specular_color':
        return collect_specular_color_info(mat)
    elif name == 'reflection':
        return collect_reflection_info(mat)
    elif name == 'environment':
        return collect_environment_info(mat)
    elif name == 'color':
        return collect_color_info(mat)
    elif name == 'specular':
        return collect_specular_info(mat)
    elif name == 'fog':
        return collect_fog_info(mat)
    elif name == 'transparency':
        return collect_transparency_info(mat)
    else:
        print("There is no channel named [{}]!".format(name))
        raise ValueError("Unknown channel named [{}]".format(name))


def collect_luminance_info(mat):
    return {
        "brightness": mat[c4d.MATERIAL_LUMINANCE_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_LUMINANCE_COLOR],
        "shader": mat[c4d.MATERIAL_LUMINANCE_SHADER],
        "texture_mixing": mat[c4d.MATERIAL_LUMINANCE_TEXTUREMIXING],
        "texture_strength": mat[c4d.MATERIAL_LUMINANCE_TEXTURESTRENGTH],
    }


def collect_normal_info(mat):
    return {
        "reverse_x": mat[c4d.MATERIAL_NORMAL_REVERSEX],
        "reverse_y": mat[c4d.MATERIAL_NORMAL_REVERSEY],
        "reverse_z": mat[c4d.MATERIAL_NORMAL_REVERSEZ],
        "shader": mat[c4d.MATERIAL_NORMAL_SHADER],
        "space": mat[c4d.MATERIAL_NORMAL_SPACE],
        "space_local": mat[c4d.MATERIAL_NORMAL_SPACE_LOCAL],
        "space_tangent": mat[c4d.MATERIAL_NORMAL_SPACE_TANGENT],
        "space_world": mat[c4d.MATERIAL_NORMAL_SPACE_WORLD],
        "strength": mat[c4d.MATERIAL_NORMAL_STRENGTH],
        "swap": mat[c4d.MATERIAL_NORMAL_SWAP],
    }


def collect_bump_info(mat):
    return {
        "mip_falloff": mat[c4d.MATERIAL_BUMP_MIPFALLOFF],
        "parallax_height": mat[c4d.MATERIAL_BUMP_PARALLAX_HEIGHT],
        "parallax_samples": mat[c4d.MATERIAL_BUMP_PARALLAX_SAMPLES],
        "shader": mat[c4d.MATERIAL_BUMP_SHADER],
        "strength": mat[c4d.MATERIAL_BUMP_STRENGTH],
    }


def collect_displacement_info(mat):
    return {
        "height": mat[c4d.MATERIAL_DISPLACEMENT_HEIGHT],
        "shader": mat[c4d.MATERIAL_DISPLACEMENT_SHADER],
        "strength": mat[c4d.MATERIAL_DISPLACEMENT_STRENGTH],
        "sub_poly": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY],
        "sub_poly_distribution": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_DISTRIBUTION],
        "sub_poly_hq_remapping": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_HQREMAPPING],
        "sub_poly_keep_edges": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_KEEPEDGES],
        "sub_poly_map_result": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_MAPRESULT],
        "sub_poly_prebuild": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_PREBUILD],
        "sub_poly_round": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_ROUND],
        "sub_poly_round_contour": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_ROUNDCONTOUR],
        "sub_poly_smooth": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_SMOOTH],
        "sub_poly_subdivision": mat[c4d.MATERIAL_DISPLACEMENT_SUBPOLY_SUBDIVISION],
        "tessellation": mat[c4d.MATERIAL_DISPLACEMENT_TESSELLATION],
        "tessellation_adaptive": mat[c4d.MATERIAL_DISPLACEMENT_TESSELLATION_ADAPTIVE],
        "tessellation_adaptive_level": mat[c4d.MATERIAL_DISPLACEMENT_TESSELLATION_ADAPTIVE_LEVEL],
        "tessellation_info": mat[c4d.MATERIAL_DISPLACEMENT_TESSELLATION_INFO],
        "tessellation_none": mat[c4d.MATERIAL_DISPLACEMENT_TESSELLATION_NONE],
        "tessellation_uniform": mat[c4d.MATERIAL_DISPLACEMENT_TESSELLATION_UNIFORM],
        "tessellation_uniform_level": mat[c4d.MATERIAL_DISPLACEMENT_TESSELLATION_UNIFORM_LEVEL],
        "type": mat[c4d.MATERIAL_DISPLACEMENT_TYPE],
        "type_contered_intensity": mat[c4d.MATERIAL_DISPLACEMENT_TYPE_CENTEREDINTENSITY],
        "type_intensity": mat[c4d.MATERIAL_DISPLACEMENT_TYPE_INTENSITY],
        "type_red_green": mat[c4d.MATERIAL_DISPLACEMENT_TYPE_REDGREEN],
        "type_rgb_local": mat[c4d.MATERIAL_DISPLACEMENT_TYPE_RGBLOCAL],
        "type_rgb_tangent": mat[c4d.MATERIAL_DISPLACEMENT_TYPE_RGBTANGENT],
        "type_rgb_world": mat[c4d.MATERIAL_DISPLACEMENT_TYPE_RGBWORLD],
    }


def collect_alpha_info(mat):
    return {
        "color": mat[c4d.MATERIAL_ALPHA_COLOR],
        "delta": mat[c4d.MATERIAL_ALPHA_DELTA],
        "image_alpha": mat[c4d.MATERIAL_ALPHA_IMAGEALPHA],
        "invert": mat[c4d.MATERIAL_ALPHA_INVERT],
        "premultiplied": mat[c4d.MATERIAL_ALPHA_PREMULTIPLIED],
        "shader": mat[c4d.MATERIAL_ALPHA_SHADER],
        "soft": mat[c4d.MATERIAL_ALPHA_SOFT],
    }


def collect_any_info(mat):
    print("MATERIAL_ANY has no attributes.")
    return {
    }


def collect_glow_info(mat):
    return {
        "brightness": mat[c4d.MATERIAL_GLOW_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_GLOW_COLOR],
        "frequency": mat[c4d.MATERIAL_GLOW_FREQUENCY],
        "inner_strength": mat[c4d.MATERIAL_GLOW_INNERSTRENGTH],
        "outer_strength": mat[c4d.MATERIAL_GLOW_OUTERSTRENGTH],
        "radius": mat[c4d.MATERIAL_GLOW_RADIUS],
        "random": mat[c4d.MATERIAL_GLOW_RANDOM],
        "use_material_color": mat[c4d.MATERIAL_GLOW_USEMATERIALCOLOR],
    }


def collect_diffusion_info(mat):
    return {
        "affect_luminance": mat[c4d.MATERIAL_DIFFUSION_AFFECT_LUMINANCE],
        "affect_reflection": mat[c4d.MATERIAL_DIFFUSION_AFFECT_REFLECTION],
        "affect_specular": mat[c4d.MATERIAL_DIFFUSION_AFFECT_SPECULAR],
        "brightness": mat[c4d.MATERIAL_DIFFUSION_BRIGHTNESS],
        "shader": mat[c4d.MATERIAL_DIFFUSION_SHADER],
        "texture_mixing": mat[c4d.MATERIAL_DIFFUSION_TEXTUREMIXING],
        "texture_strength": mat[c4d.MATERIAL_DIFFUSION_TEXTURESTRENGTH],
    }


def collect_specular_color_info(mat):
    print("SPECULAR_COLOR has no info - needs investigation")
    return {
    }


def collect_reflection_info(mat):
    return {
        "accuracy": mat[c4d.MATERIAL_REFLECTION_ACCURACY],
        "additive": mat[c4d.MATERIAL_REFLECTION_ADDITIVE],
        "anisotropy": mat[c4d.MATERIAL_REFLECTION_ANISOTROPY],
        "brightness": mat[c4d.MATERIAL_REFLECTION_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_REFLECTION_COLOR],
        "dispersion": mat[c4d.MATERIAL_REFLECTION_DISPERSION],
        "dispersion_ex": mat[c4d.MATERIAL_REFLECTION_DISPERSION_EX],
        "distribution": mat[c4d.MATERIAL_REFLECTION_DISTRIBUTION],
        "distribution_anisotropic": mat[c4d.MATERIAL_REFLECTION_DISTRIBUTION_ANISOTROPIC],
        "distribution_beckmann": mat[c4d.MATERIAL_REFLECTION_DISTRIBUTION_BECKMANN],
        "distribution_blinn": mat[c4d.MATERIAL_REFLECTION_DISTRIBUTION_BLINN],
        "distribution_simple": mat[c4d.MATERIAL_REFLECTION_DISTRIBUTION_SIMPLE],
        "distribution_ward": mat[c4d.MATERIAL_REFLECTION_DISTRIBUTION_WARD],
        "max_samples": mat[c4d.MATERIAL_REFLECTION_MAXSAMPLES],
        "min_samples": mat[c4d.MATERIAL_REFLECTION_MINSAMPLES],
        "orientation": mat[c4d.MATERIAL_REFLECTION_ORIENTATION],
        "shader": mat[c4d.MATERIAL_REFLECTION_SHADER],
        "shader_anisotropy": mat[c4d.MATERIAL_REFLECTION_SHADER_ANISOTROPY],
        "shader_dispersion": mat[c4d.MATERIAL_REFLECTION_SHADER_DISPERSION],
        "shader_orientation": mat[c4d.MATERIAL_REFLECTION_SHADER_ORIENTATION],
        "texture_mixing": mat[c4d.MATERIAL_REFLECTION_TEXTUREMIXING],
        "texture_strength": mat[c4d.MATERIAL_REFLECTION_TEXTURESTRENGTH],
        "use_bump": mat[c4d.MATERIAL_REFLECTION_USE_BUMP],
    }


def collect_environment_info(mat):
    return {
        "brightness": mat[c4d.MATERIAL_ENVIRONMENT_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_ENVIRONMENT_COLOR],
        "exclusive": mat[c4d.MATERIAL_ENVIRONMENT_EXCLUSIVE],
        "shader": mat[c4d.MATERIAL_ENVIRONMENT_SHADER],
        "texture_mixing": mat[c4d.MATERIAL_ENVIRONMENT_TEXTUREMIXING],
        "texture_strength": mat[c4d.MATERIAL_ENVIRONMENT_TEXTURESTRENGTH],
        "tiles_x": mat[c4d.MATERIAL_ENVIRONMENT_TILESX],
        "tiles_y": mat[c4d.MATERIAL_ENVIRONMENT_TILESY],
    }


def collect_color_info(mat):
    return {
        "brightness": mat[c4d.MATERIAL_COLOR_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_COLOR_COLOR],
        "diffuse_falloff": mat[c4d.MATERIAL_COLOR_DIFFUSEFALLOFF],
        "diffuse_level": mat[c4d.MATERIAL_COLOR_DIFFUSELEVEL],
        "model": mat[c4d.MATERIAL_COLOR_MODEL],
        "model_lambertian": mat[c4d.MATERIAL_COLOR_MODEL_LAMBERTIAN],
        "model_orennayar": mat[c4d.MATERIAL_COLOR_MODEL_ORENNAYAR],
        "roughness": mat[c4d.MATERIAL_COLOR_ROUGHNESS],
        "shader": mat[c4d.MATERIAL_COLOR_SHADER],
        "texture_mixing": mat[c4d.MATERIAL_COLOR_TEXTUREMIXING],
        "texture_strength": mat[c4d.MATERIAL_COLOR_TEXTURESTRENGTH],
    }


def collect_specular_info(mat):
    return {
        "brightness": mat[c4d.MATERIAL_SPECULAR_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_SPECULAR_COLOR],
        "falloff": mat[c4d.MATERIAL_SPECULAR_FALLOFF],
        "height": mat[c4d.MATERIAL_SPECULAR_HEIGHT],
        "inner_width": mat[c4d.MATERIAL_SPECULAR_INNERWIDTH],
        "mode": mat[c4d.MATERIAL_SPECULAR_MODE],
        "mode_colored": mat[c4d.MATERIAL_SPECULAR_MODE_COLORED],
        "mode_metal": mat[c4d.MATERIAL_SPECULAR_MODE_METAL],
        "mode_plastic": mat[c4d.MATERIAL_SPECULAR_MODE_PLASTIC],
        "shader": mat[c4d.MATERIAL_SPECULAR_SHADER],
        "texture_mixing": mat[c4d.MATERIAL_SPECULAR_TEXTUREMIXING],
        "texture_strength": mat[c4d.MATERIAL_SPECULAR_TEXTURESTRENGTH],
        "width": mat[c4d.MATERIAL_SPECULAR_WIDTH],
    }


def collect_fog_info(mat):
    return {
        "brightness": mat[c4d.MATERIAL_FOG_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_FOG_COLOR],
        "distance": mat[c4d.MATERIAL_FOG_DISTANCE],
    }


def collect_transparency_info(mat):
    return {
        "absorption_color": mat[c4d.MATERIAL_TRANSPARENCY_ABSORPTIONCOLOR],
        "aborption_distance": mat[c4d.MATERIAL_TRANSPARENCY_ABSORPTIONDISTANCE],
        "accuracy": mat[c4d.MATERIAL_TRANSPARENCY_ACCURACY],
        "additive": mat[c4d.MATERIAL_TRANSPARENCY_ADDITIVE],
        "brightness": mat[c4d.MATERIAL_TRANSPARENCY_BRIGHTNESS],
        "color": mat[c4d.MATERIAL_TRANSPARENCY_COLOR],
        "dispersion": mat[c4d.MATERIAL_TRANSPARENCY_DISPERSION],
        "dispersion_ex": mat[c4d.MATERIAL_TRANSPARENCY_DISPERSION_EX],
        "exit_color": mat[c4d.MATERIAL_TRANSPARENCY_EXITCOLOR],
        "exit_reflections": mat[c4d.MATERIAL_TRANSPARENCY_EXITREFLECTIONS],
        "fresnel": mat[c4d.MATERIAL_TRANSPARENCY_FRESNEL],
        "fresnel_reflectivity": mat[c4d.MATERIAL_TRANSPARENCY_FRESNELREFLECTIVITY],
        "max_samples": mat[c4d.MATERIAL_TRANSPARENCY_MAXSAMPLES],
        "min_samples": mat[c4d.MATERIAL_TRANSPARENCY_MINSAMPLES],
        "refraction": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION],
        "refraction_preset": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET],
        "refraction_preset_beer": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_BEER],
        "refraction_preset_custom": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_CUSTOM],
        "refraction_preset_diamond": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_DIAMOND],
        "refraction_preset_emerald": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_EMERALD],
        "refraction_preset_ethanol": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_ETHANOL],
        "refraction_preset_glass": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_GLASS],
        "refraction_preset_jade": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_JADE],
        "refraction_preset_milk": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_MILK],
        "refrection_preset_oil_vegetable": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_OIL_VEGETABLE],
        "refraction_preset_pearl": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_PEARL],
        "refraction_preset_pet": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_PET],
        "refraction_preset_plexiglass": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_PLEXIGLASS],
        "refraction_preset_ruby": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_RUBY],
        "refrection_preset_sapphire": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_SAPPHIRE],
        "refraction_preset_water": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_WATER],
        "refraction_preset_water_ice": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_WATER_ICE],
        "refreaction_preset-whiskey": mat[c4d.MATERIAL_TRANSPARENCY_REFRACTION_PRESET_WHISKEY],
        "shader": mat[c4d.MATERIAL_TRANSPARENCY_SHADER],
        "texture_mixing": mat[c4d.MATERIAL_TRANSPARENCY_TEXTUREMIXING],
        "texture_strength": mat[c4d.MATERIAL_TRANSPARENCY_TEXTURESTRENGTH],
    }
