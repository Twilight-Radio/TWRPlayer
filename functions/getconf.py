"""Читает конфиг."""
import yaml


def twrconf():
    """Возвращает список параметров из конфига."""
    try:
        with open('tconf.yml', 'r') as conffile:
            config = yaml.full_load(conffile)
    except FileNotFoundError:
        with open('conf.yml', 'r') as conffile:
            config = yaml.full_load(conffile)

    stream_url = config['url']
    version = config['version']
    return version, stream_url
