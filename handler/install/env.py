import os

from cepcenv.loader import load_relative
call_and_log = load_relative('util', 'call_and_log')

def run(param):
    build_dir = param['pkg_info']['dir']['build']

    env = param.get('env')

    with open(param['log_file'], 'w') as f:
        try:
            call_and_log(['which', 'gcc'], log=f, cwd=build_dir, env=env)
            call_and_log(['gcc', '--version'], log=f, cwd=build_dir, env=env)
        except Exception as e:
            f.write('Command error: {0}'.format(e))

    return True
