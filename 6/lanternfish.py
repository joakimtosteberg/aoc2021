import sys

buckets = [0]*9
with open(sys.argv[1]) as f:
    for value in f.readline().split(','):
        buckets[int(value)] = buckets[int(value)] + 1

def age_lanternfish(buckets):
    new_buckets = [0]*9
    new_buckets[0] = buckets[1]
    new_buckets[1] = buckets[2]
    new_buckets[2] = buckets[3]
    new_buckets[3] = buckets[4]
    new_buckets[4] = buckets[5]
    new_buckets[5] = buckets[6]
    new_buckets[6] = buckets[0] + buckets[7]
    new_buckets[7] = buckets[8]
    new_buckets[8] = buckets[0]

    return new_buckets

def simulate_lanternfish(buckets, days_to_simulate):
    for day in range(0,days_to_simulate):
        buckets = age_lanternfish(buckets)
    return sum(buckets)

print(f"{simulate_lanternfish(buckets, 80)} lanternfish after 80 days")
print(f"{simulate_lanternfish(buckets, 256)} lanternfish after 256 days")
