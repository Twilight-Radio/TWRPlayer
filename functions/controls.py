"""Управление воспроизведением и плеером."""
from importlib.metadata import metadata
from functions.getconf import twrconf
from functions.commwait import commandwait
import urllib3
import vlc

instance = vlc.Instance('--input-repeat=-1')
media = instance.media_new(twrconf()[1])
player = instance.media_player_new()
media.get_mrl()
player.set_media(media)
player.audio_set_volume(20)


def twrstop():
    """Останавливает воспроизведение и возвращается к ожиданию ввода."""
    player.stop()
    commandwait()


def twrplay():
    """Начинает воспроизведение и возвращается к ожиданию ввода."""
    player.play()
    media.parse()
    commandwait()


def twrexit():
    """Выходит из программы."""
    exit()


def twrversion():
    """Выводит версию и возвращается к ожиданию ввода команды."""
    version = twrconf()[0]
    print(f'TWR Player v.: {version}')
    commandwait()


def getMetaData():
    """Выводит информацию о потоке"""
    http = urllib3.PoolManager()
    metaFile = http.request('GET', twrconf()[2])
    metainfo_now = metaFile.data.decode('utf-8')
    print('\nNow Playing: ', metainfo_now, '\n')
    commandwait()