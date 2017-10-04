import os
from cepcenv.util import call

def extract(param):
    tar_file_name = param['action_param']['file'].format(**param['pkg_config'])
    tar_file = os.path.join(param['pkg_config']['download_dir'], tar_file_name)
    dst_dir = param['pkg_config']['extract_dir']

    if tar_file_name.endswith('.tar.gz') or tar_file_name.endswith('.tgz'):
        extract_arg = 'xvzf'
    elif tar_file_name.endswith('.tar.bz2'):
        extract_arg = 'xvjf'
    else:
        extract_arg = 'xvf'

    cmd = ['tar', extract_arg, tar_file]
    ret, out, err = call(cmd, cwd=dst_dir)
    return {'ok': ret==0, 'log': {'stdout': out, 'stderr': err}}
