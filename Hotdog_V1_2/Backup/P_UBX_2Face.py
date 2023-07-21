import bpy

# Get the active object
obj = bpy.context.active_object

# Separate the object into its own object
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
