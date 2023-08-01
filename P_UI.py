import bpy
import os
import bpy.utils.previews
from . import P_View3D_Operators
from . import P_UvEditor_Operators
from . import P_Website_Operators

from . import P_icons

from bpy.types import Menu, Operator, Panel, AddonPreferences, PropertyGroup
option_tap = {
    "A": {"icon": "MODIFIER", "label": "Modify"},
    "B": {"icon": "UV_FACESEL", "label": "UV edit"},
    "C": {"icon": "FILE_3D", "label": "Box builder"},
    "D": {"icon": "SHADERFX", "label": "Object"},
    "E": {"icon": "OUTLINER_OB_VOLUME", "label": "Internet"},
    # "F": {"icon": "OUTLINER_OB_VOLUME", "label": "open appication on youre pc"} NEW!
}

class VIEW3D_PT_Panda(bpy.types.Panel):  
    # bl_idname = "VIEW3D_PT_tool"
    bl_label = ""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '🐼'
    # bl_options = {"DEFAULT_CLOSED"}
    def draw_header(self, context):
        scene = context.scene
        layout = self.layout
        row = layout.row()
        if scene.option_menu_ui == "A":
            layout.label(text="Modifire", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif scene.option_menu_ui == "B":
            layout.label(text="UV Editor", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif scene.option_menu_ui == "C":  
            layout.label(text="Collider", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif scene.option_menu_ui == "D":  
            layout.label(text="Object", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif scene.option_menu_ui == "E":  
            layout.label(text="Internet", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)


    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row(align=True)
        # row.label(text="Select Name:")
        row.prop(scene, "option_menu_ui",text="", expand=True)

        if scene.option_menu_ui == "A":
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=": Setting ", icon_value=P_icons.custom_icons["custom_icon_6"].icon_id)
            row = box.row() 
            row.prop(context.scene, "bool_set_origin", text="", icon="OBJECT_ORIGIN", emboss=True)
            row.prop(context.scene, "bool_follow_uv_data", text="", icon="UV_SYNC_SELECT", emboss=True)
            row.prop(context.scene, "bool_keep_uv_conect", text="", icon="LINKED", emboss=True)
            row = box.row() 
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Transfrom").action="@_AppAllTrasfrom"
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Orient").action="@_Get_Orientation"
            row = layout.row()
            box = layout.box()
            row = box.row()
            row.label(text="Add", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row()
            row.operator(P_View3D_Operators.Empty_area.bl_idname, text="Empty", icon="EMPTY_AXIS").action="@_Add_Empty"        
            row = layout.row()
            box = layout.box()
            row = box.row()
            row.label(text="Rotation", icon_value=P_icons.custom_icons["custom_icon_8"].icon_id)
            row = box.row()
            row.label(text=" Angle:")
            row.prop(context.scene, "my_rotation_angle", text="")
            row = box.row()
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="X").action="@_RotateX"
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Y").action="@_RotateY"
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Z").action="@_RotateZ"    
        if scene.option_menu_ui == "B":
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=": UV Status ", icon_value=P_icons.custom_icons["custom_icon_6"].icon_id)
            row = box.row() 
            row.prop(context.scene, "bool_uv_sync", text="", icon="UV_SYNC_SELECT", emboss=True)
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=": UV Seam", icon_value=P_icons.custom_icons["custom_icon_4"].icon_id)
            row = box.row() 
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Make").action="@_MakeSeam"
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Clear").action="@_ClearSeam"
            row = box.row() 
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Shap").action="@_Shap_to_Seam"
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Island").action="@_Island_to_Seam"
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=": UV Unwrap ", icon_value=P_icons.custom_icons["custom_icon_2"].icon_id)
            row = box.row() 
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Quick", icon="UV").action="@_UV_quick"
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Rotate 90").action="@_RotateUV90"
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.operator(P_View3D_Operators.Uv.bl_idname, text="UV Window").action="@_OpenUVEditWindow"
            row = layout.row()
        if scene.option_menu_ui == "C":
            row = layout.row()

            box = layout.box()
            row = box.row() 
            row.label(text=": Collider Builder", icon_value=P_icons.custom_icons["custom_icon_9"].icon_id)
            row = box.row()
            row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Make Box").action="@_MakeToBox"
            row = box.row()
            
            row.prop(context.scene, "remove_reference", text="")
            row.label(text=": Delete original")
            row = layout.row()
            box = layout.box()
            row = box.row()
            row.label(text=": Selection", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row()
            row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Opposite Face").action="@_Opposite_Face"
            row = layout.row()
        if scene.option_menu_ui == "D":
            row = layout.row()
            box = layout.box()
            row = box.row()
            row.label(text=": OBject preset", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row() 
            row.operator(P_View3D_Operators.Ready_made.bl_idname, text="Hexagon").action="@_Hexagon"
            row = layout.row()
        if scene.option_menu_ui == "E": 
            # row.label(text="Web site")
            box = layout.box()
            row = box.row()
            row.label(text="Office", icon_value=P_icons.custom_icons["custom_icon_2"].icon_id)
            row = box.row()
            row.operator(P_Website_Operators.OpenWebsiteOperator.bl_idname, text="Jira DashBoard")
            row = box.row()
            row.operator(P_Website_Operators.OpenWebsiteOperator.bl_idname, text="WorkLogPro").action="@_WorkLogPro"
            row = box.row()
            row.operator(P_Website_Operators.OpenWebsiteOperator.bl_idname, text="BackOffice").action="@_BackOffice"
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
        box = layout.box()
        row = box.row() 
        row.label(text=": UV Unwrap ", icon_value=P_icons.custom_icons["custom_icon_7"].icon_id)
        row = box.row() 
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Smart Unwrap").action="@_SmartUnwrap"  
        row = layout.row()
        box = layout.box()
        row = box.row()
        row.label(text=": UV Align ", icon_value=P_icons.custom_icons["custom_icon_8"].icon_id)
        row = box.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Rotate90°").action="@_RotateUV90"  
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="AlignEdge").action="@_AlignEdgeUV" 
        row = layout.row()

        box = layout.box()
        row = box.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="PackUV").action="@_PackUV_Together"
        row = box.row()
        row.prop(context.scene, "uv_offset", text="Offset new pack")
        row = layout.row()

