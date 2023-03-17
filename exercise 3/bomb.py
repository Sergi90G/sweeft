#● int n: the number of seconds to simulate
#● string grid[r]: an array of string that represents the grid
def bomber_man(n, grid):
    row = len(grid)
    col = len(grid[0])
    bombs = [[False for j in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
           if grid[i][j] == 'O':
              bombs[i][j] = True 
              
              print()