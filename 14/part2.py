import sys

rules = []
pairs = {}
template = ''

with open(sys.argv[1]) as f:
    read_points = True
    template = f.readline().strip()
    for i in range (1,len(template)):
        pairs[template[i-1]+template[i]] = pairs.get(template[i-1]+template[i],0) + 1
    f.readline()
    for line in f:
        rule = line.strip().split(' -> ')
        rules.append(rule)
        if rule[0] not in pairs:
            pairs[rule[0]] = 0

def do_insertions(pairs, rules):
    new_pairs = {}
    for pair in pairs:
        new_pairs[pair] = 0
    for rule in rules:
        count = pairs[rule[0]]
        if not count:
            continue
        new_pairs[rule[0][0] + rule[1]] = new_pairs[rule[0][0] + rule[1]] + count
        new_pairs[rule[1] + rule[0][1]] = new_pairs[rule[1] + rule[0][1]] + count
    return new_pairs

def get_counts(pairs):
    counts = {}
    for pair in pairs:
        counts[pair[0]] = counts.get(pair[0],0) + pairs[pair]
    return counts


for i in range(0,40):
    pairs = do_insertions(pairs,rules)

counts = get_counts(pairs)
counts[template[len(template)-1]] = counts[template[len(template)-1]] + 1

max_item = None
min_item = None
for item in counts:
    if not counts[item]:
        continue
    if not max_item:
        max_item = item
        min_item = item
    else:
        if counts[item] > counts[max_item]:
            max_item = item
        if counts[item] < counts[min_item]:
            min_item = item

print(counts[max_item] - counts[min_item])
