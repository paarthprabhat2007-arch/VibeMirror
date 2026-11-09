DIMENSIONS = [
    "Emotional Intelligence",
    "Social Behaviour",
    "Decision Making",
    "Self Awareness",
    "Adaptability"
]

OPTION_SCORES = {
    1: [3, 2, 1, 2],
    2: [3, 1, 2, 1],
    3: [2, 2, 1, 3],
    4: [3, 2, 1, 2],
    5: [3, 2, 1, 2],

    6: [3, 2, 1, 3],
    7: [3, 2, 3, 1],
    8: [3, 3, 1, 2],
    9: [3, 3, 1, 2],
    10: [3, 2, 3, 2],

    11: [3, 2, 1, 3],
    12: [3, 2, 3, 1],
    13: [3, 3, 2, 2],
    14: [3, 2, 3, 1],
    15: [3, 2, 3, 1],

    16: [3, 2, 1, 2],
    17: [3, 2, 1, 3],
    18: [3, 3, 1, 3],
    19: [3, 2, 3, 1],
    20: [2, 2, 3, 3],

    21: [3, 2, 1, 2],
    22: [3, 3, 2, 2],
    23: [3, 2, 1, 3],
    24: [3, 2, 1, 3],
    25: [3, 2, 3, 2]
}


# ==========================================
# ARCHETYPES
# ==========================================

ARCHETYPES = {

    "The Quiet Strategist": {
        "trait": "Observant, thoughtful and analytical.",
        "description": (
            "You tend to observe situations before becoming involved. "
            "You may prefer understanding people and circumstances "
            "before expressing your thoughts or taking action."
        ),
        "strength": "Observation, independent thinking and thoughtful responses.",
        "growth": "Express your thoughts more openly and take initiative when needed.",
        "social": "You may prefer meaningful conversations over constant social interaction.",
        "pressure": "You may withdraw temporarily to understand and process a difficult situation.",
        "decision": "You tend to think through possibilities before committing.",
        "advice": "Remember that not every situation requires extensive analysis. Sometimes action creates clarity."
    },

    "The Social Butterfly": {
        "trait": "Friendly, expressive and socially energetic.",
        "description": (
            "You appear comfortable interacting with different people. "
            "You may enjoy conversations, new connections and shared experiences."
        ),
        "strength": "Communication, social confidence and relationship building.",
        "growth": "Protect your personal time and avoid depending too much on external validation.",
        "social": "You may naturally initiate conversations and enjoy being part of a group.",
        "pressure": "Connecting with others may help you process difficult situations.",
        "decision": "You may consider how your decisions affect people around you.",
        "advice": "Build meaningful connections while maintaining your independence and personal boundaries."
    },

    "The Deep Thinker": {
        "trait": "Reflective, curious and introspective.",
        "description": (
            "You appear interested in understanding your own behaviour, "
            "motivations and experiences. You may look beyond immediate "
            "situations to understand their deeper meaning."
        ),
        "strength": "Self-reflection, critical thinking and personal insight.",
        "growth": "Avoid getting trapped in overanalysis or excessive self-criticism.",
        "social": "You may value meaningful interactions and conversations with depth.",
        "pressure": "You may spend time analysing what happened and what could be improved.",
        "decision": "You may examine different perspectives before reaching a conclusion.",
        "advice": "Reflection is valuable, but remember to convert your understanding into action."
    },

    "The Fearless Explorer": {
        "trait": "Independent, adventurous and adaptable.",
        "description": (
            "You appear open to unfamiliar situations and new possibilities. "
            "You may enjoy experimenting, learning through experience and "
            "adjusting when circumstances change."
        ),
        "strength": "Flexibility, curiosity and willingness to explore.",
        "growth": "Balance spontaneity with preparation and long-term planning.",
        "social": "You may be comfortable meeting different kinds of people and exploring new environments.",
        "pressure": "You may prefer finding alternative approaches instead of remaining stuck.",
        "decision": "You may be willing to take calculated risks when opportunities appear.",
        "advice": "Keep exploring, but give your strongest ideas enough consistency to develop."
    },

    "The Empathetic Soul": {
        "trait": "Understanding, considerate and emotionally attentive.",
        "description": (
            "You appear attentive to how people feel and how your actions "
            "may affect them. You may value emotional understanding and "
            "supportive relationships."
        ),
        "strength": "Empathy, emotional sensitivity and understanding others.",
        "growth": "Avoid neglecting your own needs while trying to understand everyone else.",
        "social": "You may pay attention to people's comfort and emotional reactions.",
        "pressure": "You may become particularly aware of how difficult situations affect others.",
        "decision": "You may consider both practical outcomes and emotional consequences.",
        "advice": "Being considerate does not mean you must always agree or sacrifice your boundaries."
    },

    "The Natural Leader": {
        "trait": "Decisive, confident and action-oriented.",
        "description": (
            "Your responses suggest a tendency to take responsibility, "
            "make decisions and move situations forward. You may feel "
            "comfortable taking initiative."
        ),
        "strength": "Initiative, responsibility and decisive thinking.",
        "growth": "Make room for collaboration and alternative viewpoints.",
        "social": "You may naturally participate in group decisions or take initiative.",
        "pressure": "You may focus on finding solutions and regaining control of a situation.",
        "decision": "You may prefer evaluating available choices and taking responsibility for the outcome.",
        "advice": "Strong leadership includes listening, adapting and recognising when someone else has a better approach."
    },

    "The Creative Dreamer": {
        "trait": "Imaginative, curious and possibility-driven.",
        "description": (
            "You may enjoy exploring ideas, imagining alternatives and "
            "looking at situations from different perspectives. "
            "You are likely to appreciate opportunities for growth and discovery."
        ),
        "strength": "Creativity, imagination and openness to possibilities.",
        "growth": "Turn ideas into consistent action instead of constantly exploring new possibilities.",
        "social": "You may enjoy people who encourage interesting conversations and fresh perspectives.",
        "pressure": "You may look for unconventional solutions when familiar approaches do not work.",
        "decision": "You may consider possibilities that others might overlook.",
        "advice": "Give your ideas structure, priorities and deadlines so they can become real outcomes."
    },

    "The Balanced Realist": {
        "trait": "Practical, composed and situation-oriented.",
        "description": (
            "Your responses suggest a relatively balanced personality "
            "without one extremely dominant behavioural tendency. "
            "You may adjust your approach depending on the circumstances."
        ),
        "strength": "Practical thinking, flexibility and balanced judgement.",
        "growth": "Identify your priorities and develop greater confidence in your natural strengths.",
        "social": "You may adjust your communication style depending on the people and environment.",
        "pressure": "You may try to balance emotional reactions with practical solutions.",
        "decision": "You may consider multiple factors before choosing an approach.",
        "advice": "Being adaptable is useful, but don't hesitate to develop a clear personal direction."
    }
}


