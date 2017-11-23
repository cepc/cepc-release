import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def download(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'download_http.log')

    url = param['action_param']['url'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['download_dir']

    cmd = ['curl', '-f', '-L', '-s', '-S', '-O', url]
    with open(log_file, 'w') as f:
        ret = call_and_log(cmd, log=f, cwd=dst_dir)

    return ret==0
