import pymel.core as pm

def custom_rig():
    pm.parent(['environment', 'geo'], 'rig')