from typing import Dict, Any

from pydantic import BaseModel, Field


class PSessionUser(BaseModel):
    user_id: str


class PSessionApplication(BaseModel):
    application_id: str


class PSession(BaseModel):
    message_id: int
    session_id: str
    skill_id: str
    user: PSessionUser
    user_id: str
    application: PSessionApplication
    new: bool


class PRequest(BaseModel):
    command: str
    original_utterance: str
    nlu: Dict[str, Any]
    markup: Dict[str, Any]
    type: str


class Post(BaseModel):
    session: PSession
    request: PRequest
    version: str


class RResponse(BaseModel):
    text: str
    end_session: bool


class Response(BaseModel):
    response: RResponse
    version: str
