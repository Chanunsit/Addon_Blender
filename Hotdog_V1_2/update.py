import bpy
import os
import zipfile
import shutil
import urllib

# Replace with the URL of the updated addon zip file
UPDATED_ADDON_URL = "https://github.com/grammma2533/test1/blob/main/text.zip"

def update_addon():
    # Get the addon directory and the current addon file path
    addon_dir = os.path.dirname(os.path.realpath(__file__))
    addon_file = os.path.join(addon_dir, "__init__.py")
    print(addon_file)

    # Download the updated addon zip file
    response = urllib.request.urlopen(UPDATED_ADDON_URL)
    data = response.read()

    # Save the updated addon zip file in the addon directory
    updated_addon_file = os.path.join(addon_dir, "text.zip")
    with open(updated_addon_file, "wb") as f:
        f.write(data)

    # Unzip the updated addon
    with zipfile.ZipFile(updated_addon_file, 'r') as zip_ref:
        zip_ref.extractall(addon_dir)

    # Remove the downloaded zip file
    os.remove(updated_addon_file)

    # Reload the addon module
    bpy.ops.script.reload()

# Define a custom panel
class MyPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_my_panel"
    bl_label = "My Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom'

    def draw(self, context):
        layout = self.layout

        # Add a button to update the addon
        layout.operator("addon.update", text="Update Addon")

# Define the update operator
class UpdateAddonOperator(bpy.types.Operator):
    bl_idname = "addon.update"
    bl_label = "Update Addon"

    def execute(self, context):
        update_addon()
        return {'FINISHED'}

# Register the panel and operator
def register():
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(UpdateAddonOperator)

# Unregister the panel and operator
def unregister():
    bpy.utils.unregister_class(MyPanel)
    bpy.utils.unregister_class(UpdateAddonOperator)

# Run the script
if __name__ == "__main__":
    register()
