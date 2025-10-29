from pydantic import BaseModel
from typing import Dict

class PersonalityRequest(BaseModel):
    user_id: str
    answers: Dict[int, int] # {question_id: score}

class PersonalityResponse(BaseModel):
    user_id: str
    personality_type: str
    description: str
    scores: Dict[str, float]
