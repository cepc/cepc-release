import os
import platform

def run(param):
    libdir = 'lib'

    if platform.system() == 'Linux' and platform.machine() == 'x86_64':
        if not os.path.exists('/etc/debian_version'):
            libdir = 'lib64'

    config_release = param['config_release']

    geant4_path = config_release.get('attribute', {}).get('Geant4', {}).get('path', {})
    if 'lib' in geant4_path:
        geant4_path['lib'] = geant4_path['lib'].replace('/lib', '/'+libdir)

    return config_release
