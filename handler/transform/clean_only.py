def run(param):
    config_release = param['config_release']

    for pkg, cfg in config_release.get('install', {}).items():
        cfg['download'] = {}
        cfg['extract'] = {}
        cfg['pre_compile'] = {}
        cfg['compile'] = {}
        cfg['post_compile'] = {}

    return config_release
