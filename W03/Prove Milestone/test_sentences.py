from sentence import get_determiner,get_noun,get_verb
import pytest
n_tests = 10

def test_get_determiner():
    for i in range(n_tests):
        #Single
        assert get_determiner(1) in ["a", "one", "the"]
        #Plural
        assert get_determiner(2) in ["some", "many", "the"]

def test_get_noun():
    for i in range(n_tests):
        #Single
        assert get_noun(1) in ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
        #Plural
        assert get_noun(2) in ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

def test_get_verb():
    for i in range(n_tests):
        #Single
        assert get_verb(1,"past") in ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
        assert get_verb(1,"present") in ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        assert get_verb(1,"future") in ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
        #Plural
        assert get_verb(2,"past") in ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
        assert get_verb(2,"present") in ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
        assert get_verb(2,"future") in ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
 
pytest.main(["-v", "--tb=line", "-rN", __file__])