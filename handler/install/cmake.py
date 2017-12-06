import os
import pprint

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


    cmake_args = param['action_param'].get('args', [])
    cmake_args = ensure_list(cmake_args)
    cmake_args = [p.format(**param['pkg_dir_list']) for p in cmake_args]

    if not param['action_param'].get('ignore_install_prefix', False):
        cmake_args.insert(0, '-DCMAKE_INSTALL_PREFIX='+install_dir)

    envcmake = param['action_param'].get('envcmake', {})
    for k, v in envcmake.items():
        full_value = v.format(**param['pkg_dir_list'])
        full_arg = '-D{0}={1}'.format(k, full_value)
        cmake_args.append(full_arg)


    install_args = param['action_param'].get('install', ['install'])
    install_args = ensure_list(install_args)


    env = param.get('env')


    make_opt = param['config'].get('make_opt', [])
    make_opt = ensure_list(make_opt)
    make_opt = auto_make_jobs(make_opt)


    with open(param['log_file'], 'w') as f:
        cmd = ['cmake', source_dir] + cmake_args
        ret = call_and_log(cmd, log=f, cwd=build_dir, env=env)
        if ret != 0:
            return False

        cmd = ['make'] + make_opt
        ret = call_and_log(cmd, log=f, cwd=build_dir, env=env)
        if ret != 0:
            return False

        if param['action_param'].get('do_make_install', True):
            cmd = ['make'] + install_args
            ret = call_and_log(cmd, log=f, cwd=build_dir, env=env)
            if ret != 0:
                return False

    return True
