import multiprocessing

def auto_make_jobs(make_opt):
    for opt in make_opt:
        if opt.startswith('-j'):
            return make_opt

    make_opt.insert(0, '-j{0}'.format(multiprocessing.cpu_count()))
    return make_opt
