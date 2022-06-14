"""Ожидает ввода комманды и передает ее на обработку."""
from functions import controls


def infoMessage():
    print('press P to play\n'
          'I to view stream info\n'
          'S to stop\n'
          'V to show version info\n'
          'E for exit\n\n')
    commandwait()

def commandwait():
    """Ожидание и реакция на ввод команд."""
    command = input('press P to play\n'
                    'I to view stream info\n'
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
    elif command in ['I', 'i']:
        controls.getMetaData()
    else:
        infoMessage()