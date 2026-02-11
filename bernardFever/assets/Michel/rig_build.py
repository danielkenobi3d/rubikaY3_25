import pymel.core as pm


def custom_rig():
    pm.parent(['geo', 'environment'], 'rig')