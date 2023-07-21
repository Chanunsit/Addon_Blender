import bpy
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

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "COM_"
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.view3d.snap_cursor_to_center()   

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
    bl_idname = "object.speedprocess"
    bl_label = "Speed Process Operator"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = "Rotate Axis XYZ by 90°"
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):  

        if self.action == "@_RotateX90": 
            self.X_90(self, context)

        elif self.action == "@_RotateY90": 
            self.Y_90(self, context)

        elif self.action == "@_RotateZ90": 
            self.Z_90(self, context) 

        elif self.action == "@_Quick_UV": 
            self.Quick_UV(self, context)   
        
        elif self.action == "@_Get_Orientation": 
            self.Get_Orientation(self, context) 
        
        elif self.action == "@_Align_Auto": 
            self.Align_Auto(self, context) 
        
        else:
             print("worng")

        return {'FINISHED'}
    
    @staticmethod
    def X_90(self, context):
        scene = context.scene

        bpy.ops.transform.rotate(value=1.5708, orient_axis='X')

        print("Rotated X axis 90 degree")
        return {'FINISHED'}
    
    @staticmethod
    def Y_90(self, context):
        scene = context.scene

        bpy.ops.transform.rotate(value=1.5708, orient_axis='Y')

        print("Rotated Y axis 90 degree")
        return {'FINISHED'}
    
    @staticmethod
    def Z_90(self, context):
        scene = context.scene

        bpy.ops.transform.rotate(value=1.5708, orient_axis='Z')

        print("Rotated Z axis 90 degree")
        return {'FINISHED'}
    
    @staticmethod
    def Quick_UV(self, context):
        scene = context.scene
        distanc = 0.05
        if bpy.context.active_object.mode == 'EDIT':
            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=distanc)
            bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
            bpy.ops.uv.align_rotation(method='AUTO')
            bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=distanc)
            try:
                scene.td.units = "1"
                scene.td.texture_size = "1"
                bpy.ops.object.texel_density_check()
                bpy.ops.object.texel_density_set()
                bpy.ops.object.preset_set(td_value="512")
            except: pass

            bpy.context.area.ui_type = 'VIEW_3D'     
            bpy.ops.mesh.normals_tools(mode='RESET')
            bpy.ops.mesh.normals_make_consistent(inside=False)  
            bpy.context.window.workspace = bpy.data.workspaces['UV Editing']

        
        if bpy.context.active_object.mode == 'OBJECT':
    
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')

            bpy.context.area.ui_type = 'UV'
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin= distanc)
            bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
            bpy.ops.uv.align_rotation(method='AUTO')
            bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=distanc)
            try:
                scene.td.units = "1"
                scene.td.texture_size = "1"
                bpy.ops.object.texel_density_check()
                bpy.ops.object.texel_density_set()
                bpy.ops.object.preset_set(td_value="512")
            except: pass

            bpy.context.area.ui_type = 'VIEW_3D'     
            bpy.ops.mesh.normals_tools(mode='RESET')
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.context.window.workspace = bpy.data.workspaces['UV Editing']

        return {'FINISHED'}
    @staticmethod
    def Align_Auto(self, context):
        bpy.ops.uv.align_rotation(method='AUTO')

    @staticmethod
    def Get_Orientation(self, context):
        try:
            bpy.context.scene.transform_orientation_slots[0].type ="Face"
            bpy.ops.transform.delete_orientation()
        except:
            
            bpy.ops.transform.create_orientation(name='Face', use=True)       
        return {'FINISHED'} 
       
class Box_Builder(bpy.types.Operator):
    bl_idname = "object.box_builder"
    bl_label = "BoxBuilder Operator"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = "Create box cover the selected"
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
            
                #_________________________________________________________________________
            # Find and select the biggest  face
            
            if obj.type != 'MESH':
                continue
                # raise ValueError("Selected object is not a mesh.")
               
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
                #_________________________________________________________________________ 
            # Create Orientation form face select 
                try:
                    bpy.context.scene.transform_orientation_slots[0].type
                    bpy.ops.transform.delete_orientation()
                    bpy.ops.transform.create_orientation(name='Face', use=True)
                except:
                    bpy.ops.transform.create_orientation(name='Face', use=True)
                #_________________________________________________________________________ 
            # Turn on setting transform origin and align to origin
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                bpy.context.scene.tool_settings.use_transform_data_origin = True
                bpy.ops.transform.transform(mode='ALIGN', orient_type='Face')
                bpy.context.scene.tool_settings.use_transform_data_origin = False        
                #_________________________________________________________________________
            
            #  Funtion create box from bounding box
            selected_object = bpy.context.active_object
            dimensions = selected_object.dimensions
            bounding_box = [selected_object.matrix_world @ mathutils.Vector(corner) for corner in selected_object.bound_box]

            min_coord = mathutils.Vector((min([corner.x for corner in bounding_box]),
                                        min([corner.y for corner in bounding_box]),
                                        min([corner.z for corner in bounding_box])))

            max_coord = mathutils.Vector((max([corner.x for corner in bounding_box]),
                                        max([corner.y for corner in bounding_box]),
                                        max([corner.z for corner in bounding_box])))
            
            bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
            bpy.context.object.name = "UBX_"
            new_box = bpy.context.active_object
            new_box.dimensions = dimensions
            new_box.location = (max_coord + min_coord) / 2
            new_box.rotation_euler = selected_object.rotation_euler
            # bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
              # Assign material named Color_Collider
            # Get the active object
            obj = bpy.context.active_object

            # Assign material named Color_Collider.
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
            
            # Move the UBX to new collection 
            
            obj = bpy.context.active_object

                # Check if the collection named "Collider" already exists
            collider_collection = bpy.data.collections.get("Collider")

                # Create the "Collider" collection if it doesn't exist
            if not collider_collection:
                collider_collection = bpy.data.collections.new("Collider")
                bpy.context.scene.collection.children.link(collider_collection)

                # Move the object to the "Collider" collection
            if collider_collection not in obj.users_collection:
                for collection in obj.users_collection:
                    collection.objects.unlink(obj)
                collider_collection.objects.link(obj)

            obj.select_set(False)

            # delete object referent if checck box = True
        if context.scene.my_bool_prop:  
            for obj_name in object_names:
                obj = bpy.data.objects.get(obj_name)
                if obj:
                    bpy.data.objects.remove(obj, do_unlink=True)
        
        print(" Created UBX") 
        
        return {'FINISHED'}

           
classes = [MyProperties, Empty_area, Speed_process, Box_Builder]

def register():
    bpy.types.Scene.my_bool_prop = bpy.props.BoolProperty(name="Remove referent object")
    
    for cls in classes:
        bpy.utils.register_class(cls)
    Scene.Hotdog_tools = PointerProperty(type= MyProperties)
    

def unregister():
    del bpy.types.Scene.my_bool_prop
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del Scene.Hotdog_tools

