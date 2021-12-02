import queue

increases = 0
window_size = 3
window = queue.Queue(window_size)
reading_sum = 0
prev_reading_sum = -1

with open("data") as f:
    for line in f:
        reading = int(line)
        reading_sum += reading
        window.put(reading)
        if window.full():
            if prev_reading_sum != -1:
                if reading_sum > prev_reading_sum:
                    increases = increases + 1
            prev_reading_sum = reading_sum
            reading_sum = reading_sum - window.get()

print(f"{increases} increases")
        
