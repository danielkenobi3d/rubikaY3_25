import pymel.core as pm
from rubikaY3_25.wll.assets.Lou.custom_rig import rigBiped

def build_biped():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()


def custom_rig():
    pm.parent(['environment', 'geo'], 'rig')