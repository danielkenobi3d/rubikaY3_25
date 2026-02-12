from operator import invert

from rubikaY3_25.ktv.assets.Cat1.custom_rig import rigPlaneWrap
from rubikaY3_25.ktv.assets.Cat1.custom_rig import RigSoftMod
import importlib
import pymel.core as pm
import RMPY.core.rig_core as rm


def build_face():
    importlib.reload(rigPlaneWrap)


    wrapped_geo = 'C_Cat_Body2'

    # -----------------------------------------------------------------------------------------
    # LEFT EYE
    left_eye = rigPlaneWrap.RigPlaneWrap()
    left_eye.create_point_base('L_eye00_reference_pnt', wrapped_geo = wrapped_geo)
    l_eye = pm.ls('L_eye_Ctrl')[0]
    # l_eye.translateX >> left_eye.offset_group.translateX
    # l_eye.translateY >> left_eye.offset_group.translateZ
    rm.connect.times_factor(l_eye.translateX, left_eye.offset_group.translateX, -1)
    rm.connect.times_factor(l_eye.translateY, left_eye.offset_group.translateZ, -1)


    L_plane00_eye_msh = pm.ls('L_plane00_eye_msh')[0]
    L_plane00_eye_msh.scaleX.unlock()
    L_plane00_eye_msh.scaleX.set(-1)
    L_plane00_eye_msh.scaleX.lock()

    # -----------------------------------------------------------------------------------------
    # RIGHT EYE
    right_eye = rigPlaneWrap.RigPlaneWrap()
    right_eye.create_point_base('R_eye00_reference_pnt', wrapped_geo = wrapped_geo)
    r_eye = pm.ls('R_eye_Ctrl')[0]
    r_eye.translateX >> right_eye.offset_group.translateX
    r_eye.translateY >> right_eye.offset_group.translateZ


    R_plane00_eye_msh = pm.ls('R_plane00_eye_msh')[0]

    # -----------------------------------------------------------------------------------------
    # MOUTH
    mouth = rigPlaneWrap.RigPlaneWrap()
    mouth.create_point_base('C_mouth00_reference_pnt', wrapped_geo = wrapped_geo)
    mouth_ctrl = pm.ls('C_Mouth_Ctrl')[0]
    mouth_ctrl.translateX >> mouth.offset_group.translateX
    # mouth_ctrl.translateY >> mouth.offset_group.translateZ
    rm.connect.times_factor(mouth_ctrl.translateY, mouth.offset_group.translateZ, -1)


    C_plane00_mouth_msh = pm.ls('C_plane00_mouth_msh')[0]
    [C_plane00_mouth_msh.attr(a).unlock() for a in ['sx', 'sy', 'sz']]
    C_plane00_mouth_msh.scale.set(0.8, 0.8, 0.8)
    [C_plane00_mouth_msh.attr(a).lock() for a in ['sx', 'sy', 'sz']]

    # -----------------------------------------------------------------------------------------
    # APPLY TEXTURE
    L_eye_shader = pm.ls('standardSurface8SG')[0]
    L_eye_connections = pm.listConnections(L_plane00_eye_msh.getShape() , type='shadingEngine', plugs=True, connections=True )
    L_eye_connections[0][0] // L_eye_connections[0][1]
    L_eye_shader.addMember(L_plane00_eye_msh)




    R_eye_shader = pm.ls('standardSurface2SG')[0]
    R_eye_connections = pm.listConnections(R_plane00_eye_msh.getShape() , type='shadingEngine', plugs=True, connections=True )
    R_eye_connections[0][0] // R_eye_connections[0][1]
    R_eye_shader.addMember(R_plane00_eye_msh)

    C_mouth_shader = pm.ls('standardSurface3SG')[0]
    C_mouth_connections = pm.listConnections(C_plane00_mouth_msh.getShape() , type='shadingEngine', plugs=True, connections=True )
    C_mouth_connections[0][0] // C_mouth_connections[0][1]
    C_mouth_shader.addMember(C_plane00_mouth_msh)

    # -----------------------------------------------------------------------------------------
    # FRAME OFFSET
    C_Mouth_Ctrl = pm.PyNode('C_Mouth_Ctrl')
    C_Mouth_File = pm.PyNode('file2')
    pm.connectAttr(C_Mouth_Ctrl.Mouth_Shape, C_Mouth_File.frameOffset, force=True)
    #C_Mouth_Ctrl.Mouth_Shape.connect(C_Mouth_File.frameOffset, force=True)



    root_point = pm.ls('C_softModJaw00_reference_pnt')[0]
    new_soft = RigSoftMod.SoftModRig()
    geo = ['C_plane00_mouth_msh', 'C_Cat_Body2']

    new_soft.create_point_base(root_point, geo=geo,
                               type='box',
                               size=.2,
                               centered=True)
    new_soft.set_parent(pm.ls('C_fk00_jaw_ctr')[0])




