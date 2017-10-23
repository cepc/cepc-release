import os

from cepcenv.util import call

def download(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'download_http.log')

    url = param['action_param']['url'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['download_dir']

    cmd = ['curl', '-f', '-L', '-s', '-S', '-O', url]
    with open(log_file, 'w') as f:
        ret, out, err = call(cmd, cwd=dst_dir, stdout=f)

    return ret==0
