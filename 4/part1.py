import sys

class Bingo:
    def __init__(self):
        self.draws = None
        self.boards = []
        self.current_board = []

    def add_data(self, data):
        if not data:
            return
        if not self.draws:
            self.draws = [int(value) for value in data.split(',')]
        else:
            self.current_board.append([(int(value), False) for value in data.split()])
            if len(self.current_board) == 5:
                self.boards.append(self.current_board)
                self.current_board = []


    def play(self):
        for draw in self.draws:
            for board in self.boards:
                score = self.mark_board(board, draw)
                if score:
                    return score*draw

    def mark_board(self, board, draw):
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if draw == board[i][j][0]:
                    board[i][j] = (draw,True)
                    return self.check_board(board,i,j)
        return False

    def check_board(self, board, new_i, new_j):
        for i in range(0,len(board)):
            if board[i][new_j][1] == False:
                break
        else:
            return self.score_board(board)

        for j in range(0,len(board[new_i])):
            if board[new_i][j][1] == False:
                break
        else:
            return self.score_board(board)

        return False

    def score_board(self, board):
        score = 0
        for row in board:
            for item in row:
                if not item[1]:
                    score += item[0]

        return score

    def print_boards(self):
        for board in self.boards:
            self.print_board(board)


    def print_board(self, board):
        for row in board:
            print(row)
        print()
        

bingo = Bingo()

with open(sys.argv[1]) as f:
    for line in f:
        bingo.add_data(line.strip())

print(bingo.play())

#print("DRAWS")
#print(bingo.draws)
#print("BOARDS")
#bingo.print_boards()
