#1275. Find Winner on a Tic Tac Toe Game

#Work
#The game is played on a 3x3 grid. You are given a list of moves where each move is represented as a list of three integers [row, col, player].
#The moves are made alternately by player 1 and player 2.
#Determine the winner of the game or return "Draw" if there is no winner, or "Pending" if the game is still ongoing.

#Rozwiązanie

def tictactoe(moves):
    scores = {
        "row": [0, 0, 0],
        "col": [0, 0, 0],
        "diag": [0, 0]
    }
    for i, (row, col) in enumerate(moves):
        val = 1 if i % 2 == 0 else -1 
        scores["row"][row] += val
        scores["col"][col] += val
        print(i,row+col==2)
        if row == col:
            scores["diag"][0] += val
        if row + col == 2:
            scores["diag"][1] += val
        #print(i,val, row, col,"row",scores["row"])
        #print(i,"col",scores["col"])
        #print(i,"diag",scores["diag"])
        if 3 in scores["row"] or 3 in scores["col"] or 3 in scores["diag"]:
            return "A"
        if -3 in scores["row"] or -3 in scores["col"] or -3 in scores["diag"]:
            return "B"
    
    # If no one has won, check if the game is a draw or still pending
    if len(moves) == 9:
        return "Draw"
    else:
        return "Pending"        
                
                    
                        
                            
                                    

#Example 1:
#Input: moves = [[0,0],[1,1],[0,1],[1,0],[0,2],[1,2]]
#Output: "A"
moves = [[0,0],[1,1],[0,1],[1,0],[0,2],[1,2]]
output = "A"
print(f"#Example 1:\nInput: moves = {moves}\nOutput: '{output}' ==>", tictactoe(moves))

#Example 2:
#Input: moves = [[0,0],[1,1],[0,1],[1,0],[0,2],[1,2],[2,1]]
#Output: "B"
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
output = "B"
print(f"#Example 2:\nInput: moves = {moves}\nOutput: '{output}' ==>", tictactoe(moves))

#Example 3:
#Input: moves = [[0,0],[1,1],[0,1],[1,0],[0,2],[1,2],[2,0],[2,1],[2,2]]
#Output: "Draw"
moves = [[0,0],[1,1],[0,1],[1,0],[0,2],[1,2],[2,0],[2,1],[2,2]]
output = "Draw"
print(f"#Example 3:\nInput: moves = {moves}\nOutput: '{output}' ==>", tictactoe(moves))

#Boundary Example 1:
#Input: moves = [[0,0],[1,1],[0,1],[1,0],[0,2],[1,2],[2,2]]  # No winner yet
#Output: "Pending"
moves = [[0,0],[1,1],[0,1],[1,0],[0,2],[1,2],[2,2]]
output = "Pending"
print(f"#Boundary Example 1:\nInput: moves = {moves}\nOutput: '{output}' ==>", tictactoe(moves))

#Boundary Example 2:
#Input: moves = [[0,0],[1,1],[0,1],[1,0],[0,2]]  # Incomplete game
#Output: "Pending"
moves = [[0,0],[1,1],[0,1],[1,0],[0,2]]
output = "Pending"
print(f"#Boundary Example 2:\nInput: moves = {moves}\nOutput: '{output}' ==>", tictactoe(moves))

#Boundary Example 3:
#Input: moves = [[0,0],[1,1],[0,1],[1,0],[1,2],[0,2],[2,1],[2,0],[2,2]]  # Full game
#Output: "Draw"
moves = [[0,0],[1,1],[0,1],[1,0],[1,2],[0,2],[2,1],[2,0],[2,2]]
output = "Draw"
print(f"#Boundary Example 3:\nInput: moves = {moves}\nOutput: '{output}' ==>", tictactoe(moves))
