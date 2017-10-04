import os

from cepcenv.util import ensure_list
from cepcenv.util import call

from cepcenv.loader import load_relative

format_output = load_relative('util', 'format_output')


def compile(param):
    source_dir = param['pkg_config']['source_dir']

    make_root = param['action_param'].get('make_root', '')
    if not make_root:
        make_root = source_dir
    else:
        make_root = os.path.join(source_dir, make_root)
    

    env = param.get('env')

    make_opt = param['config'].get('make_opt', '')
    make_opt = ensure_list(make_opt)


    final_out = ''
    final_err = ''

    ret, out, err = call(['make']+make_opt, cwd=make_root, env=env)
    final_out += format_output(out)
    final_err += format_output(err)

    return {'ok': ret==0, 'log': {'stdout': final_out, 'stderr': final_err}}
