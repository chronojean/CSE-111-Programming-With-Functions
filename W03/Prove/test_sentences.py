from sentence import get_determiner,get_noun,get_preposition,get_verb,get_prepositional_phrase
import pytest,random

dicc = {
    "n_tests":10,
    "preps" : ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"],
    "dets" : {"s":["a", "one", "the"],"p":["some", "many", "the"]},
    "nouns" : {"s":["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"],"p":["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]},
    "verbs":{"past":["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"],
             "present":{"s":["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"],"p":["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]},
             "future":["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]}
}

def test_get_determiner():
    for i in range(dicc["n_tests"]):
        #Single
        assert get_determiner(1) in dicc["dets"]["s"]
        #Plural
        assert get_determiner(2) in dicc["dets"]["p"]

def test_get_noun():
    for i in range(dicc["n_tests"]):
        #Single
        assert get_noun(1) in dicc["nouns"]["s"]
        #Plural
        assert get_noun(2) in dicc["nouns"]["p"]

def test_get_verb():
    for i in range(dicc["n_tests"]):
        #Single
        assert get_verb(1,"past") in dicc["verbs"]["past"]
        assert get_verb(1,"present") in dicc["verbs"]["present"]["s"]
        assert get_verb(1,"future") in dicc["verbs"]["future"]
        #Plural
        assert get_verb(2,"past") in dicc["verbs"]["past"]
        assert get_verb(2,"present") in dicc["verbs"]["present"]["p"]
        assert get_verb(2,"future") in dicc["verbs"]["future"]

def test_get_preposition():
    for i in range(dicc["n_tests"]):
        assert get_preposition() in dicc["preps"]

def test_get_prepositional_phrase():
    for i in range(dicc["n_tests"]):
        quantity = i%2
        word = get_prepositional_phrase(quantity+1).split(" ")
        assert len(word) == 3
        assert word[0] in dicc["preps"]
        assert word[1] in dicc["dets"]["s" if quantity == 0 else "p"]
        assert word[2] in dicc["nouns"]["s" if quantity == 0 else "p"]
 
pytest.main(["-v", "--tb=line", "-rN", __file__])