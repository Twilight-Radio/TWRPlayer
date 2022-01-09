"""Управление воспроизведением и плеером."""
from functions.getconf import twrconf
from functions.commwait import commandwait
import vlc

instance = vlc.Instance('--input-repeat=-1')
player = instance.media_player_new()
media = instance.media_new(twrconf()[1])
player.set_media(media)
player.audio_set_volume(20)


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


def twrversion():
    """Выводит версию и возвращается к ожиданию ввода команды."""
    version = twrconf()[0]
    print(f'TWR Player v.: {version}')
    commandwait()
