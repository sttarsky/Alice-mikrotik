from typing import Dict, Any

from pydantic import BaseModel



class Session(BaseModel):
    message_id: int
    session_id: str
    skill_id: str
    user: Dict[str, str]
    user_id: str
    application: Dict[str, str]
    new: bool


class Request(BaseModel):
    command: str
    original_utterance: str
    nlu: Dict[str, Any]
    markup: Dict[str, bool]
    type: str


class Post(BaseModel):
    session: Session
    request: Request
    version: str


if __name__ == '__main__':
    test = Post.parse_obj(income_json)
    print(test.request.command)
