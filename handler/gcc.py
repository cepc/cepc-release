import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def pre_check(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'pre_check_gcc.log')

    source_dir = param['pkg_config']['source_dir']
    download_prerequisites_script = os.path.join(source_dir, 'contrib', 'download_prerequisites')

    with open(log_file, 'w') as f:
        ret = call_and_log([download_prerequisites_script], log=f, cwd=source_dir)

    return ret==0
