IHEP_PACKAGE_BASE_URL = 'http://cepcsoft.ihep.ac.cn/package/cepcsoft'

def run(param):
    config_release = param['config_release']

    for pkg, cfg in config_release.get('install', {}).items():
        handler = cfg.get('download', {}).get('handler')
        if not handler:
            continue

        version = config_release.get('package', {}).get(pkg, {}).get('version')
        if not version:
            continue

        if handler == 'http':
            filename = config_release['install'][pkg].get('extract', {}).get('param', {}).get('file')
            if filename:
                config_release['install'][pkg]['download']['param']['url'] = \
                        '{base_url}/{package}/{version}/{filename}'\
                        .format(base_url=IHEP_PACKAGE_BASE_URL, package=pkg, version=version, filename=filename)
        elif handler == 'svn':
            name = '{0}-{1}'.format(pkg, version)
            filename = name + '.tar.gz'
            config_release['install'][pkg]['download']['handler'] = 'http'
            config_release['install'][pkg]['download']['param']['url'] = \
                    '{0}/{1}/{2}/{3}'.format(IHEP_PACKAGE_BASE_URL, pkg, version, filename)
            config_release['install'][pkg]['extract'] = {}
            config_release['install'][pkg]['extract']['handler'] = 'tar'
            config_release['install'][pkg]['extract']['param'] = {}
            config_release['install'][pkg]['extract']['param']['file'] = filename
            config_release['install'][pkg]['extract']['param']['main'] = name

    return config_release
