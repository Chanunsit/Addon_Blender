import bpy
import os
from . import P_View3D_Operators
from . import P_UvEditor_Operators
from . import P_icons
from bpy.types import Menu, Operator, Panel, AddonPreferences, PropertyGroup

class VIEW3D_PT_Panda(bpy.types.Panel):  
    # bl_idname = "VIEW3D_PT_tool"
    bl_label = ""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '🐼'
    # bl_options = {"DEFAULT_CLOSED"}
    def draw_header(self, context):
        
        layout = self.layout
        row = layout.row()
        layout.label(text="Tools", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)

    def draw(self, context):
        scene = context.scene
        layout = self.layout
       
       
        box = layout.box()
        row = box.row()
        row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Set Orient", icon="ORIENTATION_GLOBAL").action="@_Get_Orientation"
        row = box.row()
        row.operator(P_View3D_Operators.Empty_area.bl_idname, text="Empty", icon="EMPTY_AXIS").action="@_Add_Empty"        
        row.operator(P_View3D_Operators.Empty_area.bl_idname, text="Socket", icon="EMPTY_ARROWS").action="@_Setup_Socket"
        
        row = layout.row()
        box = layout.box()
        row.label(text="Rotation")
        row = box.row()
        row.label(text=" Angle:")
        row.prop(context.scene, "my_rotation_angle", text="")
        row = box.row()
        row.operator(P_View3D_Operators.Speed_process.bl_idname, text="X").action="@_RotateX"
        row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Y").action="@_RotateY"
        row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Z").action="@_RotateZ"
        row = layout.row()

        box = layout.box()
        row.label(text="UV Mode")
        row = box.row() 
        row.operator(P_View3D_Operators.Uv.bl_idname, text="Shap>Seam").action="@_Shap_to_Seam"
        row.operator(P_View3D_Operators.Uv.bl_idname, text="Island>Seam").action="@_Island_to_Seam"
        row = box.row() 
        row.operator(P_View3D_Operators.Uv.bl_idname, text="Quick UV", icon="UV").action="@_UV_quick"
        row.operator(P_View3D_Operators.Uv.bl_idname, text="RotateUV").action="@_RotateUV90"
        row = box.row()
        row.operator(P_View3D_Operators.Uv.bl_idname, text="UV Window").action="@_OpenUVEditWindow"
        row = layout.row()

        row.label(text="Collider Builder")
        row = layout.row()
        box = layout.box()
        row = box.row()
        row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="UBX").action="@_Create_UBX"
        row.prop(context.scene, "remove_reference", text="", icon="TRASH")
        row = box.row()
        row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="FaceToBox").action="@_FaceToBox"
        row = layout.row()

class VIEW3D_PT_Object(bpy.types.Panel):
    # bl_idname = "ObjectReadyMade_PT_panel"
    bl_label = "🐼 Object"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '🐼'
    # bl_options = {"DEFAULT_CLOSED"}


    def draw(self, context):
        scene = context.scene
        layout = self.layout
        row = layout.row()
        row.operator(P_View3D_Operators.Ready_made.bl_idname, text="Hexagon").action="@_Hexagon"
        row = layout.row()

class UV_PT_Panda(bpy.types.Panel):
    # bl_idname = "UV_EDIT_PT_my_panel"
    bl_label = ""
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = '🐼'
    def draw_header(self, context): 
        
        self.layout.label(text="UV Editor", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        row = layout.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Smart Unwrap").action="@_SmartUnwrap"  
        row = layout.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Rotate90°").action="@_RotateUV90"  
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="AlignEdge").action="@_AlignEdgeUV" 
        row = layout.row()

        box = layout.box()
        row = box.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="PackUV").action="@_PackUV_Together"
        row = box.row()
        row.prop(context.scene, "uv_offset", text="Offset new pack")
        row = layout.row()


classes = [VIEW3D_PT_Panda,VIEW3D_PT_Object,UV_PT_Panda]

def register():
    
    for cls in classes:
        bpy.utils.register_class(cls)
      

def unregister():
  
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
