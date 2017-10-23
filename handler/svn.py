import os

from cepcenv.util import call

def download(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'download_svn.log')

    url = param['action_param']['url'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['package_root']
    version = param['pkg_config']['version']

    cmd = ['svn', 'export', '--force', url, version]
    with open(log_file, 'w') as f:
        ret, out, err = call(cmd, cwd=dst_dir, stdout=f)

    return ret==0
