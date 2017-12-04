import os

from cepcenv.util import ensure_list
from cepcenv.util import safe_mkdir

from cepcenv.loader import load_relative
auto_make_jobs = load_relative('util', 'auto_make_jobs')
call_and_log = load_relative('util', 'call_and_log')


def run(param):
    source_dir = param['pkg_info']['dir']['source']
    build_dir = param['pkg_info']['dir']['build']
    install_dir = param['pkg_info']['dir']['install']

    safe_mkdir(build_dir)
    safe_mkdir(install_dir)

    configure_args = param['action_param'].get('configure', [])
    configure_args = ensure_list(configure_args)
    configure_args = [p.format(**param['pkg_dir_list']) for p in configure_args]

    if not param['action_param'].get('ignore_install_prefix', False):
        configure_args.insert(0, '--prefix='+install_dir)

    install_args = param['action_param'].get('install', ['install'])
    install_args = ensure_list(install_args)

    env = param.get('env')
    env_configure = env.copy()
    for k, v in param['action_param'].get('env_configure', {}).items():
        env_configure[k] = v.format(**param['pkg_path'])
    env_make = env.copy()
    for k, v in param['action_param'].get('env_make', {}).items():
        env_make[k] = v.format(**param['pkg_path'])
    env_install = env.copy()
    for k, v in param['action_param'].get('env_install', {}).items():
        env_install[k] = v.format(**param['pkg_path'])

    make_opt = param['config'].get('make_opt', [])
    make_opt = ensure_list(make_opt)
    make_opt = auto_make_jobs(make_opt)

    configure_path = os.path.join(source_dir, 'configure')


    with open(param['log_file'], 'w') as f:
        cmd = [configure_path] + configure_args
        ret = call_and_log(cmd, log=f, cwd=build_dir, env=env_configure)
        if ret != 0:
            return False

        cmd = ['make'] + make_opt
        ret = call_and_log(cmd, log=f, cwd=build_dir, env=env_make)
        if ret != 0:
            return False

        cmd = ['make'] + install_args
        ret = call_and_log(cmd, log=f, cwd=build_dir, env=env_install)

    return ret==0
