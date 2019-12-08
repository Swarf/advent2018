from string import ascii_uppercase


class Node:
    def __init__(self, label):
        self.label = label
        self.next = set()
        self.prev = set()

    def __repr__(self):
        return '<{}>'.format(self.label)


all_nodes = {}
front_nodes = set()

with open('data/day7.txt') as data:
    for line in data:
        pre_label = line[5]
        nex_label = line[36]

        if pre_label in all_nodes:
            pre = all_nodes[pre_label]
        else:
            pre = Node(pre_label)
            all_nodes[pre_label] = pre
            front_nodes.add(pre)

        if nex_label in all_nodes:
            nex = all_nodes[nex_label]
        else:
            nex = Node(nex_label)
            all_nodes[nex_label] = nex

        front_nodes.discard(nex)
        pre.next.add(nex)
        nex.prev.add(pre)

original_front_nodes = frozenset(front_nodes)
nodes_list = set()  # Prep for part 2
order = []
while front_nodes:
    current_node = sorted(front_nodes, key=lambda x: x.label)[0]
    front_nodes.remove(current_node)
    order.append(current_node)
    del all_nodes[current_node.label]

    for next_node in current_node.next:
        if not any(filter(lambda x: x.label in all_nodes, next_node.prev)):
            front_nodes.add(next_node)

print('alpha order', ''.join([node.label for node in order]))


front_nodes = set(original_front_nodes)

current_time = 0
next_finish_time = 0
in_progress = {}
worker_count = 5
task_baseline_time = 60
all_nodes = set(order)


while front_nodes or in_progress:
    current_time = next_finish_time
    next_finish_time = None
    done = set()
    for node, time_done in in_progress.items():
        if time_done <= current_time:
            done.add(node)
            all_nodes.remove(node)
        elif next_finish_time is None or time_done < next_finish_time:
            next_finish_time = time_done

    for node in done:
        del in_progress[node]
        for next_node in node.next:
            if not any(filter(lambda x: x in all_nodes, next_node.prev)):
                front_nodes.add(next_node)

    for current_node in sorted(front_nodes, key=lambda x: x.label):
        if len(in_progress) >= worker_count:
            break

        front_nodes.remove(current_node)
        time_done = ascii_uppercase.index(current_node.label) + 1 + current_time + task_baseline_time
        in_progress[current_node] = time_done
        if next_finish_time is None or time_done < next_finish_time:
            next_finish_time = time_done

print('total time', current_time)
