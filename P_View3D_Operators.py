import bpy
import math
from bpy.types import Scene
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from . import P_Funtion

   
class MyProperties(PropertyGroup):
    saveList : StringProperty(name="Save List")

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

        if self.action == "@_RotateX": 
            self.X_axis(self, context)

        elif self.action == "@_RotateY": 
            self.Y_axis(self, context)

        elif self.action == "@_RotateZ": 
            self.Z_axis(self, context)  
        
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
        bevel_offset_shape = (context.scene.bevel_offset_input_shape)
        bevel_segments_shape = (context.scene.bevel_segments_input_shape)

        bevel_offset_smooth = (context.scene.bevel_offset_input_smooth)
        bevel_segments_smooth = (context.scene.bevel_segments_input_smooth)

        bpy.ops.mesh.mark_sharp(clear=True)
        if context.scene.bevle_shape:
             bpy.ops.mesh.bevel(offset=bevel_offset_shape, segments=bevel_segments_shape ,profile=1)
        else:
            bpy.ops.mesh.bevel(offset=bevel_offset_smooth, segments=bevel_segments_smooth ,profile=0.5)
            
        print("Bevel_Custom")
        return {'FINISHED'}
    
    @staticmethod
    def Appy_all_trasfrom(self, context):

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        print("Appy all trasfrom")
        return {'FINISHED'}
    
    @staticmethod
    def X_axis(self, context):
        scene = context.scene
        obj = context.active_object
        rotation_angle = math.radians(context.scene.my_rotation_angle)
        if obj.mode == 'OBJECT':
            obj.rotation_euler.x += rotation_angle
        elif obj.mode == 'EDIT':
            orient_type = bpy.context.scene.transform_orientation_slots[0].type
            bpy.ops.transform.rotate(value=rotation_angle, orient_axis='X', orient_type=orient_type)

        print("Rotated X axis")
        return {'FINISHED'}
    
    @staticmethod
    def Y_axis(self, context):
        scene = context.scene
        obj = context.active_object
        rotation_angle = math.radians(context.scene.my_rotation_angle)
        if obj.mode == 'OBJECT':
            obj.rotation_euler.y += rotation_angle
        elif obj.mode == 'EDIT':
            orient_type = bpy.context.scene.transform_orientation_slots[0].type
            bpy.ops.transform.rotate(value=rotation_angle, orient_axis='Y', orient_type=orient_type)

        print("Rotated Y axis")
        return {'FINISHED'}
    
    @staticmethod
    def Z_axis(self, context):
        scene = context.scene
        obj = context.active_object
        rotation_angle = math.radians(context.scene.my_rotation_angle)

        if obj.mode == 'OBJECT':
            obj.rotation_euler.z += rotation_angle
        elif obj.mode == 'EDIT':
            orient_type = bpy.context.scene.transform_orientation_slots[0].type
            bpy.ops.transform.rotate(value=rotation_angle, orient_axis='Z', orient_type=orient_type)

        print("Rotated Z axis")
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
        
        else:
            print("UV_quick has no action")

        
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
            
            # bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin = distance)
            bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
            bpy.ops.uv.align_rotation(method='AUTO')
            bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=distance)
            P_Funtion.settexel_512(self, context)
            bpy.context.area.ui_type = 'VIEW_3D'
            
        elif bpy.context.active_object.mode == 'OBJECT': 

            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.context.area.ui_type = 'UV'
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin = distance)
            bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
            bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=distance)
            P_Funtion.settexel_512(self, context)
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
            if context.scene.remove_reference:  
                for obj_name in object_names:
                    obj = bpy.data.objects.get(obj_name)
                    if obj:
                        bpy.data.objects.remove(obj, do_unlink=True)
            print(" Created UBX") 

        if bpy.context.active_object.mode == 'EDIT':
            if context.scene.remove_reference == False:  
                bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
            P_Funtion.GetFaceSeperated()
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            selected_objects = bpy.context.selected_objects
            object_names = []
            for obj in selected_objects:
                object_names.append(obj.name)
                
            if context.scene.auto_orient:
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


    
classes = [Empty_area, Speed_process,Uv, Box_Builder, MyProperties,Ready_made,ExampleClass]

def register():
    bpy.types.Scene.uv_sync= bpy.props.BoolProperty(name="Uv Sync selection",default=False)
    bpy.types.Scene.auto_orient= bpy.props.BoolProperty(name="Auto Orient",default=True)
    bpy.types.Scene.remove_reference= bpy.props.BoolProperty(name="Remove referent object")
    bpy.types.Scene.bevle_shape= bpy.props.BoolProperty(name="bevel Shape",default=False)
    
    bpy.types.Scene.my_rotation_angle = bpy.props.FloatProperty(
        name="My Rotation Angle",
        description="Input any number with a maximum value of 360",
        default=90.0,
        min=-360.0,
        max=360.0,
    )
    bpy.types.Scene.bevel_offset_input_shape = bpy.props.FloatProperty(
        name="Bevel Offset Input Shape",
        description="Input offset",
        default=0.1,
        min=0.0,
        max=10.0,
    )
    bpy.types.Scene.bevel_segments_input_shape = bpy.props.IntProperty(
        name="Bevel segments Input Shape",
        description="Input segments",
        default= 2,
        min=0,
        max=10,
    )
    
    bpy.types.Scene.bevel_offset_input_smooth = bpy.props.FloatProperty(
        name="Bevel Offset Input Smooth",
        description="Input offset",
        default=0.02,
        min=0.0,
        max=10.0,
    )
    bpy.types.Scene.bevel_segments_input_smooth = bpy.props.IntProperty(
        name="Bevel segments Input smooth",
        description="Input segments",
        default= 1,
        min=0,
        max=10,
    )
    for cls in classes:
        bpy.utils.register_class(cls)
    Scene.PandaTools = PointerProperty(type= MyProperties)

def unregister():
    del bpy.types.Scene.uv_sync
    del bpy.types.Scene.auto_orient
    del bpy.types.Scene.remove_reference
    del bpy.types.Scene.bevle_shape
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del Scene.PandaTools



