import solvable


class Solution:
    def solve(self, board):
        dict = {}
        one_d_puzzle = []
        for i in range(len(board)):
            one_d_puzzle += board[i]
            print(board[i])
        one_d_puzzle = tuple(one_d_puzzle)
        print(one_d_puzzle)

        dict[one_d_puzzle] = 0

        if one_d_puzzle == (0, 1, 2, 3, 4, 5, 6, 7, 8):
            return 0

        return self.get_paths(dict)

    def get_paths(self, dict):
        cnt = 0
        while True:
            current_nodes = [x for x in dict if dict[x] == cnt]
            if len(current_nodes) == 0:
                return -1

            for node in current_nodes:
                next_moves = self.find_next(node)
                for move in next_moves:
                    if move not in dict:
                        dict[move] = cnt + 1
                    if move == (0, 1, 2, 3, 4, 5, 6, 7, 8):
                        return cnt + 1
            cnt += 1

    def find_next(self, node):
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7],
        }

        results = []
        pos_0 = node.index(0)
        for move in moves[pos_0]:
            new_node = list(node)
            new_node[move], new_node[pos_0] = new_node[pos_0], new_node[move]
            results.append(tuple(new_node))

        return results


ob = Solution()
puzzle = [
    [5, 4, 1],
    [0, 2, 8],
    [3, 6, 7]
]

if solvable.is_solvable(puzzle):
   print("Is puzzle solvable: ", solvable.is_solvable(puzzle))
   print(ob.solve(puzzle))
else:
    print(solvable.is_solvable(puzzle))
