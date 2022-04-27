import logging
from func import tree_builder

source1 = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]
expected1 = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

# Expected valid tree
source2 = [
    (None, 'a'),
    ('b11', 'b111'),
    ('a', 'a1'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('a', 'a2'),
    (None, 'b'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b2'),
    (None, 'c'),
    ('c', 'c1'),
]
expected2 = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

# Expected valid tree
source3 = [
    (None, 'a'),
    (None, 'b'),
    ('b', 'c'),
    ('c', 'd'),
    ('a', 'e'),
]
expected3 = {
    'a': {'e': {}},
    'b': {'c': {'d': {}}},
}

# Expected error
source4 = [
    (None, 'a'),
    (None, 'b'),
    ('a', 'c'),
    ('b', 'c'),
]
expected4 = "Exception: два дерева ссылаются на один узел" # Ошибка: два дерева ссылаются на один узел

# Expected error
source5 = [
    (None, 'a'),
    (None, 'b'),
    ('a', 'c'),
    ('b', 'd'),
    ('d', 'e'),
    ('c', 'e'),
]
expected5 = "Exception: два дерева ссылаются на один узел" # Ошибка: два дерева ссылаются на один узел

# Expected error
source6 = [
    (None, 'a'),
    (None, 'b'),
    ('c', 'd'),
]
expected6 = "Exception: узлы которые не встраиваются в дерево" # Висячие узлы

# Expected error
source7 = [
    (None, 'a'),
    ('a', 'b'),
    ('b', 'a'),
]
expected7 = "Exception: Замкнутый цикл" # цикл!





try:
    print("== source1 v1")
    print("source1")
    print(source1)
    print("tree v2")
    print(tree_builder(source1))
    print("expected")
    print(expected1)
    print('check v2:')
    print(tree_builder(source1)==expected1)
    print("\n\n")
except Exception as err:
    print ("Error")
    print (err)

try:
    print("== source2 v1")
    print("source2")
    print(source2)
    print("tree v2")
    print(tree_builder(source2))
    print("expected")
    print(expected2)
    print('check v2:')
    print(tree_builder(source2)==expected2)
    print("\n\n")
except Exception as err:
    print ("Error")
    print (err)


try:
    print("== source3 v1")
    print("source3")
    print(source3)
    print("tree v2")
    print(tree_builder(source3))
    print("expected")
    print(expected3)
    print('check v2:')
    print(tree_builder(source3)==expected3)
    print("\n\n")
except Exception as err:
    print ("Error")
    print (err)

try:
    print("== source4 v1")
    print("source4")
    print(source4)
    print("tree v2")
    print(tree_builder(source4))
    print("expected")
    print(expected4)
    print('check v2:')
    print(tree_builder(source4)==expected4)
    print("\n\n")
except Exception as err:
    print ("Error")
    print (err)

try:
    print("== source5 v1")
    print("source5")
    print(source5)
    print("tree v2")
    print(tree_builder(source5))
    print("expected")
    print(expected5)
    print('check v2:')
    print(tree_builder(source5)==expected5)
    print("\n\n")
except Exception as err:
    print ("Error")
    print (err)


try:
    print("== source6 v1")
    print("source6")
    print(source6)
    print("tree v2")
    print(tree_builder(source6))
    print("expected")
    print(expected6)
    print('check v2:')
    print(tree_builder(source6)==expected6)
    print("\n\n")
except Exception as err:
    print ("Error")
    print (err)

try:
    print("== source7 v1")
    print("source7")
    print(source7)
    print("tree v2")
    print(tree_builder(source7))
    print("expected")
    print(expected7)
    print('check v2:')
    print(tree_builder(source7)==expected7)
    print("\n\n")
except Exception as err:
    print ("Error")
    print (err)

