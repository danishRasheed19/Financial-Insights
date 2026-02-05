from data.personality_data.planning_map import planning_map
from data.personality_data.risk_map import risk_map
def get_traits(answers,QUESTION_MAP):
    traits = {}
    for question_id,score in answers.items():
        trait=QUESTION_MAP[question_id]
        if trait:
            traits.setdefault(trait,[]).append(score)
    # Compute average score per trait
    return { trait: sum(scores) / len(scores) for trait, scores in traits.items()}

def classify_personality(trait_scores,personality_types,core_traits):
    """
    Classifies the financial personality based on scores from the quiz

    Parameters:
        trait_scores: dictionary of trait scores from quiz
        personality_types: dictionary of personality types containing description and key_traits of the personality type
        core_traits: list of traits using which we determine the personality type

    returns:
    Dict: (personality_type,description,key_traits)

    """
    best_match = None
    min_distance = float('inf')
    for name,personality in personality_types.items():
        # Compute distance between user and this personality type
        distance = 0
        for trait in core_traits:
            print("Checking trait:", trait)
            print("User score:", trait_scores.get(trait))
            print("Personality key trait:", personality['key_traits'].get(trait))

            distance += abs(trait_scores.get(trait, 0) - personality['key_traits'].get(trait, 0))
            print("Current distance:", distance)
        risk_desc=get_risk_desc(personality['key_traits'].get("risk"))
        print("Risk Desc:", risk_desc)
        planning_desc=get_planning_desc(personality['key_traits'].get("planning"))
        if distance < min_distance:
            min_distance = distance
            best_match = {
                "type": name,
                "description": personality['description'],
                "key_traits": personality['key_traits'],
                "risk": risk_desc,
                "planning": planning_desc
            }
    print("Best match:", best_match)
    return best_match


def get_risk_desc(risk_level):
    risk_level=int(round(risk_level))
    return risk_map[risk_level]['label']

def get_planning_desc(planning_level):
    planning_level=int(round(planning_level))
    return planning_map[planning_level]['label']