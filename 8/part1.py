import sys

def find_mapping(sequence):
    mapping = {}
    for segments in sequence:
        if len(segments) == 2:
            mapping["".join(sorted(segments))] = 1
        elif len(segments) == 4:
            mapping["".join(sorted(segments))] = 4
        elif len(segments) == 3:
            mapping["".join(sorted(segments))] = 7
        elif len(segments) == 7:
            mapping["".join(sorted(segments))] = 8
    return mapping

def count_digits(output, mapping):
    count = 0
    for segment in output:
        if "".join(sorted(segment)) in mapping:
            count = count + 1
    return count

with open(sys.argv[1]) as f:
    total_count = 0
    for line in f:
        data = line.split(' | ')
        sequence = data[0].split()
        mapping = find_mapping(sequence)
        output = data[1].split()
        total_count = total_count + count_digits(output, mapping)

print(total_count)
