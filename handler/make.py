import os

from cepcenv.util import ensure_list

from cepcenv.loader import load_relative
auto_make_jobs = load_relative('util', 'auto_make_jobs')
call_and_log = load_relative('util', 'call_and_log')


def run(param):
    source_dir = param['pkg_info']['dir']['source']

    make_root = param['action_param'].get('make_root', '')
    if not make_root:
        make_root = source_dir
    else:
        make_root = os.path.join(source_dir, make_root)
    

    env = param.get('env')

    make_opt = param['config'].get('make_opt', [])
    make_opt = ensure_list(make_opt)
    make_opt = auto_make_jobs(make_opt)


    with open(param['log_file'], 'w') as f:
        ret = call_and_log(['make']+make_opt, log=f, cwd=make_root, env=env)

    return ret==0
