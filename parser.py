
from constant import SKILL_ID
from guess import guesser
from models import Post


async def parser(item: Post):
    skill = SKILL_ID
    match item.session.skill_id:
        case str(skill):
            if item.request.command:
                result = guesser(item.request.command)
            else:
                result = True, 'Скилл доступен'
        case _:
            result = False, "Внутренняя ошибка"
    return result

