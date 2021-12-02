class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def run_command(self, command, args):
        if command == "forward":
            self.move(int(args[0]), 0)
        elif command == "down":
            self.alter_aim(int(args[0]))
        elif command == "up":
            self.alter_aim(-int(args[0]))

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + self.aim * x

    def alter_aim(self, aim):
        self.aim = self.aim + aim

    def get_pos(self):
        return self.x, self.y
        
    

sub = Submarine()

with open("data") as f:
    for line in f:
        command = line.split()
        sub.run_command(command[0],
                        command[1:])


x, y = sub.get_pos()

print(f"solution={x*y}")
