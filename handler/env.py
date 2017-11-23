import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def pre_check(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'pre_check_env.log')

    build_dir = param['pkg_config']['build_dir']

    env = param.get('env')

    with open(log_file, 'w') as f:
        call_and_log(['which', 'gcc'], log=f, cwd=build_dir, env=env)
        call_and_log(['gcc', '--version'], log=f, cwd=build_dir, env=env)

    return True
