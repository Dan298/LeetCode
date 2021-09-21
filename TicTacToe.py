

class Solution(object):
    def __init__(self):
        self.diagonal1 = [[0,0],[1,1],[2,2]]
        self.diagonal2 = [[0,2],[1,1],[2,0]]

    def checkA(self, a_list):
        columns = []
        rows = []
        three_check = []

        if (all(x in a_list for x in self.diagonal1)):
            return 'A wins'
        if (all(x in a_list for x in self.diagonal2)):
            return 'A wins'

        for x in a_list:
            columns.append(x[0])
            rows.append(x[1])

        three_check.append(columns.count(0))
        three_check.append(columns.count(1))
        three_check.append(columns.count(2))

        three_check.append(rows.count(0))
        three_check.append(rows.count(1))
        three_check.append(rows.count(2))

        for x in three_check:
            if x == 3:
                return 'A wins'
        return ''

    def tictactoe(self, moves):
        a_list = []
        b_list = []


        count = 0
        for move in moves:
            if count % 2 == 0:
                a_list.append(move)
            else:
                b_list.append(move)
            count += 1

        outcomeA = self.checkA(a_list)
        outcomeB = self.checkB(b_list)
        final = outcomeA + outcomeB
        if final == '':
            if len(moves) < 9:
                return "Pending"
            else:
                return 'Draw'
        return final




    def checkB(self, b_list):
        columns = []
        rows = []
        three_check = []

        if (all(x in b_list for x in self.diagonal1)):
            return 'B wins'
        if (all(x in b_list for x in self.diagonal2)):
            return 'B wins'

        for x in b_list:
            columns.append(x[0])
            rows.append(x[1])

        three_check.append(columns.count(0))
        three_check.append(columns.count(1))
        three_check.append(columns.count(2))

        three_check.append(rows.count(0))
        three_check.append(rows.count(1))
        three_check.append(rows.count(2))

        for x in three_check:
            if x == 3:
                return 'B wins'
        return ''

game = Solution()
output = game.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
print(output)