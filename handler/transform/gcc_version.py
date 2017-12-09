def _append_gcc_version(root, platform_append):
    pos = root.find('{platform}')
    if pos == -1:
        return root
    root_pre = root[:pos+10]
    root_post = root[pos+10:]
    return root_pre + platform_append + root_post

def _modify_categories(config_release, platform_append):
    categories = config_release.get('setting', {}).get('category', {}).get('categories', {})
    for ctg, config in categories.items():
        if 'root' in config:
            config['root'] = _append_gcc_version(config['root'], platform_append)

def run(param):
    config_release = param['config_release']
    gcc_cfg = config_release.get('package', {}).get('GCC', {})
    gcc_category = gcc_cfg.get('category')
    gcc_version = gcc_cfg.get('version')

    if gcc_category and gcc_version:
        ctg = config_release.get('setting', {}).get('category', {}).get('categories', {}).get(gcc_category, {})
        if ctg.get('install'):
            ver_frag = gcc_version.split('.')
            if len(ver_frag) >= 2:
                gcc_v2 = ''.join(ver_frag[:2])
                platform_append = '-gcc' + gcc_v2
                _modify_categories(config_release, platform_append)

    return config_release
