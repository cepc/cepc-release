import os

from cepcenv.util import call

def _format_output(out):
    return '='*80 + '\n' + out

def install(param):
    source_dir = param['pkg_config']['source_dir']
    build_dir = param['pkg_config']['build_dir']
    install_dir = param['pkg_config']['install_dir']

    configure_path = os.path.join(source_dir, 'configure')

    final_out = ''
    final_err = ''

    ret, out, err = call([configure_path, '--prefix='+install_dir], cwd=build_dir)
    final_out += _format_output(out)
    final_err += _format_output(err)

    ret, out, err = call(['make', '-j4'], cwd=build_dir)
    final_out += _format_output(out)
    final_err += _format_output(err)

    ret, out, err = call(['make', 'install'], cwd=build_dir)
    final_out += _format_output(out)
    final_err += _format_output(err)

    return {'log': {'stdout': final_out, 'stderr': final_err}}
