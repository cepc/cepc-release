import os
import subprocess

def download(param):
    url = param['action_param']['url'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['download_dir']

    full_cmd = ['curl', '-O', url]
    p = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dst_dir)
    out, err = p.communicate()
    out = out.decode()
    err = err.decode()
    ret = p.returncode

    return {'filename': os.path.basename(url)}
