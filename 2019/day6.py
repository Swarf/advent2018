# day 6


class Node:
    def __init__(self, name):
        self.name = name
        self.generation = None
        self.parent = None
        self.children = []

    def __str__(self):
        return self.name


nodes = {}
orbits = 0

with open('data/day6') as data_file:
    for line in data_file:
        center, satellite = line.rstrip().split(')')
        c_node = nodes.get(center, None) or nodes.setdefault(center, Node(center))
        s_node = nodes.get(satellite, None) or nodes.setdefault(satellite, Node(satellite))
        c_node.children.append(s_node)
        s_node.parent = c_node


def count_orbits(node: Node, generation=0):
    global orbits
    generation += 1
    for child in node.children:
        orbits += generation
        child.generation = generation
        count_orbits(child, generation)


# Part 1
count_orbits(nodes['COM'])
print(orbits)


def parent_chain(node: Node) -> [Node]:
    if node.parent:
        chain = parent_chain(node.parent)
        chain.append(node)
    else:
        chain = [node]
    return chain


# Part 2
you_chain = parent_chain(nodes['YOU'])
san_chain = parent_chain(nodes['SAN'])
common_gen = 0
common_node = None

while True:
    if you_chain[common_gen] is san_chain[common_gen]:
        common_node = you_chain[common_gen]
        common_gen += 1
    else:
        break

print('Common generation is {}'.format(common_node.generation))
print('Jumps = {}'.format(nodes['YOU'].generation - common_gen + nodes['SAN'].generation - common_gen))
