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
def build():
    env = environment.Environment()
    facial_definition = env.get_variables_from_path(environment.pipe_config.facial_definition)

    # facial_controls = rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')

    rigFacial.RigFacial(facial_definition.definition,
                        prefix_geometry_list=facial_definition.prefix_geometry_list)