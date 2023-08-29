import bpy
import math
import os
from bpy.types import Scene
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from . import P_Funtion
from . import P_UI

class ExampleClass(bpy.types.Operator):
    bl_idname = "object.name"
    bl_label = "name"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = "Empty & Socket: to center of active "
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):

        if self.action == "@_name":
            self.Funtion(self, context)

        else:
            print("Descriptiont")

        return {'FINISHED'}
    
    @staticmethod
    def Add_Empty(self, context):
        scene = context.scene
      
        # Add Funtion

        print("Added_Socket")
        return {'FINISHED'}

class Empty_area(bpy.types.Operator):
    bl_idname = "object.empty_area"
    bl_label = "Empty Operator"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = "Empty & Socket: to center of active "
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):

        if self.action == "@_Add_Empty":
            self.Add_Empty(self, context)

        else:
            print("Empty area has no action")

        return {'FINISHED'}
    
    @staticmethod
    def Add_Empty(self, context):
        scene = context.scene
        try:
            if bpy.context.active_object.mode == 'OBJECT': 
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.context.object.name = "COM_"
                bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
                bpy.ops.view3d.snap_cursor_to_center() 
                 
            elif bpy.context.active_object.mode == 'EDIT': 
                bpy.ops.view3d.snap_cursor_to_selected()
                P_Funtion.SetOriantface()
                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.empty_add(type='ARROWS', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.context.object.name = "Socket_"
                bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)    
                bpy.ops.transform.transform(mode='ALIGN', orient_type='Face')
                bpy.ops.view3d.snap_cursor_to_center()   
        except:
            self.report({'ERROR'}, "For object mode only.")

        print("Add_Empty")
        return {'FINISHED'}
    


