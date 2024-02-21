import json
from constant import SKILL_ID
from guess import guesser


async def parser(plain_text: str):
    item: dict = json.loads(plain_text)
    skill = SKILL_ID
    match item.get('session').get('skill_id'):
        case str(skill):
            request = item.get('request')
            if request.get('command'):
                result = guesser(item.get('request').get('command'))
            else:
                result = True, 'Скилл доступен'
        case _:
            result = False, "Внутрення ошибка"
    return result

