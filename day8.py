
with open('data/day8.txt') as data_file:
    data = [int(x) for x in data_file.readline().split(' ')]


class Node:
    def __init__(self, child_count, meta_count):
        self.children = []
        self.missing = child_count
        self.metadata = None
        self.meta_count = meta_count

    def sum_metadata(self):
        return sum(self.metadata) + sum([c.sum_metadata() for c in self.children])

    def meta_value2(self):
        return sum([self.children[i - 1].meta_value2() for i in self.metadata if 0 < i <= len(self.children)]) \
            if self.children else sum(self.metadata)


head = Node(*data[:2])
del data[:2]
stack = [head]
current = head

index = 2
while data:
    if current.missing:
        new_node = Node(*data[:2])
        current.children.append(new_node)
        current.missing -= 1

        del data[:2]
        stack.append(new_node)
        current = new_node
    else:
        current.metadata = data[:current.meta_count]
        del data[:current.meta_count]
        del stack[-1]
        current = stack[-1] if stack else None


print('metadata', head.sum_metadata())
print('meta2', head.meta_value2())