class Speed_process(bpy.types.Operator):

    bl_idname = "object.speedprocess_operator"
    bl_label = "Speed Process Operator"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = "Rotate Axis XYZ by 90°"
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")
    
    def execute(self, context):  
        bpy.context.scene.tool_settings.use_transform_correct_keep_connected = True

        if self.action == "@_RotateX": 
            self.X_axis(self, context)

        elif self.action == "@_RotateY": 
            self.Y_axis(self, context)

        elif self.action == "@_RotateZ": 
            self.Z_axis(self, context) 

        elif self.action == "@_ScaleXYZ": 
            self.XYZ_Scale(self, context)  
        
        elif self.action == "@_Get_Orientation": 
            self.Get_Orientation(self, context) 
        
        elif self.action == "@_AppAllTrasfrom": 
            self.Appy_all_trasfrom(self, context)

        elif self.action == "@_Bevel_Custom": 
            self.Bevel_Custom(self, context)
        
        else:
             print("worng")

        return {'FINISHED'}
    
    @staticmethod
    def Bevel_Custom(self, context):
        scene = context.scene
        bevel_offset_shape = (context.scene.Panda_Tools.bevel_offset_input_shape)
        bevel_segments_shape = (context.scene.Panda_Tools.bevel_segments_input_shape)

        bevel_offset_smooth = (context.scene.Panda_Tools.bevel_offset_input_smooth)
        bevel_segments_smooth = (context.scene.Panda_Tools.bevel_segments_input_smooth)

        bpy.ops.mesh.mark_sharp(clear=True)
        if context.scene.Panda_Tools.bevle_shape:
             bpy.ops.mesh.bevel(offset=bevel_offset_shape, segments=bevel_segments_shape ,profile=1)
        else:
            bpy.ops.mesh.bevel(offset=bevel_offset_smooth, segments=bevel_segments_smooth ,profile=0.5)
            
        print("Bevel_Custom")
        return {'FINISHED'}
    
    @staticmethod
    def Appy_all_trasfrom(self, context):

        # bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True, isolate_users=True)

        print("Appy all trasfrom")
        return {'FINISHED'}
    
    @staticmethod
    def X_axis(self, context):
        scene = context.scene
        obj = context.active_object
        Panda_Property = scene.Panda_Tools

        if Panda_Property.option_trasfrom_xyz == "Rotate":
            rotation_angle = math.radians(context.scene.Panda_Tools.my_rotation_angle)
            if obj.mode == 'OBJECT':
                selected_objects = bpy.context.selected_objects
                for obj in selected_objects:
                    bpy.context.view_layer.objects.active = obj 
                    bpy.ops.transform.rotate(value=rotation_angle, orient_axis='X')
                
            elif obj.mode == 'EDIT':
                orient_type = bpy.context.scene.transform_orientation_slots[0].type
                bpy.ops.transform.rotate(value=rotation_angle, orient_axis='X', orient_type=orient_type)
            
            print("Rotated X axis")

        if Panda_Property.option_trasfrom_xyz == "Scale":
            scale_value = (context.scene.Panda_Tools.my_scale_value)
            orient_type = bpy.context.scene.transform_orientation_slots[0].type
            bpy.ops.transform.resize(value=(scale_value, 1, 1))
            print("scale X axis")


        return {'FINISHED'}
    
    @staticmethod
    def Y_axis(self, context):
        scene = context.scene
        obj = context.active_object
        Panda_Property = scene.Panda_Tools

        if Panda_Property.option_trasfrom_xyz == "Rotate":
            rotation_angle = math.radians(context.scene.Panda_Tools.my_rotation_angle)
            if obj.mode == 'OBJECT':
                selected_objects = bpy.context.selected_objects
                for obj in selected_objects:
                    bpy.context.view_layer.objects.active = obj 
                    bpy.ops.transform.rotate(value=rotation_angle, orient_axis='Y')
            elif obj.mode == 'EDIT':
                orient_type = bpy.context.scene.transform_orientation_slots[0].type
                bpy.ops.transform.rotate(value=rotation_angle, orient_axis='Y', orient_type=orient_type)
            print("Rotated Y axis")

        if Panda_Property.option_trasfrom_xyz == "Scale":
            scale_value = (context.scene.Panda_Tools.my_scale_value)
            orient_type = bpy.context.scene.transform_orientation_slots[0].type
            bpy.ops.transform.resize(value=(1, scale_value, 1))
            print("scale Y axis")
        
        return {'FINISHED'}
    
    @staticmethod
    def Z_axis(self, context):
        scene = context.scene
        obj = context.active_object
        Panda_Property = scene.Panda_Tools
        if Panda_Property.option_trasfrom_xyz == "Rotate":
            rotation_angle = math.radians(context.scene.Panda_Tools.my_rotation_angle)

            if obj.mode == 'OBJECT':
                selected_objects = bpy.context.selected_objects
                for obj in selected_objects:
                    bpy.context.view_layer.objects.active = obj 
                    bpy.ops.transform.rotate(value=rotation_angle, orient_axis='Z')
            elif obj.mode == 'EDIT':
                orient_type = bpy.context.scene.transform_orientation_slots[0].type
                bpy.ops.transform.rotate(value=rotation_angle, orient_axis='Z', orient_type=orient_type)

            print("Rotated Z axis")

        if Panda_Property.option_trasfrom_xyz == "Scale":
            scale_value = (context.scene.Panda_Tools.my_scale_value)
            orient_type = bpy.context.scene.transform_orientation_slots[0].type
            bpy.ops.transform.resize(value=(1 ,1 , scale_value))
            print("scale Z axis")
        
        return {'FINISHED'}
    @staticmethod
    def XYZ_Scale(self, context):
        scale_value = (context.scene.Panda_Tools.my_scale_value)
        bpy.ops.transform.resize(value=(scale_value ,scale_value , scale_value))
        print("scale Z axis")
        return {'FINISHED'}

    @staticmethod
    def Get_Orientation(self, context):  
        try:
            bpy.context.scene.transform_orientation_slots[0].type ="Face"
            bpy.ops.transform.delete_orientation()      
        except:
            pass
        try:
            bpy.ops.transform.create_orientation(name='Face', use=True)
        except:
            self.report({'ERROR'}, "Pls Select any face")
                
                      
        return {'FINISHED'}