# ==========================================
# DIMENSION INTERPRETATIONS
# ==========================================

DIMENSION_DETAILS = {

    "Emotional Intelligence": {
        "high": {
            "title": "Emotionally Attentive",
            "description": "Your answers suggest that you tend to recognise emotional situations and consider how people feel before responding.",
            "strength": "Emotional understanding and thoughtful communication.",
            "growth": "Maintain emotional boundaries and avoid carrying everyone's feelings."
        },
        "medium": {
            "title": "Emotionally Flexible",
            "description": "Your emotional responses may depend on the situation, the people involved and your own state of mind.",
            "strength": "Ability to balance emotional and practical considerations.",
            "growth": "Practise recognising your emotions before reacting to difficult situations."
        },
        "low": {
            "title": "Private Emotional Processor",
            "description": "You may prefer processing emotional situations privately or taking time before communicating your feelings.",
            "strength": "Potential for independent emotional processing.",
            "growth": "Practise expressing your feelings clearly instead of leaving them unspoken."
        }
    },

    "Social Behaviour": {
        "high": {
            "title": "Socially Expressive",
            "description": "You appear comfortable initiating conversations, participating in groups and connecting with people.",
            "strength": "Social confidence and relationship building.",
            "growth": "Balance social energy with personal space and deeper connections."
        },
        "medium": {
            "title": "Socially Flexible",
            "description": "You may enjoy social interaction while also valuing personal space and selective connections.",
            "strength": "Ability to adjust to different social environments.",
            "growth": "Build confidence in expressing your opinions in unfamiliar groups."
        },
        "low": {
            "title": "Socially Observant",
            "description": "You may prefer observing people and understanding the environment before actively participating.",
            "strength": "Careful observation and selective interaction.",
            "growth": "Take small opportunities to initiate conversations and build connections."
        }
    },

    "Decision Making": {
        "high": {
            "title": "Decisive Thinker",
            "description": "Your responses suggest that you are comfortable evaluating options, taking responsibility and moving towards decisions.",
            "strength": "Initiative and willingness to make choices.",
            "growth": "Make sure confidence does not turn into rushing or ignoring useful advice."
        },
        "medium": {
            "title": "Considered Decision Maker",
            "description": "You appear to balance independent judgement with research, advice and consideration of possible outcomes.",
            "strength": "Balanced evaluation of alternatives.",
            "growth": "Develop confidence in making decisions when complete information is unavailable."
        },
        "low": {
            "title": "Careful Evaluator",
            "description": "You may prefer additional clarity, reassurance or time before making important decisions.",
            "strength": "Caution and consideration of possible consequences.",
            "growth": "Practise making smaller decisions independently and learning from their outcomes."
        }
    },

    "Self Awareness": {
        "high": {
            "title": "Self Reflective",
            "description": "Your responses suggest that you regularly examine your behaviour, motivations, achievements and areas of improvement.",
            "strength": "Self-reflection and personal development.",
            "growth": "Avoid excessive self-criticism and comparison."
        },
        "medium": {
            "title": "Developing Self Awareness",
            "description": "You demonstrate some self-reflection, although your understanding of yourself may vary across situations.",
            "strength": "Willingness to reflect and recognise personal patterns.",
            "growth": "Spend time identifying recurring habits, motivations and personal priorities."
        },
        "low": {
            "title": "Action Focused",
            "description": "You may focus more on experiences and immediate actions than on analysing your own behaviour.",
            "strength": "Potential preference for practical experience over excessive reflection.",
            "growth": "Pause occasionally to understand what motivates your decisions and reactions."
        }
    },

    "Adaptability": {
        "high": {
            "title": "Change Ready",
            "description": "You appear comfortable exploring unfamiliar situations, adjusting plans and experimenting with different approaches.",
            "strength": "Flexibility and openness to new experiences.",
            "growth": "Balance experimentation with consistency and planning."
        },
        "medium": {
            "title": "Situationally Adaptive",
            "description": "You can adjust to change, although you may prefer some preparation before entering unfamiliar situations.",
            "strength": "Ability to balance familiarity with new experiences.",
            "growth": "Become more comfortable with uncertainty through gradual experimentation."
        },
        "low": {
            "title": "Structure Oriented",
            "description": "You may prefer familiar routines, predictable environments and established approaches.",
            "strength": "Potential preference for consistency and structure.",
            "growth": "Experiment with small changes instead of avoiding unfamiliar situations."
        }
    }
}


