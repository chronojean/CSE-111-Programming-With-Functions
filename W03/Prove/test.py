
# def get_verb(quantity, tense):
#     """Return a randomly chosen verb.
#     If tense is "past",
#     this function will return one of these ten verbs:
#         "drank", "ate", "grew", "laughed", "thought",
#         "ran", "slept", "talked", "walked", "wrote"
#     If tense is "present" and quantity is 1, this
#     function will return one of these ten verbs:
#         "drinks", "eats", "grows", "laughs", "thinks",
#         "runs", "sleeps", "talks", "walks", "writes"
#     If tense is "present" and quantity is NOT 1,
#     this function will return one of these ten verbs:
#         "drink", "eat", "grow", "laugh", "think",
#         "run", "sleep", "talk", "walk", "write"
#     If tense is "future", this function will return one of
#     these ten verbs:
#         "will drink", "will eat", "will grow", "will laugh",
#         "will think", "will run", "will sleep", "will talk",
#         "will walk", "will write"

#     Parameters
#         quantity: an integer that determines if the
#             returned verb is single or plural.
#         tense: a string that determines the verb conjugation,
#             either "past", "present" or "future".
#     Return: a randomly chosen verb.
#     """
#     verbs = {"past":["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"],
#              "present":{"s":["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"],
#                         "p":["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]},
#              "future":["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]}
#     if tense == "past":
#         return random.choice(verbs["past"])
#     elif tense == "present":
#         return random.choice(verbs["present"]["s"] if quantity == 1 else verbs["present"]["p"])
#     elif tense == "future":
#         return random.choice(verbs["future"])

# def test_get_verb():
#     for i in range(n_tests):
#         #Single
#         assert get_verb(1,"past") in ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
#         assert get_verb(1,"present") in ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
#         assert get_verb(1,"future") in ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
#         #Plural
#         assert get_verb(2,"past") in ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
#         assert get_verb(2,"present") in ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
#         assert get_verb(2,"future") in ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
