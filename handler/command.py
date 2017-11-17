import os

from cepcenv.util import call

def pre_check(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'pre_check_command.log')

    source_dir = param['pkg_config']['source_dir']
    cmd = param['action_param']['cmd']

    with open(log_file, 'w') as f:
        ret, out, err = call(cmd, cwd=source_dir, stdout=f)

    return ret==0
