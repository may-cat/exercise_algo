import logging


def get_children(source, parent_to_search, used_nodes):
    result = {}

    for el in source.copy():
        if el[0] == parent_to_search:
            if el[1] in used_nodes:
                logging.error("Попытка сделать узлу два родителя!")
                logging.error(el[1])
                raise Exception("Попытка сделать узлу два родителя!")
            else:
                used_nodes.append(el[1])
            result[el[1]] = get_children(source, el[1], used_nodes)
            source.remove(el)

    return result


def tree_builder(original_source):
    source_copy = original_source.copy()
    used_nodes = []
    # Check if any non-rooted elements left
    resl = get_children(source_copy, None, used_nodes)

    if len(source_copy) > 0:
        logging.error("Узлы, которые не получается встроить в дерево")
        logging.error(source_copy)
        raise Exception("Часть узлов не может быть встроена в дерево!")

    return resl

