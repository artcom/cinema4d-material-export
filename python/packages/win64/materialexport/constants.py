'''A collection of used constants, together with friendly names'''
import c4d

MATERIAL_CHANNELS = {
    "color": c4d.CHANNEL_COLOR,
    "luminance": c4d.CHANNEL_LUMINANCE,
    "transparency": c4d.CHANNEL_TRANSPARENCY,
    "reflection": c4d.CHANNEL_REFLECTION,
    "environment": c4d.CHANNEL_ENVIRONMENT,
    "fog": c4d.CHANNEL_FOG,
    "bump": c4d.CHANNEL_BUMP,
    "alpha": c4d.CHANNEL_ALPHA,
    "specular": c4d.CHANNEL_SPECULAR,
    "specular_color": c4d.CHANNEL_SPECULARCOLOR,
    "glow": c4d.CHANNEL_GLOW,
    "displacement": c4d.CHANNEL_DISPLACEMENT,
    "diffusion": c4d.CHANNEL_DIFFUSION,
    "normal": c4d.CHANNEL_NORMAL,
    "any": c4d.CHANNEL_ANY
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
