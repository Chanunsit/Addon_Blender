import bpy
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from . import P_Funtion
from . import P_Property

class MyProperties(PropertyGroup):
    saveList : StringProperty(name="Save List")

class UV_Editor(bpy.types.Operator):
    bl_idname = "uv.my_operator"
    bl_label = "My Operator"
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):
        if self.action == "@_SmartUnwrap": 
            self.SmartUnwrap(self, context)
        elif self.action == "@_RotateUV90": 
            self.RotateUV90(self, context)
        elif self.action == "@_AlignEdgeUV": 
            self.AlignEdgeUV(self, context)
        elif self.action == "@_PackUV_Together": 
            self.PackUV_Together(self, context)
        elif self.action == "@_Texel_value_increase": 
            self.Texel_value_increase(self, context)
        elif self.action == "@_Texel_value_reduce": 
            self.Texel_value_reduce(self, context)
        else:
             print("")

        return {'FINISHED'}
    
    @staticmethod
    def SmartUnwrap(self, context):
        scene = context.scene
        uv_texel_value = (context.scene.Panda_Tools.uv_texel_value)

        bpy.ops.uv.snap_cursor(target='SELECTED')
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.05)
        bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
        bpy.ops.uv.align_rotation(method='AUTO')
        bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')
        P_Funtion.settexel_custom(self, context)

        # P_Funtion.settexel_512(self, context)
        bpy.ops.uv.snap_cursor(target='ORIGIN')

        
        print("Unwraped")
        return {'FINISHED'}
    
    @staticmethod
    def RotateUV90(self, context):
        scene = context.scene
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Z')
        print("Rotated UV 90")
        return {'FINISHED'}
    
    @staticmethod
    def AlignEdgeUV(self, context):
        scene = context.scene
        bpy.ops.uv.align_rotation(method='EDGE')
        print("AlignEdgeUV")
        return {'FINISHED'}
    
    @staticmethod
    def PackUV_Together(self, context):
        scene = context.scene
        bpy.ops.uv.snap_cursor(target='SELECTED')
        bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=0.05)
        bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')
        P_Funtion.settexel_512(self, context)
        bpy.ops.uv.snap_cursor(target='ORIGIN')

        # if context.scene.Panda_Tools.uv_offset: 
        #     # Set the 3D cursor position in the Image Editor
        #     context.space_data.cursor_location[0] += 2.0
        #     context.space_data.cursor_location[1] += 0
        #     bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')
        
        print("AlignEdgeUV")
        return {'FINISHED'}
    @staticmethod
    def Texel_value_increase(self, context):
        
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        texel = int (Panda_Property.uv_texel_value) 
        if texel < 4096:
            texel *= 2
        Panda_Property.uv_texel_value = str (texel)

        print("Texel value X2")
        return {'FINISHED'}
    @staticmethod
    def Texel_value_reduce(self, context):
        
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        texel = int (Panda_Property.uv_texel_value) 
        if texel > 1:
            texel //= 2
        Panda_Property.uv_texel_value = str (texel)
        
        print("Texel value /2")
        return {'FINISHED'}




def register():
    
    bpy.utils.register_class(UV_Editor)
    bpy.utils.register_class(MyProperties)
def unregister():
    bpy.utils.unregister_class(UV_Editor)
    bpy.utils.unregister_class(MyProperties)

if __name__ == "__main__":
    register()