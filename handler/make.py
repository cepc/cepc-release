import os

from cepcenv.util import ensure_list
from cepcenv.util import call

from cepcenv.loader import load_relative


def compile(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'compile_make.log')

    source_dir = param['pkg_config']['source_dir']

    make_root = param['action_param'].get('make_root', '')
    if not make_root:
        make_root = source_dir
    else:
        make_root = os.path.join(source_dir, make_root)
    

    env = param.get('env')

    make_opt = param['config'].get('make_opt', '')
    make_opt = ensure_list(make_opt)


    with open(log_file, 'w') as f:
        ret, out, err = call(['make']+make_opt, cwd=make_root, env=env, stdout=f)

    return ret==0
