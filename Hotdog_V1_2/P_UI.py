import bpy
from . import P_Operators
class Panda_modifyer(bpy.types.Panel):
    
    bl_idname = "VIEW3D_PT_tool"
    bl_label = "🐼"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '🐼'
    # bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        scene = context.scene
       

        layout = self.layout
        row = layout.row()
        row.operator(P_Operators.Empty_area.bl_idname, text="Empty", icon="EMPTY_AXIS").action="@_Add_Empty"        
        row.operator(P_Operators.Empty_area.bl_idname, text="Socket", icon="EMPTY_ARROWS").action="@_Setup_Socket"
        row = layout.row()
        row.label(text="90°")
        
        row.operator(P_Operators.Speed_process.bl_idname, text="X").action="@_RotateX90"
        row.operator(P_Operators.Speed_process.bl_idname, text="Y").action="@_RotateY90"
        row.operator(P_Operators.Speed_process.bl_idname, text="Z").action="@_RotateZ90"
        row = layout.row()   
        row.operator(P_Operators.Speed_process.bl_idname, text="Set Orient", icon="ORIENTATION_GLOBAL").action="@_Get_Orientation"
        row = layout.row()  
        row.operator(P_Operators.Speed_process.bl_idname, text="Quick UV", icon="UV").action="@_Quick_UV"  
        row.operator(P_Operators.Speed_process.bl_idname, text="Align_Auto").action="@_Align_Auto"  
        row = layout.row()
        row.label(text="Collider Builder")
        row = layout.row()
        row.operator(P_Operators.Box_Builder.bl_idname, text="UBX").action="@_Create_UBX"
        row.prop(context.scene, "my_bool_prop", text="", icon="TRASH")
        row = layout.row()
        
           



classes = [Panda_modifyer,]

def register():
    
    for cls in classes:
        bpy.utils.register_class(cls)
    
    

def unregister():
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
    