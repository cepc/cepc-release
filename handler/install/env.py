import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def _single_command(cmd, f, env):
    try:
        call_and_log(cmd, log=f, env=env)
    except Exception as e:
        f.write('Command error: {0}'.format(e))
        f.flush()

def run(param):
    env = param.get('env')

    with open(param['log_file'], 'w') as f:
        _single_command(['which', 'gcc'], f, env)
        _single_command(['gcc', '--version'], f, env)
        _single_command(['which', 'cmake'], f, env)
        _single_command(['cmake', '--version'], f, env)

    return True
