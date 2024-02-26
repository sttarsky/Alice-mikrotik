import subprocess

import mikrotik
from constant import WoL_MACADD, DEFAULT_SRV


def guesser(value: str):
    match value.split():
        case *arg, "включи" | "включить", "пк" | "комп":
            result = mikrotik.connect(command=f'tool wol mac={WoL_MACADD}')
        case *arg, "перезагрузи" | "перезагрузить", "роутер" | "микротик":
            result = mikrotik.connect(command=f'/system reboot')
        case *arg, "перезагрузи" | "перезагрузить", "vpn" | "впн" | "випиэн":
            output = subprocess.run(['ssh', '-i', '/root/id_rsa', f'root@{DEFAULT_SRV}', 'reboot'], capture_output=True,
                   text=True)
            if output.returncode == 0:
                result = True, 'сервер перезагружен'
            else:
                result = False, 'сервер недоступен'
        case _:
            result = False, 'команда не распознана'
    return result

