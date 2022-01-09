"""Ожидает ввода комманды и передает ее на обработку."""
from functions import controls


def commandwait():
    """Ожидание и реакция на ввод команд."""
    command = input('press P to play\n'
                    'S to stop\n'
                    'V to show version info\n'
                    'E for exit\n\n')
    if command in ['S', 's']:
        controls.twrstop()
    elif command in ['P', 'p']:
        controls.twrplay()
    elif command in ['E', 'e']:
        controls.twrexit()
    elif command in ['V', 'v']:
        controls.twrversion()
