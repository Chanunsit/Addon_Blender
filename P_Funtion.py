import bpy
import bmesh
import mathutils
import os
import shutil

from . import P_icons
def report_message(message, type='INFO'):
    bpy.ops.wm.popup_menu(message=message, title="Message", icon=type,icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
    # bpy.ops.wm.popup_menu(message=message, title="Message", icon=type, icon_value=bpy.data.images.load(icon_path).icon_id)

def GetBiggestFace():
    # Get the active object
    obj = bpy.context.active_object

    # Ensure the object is a mesh
    if obj.type != 'MESH':
        raise ValueError("Selected object is not a mesh.")

    # Get the face with the maximum area
    max_area = 0
    max_face_index = None

    for face_index, face in enumerate(obj.data.polygons):
        area = face.area
        if area > max_area:
            max_area = area
            max_face_index = face_index

    # Deselect all faces
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    # Select the biggest face
    if max_face_index is not None:
        obj.data.polygons[max_face_index].select = True

    # Switch to Edit Mode to see the selected face
    bpy.ops.object.mode_set(mode='EDIT')

def GetFaceSeperated():
    
    obj = bpy.context.active_object

    #   bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1})
    #bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.separate(type='SELECTED')
    bpy.ops.object.mode_set(mode='OBJECT')

    # Get the newly separated objects
    separated_objects = bpy.context.selected_objects

    # Find the active object among the separated objects
    active_separated_object = None
    for separated_object in separated_objects:
        if separated_object != obj:
            active_separated_object = separated_object
            break

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the active separated object
    if active_separated_object:
        active_separated_object.select_set(True)
        bpy.context.view_layer.objects.active = active_separated_object
        
def settexel_textool(self, context): 
    scene = context.scene 
    uv_texel_value = (context.scene.Panda_Tools.uv_texel_value)      
    try:
        bpy.context.scene.texToolsSettings.texel_get_mode = '1024'
        # print(scene.texToolsSettings.texel_set_mode)
        # if context.scene.Panda_Tools.uv_keep_position:
        #     bpy.context.scene.texToolsSettings.texel_set_mode = 'ISLAND'
        # else:
        bpy.context.scene.texToolsSettings.texel_set_mode = 'ALL'
        scene.texToolsSettings.texel_density = int(uv_texel_value) 
        bpy.ops.uv.textools_texel_density_set()
        
    except: pass

# def settexel_custom(self, context): 
#     scene = context.scene 
#     uv_texel_value = (context.scene.Panda_Tools.uv_texel_value)      
#     try:
#         scene.td.units = "1"
#         scene.td.texture_size = "1"
#         bpy.context.scene.td.density_set = str(uv_texel_value)
#         bpy.ops.object.texel_density_check()
#         bpy.ops.object.texel_density_set()
#     except: pass
 
def BoundingToBox():
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
        
        new_box = bpy.context.active_object
        new_box.dimensions = dimensions
        new_box.location = (max_coord + min_coord) / 2
        new_box.rotation_euler = selected_object.rotation_euler
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
    
def MoveObjectToCollection(): 
            
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

def SetOriantface():
    # Create Orientation form face select 
    try:
        bpy.context.scene.transform_orientation_slots[0].type
        bpy.ops.transform.delete_orientation()
        bpy.ops.transform.create_orientation(name='Face', use=True)
    except:
        bpy.ops.transform.create_orientation(name='Face', use=True)

def find_opposite_face():
    if bpy.context.mode != 'EDIT_MESH':
        print("Please enter Edit Mode with a mesh object selected.")
        return

    obj = bpy.context.edit_object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    selected_faces = [f for f in bm.faces if f.select]

    if len(selected_faces) != 1:
        print("Please select a single face.")
        report_message("One face only.", type='INFO')
        return {'FINISHED'}

    selected_face = selected_faces[0]

    # Calculate the normal vector of the selected face
    selected_normal = selected_face.normal

    # Find the closest opposite face with the opposite normal
    closest_opposite_face = None
    min_distance = float('inf')

    for face in bm.faces:
        if face.normal.dot(selected_normal) < -0.9999:
            distance = (face.calc_center_median() - selected_face.calc_center_median()).length
            if distance < min_distance:
                closest_opposite_face = face
                min_distance = distance

    if closest_opposite_face:
        # Deselect all faces
        for face in bm.faces:
            face.select = False

        closest_opposite_face.select = True  # Select the closest opposite face
        selected_face.select = True
        # Update the mesh to reflect the selection change
        bmesh.update_edit_mesh(me)

        # Extrude the selected face to the closest opposite face
        # bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (closest_opposite_face.calc_center_median() - selected_face.calc_center_median())})
        # bpy.ops.mesh.select_linked() # select the element

        print("Closest opposite face found and selected.")
    else:
        print("No opposite face found.")
        report_message("I'm not found opposite face", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id ,type='INFO')
        # report_message("Please, select a face.", icon_path, type='INFO')

def Extrude_to_opposite():
    if bpy.context.mode != 'EDIT_MESH':
        print("Please enter Edit Mode with a mesh object selected.")
        return

    obj = bpy.context.edit_object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    selected_faces = [f for f in bm.faces if f.select]

    if len(selected_faces) != 1:
        print("Please select a single face.")
        report_message("One face only.", type='INFO')
        return {'FINISHED'}

    selected_face = selected_faces[0]

    # Calculate the normal vector of the selected face
    selected_normal = selected_face.normal

    # Find the closest opposite face with the opposite normal
    closest_opposite_face = None
    min_distance = float('inf')

    for face in bm.faces:
        if face.normal.dot(selected_normal) < -0.9999:
            distance = (face.calc_center_median() - selected_face.calc_center_median()).length
            if distance < min_distance:
                closest_opposite_face = face
                min_distance = distance

    if closest_opposite_face:
        # Deselect all faces
        for face in bm.faces:
            face.select = False

        # closest_opposite_face.select = True  # Select the closest opposite face
        selected_face.select = True
        # Update the mesh to reflect the selection change
        bmesh.update_edit_mesh(me)

        # Extrude the selected face to the closest opposite face
        
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (closest_opposite_face.calc_center_median() - selected_face.calc_center_median())})
        # bpy.ops.mesh.select_linked() # select the element

        print("Closest opposite face found and selected.")
    else:
        print("No opposite face found.")
        
