import random

def get_determiner(quantity=1):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    determinier = {"s":["a", "one", "the"],"p":["some", "many", "the"]}
    
    return random.choice(determinier["s"] if quantity == 1 else determinier["p"]) 

def get_noun(quantity=1):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    nouns = {"s":["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"],"p":["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]}
    
    return random.choice(nouns["s"] if quantity == 1 else nouns["p"])

def get_verb(quantity, tense):
    """Return a randomly chosen verb.
    If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    verbs = {"past":["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"],
             "present":{"s":["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"],
                        "p":["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]},
             "future":["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]}
    if tense == "past":
        return random.choice(verbs["past"])
    elif tense == "present":
        return random.choice(verbs["present"]["s"] if quantity == 1 else verbs["present"]["p"])
    elif tense == "future":
        return random.choice(verbs["future"])

def main():
    tense = ["past","present","future"]
    counter = 0
    for i in range(6):
         
        if i%3 == 0:
            counter +=1
            print("Singular:" if counter== 1 else "Plural:")
        print("\t------",tense[i%3],"------")
        quantity = 1 if i < 3 else 2
        print("\t",get_determiner(quantity),get_noun(quantity),get_verb(quantity,tense[i%3]))
if __name__ == "__main__":    
    main()