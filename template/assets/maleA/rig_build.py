from RMPY.rig import rigFromHierarchy
from RMPY.rig import rigWorld
import pymel.core as pm

def custom_rig():
    rig_world = rigWorld.RigWorld()
    my_rig = rigFromHierarchy.RigFromHierarchy()
    my_rig.create_point_base(*pm.ls('C_COG00_reference_pnt'), centered =True)
    my_rig.set_parent(rig_world)