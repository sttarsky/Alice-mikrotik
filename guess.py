import mikrotik
from constant import WoL_MACADD

def guesser(value: str):
    match value.split():
        case *arg, "включи", "пк" | "комп":
            result = mikrotik.connect(command=f'tool wol mac={WoL_MACADD}')
        case *arg, "выключи", "wifi"|"вайфай":
            result = mikrotik.connect(command=f'/interface wifiwave2 disable wifi2')
        case _:
            result = False, 'команда нераспознанна'
    if result[0] is True and result[1] == '':
        result = True, 'выполнено'
    return result
