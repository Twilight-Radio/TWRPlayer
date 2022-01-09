"""Простой консольный плеер потока."""
import vlc
import yaml
import time

try:
    with open('conf.yml', 'r') as conffile:
        config = yaml.full_load(conffile)
except FileNotFoundError:
    with open('tconf.yml', 'r') as conffile:
        config = yaml.full_load(conffile)

version = config['version']
stream_url = config['url']


def twrstop():
    """Останавливает воспроизведение и возвращается к ожиданию ввода."""
    player.stop()
    commandwait()


def twrplay():
    """Начинает воспроизведение и возвращается к ожиданию ввода."""
    player.play()
    commandwait()


def twrexit():
    """Выходит из программы."""
    exit()


def commandwait():
    """Ожидание и реакция на ввод команд."""
    command = input('press P to play\n'
                    'S to stop\n'
                    'E for exit\n\n')
    if command in ['S', 's']:
        twrstop()
    elif command in ['P', 'p']:
        twrplay()
    elif command in ['E', 'e']:
        twrexit()
    elif command in ['V', 'v']:
        print(version)


instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()
media = instance.media_new(stream_url)
player.set_media(media)
player.audio_set_volume(20)

print(f'TWR Player v.: {version}')

time.sleep(2)
stream_title = player.audio_get_track()
commandwait()
