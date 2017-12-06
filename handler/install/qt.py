import os

from cepcenv.util import ensure_list
from cepcenv.util import safe_mkdir
from cepcenv.util import safe_rmdir

from cepcenv.loader import load_relative
auto_make_jobs = load_relative('util', 'auto_make_jobs')
call_and_log = load_relative('util', 'call_and_log')


def run(param):
    source_dir = param['pkg_info']['dir']['source']
    build_dir = param['pkg_info']['dir']['build']
    install_dir = param['pkg_info']['dir']['install']

    safe_rmdir(build_dir)
    safe_mkdir(build_dir)
    safe_rmdir(install_dir)
    safe_mkdir(install_dir)

    configure_args = param['action_param'].get('configure', [])
    configure_args = ensure_list(configure_args)
    configure_args = [p.format(**param['pkg_dir_list']) for p in configure_args]

    install_args = param['action_param'].get('install', ['install'])
    install_args = ensure_list(install_args)

    env = param.get('env')

    make_opt = param['config'].get('make_opt', [])
    make_opt = ensure_list(make_opt)
    make_opt = auto_make_jobs(make_opt)

    configure_path = os.path.join(source_dir, 'configure')


    with open(param['log_file'], 'w') as f:
        ret = call_and_log([configure_path, '-prefix', install_dir]+configure_args, log=f, cwd=build_dir, env=env, input=b'yes\n')
        if ret != 0:
            return False

        ret = call_and_log(['make']+make_opt, log=f, cwd=build_dir, env=env)
        if ret != 0:
            return False

        ret = call_and_log(['make']+install_args, log=f, cwd=build_dir, env=env)

    return ret==0
