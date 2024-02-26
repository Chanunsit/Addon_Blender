import bpy
import os
from bpy.utils import previews

custom_icons = previews.new()
icon_path = os.path.join(os.path.dirname(__file__), "icons")
for entry in os.scandir(icon_path):
    if entry.name.endswith(".png"):
        name = os.path.splitext(entry.name)[0]
        custom_icons.load(name, os.path.join(icon_path, entry.name), 'IMAGE')

    