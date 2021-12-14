import sys

rules = []
template = ''

with open(sys.argv[1]) as f:
    read_points = True
    template = f.readline().strip()
    f.readline()
    for line in f:
        rules.append(line.strip().split(' -> '))

def do_insertions(template, rules):
    result = template[0]
    for i in range(1,len(template)):
        for rule in rules:
            if ((rule[0][0] == template[i-1]) and
                (rule[0][1] == template[i])):
                result = result + rule[1]
                break
        result = result + template[i]
    return result


for i in range(0,10):
    template = do_insertions(template,rules)


counts = {}
for c in template:
    counts[c] = counts.get(c,1) + 1

print(counts)

max_item = None
min_item = None
for item in counts:
    if not max_item:
        max_item = item
        min_item = item
    else:
        if counts[item] > counts[max_item]:
            max_item = item
        if counts[item] < counts[min_item]:
            min_item = item


print(counts[max_item] - counts[min_item])