def bool_property_update(self, context): 
    bpy.ops.addon.boolean_operator()
    return {'FINISHED'}
def bool_origin_update(self, context): 
    bpy.ops.addon.boolean_origin()
    return {'FINISHED'}
def bool_follow_uv_data(self, context): 
    bpy.ops.addon.follow_uvdata()
    return {'FINISHED'}
def bool_keep_uv_conect(self, context): 
    bpy.ops.addon.keep_uv_conect()
    return {'FINISHED'}

classes = [VIEW3D_PT_Panda,UV_PT_Panda]

def register():
    
    bpy.types.Scene.bool_uv_sync = bpy.props.BoolProperty(
        name="UV Sync",
        description="Turn on/off UV Sync",
        default=False,
        update=bool_property_update
    )
    bpy.types.Scene.bool_set_origin = bpy.props.BoolProperty(
        name="Set origin",
        description="Turn on/off Set origin",
        default=False,
        update=bool_origin_update
    )
    bpy.types.Scene.bool_follow_uv_data = bpy.props.BoolProperty(
        name="Correct UV data",
        description="Turn on/off UV data",
        default=False,
        update=bool_follow_uv_data
    )
    bpy.types.Scene.bool_keep_uv_conect = bpy.props.BoolProperty(
        name="keep uv conect",
        description="Turn on/off keep uv conect",
        default=False,
        update=bool_keep_uv_conect
    )
    bpy.types.Scene.option_menu_ui = bpy.props.EnumProperty(items=[(name, option_tap[name]["label"], "", option_tap[name]["icon"], i) for i, name in enumerate(option_tap.keys())])
    for cls in classes:
        bpy.utils.register_class(cls)
      

def unregister():
    del bpy.types.Scene.bool_uv_sync
    del bpy.types.Scene.bool_set_origin
    del bpy.types.Scene.bool_follow_uv_data
    del bpy.types.Scene.bool_keep_uv_conect
    del bpy.types.Scene.option_menu_ui
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
