from fastapi import APIRouter
from schemas.personality_schema import PersonalityRequest, PersonalityResponse,Personality
from utils.scoring import classify_personality,get_traits
from data.personality_questions.questions_data import QUESTIONS,QUESTION_MAP
from data.personality_data.personality_types import PERSONALITY_TYPES
from data.personality_data.financial_traits import TRAITS
router = APIRouter(prefix="/personality", tags=["Personality"])

@router.get("/questions")
async def get_questions():
    """Returns the list of quiz questions"""
    return {"questions": QUESTIONS}


@router.post("/submit", response_model=PersonalityResponse)
def submit_personality(request: PersonalityRequest):
    """Receives answers, computes and returns a personality type"""
    trait_scores=get_traits(request.answers,QUESTION_MAP)
    personality_type = classify_personality(trait_scores,PERSONALITY_TYPES,TRAITS)

    response = PersonalityResponse(
        user_id=request.user_id,
        personality_type=personality_type["type"],
        description=personality_type["description"],
        risk=personality_type["risk"],
        planning=personality_type["planning"],
        scores=trait_scores
    )
    return response

@router.post("/personalityType", response_model=PersonalityResponse)
async def get_personality(request: Personality):
    """Receives user_id, and returns a  personality type along with its traits"""
    response = PersonalityResponse(
        user_id=request.user_id,
        personality_type="Saver",
        risk="No-risk",
        planning="Long term focused",
        description= "Cautious and disciplined, prioritizes saving over spending.",
        scores = {"risk": 0, "planning": 4, "spending": 0, "awareness": 3}
    )
    return response