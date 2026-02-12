import pymel.core as pm
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigBase
import maya.mel as mel

class RigPlaneWrapModel(rigSingleJoint.ModelSingleJoint):
    def __init__(self):
        super(RigPlaneWrapModel, self).__init__()
        self.plane_transform = None
        self.plane_creation = None
        self.shrink_wrap = None
        self.offset_group = None

class RigPlaneWrap(rigSingleJoint.RigSingleJoint):
    def __init__(self, *args, **kwargs):
        kwargs['model'] = kwargs.pop('model', RigPlaneWrapModel())
        super(RigPlaneWrap, self).__init__(*args, **kwargs)
    def create_point_base(self, *locator_list, wrapped_geo = ''):
        super(RigPlaneWrap, self).create_point_base(*locator_list)
        self._model.plane_transform, self._model.plane_creation = pm.polyPlane()
        pm.matchTransform(self.plane_transform,locator_list[0])
        #self.plane_transform.rotateX.set(-90)
        pm.skinCluster(self.joints,self.plane_transform)
        pm.select(self.plane_transform, wrapped_geo)
        mel.eval('CreateShrinkWrap;')
        self._model.shrink_wrap = pm.ls('shrinkWrap1')[0]
        self.name_convention.rename_name_in_format(self.plane_transform, name='plane')
        self.name_convention.rename_name_in_format(self.shrink_wrap, name='shrinkWrap')
        pm.parent(self.plane_transform, self.rig_system.display)
        self.shrink_wrap.offset.set(0.008)
        self.shrink_wrap.projection.set(3)
        self.offset_group =  self.create.group.point_base(self.controls[0])
        self.rig_system.display.overrideDisplayType.set(2)
        self.controls[0].visibility.set(False)

if __name__ == '__main__':
    my_rig = RigPlaneWrap()
    print(my_rig.geometry)