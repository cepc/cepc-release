def run(param):
    config_release = param['config_release']

    for pkg, cfg in config_release.get('install', {}).items():
        cfg['clean'] = {}

    return config_release
