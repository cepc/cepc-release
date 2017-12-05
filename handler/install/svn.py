import os

from cepcenv.util import safe_mkdir

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def run(param):
    version = param['pkg_info']['package']['version']
    url = param['action_param']['url'].format(version=version)
    dst_dir = param['pkg_info']['dir']['root']

    safe_mkdir(dst_dir)

    cmd = ['svn', 'export', '--force', url, version]
    with open(param['log_file'], 'w') as f:
        ret = call_and_log(cmd, log=f, cwd=dst_dir)

    return ret==0