# ==========================================
# VALIDATION
# ==========================================

def validate_answers(answers):

    return (
        isinstance(answers, dict)
        and len(answers) == 25
        and all(
            qid in answers
            and isinstance(answers[qid], int)
            and not isinstance(answers[qid], bool)
            and answers[qid] in [1, 2, 3, 4]
            for qid in range(1, 26)
        )
    )


# ==========================================
# SCORE CALCULATION
# ==========================================

def analyse_personality(answers):

    if not validate_answers(answers):
        raise ValueError("Please answer all 25 questions.")

    results = {}

    for index, dimension in enumerate(DIMENSIONS):

        total = 0

        for qid in range(index * 5 + 1, index * 5 + 6):

            selected_option = answers[qid]

            total += OPTION_SCORES[qid][selected_option - 1]

        results[dimension] = round((total / 15) * 100, 2)

    return results


# ==========================================
# SCORE LEVEL
# ==========================================

def get_level(score):

    if score >= 75:
        return "high"

    elif score >= 55:
        return "medium"

    return "low"


# ==========================================
# ARCHETYPE MATCHING
# ==========================================

def get_archetype_matches(results):

    emotional = results["Emotional Intelligence"]
    social = results["Social Behaviour"]
    decision = results["Decision Making"]
    awareness = results["Self Awareness"]
    adaptability = results["Adaptability"]

    matches = {

        "The Quiet Strategist":
            (100 - social) * 0.55 + awareness * 0.25 + decision * 0.20,

        "The Social Butterfly":
            social * 0.65 + emotional * 0.20 + adaptability * 0.15,

        "The Deep Thinker":
            awareness * 0.55 + decision * 0.25 + emotional * 0.20,

        "The Fearless Explorer":
            adaptability * 0.55 + decision * 0.30 + social * 0.15,

        "The Empathetic Soul":
            emotional * 0.60 + social * 0.20 + awareness * 0.20,

        "The Natural Leader":
            decision * 0.50 + social * 0.25 + adaptability * 0.25,

        "The Creative Dreamer":
            adaptability * 0.35 + awareness * 0.35 + emotional * 0.15 + social * 0.15,

        "The Balanced Realist":
            100 - (
                max(results.values()) - min(results.values())
            )
    }

    return sorted(
        matches.items(),
        key=lambda item: item[1],
        reverse=True
    )


