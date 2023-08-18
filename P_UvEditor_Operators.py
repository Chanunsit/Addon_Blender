import bpy
import os
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from . import P_Funtion
from . import P_Property


class MyProperties(PropertyGroup):
    saveList : StringProperty(name="Save List")

class UV_Editor(bpy.types.Operator):
    bl_idname = "uv.my_operator"
    bl_label = "My Operator"
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):
        if self.action == "@_SmartUnwrap": 
            self.SmartUnwrap(self, context)
        elif self.action == "@_Unwrapmaster": 
            self.Unwrapmaster(self, context)
        elif self.action == "@_RotateUV90": 
            self.RotateUV90(self, context)
        elif self.action == "@_AlignEdgeUV": 
            self.AlignEdgeUV(self, context)
        elif self.action == "@_PackUV_Together": 
            self.PackUV_Together(self, context)
        elif self.action == "@_Texel_value_increase": 
            self.Texel_value_increase(self, context)
        elif self.action == "@_Texel_value_reduce": 
            self.Texel_value_reduce(self, context)
        elif self.action == "@_Seam_from_island": 
            self.Seam_from_island(self, context)
        elif self.action == "@_Checker": 
            self.Assign_Checker(self, context)
        else:
             print("")

        return {'FINISHED'}
    @staticmethod
    def Assign_Checker(self, context):
        selected_texture = context.scene.Panda_Tools.selected_texture
        textures_path = os.path.join(os.path.dirname(__file__), "P_Texture")
        # Get the active object's material or create a new one
        active_object = context.active_object
        if active_object:
            if not active_object.data.materials:
                new_material = bpy.data.materials.new(name="New Material")
                active_object.data.materials.append(new_material)
                material = new_material
                bpy.context.object.active_material.use_nodes = True
            else:
                material = active_object.active_material
                

            if material:
                 # Check if the image with the same name already exists
                 
                image_name = selected_texture + ".png"
                existing_image = bpy.data.images.get(image_name)
                texture_node = material.node_tree.nodes.new(type='ShaderNodeTexImage')
                texture_node.location = (0, 0)
                texture_path = os.path.join(textures_path, image_name)
                
                if existing_image:
                    texture_node = material.node_tree.nodes.get("Image Texture")
                    if texture_node:
                        texture_node.image = existing_image
                else:
                    
                    new_image = bpy.data.images.load(filepath=texture_path)
                    texture_node.image = new_image
                    # If the image doesn't exist, load it and assign
                
                

                # Connect the image texture node to the base color input
                principled_node = material.node_tree.nodes.get("Principled BSDF")
                if principled_node:
                    material.node_tree.links.new(texture_node.outputs["Color"], principled_node.inputs["Base Color"])
        print("Assign Checker")
        return {'FINISHED'}
    @staticmethod
    def SmartUnwrap(self, context):
        scene = context.scene
        uv_texel_value = (context.scene.Panda_Tools.uv_texel_value)

        bpy.ops.uv.snap_cursor(target='SELECTED')
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.05)
        bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
        bpy.ops.uv.align_rotation(method='AUTO')
        bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')
        P_Funtion.settexel_custom(self, context)

        # P_Funtion.settexel_512(self, context)
        bpy.ops.uv.snap_cursor(target='ORIGIN')

        
        print("Unwraped")
        return {'FINISHED'}
    @staticmethod
    def Unwrapmaster(self, context):
        scene = context.scene
        bpy.ops.uv.smart_project()
        bpy.ops.uv.smart_project(angle_limit=0.785398)
        bpy.ops.uv.smart_project(island_margin=0.01)


    
        print("Unwraped")
        return {'FINISHED'}
    
    @staticmethod
    def RotateUV90(self, context):
        scene = context.scene
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Z')
        print("Rotated UV 90")
        return {'FINISHED'}
    
    @staticmethod
    def AlignEdgeUV(self, context):
        scene = context.scene
        bpy.ops.uv.align_rotation(method='EDGE')
        print("AlignEdgeUV")
        return {'FINISHED'}
    
    @staticmethod
    def PackUV_Together(self, context):
        scene = context.scene
        bpy.ops.uv.snap_cursor(target='SELECTED')
        bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=0.05)
        bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')
        P_Funtion.settexel_512(self, context)
        bpy.ops.uv.snap_cursor(target='ORIGIN')

        # if context.scene.Panda_Tools.uv_offset: 
        #     # Set the 3D cursor position in the Image Editor
        #     context.space_data.cursor_location[0] += 2.0
        #     context.space_data.cursor_location[1] += 0
        #     bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')
        
        print("AlignEdgeUV")
        return {'FINISHED'}
    @staticmethod
    def Texel_value_increase(self, context):
        
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        texel = int (Panda_Property.uv_texel_value) 
        if texel < 4096:
            texel *= 2
        Panda_Property.uv_texel_value = str (texel)

        print("Texel value X2")
        return {'FINISHED'}
    @staticmethod
    def Texel_value_reduce(self, context):
        
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        texel = int (Panda_Property.uv_texel_value) 
        if texel > 1:
            texel //= 2
        Panda_Property.uv_texel_value = str (texel)
        
        print("Texel value /2")
        return {'FINISHED'}
    
    @staticmethod
    def Seam_from_island(self, context):
        scene = context.scene
        bpy.ops.uv.seams_from_islands()

        print("seams from islands")
        return {'FINISHED'}



def register():
    
    bpy.utils.register_class(UV_Editor)
    bpy.utils.register_class(MyProperties)
def unregister():
    bpy.utils.unregister_class(UV_Editor)
    bpy.utils.unregister_class(MyProperties)

if __name__ == "__main__":
    register()