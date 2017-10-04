import pprint

from cepcenv.util import ensure_list
from cepcenv.util import call

from cepcenv.loader import load_relative

format_output = load_relative('util', 'format_output')


def compile(param):
    source_dir = param['pkg_config']['source_dir']
    build_dir = param['pkg_config']['build_dir']
    install_dir = param['pkg_config']['install_dir']


    cmake_args = param['action_param'].get('args', [])
    cmake_args = ensure_list(cmake_args)
    cmake_args = [p.format(**param['pkg_path']) for p in cmake_args]

    if not param['action_param'].get('ignore_install_prefix', False):
        cmake_args.insert(0, '-DCMAKE_INSTALL_PREFIX='+install_dir)

    envcmake = param['action_param'].get('envcmake', {})
    for k, v in envcmake.items():
        full_value = v.format(**param['pkg_path'])
        full_arg = '-D{0}={1}'.format(k, full_value)
        cmake_args.append(full_arg)


    install_args = param['action_param'].get('install', ['install'])
    install_args = ensure_list(install_args)


    env = param.get('env')


    make_opt = param['config'].get('make_opt', '')
    make_opt = ensure_list(make_opt)


    final_out = ''
    final_err = ''
    final_out += ('all env:\n' + pprint.pformat(env) + '\n')

    cmd = ['cmake', source_dir] + cmake_args
    ret, out, err = call(cmd, cwd=build_dir, env=env)
    final_out += (str(cmd) + '\n')
    final_out += format_output(out)
    final_err += format_output(err)

    if ret != 0:
        return {'ok': ret==0, 'log': {'stdout': final_out, 'stderr': final_err}}

    cmd = ['make'] + make_opt
    ret, out, err = call(cmd, cwd=build_dir, env=env)
    final_out += (str(cmd) + '\n')
    final_out += format_output(out)
    final_err += format_output(err)

    if ret != 0:
        return {'ok': ret==0, 'log': {'stdout': final_out, 'stderr': final_err}}

    cmd = ['make'] + install_args
    ret, out, err = call(cmd, cwd=build_dir, env=env)
    final_out += (str(cmd) + '\n')
    final_out += format_output(out)
    final_err += format_output(err)

    return {'ok': ret==0, 'log': {'stdout': final_out, 'stderr': final_err}}
