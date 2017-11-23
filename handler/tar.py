import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def extract(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'extract_tar.log')

    tar_file_name = param['action_param']['file'].format(**param['pkg_config'])
    tar_file = os.path.join(param['pkg_config']['download_dir'], tar_file_name)
    main_dir = param['action_param']['main'].format(**param['pkg_config'])
    dst_dir = param['pkg_config']['source_dir']

    strip_number = main_dir.strip(os.sep).count(os.sep) + 1

    cmd = ['tar', '--strip-components', str(strip_number), '-xvf', tar_file, main_dir]

    with open(log_file, 'w') as f:
        ret = call_and_log(cmd, log=f, cwd=dst_dir)

    return ret==0
