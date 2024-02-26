import bpy


active_object = bpy.context.active_object
color_attribute_name = "Mask_Color"
if active_object and active_object.type == 'MESH':
    if color_attribute_name not in active_object.data.attributes:
         
#if color_attribute_add is None:
        bpy.ops.geometry.color_attribute_add(name="Mask_Color", color = (1,1,1,1))
    else:
        print(" Mask_Color : already exist")

Material_name = "Bake Mask"
material = bpy.data.materials.get(Material_name)
if material is None:
    new_material = bpy.data.materials.new(name= Material_name)

    new_material.use_nodes = True

    shader_node = new_material.node_tree.nodes["Principled BSDF"]

    vertex_color_node = new_material.node_tree.nodes.new(type='ShaderNodeVertexColor')
    vertex_color_layer_name = "Mask_Color"

    new_material.node_tree.links.new(vertex_color_node.outputs["Color"], shader_node.inputs["Base Color"])
    vertex_color_node.layer_name = vertex_color_layer_name
    
    new_material.node_tree.nodes.new(type='ShaderNodeTexImage')