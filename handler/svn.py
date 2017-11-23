import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def download(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'download_svn.log')

    url = param['action_param']['url'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['package_root']
    version = param['pkg_config']['version']

    cmd = ['svn', 'export', '--force', url, version]
    with open(log_file, 'w') as f:
        ret = call_and_log(cmd, log=f, cwd=dst_dir)

    return ret==0
