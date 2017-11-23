import pprint
import multiprocessing

from cepcenv.util import call

def auto_make_jobs(make_opt):
    for opt in make_opt:
        if opt.startswith('-j'):
            return make_opt

    make_opt.insert(0, '-j{0}'.format(multiprocessing.cpu_count()))
    return make_opt

def call_and_log(cmd, log, cwd=None, env=None, input=None):
    log.write('='*80 + '\n')
    log.write(' - Command: {0}\n'.format(cmd))
    log.write(' - Cwd: {0}\n'.format(cwd))
    log.write(' - Env:\n{0}\n'.format(pprint.pformat(env)))
    log.write('-'*80 + '\n')
    log.flush()

    ret, out, err = call(cmd, stdout=log, cwd=cwd, env=env, input=input)
    log.flush()

    return ret
