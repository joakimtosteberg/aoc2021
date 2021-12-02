previous_reading = -1
increases = 0

with open("data") as f:
    for line in f:
        reading = int(line)
        if previous_reading != -1:
            if reading > previous_reading:
                increases = increases + 1
        previous_reading = reading

print(f"{increases} increases")
        
