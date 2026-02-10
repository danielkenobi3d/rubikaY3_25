from rubikaY3_25.ktv.assets.Cat1.custom_rig import rigPlaneWrap
import importlib
import pymel.core as pm

importlib.reload(rigPlaneWrap)

wrapped_geo = 'C_Cat_Body2'

left_eye = rigPlaneWrap.RigPlaneWrap()
left_eye.create_point_base('L_eye00_reference_pnt', wrapped_geo = wrapped_geo)
l_eye = pm.ls('L_eye_Ctrl')[0]
l_eye.translateX >> left_eye.offset_group.translateX
l_eye.translateY >> left_eye.offset_group.translateZ

right_eye = rigPlaneWrap.RigPlaneWrap()
right_eye.create_point_base('R_eye00_reference_pnt', wrapped_geo = wrapped_geo)
r_eye = pm.ls('R_eye_Ctrl')[0]
r_eye.translateX >> right_eye.offset_group.translateX
r_eye.translateY >> right_eye.offset_group.translateZ



mouth = rigPlaneWrap.RigPlaneWrap()
mouth.create_point_base('C_mouth00_reference_pnt', wrapped_geo = wrapped_geo)
mouth_ctrl = pm.ls('C_Mouth_Ctrl')[0]
mouth_ctrl.translateX >> mouth.offset_group.translateX
mouth_ctrl.translateY >> mouth.offset_group.translateZ