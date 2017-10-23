import os

from cepcenv.util import call

def pre_check(param):
    log_file = os.path.join(param['pkg_config']['log_dir'], 'pre_check_gcc.log')

    source_dir = param['pkg_config']['source_dir']
    download_prerequisites_script = os.path.join(source_dir, 'contrib', 'download_prerequisites')

    with open(log_file, 'w') as f:
        ret, out, err = call([download_prerequisites_script], cwd=source_dir, stdout=f)

    return ret==0
