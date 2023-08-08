import bpy

from bpy.types import Scene
from bpy.types import (PropertyGroup)
from bpy.props import (EnumProperty, PointerProperty, StringProperty, FloatVectorProperty, FloatProperty, IntProperty, BoolProperty)

def bool_keep_uv_conect(self, context): 
    scene = context.scene
    PandaTools = scene.Panda_Tools
    print("test")
    # bpy.ops.addon.keep_uv_conect()
    if PandaTools.bool_keep_uv_conect == True :
        bpy.context.scene.tool_settings.use_transform_correct_keep_connected = True
        
        print("Keep_UV_Conect = True")
    elif PandaTools.bool_keep_uv_conect == False:
        bpy.context.scene.tool_settings.use_transform_correct_keep_connected = False

        print("Keep_UV_Conect = False")
    
   

class MyProperties(PropertyGroup):
    bool_keep_uv_conect: bpy.props.BoolProperty(
        name="keep uv conect",
        description="Turn on/off keep uv conect",
        default=True,
        update=bool_keep_uv_conect
    )
classes = [MyProperties]
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    Scene.Panda_Tools = PointerProperty(type= MyProperties)
   


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del Scene.Panda_Tools
