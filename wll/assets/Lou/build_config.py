build_order = ['source', 'rig', 'load data',  'finalize']
build = {
    'source': [
        ('Import geometry', ['rig_build.import_geometry']),
        ('Import reference files', ['rig_build.import_reference_points'])
        ],
    'rig': [
        ('Build biped', ['rig_build.build_biped']),
        ('Custom rig', ['rig_build.custom_rig']),
        ('Visibility switches', ['visibility_switches.build'] ),
        ('rig facial', ['rig_facial.build'])
        ],
    'load data': [
        ('load skinning', ['rig_build.load_skinning_data']),
        ('load shapes', ['rig_build.load_shapes_data'])
    ],
    'finalize': [
        ('cleanup', ['rig_build.cleanup']),
        ('custom finalize', ['rig_build.custom_finalize'])
    ],
}