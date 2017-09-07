import os

from cepcenv.util import call

def download(param):
    url = param['action_param']['url'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['download_dir']

    cmd = ['curl', '-L', '-s', '-O', url]
    ret, out, err = call(cmd, cwd=dst_dir)

    return {'log': {'stdout': out, 'stderr': err}}
