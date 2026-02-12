from RMPY.rig import rigFromHierarchy

def custom_rig():
    my_rig = rigFromHierarchy.RigFromHierarchy()
    my_rig.create_point_base(*pm.ls('C_COG00_reference_pnt'))