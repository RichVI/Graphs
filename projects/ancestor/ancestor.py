from util import Queue

# ```
#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```

def earliest_ancestor(ancestors, starting_node):
    dictionary = {}
    queue = Queue()
    visited = set()
    longest_path_len = 1
    earliest_ancestor = -1
    
    # loop through the given ancestors list
    # create my dictionary dict {child: {parents}}
    for pairs in ancestors:
        dictionary[pairs[1]] = set()
    for pairs in ancestors:
        dictionary[pairs[1]].add(pairs[0])
    print("dict",dictionary)

    # if the starting node is a not a key of dictionary, means no parent, return -1
    if starting_node not in dictionary:
        return -1


    queue.enqueue([starting_node])

    # while the queue is not empty
    while queue.size() > 0:
        current_path = queue.dequeue()
        print("current path", current_path)

        current_node = current_path[-1] 
        print("current node", current_node)   

        # if it's not in visited, mark as visited
        if current_node not in visited:
            visited.add(current_node)
            # get the neighbors
            neighbors = dictionary.get(current_node)

            # loop through neighbors, and if neighbor is not none
            if neighbors is not None:

                # construct new path by adding each neighbor to the end
                for neighbor in neighbors:
                    print("neighbor", neighbor)
                    new_path = current_path + [neighbor]
                    print("new path", new_path)
                    queue.enqueue(new_path)

            # at the end of the path when there's no neighbors
            else:

                # check if the length of current path is longer or equal to the length of the longest path
                if len(current_path) >= longest_path_len:
                    longest_path_len = len(current_path)

                    # assign current node to earliest ancestor
                    earliest_ancestor = current_node
                    print("earliest_ancestor", earliest_ancestor)
    return earliest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))