def get_archetype(results):

    matches = get_archetype_matches(results)

    return matches[0][0]


# ==========================================
# COMPLETE PERSONALITY REPORT
# ==========================================

def generate_personality_report(answers, results=None):

    if results is None:
        results = analyse_personality(answers)

    matches = get_archetype_matches(results)

    primary = matches[0][0]
    secondary = matches[1][0]

    profile = ARCHETYPES[primary]
    secondary_profile = ARCHETYPES[secondary]

    sorted_dimensions = sorted(
        results.items(),
        key=lambda item: item[1],
        reverse=True
    )

    average = round(
        sum(results.values()) / len(results),
        2
    )

    strongest = sorted_dimensions[0]
    weakest = sorted_dimensions[-1]

    score_range = strongest[1] - weakest[1]

    if score_range <= 12:
        personality_pattern = "Well Distributed Personality"
        pattern_description = (
            "Your scores are relatively close to each other. "
            "No single dimension strongly dominates your responses."
        )

    elif score_range <= 25:
        personality_pattern = "Multi-Dimensional Personality"
        pattern_description = (
            "You show a combination of different behavioural tendencies. "
            "Some dimensions are more prominent, while others remain important."
        )

    else:
        personality_pattern = "Strongly Defined Personality Pattern"
        pattern_description = (
            "Your responses show a noticeable difference between your "
            "strongest and weakest dimensions."
        )

    dimension_reports = {}

    for dimension, score in results.items():

        level = get_level(score)

        dimension_reports[dimension] = {
            "score": score,
            "level": level,
            **DIMENSION_DETAILS[dimension][level]
        }

    return {

        "primary": primary,
        "secondary": secondary,

        "primary_profile": profile,
        "secondary_profile": secondary_profile,

        "matches": matches,

        "average": average,

        "strongest": strongest,
        "weakest": weakest,

        "personality_pattern": personality_pattern,
        "pattern_description": pattern_description,

        "dimensions": dimension_reports,

        "social_style": profile["social"],
        "pressure_style": profile["pressure"],
        "decision_style": profile["decision"],

        "strengths": [
            profile["strength"],
            DIMENSION_DETAILS[strongest[0]][
                get_level(strongest[1])
            ]["strength"]
        ],

        "growth_areas": [
            profile["growth"],
            DIMENSION_DETAILS[weakest[0]][
                get_level(weakest[1])
            ]["growth"]
        ],

        "advice": profile["advice"]
    }


# ==========================================
# TERMINAL TEST
# ==========================================

def display_analysis(answers):

    results = analyse_personality(answers)

    report = generate_personality_report(
        answers,
        results
    )

    print("\n========== VIBEMIRROR RESULTS ==========\n")

    for dimension, score in results.items():
        print(f"{dimension}: {score}/100")

    print("\n========== PERSONALITY REVEAL ==========")

    print("\nPrimary Archetype:", report["primary"])
    print("Secondary Archetype:", report["secondary"])

    print("\n", report["primary_profile"]["description"])

    print("\nPersonality Pattern:")
    print(report["personality_pattern"])

    print("\nStrongest Dimension:")
    print(report["strongest"])

    print("\nWeakest Dimension:")
    print(report["weakest"])

    print("\n========================================")


if __name__ == "__main__":

    sample_answers = {
        qid: 2 for qid in range(1, 26)
    }

    display_analysis(sample_answers)