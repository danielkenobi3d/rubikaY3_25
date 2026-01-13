from RMPY.rig import rigFromhierarchy

def custom_rig():
    my_rig = rigFromhierarchy.RigFromHierarchy()
    my_rig.create_point_base(*pm.ls('C_COG00_reference_pnt'))