import sys
#6=096
#5=235

def num_matching(segments1, segments2):
    count = 0
    for segment in segments1:
        if segment in segments2:
            count = count + 1
    return count

def find_mapping(sequence):
    mapping = {}
    rev_mapping = {}
    for segments in sequence:
        if len(segments) == 2:
            mapping[segments] = 1
            rev_mapping[1] = segments
        elif len(segments) == 4:
            mapping[segments] = 4
            rev_mapping[4] = segments
        elif len(segments) == 3:
            mapping[segments] = 7
            rev_mapping[7] = segments
        elif len(segments) == 7:
            mapping[segments] = 8
            rev_mapping[8] = segments

    # Identify no 0,6
    for segments in sequence:
        if len(segments) == 6:
            if num_matching(segments, rev_mapping[1]) == 1:
                rev_mapping[6] = segments
                mapping[segments] = 6
            elif num_matching(segments, rev_mapping[4]) == 4:
                rev_mapping[9] = segments
                mapping[segments] = 9
            else:
                rev_mapping[0] = segments
                mapping[segments] = 0

        if len(segments) == 5:
            if num_matching(segments, rev_mapping[1]) == 2:
                rev_mapping[3] = segments
                mapping[segments] = 3
            elif num_matching(segments, rev_mapping[4]) == 2:
                rev_mapping[2] = segments
                mapping[segments] = 2
            else:
                rev_mapping[5] = segments
                mapping[segments] = 5

    return mapping

def get_digits(output, mapping):
    count = 0
    digits = 0
    for i in range(0,len(output)):
        value = 10**(len(output)-i-1) * mapping[output[i]]
        digits = digits + value
    return digits

with open(sys.argv[1]) as f:
    total_sum = 0
    for line in f:
        data = line.split(' | ')
        sequence = ["".join(sorted(segments)) for segments in data[0].split()]
        mapping = find_mapping(sequence)
        output = ["".join(sorted(segments)) for segments in data[1].split()]
        digits = get_digits(output, mapping)
        total_sum = total_sum + digits
print(total_sum)

