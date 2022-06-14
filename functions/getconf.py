"""Читает конфиг."""
import yaml
import os

base_dir = os.path.dirname(__file__)
rel_tconf_path = '../conf/tconf.yml'
rel_conf_path  = '../conf/conf.yml'
abs_tconf_path = os.path.join(base_dir, rel_tconf_path)
abs_conf_path = os.path.join(base_dir, rel_conf_path)

def twrconf():
    """Возвращает список параметров из конфига."""
    try:
        with open(abs_tconf_path, 'r') as conffile:
            config = yaml.full_load(conffile)
    except FileNotFoundError:
        try:
            with open(abs_conf_path, 'r') as conffile:
                config = yaml.full_load(conffile)
        except FileNotFoundError:
            print('No Configs Found!')
            print(abs_conf_path, r'\n')
            print(abs_tconf_path)
            exit()

    stream_url = config['url']
    version = config['version']
    nowplaying = config['metaurl']
    return version, stream_url, nowplaying

if __name__ == '__main__':
    twrconf()