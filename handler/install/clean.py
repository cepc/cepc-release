from cepcenv.util import safe_rmdir

from cepcenv.logger import get_logger
_logger = get_logger()

def run(param):
    clean_dirs = param['action_param'].get('dir', [])

    for d in clean_dirs:
        dir_path = param['pkg_info']['dir'].get(d)
        if dir_path:
            safe_rmdir(dir_path)
            _logger.debug('Clean "{0}": {1}'.format(d, dir_path))
        else:
            _logger.debug('Clean directory not found for: {0}'.format(d))

    return True
