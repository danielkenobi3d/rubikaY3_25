import pymel.core as pm
from RMPY.rig import rigFacial
from RMPY.rig import rigBlendShapeControls
import pymel.core as pm
from RMPY.rig import rigHierarchy
from RMPY.rig import rigStaticLayer
from RMPY.rig.switches import rigFloatSwitch
from RMPY.core import rig_core
from RMPY.creators import blendShape
from builder.pipeline import environment
import maya.mel as mel

def build():
    env = environment.Environment()
    facial_definition = env.get_variables_from_path(environment.pipe_config.facial_definition)

    # facial_controls = rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')

    rigFacial.RigFacial(facial_definition.definition,
                        prefix_geometry_list=facial_definition.prefix_geometry_list)

    pm.parent('character', 'geo')

    for each in facial_definition.direct_blendshape:
        static_connection(each, facial_definition.direct_blendshape[each])


def static_connection(source, destination):
    pm.select(destination, source)
    mel.eval('Morph - componentMatch')
    pm.setAttr('{}.visibility'.format(source), False)