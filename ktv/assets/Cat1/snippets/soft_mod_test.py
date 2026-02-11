from rubikaY3_25.ktv.assets.Cat1.custom_rig import RigSoftMod
root_point = pm.ls('C_testPoint_reference_pnt')[0]
new_soft = RigSoftMod.SoftModRig()
geo = ['pSphere1', 'pCylinder1']
new_soft.create_point_base(root_point, geo=geo,
                           type='box',
                           size=.2,
                           centered=True)