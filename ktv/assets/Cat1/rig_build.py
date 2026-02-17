from rubikaY3_25.ktv.assets.Cat1 import rigBiped

import pymel.core as pm

from rubikaY3_25.ktv.assets.Cat1.snippets import wrapTest
import importlib
importlib.reload(wrapTest)
importlib.reload(rigBiped)

def build_biped():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent(['environment', 'geo', 'controlers'], 'rig')


def custom_rig():
    wrapTest.build_face()
