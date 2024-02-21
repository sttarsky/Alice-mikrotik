import mikrotik
from constant import WoL_MACADD


def guesser(value: str):
    match value.split():
        case *arg, "включи" | "включить", "пк" | "комп":
            result = mikrotik.connect(command=f'tool wol mac={WoL_MACADD}')
        case *arg, "перезагрузи" | "перезагрузить", "роутер" | "микротик":
            result = mikrotik.connect(command=f'/system reboot')
        case *arg, "перезагрузи" | "перезагрузить", "vpn" | "впн" | "випиэн":
            result = mikrotik.connect(command=f'')
        case _:
            result = False, 'команда не распознана'
    return result
