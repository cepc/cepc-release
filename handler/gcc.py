import os

from cepcenv.util import call

def pre_check(param):
    source_dir = param['pkg_config']['source_dir']
    download_prerequisites_script = os.path.join(source_dir, 'contrib', 'download_prerequisites')
    ret, out, err = call([download_prerequisites_script], cwd=source_dir)

    return {'ok': ret==0, 'log': {'stdout': out, 'stderr': err}}
