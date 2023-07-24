import bpy
import mathutils

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

    bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1})
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
        
def settexel_512(self, context): 
    scene = context.scene       
    try:
        scene.td.units = "1"
        scene.td.texture_size = "1"
        bpy.ops.object.texel_density_check()
        bpy.ops.object.texel_density_set()
        bpy.ops.object.preset_set(td_value="512")
    except: pass
 
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


    