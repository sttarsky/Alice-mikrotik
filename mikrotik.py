from netmiko import ConnectHandler, NetmikoTimeoutException
from constant import *


def connect(command: str = '/sys ide pr'):
    mikrotik_ros = {
        'device_type': 'mikrotik_routeros',
        'host': IP_MIKR,
        'port': '22',
        'username': USR_MIKR,
        'password': PASSW_MIKR
    }
    try:
        with ConnectHandler(**mikrotik_ros) as ssh:
            result = ssh.send_command(command)
        return True, result
    except NetmikoTimeoutException as error:
        return False, 'микротик недоступен'


if __name__ == '__main__':
    print(connect())