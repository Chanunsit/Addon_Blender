import bpy
import webbrowser
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from . import P_Funtion

class Bake_material(bpy.types.Operator):
    bl_idname = "object.bakematerial"
    bl_label = "Bake Material"
    bl_icon = "CONSOLE"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI" 
    bl_description = "Bake material"
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):

        if self.action == "@_Bake":
            self.Bake(self, context)
        elif self.action == "@_Assigen_Black":
            self.AssigeMat_Black(self, context)
        elif self.action == "@_Assigen_Red":
            self.AssigeMat_Red(self, context)
        elif self.action == "@_Assigen_Green":
            self.AssigeMat_Green(self, context)
        elif self.action == "@_Assigen_Blue":
            self.AssigeMat_Blue(self, context)
        elif self.action == "@_Create_Mask_Mat":
            self.Create_Mask_Mat(self, context)
        else:
            print("Descriptiont")

        return {'FINISHED'}
    
    @staticmethod
    def Bake(self, context):
        scene = context.scene
        bpy.context.scene.render.engine = 'CYCLES'

        active_uv_map_index = context.scene.Panda_Tools.active_uv_map_index
        if bpy.context.active_object and bpy.context.active_object.type == 'MESH':
            obj = bpy.context.active_object
            if 0 <= active_uv_map_index < len(obj.data.uv_layers):
                obj.data.uv_layers.active_index = active_uv_map_index
        
        

        active_material = bpy.context.active_object.active_material

        # Check if the material already has a "Bake" image texture node
        bake_texture_node = None
        for node in active_material.node_tree.nodes:
            if node.type == 'TEX' and node.name == "Bake":
                bake_texture_node = node
                break

        # If the "Bake" texture node doesn't exist, create it
        if bake_texture_node is None:
            bake_texture_node = active_material.node_tree.nodes.new(type='ShaderNodeTexImage')
            bake_texture_node.name = "Bake"
            bake_texture_node.label = "Bake"

        # Set the properties of the "Bake" texture node as needed
        bake_texture_node.location = (0, 0)  # Set the node's location in the shader editor
        bake_texture_node.image = bpy.data.images.new(name="Bake", width=1024, height=1024)  # Create a new image with specified dimensions
        
        bpy.context.scene.cycles.bake_type = 'DIFFUSE'
        bpy.ops.object.bake(type='COMBINED')
        

        print("Bake !")
        return {'FINISHED'}
    
    @staticmethod
    def Create_Mask_Mat(self, context):
        black_material = "Mask_Black"
        red_material ="Mask_Red"
        green_material ="Mask_Green"
        blue_material ="Mask_Blue"
        # if "Mask_Black" not in bpy.data.materials:

        material_1 = bpy.data.materials.get(black_material)
        if material_1 is None:
            black_material = bpy.data.materials.new(name="Mask_Black")
            black_material.diffuse_color = (0, 0, 0, 1) 
            black_material.roughness = 1

        material_2 = bpy.data.materials.get(red_material)
        if material_2 is None:
            red_material = bpy.data.materials.new(name="Mask_Red")
            red_material.diffuse_color = (1, 0, 0, 1) 
            red_material.roughness = 1
        
        material_3 = bpy.data.materials.get(green_material)
        if material_3 is None:
            green_material = bpy.data.materials.new(name="Mask_Green")
            green_material.diffuse_color = (0, 1, 0, 1)
            green_material.roughness = 1

        material_4 = bpy.data.materials.get(blue_material)
        if material_4 is None:
            blue_material = bpy.data.materials.new(name="Mask_Blue")
            blue_material.diffuse_color = (0, 0, 1, 1)
            blue_material.roughness = 1 
        

        print("Bake !")
        return {'FINISHED'}
    @staticmethod
    def AssigeMat_Black(self, context):
        
        selected_object = bpy.context.selected_objects[0]
        Material_name = "Mask_Black"
        if Material_name not in [slot.material.name for slot in selected_object.material_slots]:
            
            selected_object.data.materials.append(bpy.data.materials[Material_name])
        
        for i, slot in enumerate(selected_object.material_slots):
            if slot.material and slot.material.name == Material_name:
                selected_object.active_material_index = i
                break
        bpy.ops.object.material_slot_assign()   
        
        return {'FINISHED'}
    @staticmethod
    def AssigeMat_Red(self, context):

        selected_object = bpy.context.selected_objects[0]
        Material_name = "Mask_Red"
        if Material_name not in [slot.material.name for slot in selected_object.material_slots]:
            
            selected_object.data.materials.append(bpy.data.materials[Material_name])
        
        for i, slot in enumerate(selected_object.material_slots):
            if slot.material and slot.material.name == Material_name:
                selected_object.active_material_index = i
                break
        bpy.ops.object.material_slot_assign()   
        

        return {'FINISHED'}
    @staticmethod

    def AssigeMat_Green(self, context):
        selected_object = bpy.context.selected_objects[0]
        Material_name = "Mask_Green"
        if Material_name not in [slot.material.name for slot in selected_object.material_slots]:
            
            selected_object.data.materials.append(bpy.data.materials[Material_name])
        
        for i, slot in enumerate(selected_object.material_slots):
            if slot.material and slot.material.name == Material_name:
                selected_object.active_material_index = i
                break
        bpy.ops.object.material_slot_assign()  
        print(slot)

        return {'FINISHED'}
    
    @staticmethod
    def AssigeMat_Blue(self, context):

        selected_object = bpy.context.selected_objects[0]
        Material_name = "Mask_Blue"
        if Material_name not in [slot.material.name for slot in selected_object.material_slots]:
            
            selected_object.data.materials.append(bpy.data.materials[Material_name])
        
        for i, slot in enumerate(selected_object.material_slots):
            if slot.material and slot.material.name == Material_name:
                selected_object.active_material_index = i
                break
        bpy.ops.object.material_slot_assign()  
        print(slot)

        return {'FINISHED'}
    
def register():
    
    bpy.utils.register_class(Bake_material)
    
def unregister():
    bpy.utils.unregister_class(Bake_material)
  

if __name__ == "__main__":
    register()