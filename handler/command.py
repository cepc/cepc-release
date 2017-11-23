import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def pre_check(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'pre_check_command.log')

    source_dir = param['pkg_config']['source_dir']
    cmd = param['action_param']['cmd']

    with open(log_file, 'w') as f:
        ret = call_and_log(cmd, log=f, cwd=source_dir)

    return ret==0
