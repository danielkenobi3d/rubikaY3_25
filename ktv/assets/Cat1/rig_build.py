from rubikaY3_25.ktv.assets.Cat1 import rigBiped
import importlib
importlib.reload(rigBiped)
import pymel.core as pm

def build_biped():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent(['environment', 'geo', 'controlers'], 'rig')
