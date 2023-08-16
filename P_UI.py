import bpy
import os
import bpy.utils.previews
from . import P_View3D_Operators
from . import P_UvEditor_Operators
from . import P_Website_Operators

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
        scene = context.scene
        layout = self.layout
        Panda_Property = scene.Panda_Tools
        row = layout.row()
        if Panda_Property.option_menu_ui == "A":
            layout.label(text="Modifire", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "B":
            layout.label(text="UV Editor", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "C":  
            layout.label(text="Collider", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "D":  
            layout.label(text="Object", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "E":  
            layout.label(text="Internet", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        row = layout.row(align=True)    
        row.prop(Panda_Property, "option_menu_ui",text="", expand=True)

        if Panda_Property.option_menu_ui == "A":
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=":  Option ", icon_value=P_icons.custom_icons["custom_icon_6"].icon_id)
            
            
            if Panda_Property.option_on_off:
                row.prop(Panda_Property, "option_on_off", text="",icon="TRIA_DOWN")
                row = box.row() 
                row.prop(context.scene.tool_settings, "use_transform_correct_face_attributes", text="UV face")
                if bpy.context.scene.tool_settings.use_transform_correct_face_attributes == True:
                    row.prop(context.scene.tool_settings, "use_transform_correct_keep_connected", text="Connect")
                # row.label(text="Overay")
                row = box.row() 
                row.prop(context.space_data.overlay, "show_face_orientation", text="Backface")
                row.prop(context.space_data.overlay, "show_wireframes", text="Wireframes")
                row = box.row() 
                row.prop(context.space_data.overlay, "show_edge_seams", text="Seams")
                row.prop(context.space_data.overlay, "show_edge_sharp", text="Sharp")
                row = box.row()
                row.prop(context.space_data.overlay, "show_extra_edge_length", text="Edge length")

                row = layout.row()
            else:
                row.prop(Panda_Property, "option_on_off", text="",icon="TRIA_RIGHT")
            
            box = layout.box()
            row = box.row()
            row.label(text=": Tools", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row()
            row.prop(context.scene.tool_settings, "use_transform_data_origin", text="Set Origin", icon="OBJECT_ORIGIN")
            row = box.row()
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Transfrom").action="@_AppAllTrasfrom"
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Orient").action="@_Get_Orientation"
            row = box.row()
            row.operator(P_View3D_Operators.Empty_area.bl_idname, text="Empty", icon="EMPTY_AXIS").action="@_Add_Empty"        
            row = layout.row()

            box = layout.box()
            row = box.row()
            if Panda_Property.option_trasfrom_xyz == "Rotate":
                row.label(text="", icon_value=P_icons.custom_icons["custom_icon_8"].icon_id)
            else:
                row.label(text="", icon_value=P_icons.custom_icons["custom_icon_11"].icon_id)
            row.prop(Panda_Property, "option_trasfrom_xyz",text="list", expand=True)
            row = box.row()
            
            if Panda_Property.option_trasfrom_xyz == "Rotate":
                row.label(text=" Angle:")
                row.prop(Panda_Property, "my_rotation_angle", text="")
                row = box.row()
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="X").action="@_RotateX"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Y").action="@_RotateY"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Z").action="@_RotateZ"    
           
            if Panda_Property.option_trasfrom_xyz == "Scale":
                row.label(text=" scale:")
                row.prop(Panda_Property, "my_scale_value", text="")
                row = box.row()
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="X").action="@_RotateX"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Y").action="@_RotateY"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Z").action="@_RotateZ"    
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="XYZ").action="@_ScaleXYZ" 

            box = layout.box()
            row = box.row() 
            row.label(text="", icon_value=P_icons.custom_icons["custom_icon_12"].icon_id)
            # row.label(text=": Bevel")
            # row = box.row()
            row.prop(Panda_Property, "bevle_shape", text="Shape")
            row = box.row()
            if Panda_Property.bevle_shape:
                row.prop(Panda_Property, "bevel_offset_input_shape", text="")
                row.prop(Panda_Property, "bevel_segments_input_shape", text="")
            else:
                row.prop(Panda_Property, "bevel_offset_input_smooth", text="")
                row.prop(Panda_Property, "bevel_segments_input_smooth", text="")
            row = box.row()
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Bevel").action="@_Bevel_Custom" 
           
        
        if Panda_Property.option_menu_ui == "B":
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=": UV Status ", icon_value=P_icons.custom_icons["custom_icon_6"].icon_id)
            row = box.row()
            row.prop(context.scene.tool_settings, "use_uv_select_sync", text="UV sync")
            
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
        if Panda_Property.option_menu_ui == "C":
            row = layout.row()

            box = layout.box()
            row = box.row() 
            row.label(text=": Collider Builder", icon_value=P_icons.custom_icons["custom_icon_9"].icon_id)
            row = box.row()
            row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Make Box").action="@_MakeToBox"
            row = box.row()
            row.prop(Panda_Property, "auto_orient", text=": Auto Orient")
            row = box.row()
            row.prop(Panda_Property, "remove_reference", text=": Delete original")
            row = layout.row()
            # row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Extrude to Opposite").action="@_Extrude_to_opposite"
            box = layout.box()
            row = box.row()
            row.label(text=": Selection", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row()
            
            row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Opposite Face").action="@_Opposite_Face"
            row = layout.row()
        if Panda_Property.option_menu_ui == "D":
            row = layout.row()
            box = layout.box()
            row = box.row()
            row.label(text=": OBject preset", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row() 
            row.operator(P_View3D_Operators.Ready_made.bl_idname, text="Hexagon").action="@_Hexagon"
            row = layout.row()
        if Panda_Property.option_menu_ui == "E": 
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

             # Add a label
            layout.label(text="Web favorite")

            # Input for label and link
            layout.prop(context.scene, "website_label", text="Label")
            layout.prop(context.scene, "website_link", text="Link")
            row = layout.row()
            # Button to add website link
            row.operator("addon.add_website_link", text="Add Link")
            box = layout.box()
            # Display the list of added website links
            for idx, website_link in enumerate(context.scene.website_links):
                
                row = box.row()
                row.label(text=website_link.label)
                row.operator("addon.open_website_link", text="Open").website_index = idx
                if Panda_Property.show_remove_link:
                    row.operator("addon.remove_website_link", text="",icon="TRASH").website_index = idx
                
            
            row = layout.row()
            row.prop(Panda_Property, "show_remove_link", text="Remove link")
    

class UV_PT_Panda(bpy.types.Panel):

    bl_label = ""
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = '🐼'
    def draw_header(self, context): 
        
        self.layout.label(text="UV Editor", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        Panda_Property = scene.Panda_Tools
        row = layout.row()
        box = layout.box()
        row = box.row() 
        row.label(text=": UV Unwrap ", icon_value=P_icons.custom_icons["custom_icon_7"].icon_id)
        row = box.row() 
        row.label(text="Texel set :")
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon="REMOVE").action="@_Texel_value_reduce" 
        row.prop(Panda_Property, "uv_texel_value")
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon= "ADD").action="@_Texel_value_increase" 
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
        # row.prop(Panda_Property, "uv_offset", text="Offset new pack")
        row = layout.row()

classes = [VIEW3D_PT_Panda,UV_PT_Panda]

def register():

    
    for cls in classes:
        bpy.utils.register_class(cls)
      
def unregister():
      
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