class Uv(bpy.types.Operator):
    bl_idname = "object.uv"
    bl_label = "UV Operator"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = " UV "
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):
    
        if self.action == "@_UV_quick":
            self.Quick_UV(self, context)
        elif self.action == "@_RotateUV90":
            self.RotateinUV90(self, context)
        elif self.action == "@_Shap_to_Seam":
            self.ShapToSeam(self, context)
        elif self.action == "@_Island_to_Seam":
            self.IslandToSeam(self, context)
        elif self.action == "@_OpenUVEditWindow":
            self.OpenUVEditWindow(self, context)
        elif self.action == "@_MakeSeam":
            self.MakeSeam(self, context)
        elif self.action == "@_ClearSeam":
            self.ClearSeam(self, context)
        elif self.action == "@_View_uv1":
            self.View_uv1(self, context)
        elif self.action == "@_View_uv2":
            self.View_uv2(self, context)
        elif self.action == "@_Set_name_uv_chanel":
            self.Set_name_uv_chanel(self, context)
        elif self.action == "@_remove_uv_chanel":
            self.remove_uv_chanel(self, context)
        elif self.action == "@_Vertex_group":
            self.Vertex_group(self, context)
        elif self.action == "@_Select_group":
            self.Select_group(self, context)
        elif self.action == "@_Clear_group":
            self.Clear_group(self, context)
        elif self.action == "@_Pack_UV":
            self.Pack_UV(self, context)
        elif self.action == "@_Hide_Select": 
            self.hide_select(self, context)
        else:
            print("UV_quick has no action")

        
        return {'FINISHED'}
    @staticmethod
    def Pack_UV(self, context):
        scene = context.scene
        value_magin = context.scene.Panda_Tools.Magin
        if context.scene.Panda_Tools.pack_by_part:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.separate(type='LOOSE')
            # -------------------------------------------
            
            bpy.ops.object.mode_set(mode='OBJECT')
            selected_objects = bpy.context.selected_objects
            value_magin = context.scene.Panda_Tools.Magin
            for obj in selected_objects:
                
                obj.data.uv_layers[0].active_render = True
                
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)

                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')

                bpy.context.area.ui_type = 'UV'    
                bpy.ops.uv.select_all(action='SELECT')

                # bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
                bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=value_magin)
                if context.scene.Panda_Tools.texel_set:    
                    P_Funtion.settexel_textool(self, context) 

                if context.space_data.cursor_location[0] <= 10:
                    context.space_data.cursor_location[0] += 1.5
                    context.space_data.cursor_location[1] += 0
                
                else:
                    
                    context.space_data.cursor_location[0] = 1.5
                    context.space_data.cursor_location[1] -= 1.5
            
                      
                bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')

                bpy.context.area.ui_type = 'VIEW_3D'
                bpy.ops.object.mode_set(mode='OBJECT')
                
            
            for obj in selected_objects:
                obj.select_set(True)

            bpy.context.view_layer.objects.active = selected_objects[0]
            bpy.ops.object.join()

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.context.area.ui_type = 'UV'
            bpy.ops.uv.select_all(action='SELECT')
                 
            bpy.ops.uv.snap_cursor(target='ORIGIN')
            bpy.context.area.ui_type = 'VIEW_3D'
        # ------------------------------------------------------------------------------------------------------------
        else:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            
            bpy.context.scene.tool_settings.use_uv_select_sync = False
            bpy.context.area.ui_type = 'UV'
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=value_magin)
            
            
            if context.scene.Panda_Tools.texel_set:
                P_Funtion.settexel_textool(self, context)      
            bpy.ops.uv.snap_cursor(target='ORIGIN')
            
            bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')
            bpy.context.scene.tool_settings.use_uv_select_sync = True
            bpy.context.area.ui_type = 'VIEW_3D'
         
        print("Pack UV")
        return {'FINISHED'}
        
        
    @staticmethod
    def hide_select(self, context):
        bpy.ops.mesh.select_linked(delimit={'NORMAL'})
        bpy.ops.mesh.hide(unselected=False)


        print("Hide Select")
        return {'FINISHED'}
    @staticmethod
    def Vertex_group(self, context):
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            # if obj.type == 'MESH':
            #     if "MyVertexGroup" not in obj.vertex_groups:
            #         obj.vertex_groups.new(name="MyVertexGroup")
                    
            #     bpy.ops.object.vertex_group_assign()
            if obj.type == 'MESH':
               
                if "MyFaceMap" not in obj.face_maps:
                    obj.face_maps.new(name="MyFaceMap")
                else:
                    obj.face_maps.active_index = 0
                bpy.ops.object.face_map_assign()
                
        print("Vertex_group")
        return {'FINISHED'}
    
    @staticmethod
    def Select_group(self, context):
        
        bpy.ops.object.face_map_select()
        # bpy.ops.object.vertex_group_select()
        print("select_group")
        return {'FINISHED'}
    
    @staticmethod
    def Clear_group(self, context):
        bpy.ops.object.face_map_remove()
        # bpy.ops.object.vertex_group_remove(all=False, all_unlocked=False)
        print("Clear_group")
        return {'FINISHED'}
    
    @staticmethod
    def MakeSeam(self, context):
        try:
           bpy.ops.mesh.mark_seam(clear=False)
        except:
            self.report({'ERROR'}, "Pls,Do in edit mode")
        
        return {'FINISHED'}
    @staticmethod
    def ClearSeam(self, context):
        try:
            bpy.ops.mesh.mark_seam(clear=True)
        except:
            self.report({'ERROR'}, "Pls,Do in edit mode")
        return {'FINISHED'}    
    
    @staticmethod
    def ShapToSeam(self, context):
        try:
            bpy.ops.mesh.edges_select_sharp()
            bpy.ops.mesh.mark_seam(clear=False)
        except:
            self.report({'ERROR'}, "Pls,Do in edit mode")
        return {'FINISHED'} 
    
    @staticmethod
    def IslandToSeam(self, context):
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.context.area.ui_type = 'UV'
        bpy.ops.uv.select_all(action='SELECT')
        bpy.ops.uv.seams_from_islands()
        bpy.context.area.ui_type = 'VIEW_3D'
        bpy.ops.object.mode_set(mode='OBJECT')


        return {'FINISHED'}
    
    @staticmethod
    def Quick_UV(self, context):
        scene = context.scene
        distance = 0.07
        if bpy.context.active_object.mode == 'EDIT':
            bpy.context.area.ui_type = 'UV'
            if context.scene.Panda_Tools.uv_keep_position:
                bpy.ops.uv.snap_cursor(target='SELECTED')
            if context.scene.Panda_Tools.pack_by_linked:
                bpy.ops.mesh.select_linked(delimit={'NORMAL'})
            
            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin = distance)
            bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
            bpy.ops.uv.align_rotation(method='AUTO')
            bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=distance)
            
            if context.scene.Panda_Tools.texel_set:
                P_Funtion.settexel_textool(self, context)
            
            bpy.context.area.ui_type = 'VIEW_3D'
            
        elif bpy.context.active_object.mode == 'OBJECT': 

            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.context.area.ui_type = 'UV'
            if context.scene.Panda_Tools.uv_keep_position:
                bpy.ops.uv.snap_cursor(target='SELECTED')
            if context.scene.Panda_Tools.pack_by_linked:
                bpy.ops.mesh.select_linked(delimit={'NORMAL'})

            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin = distance)
            bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
            bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=distance)
            
            if context.scene.Panda_Tools.texel_set:
                P_Funtion.settexel_textool(self, context)

            bpy.context.area.ui_type = 'VIEW_3D'
            bpy.ops.mesh.normals_tools(mode='RESET')
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.mesh.select_all(action='SELECT')   

        return {'FINISHED'}
    @staticmethod
    def RotateinUV90(self, context):
        scene = context.scene 
        bpy.context.area.ui_type = 'UV'
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Z')
        bpy.context.area.ui_type = 'VIEW_3D'

        return {'FINISHED'}
    @staticmethod
    def OpenUVEditWindow(self, context):
        scene = context.scene 
        bpy.ops.wm.window_new()
        bpy.context.area.ui_type = 'UV'

        
        return {'FINISHED'}
    @staticmethod
    def View_uv1(self, context):
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type == 'MESH':
                obj.data.uv_layers[0].active_render = True
                obj.data.uv_layers.active_index = 0
        return {'FINISHED'}
    @staticmethod
    def View_uv2(self, context):
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type == 'MESH':
                if len(obj.data.uv_layers) <= 1:
                    obj.data.uv_layers.new(name="uv2")
                obj.data.uv_layers[1].active_render = True
                obj.data.uv_layers.active_index = 1
        return {'FINISHED'}
    @staticmethod
    def Set_name_uv_chanel(self, context):
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type == 'MESH':
                obj.data.uv_layers[0].name = "uv1"
                obj.data.uv_layers[1].name = "uv2"
        return {'FINISHED'}
    @staticmethod
    def remove_uv_chanel(self, context):
        selected_objects = bpy.context.selected_objects

        for obj in selected_objects:
            if obj.type == 'MESH':
                # Remove UV maps with index greater than 2
                for i in range(2, len(obj.data.uv_layers)):
                    obj.data.uv_layers.remove(obj.data.uv_layers[2])
        print ("Removed UV more then 2")
        return {'FINISHED'}
