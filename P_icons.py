import bpy.utils.previews
import os

custom_icons = None



def register():
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    addon_path =  os.path.dirname(__file__)
    icons_dir = os.path.join(addon_path, "icons")

    custom_icons.load("custom_icon_1", os.path.join(icons_dir, "icon1.png"), 'IMAGE')
  

def unregister():
    global custom_icons
    bpy.utils.previews.remove(custom_icons)

    