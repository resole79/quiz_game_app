import requests

parameters = {
    "amount": 10,
    # "category": 12,
    # "difficulty": "medium",
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]

"""
question_data = [
    {"category": "Entertainment: Music",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The music group Daft Punk got their name from a negative review they recieved.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
     "type": "boolean",
      "difficulty": "medium",
     "question": "Arcade Fire's 'The Suburbs' won the Album of the Year award in the 2011 Grammys.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "medium",
     "question": "The cover of The Beatles album 'Abbey Road' featured a Volkswagen Beetle in the background.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "medium",
     "question": "Scottish producer Calvin Harris is from the town of Dumfries, Scotland.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "medium",
     "question": "Norwegian producer Kygo released a remix of the song 'Sexual Healing' by Marvin Gaye.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "medium",
     "question": "Ashley Frangipane performs under the stage name Halsey.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "medium",
     "question": "For his performance at ComplexCon 2016 in Long Beach, California, Skrillex revived his 'Mothership'; set piece for one night only.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "easy",
     "question": "Daft Punk originated in France.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "easy",
     "question": "Scatman John's real name was John Paul Larkin.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "medium",
     "question": "Metallica collaborated with Rowan Atkinson's Mr Bean on a 1992 comic relief single.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]
     },
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "easy",
     "question": "Lead Singer Rivers Cuomo of American rock band Weezer attended Harvard.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music",
    "type": "boolean",
    "difficulty": "medium",
     "question": "Green Day's album 'American Idiot'; is considered a 'punk rock opera.'",
     "correct_answer": "True",
     "incorrect_answers": ["False"]
     }
]
"""