class Box_Builder(bpy.types.Operator):
    bl_idname = "object.box_builder"
    bl_label = "BoxBuilder Operator"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = "Create collision"
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):

        if self.action == "@_MakeToBox": 
            self.MakeToBox(self, context)
        elif self.action == "@_Opposite_Face": 
            self.Opposite_Face(self, context)
        elif self.action == "@_Extrude_to_opposite": 
            self.Extrude_to_opposite(self, context)
        else:
            print("Empty area has no action")

        return {'FINISHED'}
    
    @staticmethod
    def MakeToBox(self, context):
        
        if bpy.context.active_object.mode == 'OBJECT':
            #  loop to run funtion to object one by one 
            selected_objects = bpy.context.selected_objects
            # Collect object name to remove in the end 
            object_names = []
            for obj in selected_objects:
                object_names.append(obj.name)

            bpy.ops.object.select_all(action='DESELECT') 
            
            for obj in selected_objects: 
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj   
                P_Funtion.GetBiggestFace() 
                P_Funtion.SetOriantface() 
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                P_Funtion.TransFromToOrient_Origin()
                P_Funtion.BoundingToBox()
                bpy.context.object.name = "UBX_"
                P_Funtion.Assign_Material()
                P_Funtion.MoveObjectToCollection()
                obj.select_set(False)

                # delete object referent if checck box = True
            if context.scene.Panda_Tools.remove_reference:  
                for obj_name in object_names:
                    obj = bpy.data.objects.get(obj_name)
                    if obj:
                        bpy.data.objects.remove(obj, do_unlink=True)
            print(" Created UBX") 

        if bpy.context.active_object.mode == 'EDIT':
            if context.scene.Panda_Tools.remove_reference == False:  
                bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            P_Funtion.GetFaceSeperated()
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            selected_objects = bpy.context.selected_objects
            object_names = []
            for obj in selected_objects:
                object_names.append(obj.name)
                
            if context.scene.Panda_Tools.auto_orient:
                P_Funtion.GetBiggestFace()
                P_Funtion.SetOriantface()
            else:
                print("pass")
            # try:
            #     bpy.context.scene.transform_orientation_slots[0].type
            #     bpy.ops.transform.delete_orientation()
            # except:
            #     pass

            bpy.ops.object.mode_set(mode='OBJECT') 
            P_Funtion.TransFromToOrient_Origin()
            P_Funtion.BoundingToBox()
            P_Funtion.Assign_Material()
            P_Funtion.MoveObjectToCollection()
            bpy.context.object.name = "UBX_"
            for obj_name in object_names:
                obj = bpy.data.objects.get(obj_name)
                if obj:
                    bpy.data.objects.remove(obj, do_unlink=True)
        return {'FINISHED'}
    
    @staticmethod
    def Opposite_Face(self, context):
        try:
            P_Funtion.find_opposite_face()
        except:
            self.report({'ERROR'}, "Pls,Select a face.")
        return {'FINISHED'}
    
    @staticmethod
    def Extrude_to_opposite(self, context):
        
        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1})
        # P_Funtion.GetFaceSeperated()
        # P_Funtion.GetBiggestFace()
        # P_Funtion.SetOriantface()
        P_Funtion.Extrude_to_opposite()
        
        
        return {'FINISHED'}
    


class Ready_made(bpy.types.Operator):
    bl_idname = "object.ready_made"
    bl_label = "Ready made Object"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = " object asset add to on surface select "
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):
         
        if self.action == "@_Hexagon":
            self.Ready_made(self, context) 
        else:
            print("")
        return {'FINISHED'}
        
    @staticmethod
    def Ready_made(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        P_Funtion.SetOriantface()
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.025,depth=0.33)
        bpy.ops.transform.transform(mode='ALIGN', orient_type='Face')
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        bpy.ops.object.editmode_toggle()
        bpy.context.area.ui_type = 'UV'
        bpy.ops.uv.select_all(action='SELECT')
        bpy.ops.uv.seams_from_islands()
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.07)
        bpy.context.area.ui_type = 'VIEW_3D'
        bpy.ops.object.mode_set(mode='OBJECT')
        
        return {'FINISHED'}


    
classes = [Empty_area, Speed_process,Uv, Box_Builder, Ready_made,ExampleClass]

def register():
   
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
 
    for cls in classes:
        bpy.utils.unregister_class(cls)
   



