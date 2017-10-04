import os

from cepcenv.util import safe_mvdir

def source(param):
    src_dir = param['pkg_config']['extract_dir']
    dst_dir = param['pkg_config']['source_dir']
    main_dir = param['action_param']['main'].format(**param['pkg_config'])
    safe_mvdir(os.path.join(src_dir, main_dir), dst_dir)
    return {'ok': True, 'log': {'stdout': 'Move OK', 'stderr': ''}}
