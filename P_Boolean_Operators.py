
import bpy

class Boolean_OP(bpy.types.Operator):
    bl_idname = "addon.boolean_operator"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.bool_uv_sync:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.context.area.ui_type = 'UV'
            bpy.context.scene.tool_settings.use_uv_select_sync = True
            bpy.context.area.ui_type = 'VIEW_3D' 
            print("UV Sync True")
        else:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.context.area.ui_type = 'UV'
            bpy.context.scene.tool_settings.use_uv_select_sync = False
            bpy.context.area.ui_type = 'VIEW_3D'
            print("UV Sync False")
        return {'FINISHED'}

class Boolean_Origin_OP(bpy.types.Operator):
    bl_idname = "addon.boolean_origin"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.bool_set_origin:
            bpy.context.scene.tool_settings.use_transform_data_origin = True
    
            print("UV Sync True")
        else:
            bpy.context.scene.tool_settings.use_transform_data_origin = False
            print("UV Sync False")
        return {'FINISHED'}

class Boolean_follow_uv_data_OP(bpy.types.Operator):
    bl_idname = "addon.follow_uvdata"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.bool_follow_uv_data:

            bpy.context.scene.tool_settings.use_transform_correct_face_attributes = True
            
            print("Correct face attricutes = True")
        else:
            bpy.context.scene.tool_settings.use_transform_correct_face_attributes = False

            print("Correct face attricutes = False")
        return {'FINISHED'}

    
class Boolean_keep_uv_conect_OP(bpy.types.Operator):
    bl_idname = "addon.keep_uv_conect"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.bool_keep_uv_conect:
            bpy.context.scene.tool_settings.use_transform_correct_keep_connected = True

            
            print("Keep_UV_Conect = True")
        else:
            bpy.context.scene.tool_settings.use_transform_correct_keep_connected = False


            print("Keep_UV_Conect = False")
        return {'FINISHED'}

class Boolean_OverayShape_OP(bpy.types.Operator):
    bl_idname = "addon.show_overayshape"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.bool_overayshape:
            bpy.context.space_data.overlay.show_edge_sharp = True
            
            print("Enble overay shape edge")
        else:
            bpy.context.space_data.overlay.show_edge_sharp = False

            print("Disble overay shape edge")
        return {'FINISHED'}

class Boolean_OveraySeamUV_OP(bpy.types.Operator):
    bl_idname = "addon.show_overayseam"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.bool_overayseam:
            bpy.context.space_data.overlay.show_edge_seams = True
            
            print("Enble overay seam UV")
        else:
            bpy.context.space_data.overlay.show_edge_seams = False

            print("Disble overay seam UV")
        return {'FINISHED'}

classes = [Boolean_OP,Boolean_Origin_OP,Boolean_follow_uv_data_OP,Boolean_keep_uv_conect_OP,Boolean_OverayShape_OP,Boolean_OveraySeamUV_OP]

def register():
 
    for cls in classes:
        bpy.utils.register_class(cls)
      

def unregister():
    
    for cls in classes:
        bpy.utils.unregister_class(cls)    

