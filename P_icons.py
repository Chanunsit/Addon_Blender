import bpy.utils.previews
import os

custom_icons = None



def register():
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    addon_path =  os.path.dirname(__file__)
    icons_dir = os.path.join(addon_path, "icons")

    custom_icons.load("custom_icon_1", os.path.join(icons_dir, "P_PandaFace.png"), 'IMAGE')
    custom_icons.load("custom_icon_2", os.path.join(icons_dir, "P_PandaSleep.png"), 'IMAGE')
    custom_icons.load("custom_icon_3", os.path.join(icons_dir, "P_PandaFeet.png"), 'IMAGE')
    custom_icons.load("custom_icon_4", os.path.join(icons_dir, "P_MakeSeam.png"), 'IMAGE')
    custom_icons.load("custom_icon_5", os.path.join(icons_dir, "P_Box.png"), 'IMAGE')
    custom_icons.load("custom_icon_6", os.path.join(icons_dir, "P_Light.png"), 'IMAGE')
    custom_icons.load("custom_icon_7", os.path.join(icons_dir, "P_UV.png"), 'IMAGE')
    custom_icons.load("custom_icon_8", os.path.join(icons_dir, "P_Rotate.png"), 'IMAGE')
    custom_icons.load("custom_icon_9", os.path.join(icons_dir, "P_Box_orange.png"), 'IMAGE')
def unregister():
    global custom_icons
    bpy.utils.previews.remove(custom_icons)

    