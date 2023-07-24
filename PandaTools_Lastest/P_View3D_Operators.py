import bpy
import math
import mathutils
from bpy.types import Scene
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from . import P_Funtion
   
class MyProperties(PropertyGroup):
    saveList : StringProperty(name="Save List")

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

        elif self.action == "@_Setup_Socket": 
            self.Setup_Socket(self, context)
        else:
            print("Empty area has no action")

        return {'FINISHED'}
    
    @staticmethod
    def Add_Empty(self, context):
        scene = context.scene
        try:
            bpy.ops.view3d.snap_cursor_to_selected()
            bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.context.object.name = "COM_"
            bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
            bpy.ops.view3d.snap_cursor_to_center()  
        except:
            self.report({'ERROR'}, "For object mode only.")

        print("Add_Empty")
        return {'FINISHED'}
    
    @staticmethod
    def Setup_Socket(self, context):
        scene = context.scene
        context = bpy.context 
            
        if bpy.context.active_object.mode == 'OBJECT': 
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            P_Funtion.GetBiggestFace()
            bpy.ops.view3d.snap_cursor_to_selected()

            
        try:
            bpy.context.scene.transform_orientation_slots[0].type
            bpy.ops.transform.delete_orientation()
            bpy.ops.transform.create_orientation(name='Face', use=True)
        except:
            bpy.ops.transform.create_orientation(name='Face', use=True)

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.empty_add(type='ARROWS', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "Socket_"
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)    
        bpy.ops.transform.transform(mode='ALIGN', orient_type='Face')
        bpy.ops.view3d.snap_cursor_to_center()   

        print("Added_Socket")
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
        
        else:
             print("worng")

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
        
        else:
            print("UV_quick has no action")

        
        return {'FINISHED'}
        
    
    @staticmethod
    def ShapToSeam(self, context):
        bpy.ops.mesh.edges_select_sharp()
        bpy.ops.mesh.mark_seam(clear=False)

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

        if self.action == "@_Create_UBX": 
            self.Create_UBX(self, context)
        else:
            print("Empty area has no action")

        return {'FINISHED'}
    
    @staticmethod
    def Create_UBX(self, context):
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
            # Find and select the biggest  face
            if obj.type != 'MESH':
                continue
            # Get the face with the maximum area
            max_area = 0
            max_face_index = None

            for face_index, face in enumerate(obj.data.polygons):
                area = face.area
                if area > max_area:
                    max_area = area
                    max_face_index = face_index

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')
            
            # Select the biggest face
            if max_face_index is not None:
                obj.data.polygons[max_face_index].select = True
                bpy.ops.object.mode_set(mode='EDIT')  
                P_Funtion.SetOriantface() 
            #_________________________________________________________________________ 
            # Turn on setting transform origin and align to origin
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                bpy.context.scene.tool_settings.use_transform_data_origin = True
                bpy.ops.transform.transform(mode='ALIGN', orient_type='Face')
                bpy.context.scene.tool_settings.use_transform_data_origin = False        
                #_________________________________________________________________________
            P_Funtion.BoundingToBox()
            # set name new box after BoundingToBox
            bpy.context.object.name = "UBX_"
              # Assign material named Color_Collider
            #  Get the active object
            obj = bpy.context.active_object
            material_name = "Color_Collider"
            material = bpy.data.materials.get(material_name)

            # If material doesn't exist, create a new material
            if material is None:
                material = bpy.data.materials.new(name=material_name)
               
            material.diffuse_color = (0.385147, 0.8, 0.31554, 1)

            # Assign the material to the object
            if obj.data.materials:
                obj.data.materials[0] = material
            else:
                obj.data.materials.append(material)
                # _________________________________________________________________________ 
            P_Funtion.MoveObjectToCollection()
            obj.select_set(False)

            # delete object referent if checck box = True
        if context.scene.remove_reference:  
            for obj_name in object_names:
                obj = bpy.data.objects.get(obj_name)
                if obj:
                    bpy.data.objects.remove(obj, do_unlink=True)
        
        print(" Created UBX") 
        
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


    
classes = [Empty_area, Speed_process,Uv, Box_Builder, MyProperties,Ready_made]

def register():
    bpy.types.Scene.remove_reference= bpy.props.BoolProperty(name="Remove referent object")
    bpy.types.Scene.my_rotation_angle = bpy.props.FloatProperty(
        name="My Rotation Angle",
        description="Input any number with a maximum value of 360",
        default=90.0,
        min=-360.0,
        max=360.0,
    )
    for cls in classes:
        bpy.utils.register_class(cls)
    Scene.PandaTools = PointerProperty(type= MyProperties)

def unregister():
    del bpy.types.Scene.remove_reference
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del Scene.PandaTools