def TransFromToOrient_Origin():
    bpy.context.scene.tool_settings.use_transform_data_origin = True
    bpy.ops.transform.transform(mode='ALIGN')
    # bpy.ops.transform.transform(mode='ALIGN', orient_type='Face')
    bpy.context.scene.tool_settings.use_transform_data_origin = False  
    
def ObjNameToList():
    selected_objects = bpy.context.selected_objects
    # Collect object name to remove in the end 
    object_names = []
    for obj in selected_objects:
        object_names.append(obj.name)

def Assign_Material():

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

def copy_files_from_subfolder(main_folder, sub_folder):
    main_folder_path = bpy.path.abspath(main_folder)
    sub_folder_path = os.path.join(main_folder_path, sub_folder)
    
    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)
    
    if os.path.exists(sub_folder_path):
        for filename in os.listdir(sub_folder_path):
            source_file_path = os.path.join(sub_folder_path, filename)
            destination_file_path = os.path.join(main_folder_path, filename)
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied '{filename}' from subfolder to main folder.")

def SmartUnwrap(self, context):
        scene = context.scene
        value_magin = context.scene.Panda_Tools.Magin
        if bpy.context.active_object.mode == 'EDIT':
            bpy.context.area.ui_type = 'UV'
        else:
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.context.area.ui_type = 'UV'

        if context.scene.Panda_Tools.uv_keep_position:
            bpy.ops.uv.snap_cursor(target='SELECTED')
        if context.scene.Panda_Tools.pack_by_linked:
            bpy.ops.mesh.select_linked(delimit={'NORMAL'})
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=value_magin)
        bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
        bpy.ops.uv.align_rotation(method='AUTO')
        if context.scene.Panda_Tools.texel_set:
            settexel_textool(self, context)     
        bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')  
        bpy.ops.uv.snap_cursor(target='ORIGIN')

def Find_object_by_size():
    
    size_threshold = 2.0 
    for obj in bpy.context.selected_objects:
        
        if obj.type == 'MESH':
            size = max(obj.dimensions)  
            if size > size_threshold:
                
                print(f"Object Name: {obj.name}, Size: {size}")
            
# Specify the main folder and subfolder names
def focus_UV_editor_area():
    for area in [a for a in bpy.context.screen.areas if a.type == 'IMAGE_EDITOR']:
                for region in [r for r in area.regions if r.type == 'WINDOW']:
                    override = {'area':area, 'region': region}
                    bpy.ops.image.view_selected(override)