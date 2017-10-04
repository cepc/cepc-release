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

    install_args = param['action_param'].get('install', ['install'])
    install_args = ensure_list(install_args)

    env = param.get('env')

    make_opt = param['config'].get('make_opt', '')
    make_opt = ensure_list(make_opt)


    final_out = ''
    final_err = ''

    ret, out, err = call(['cmake', source_dir]+cmake_args, cwd=build_dir, env=env)
    final_out += format_output(out)
    final_err += format_output(err)

    if ret != 0:
        return {'ok': ret==0, 'log': {'stdout': final_out, 'stderr': final_err}}

    ret, out, err = call(['make']+make_opt, cwd=build_dir, env=env)
    final_out += format_output(out)
    final_err += format_output(err)

    if ret != 0:
        return {'ok': ret==0, 'log': {'stdout': final_out, 'stderr': final_err}}

    ret, out, err = call(['make']+install_args, cwd=build_dir, env=env)
    final_out += format_output(out)
    final_err += format_output(err)

    return {'ok': ret==0, 'log': {'stdout': final_out, 'stderr': final_err}}
