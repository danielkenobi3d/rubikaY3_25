import maya.cmds as cmds

def build():
    cmds.reorderDeformers("shrinkWrap2", "C_object01_Cat_Eyebrow_Plane_rig_skn", "R_Cat_Eyebrow_Plane")
    cmds.reorderDeformers("shrinkWrap1", "C_object00_Cat_Eyebrow_Plane_rig_skn",  "L_Cat_Eyebrow_Plane")

