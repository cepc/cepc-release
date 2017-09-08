import os
from cepcenv.util import call

def extract(param):
    tar_file = os.path.join(param['pkg_config']['download_dir'], param['action_param']['file'].format(**param['pkg_config']))
    dst_dir = param['pkg_config']['source_dir']
    cmd = ['tar', 'xvzf', tar_file]
    ret, out, err = call(cmd, cwd=dst_dir)
    return {'log': {'stdout': out, 'stderr': err}}
