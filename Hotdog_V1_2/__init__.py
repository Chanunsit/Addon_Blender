bl_info = {
    "name" : "Panda tool",
    "author" : "Gramma",
    "description" : "",
    "blender" : (3, 4, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "3D View"
}

from . import P_Operators
from . import P_UI
from . import update


def register():
    P_Operators.register()
    P_UI.register()
    update.register()
def unregister():
    P_Operators.unregister()
    P_UI.unregister()
    update.unregister()
if __name__ == '__main__':
    register()
    unregister()
