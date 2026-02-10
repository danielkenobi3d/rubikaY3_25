import pymel.core as pm
scene_object = pm.ls('pSphere1')[0]
surface_shader = pm.ls('Cat_v011:aiStandardSurface2SG')[0]
connections = pm.listConnections(scene_object.getShape() , type='shadingEngine', plugs=True, connections=True )
connections[0][0] // connections[0][1]

surface_shader.addMember(scene_object)