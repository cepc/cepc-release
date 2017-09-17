import os

from cepcenv.util import call

def download(param):
    url = param['action_param']['url'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['package_root']
    version = param['pkg_config']['version']

    cmd = ['svn', 'export', '--force', url, version]
    ret, out, err = call(cmd, cwd=dst_dir)

    return {'log': {'stdout': out, 'stderr': err}}
