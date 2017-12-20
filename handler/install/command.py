import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def run(param):
    source_dir = param['pkg_info']['dir']['source']
    cmd = param['action_param']['cmd']
    if not isinstance(cmd[0], list):
        cmd = [cmd]

    with open(param['log_file'], 'w') as f:
        for c in cmd:
            ret = call_and_log(c, log=f, cwd=source_dir)

    return ret==0
