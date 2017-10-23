import os

from cepcenv.util import safe_cpdir

def source(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'source_copy.log')

    src_dir = param['pkg_config']['extract_dir']
    dst_dir = param['pkg_config']['source_dir']
    main_dir = param['action_param']['main'].format(**param['pkg_config'])
    safe_cpdir(os.path.join(src_dir, main_dir), dst_dir)

    with open(log_file, 'w') as f:
        f.write('Copy "{0}" to "{1}" OK!\n'.format(os.path.join(src_dir, main_dir), dst_dir))

    return True
