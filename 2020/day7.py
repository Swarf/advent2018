import re


class BagColor:
    def __init__(self, name):
        self.name = name
        self.parents = set()
        self.children = {}

    def __str__(self):
        return '<{} -> {}>'.format(self.name, ', '.join([x.name for x in self.children]))


colors = {}

line_pat = re.compile(r'^(.+) bags contain (.+)\.$')
child_pat = re.compile(r'^(\d+) (.+) bags?$')
with open('data/day7') as data_file:
    for line in [x.rstrip() for x in data_file]:
        match = line_pat.match(line)
        if not match:
            raise ValueError("Failed to parse: {}".format(line))
        color_name = match.group(1)
        bag_color = colors.get(color_name)
        if not bag_color:
            bag_color = BagColor(color_name)
            colors[color_name] = bag_color

        for child_clause in match.group(2).split(', '):
            match = child_pat.match(child_clause)
            if match:
                child_color_name = match.group(2)
                child_bag = colors.get(child_color_name)
                if not child_bag:
                    child_bag = BagColor(child_color_name)
                    colors[child_color_name] = child_bag

                bag_color.children[child_bag] = int(match.group(1))
                child_bag.parents.add(bag_color)
            elif child_clause != 'no other bags':
                raise ValueError("Fail to parse child: {}".format(child_clause))

to_check = {colors['shiny gold']}
checked = set()

while to_check:
    check_bag = to_check.pop()
    if check_bag in checked:
        continue

    checked.add(check_bag)
    to_check.update(check_bag.parents)

print('7a: ', len(checked) - 1)


def count_children(bag: BagColor):
    child_count = 0
    for child, count in bag.children.items():
        child_count += count
        child_count += count * count_children(child)

    return child_count


print('7b: {}'.format(count_children(colors['shiny gold'])))



