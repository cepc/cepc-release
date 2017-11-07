import os

from cepcenv.util import ensure_list
from cepcenv.util import call

from cepcenv.loader import load_relative
auto_make_jobs = load_relative('util', 'auto_make_jobs')


def compile(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'compile_conf_make.log')

    source_dir = param['pkg_config']['source_dir']
    build_dir = param['pkg_config']['build_dir']
    install_dir = param['pkg_config']['install_dir']

    configure_args = param['action_param'].get('configure', [])
    configure_args = ensure_list(configure_args)
    configure_args = [p.format(**param['pkg_path']) for p in configure_args]

    install_args = param['action_param'].get('install', ['install'])
    install_args = ensure_list(install_args)

    env = param.get('env')

    make_opt = param['config'].get('make_opt', [])
    make_opt = ensure_list(make_opt)
    make_opt = auto_make_jobs(make_opt)

    configure_path = os.path.join(source_dir, 'configure')


    with open(log_file, 'w') as f:
        cmd = [configure_path, '--prefix='+install_dir] + configure_args
        f.write('='*80 + '\n')
        f.write('{0}\n'.format(cmd))
        f.flush()
        ret, out, err = call(cmd, cwd=build_dir, env=env, stdout=f)
        if ret != 0:
            return False

        cmd = ['make'] + make_opt
        f.write('\n' + '='*80 + '\n')
        f.write('{0}\n'.format(cmd))
        f.flush()
        ret, out, err = call(cmd, cwd=build_dir, env=env, stdout=f)
        if ret != 0:
            return False

        cmd = ['make'] + install_args
        f.write('\n' + '='*80 + '\n')
        f.write('{0}\n'.format(cmd))
        f.flush()
        ret, out, err = call(cmd, cwd=build_dir, env=env, stdout=f)

    return ret==0
