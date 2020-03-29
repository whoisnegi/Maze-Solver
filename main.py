import argparse
import datetime

'''function to solve the maze using backtracking'''
def solveMaze(r, c):
    #if destination is reached
    if (r==SIZE-1) and (c==SIZE-1):
        solution[r][c] = 1;
        return True
    #checking if we can visit in the cell or not    
    if r>=0 and c>=0 and r<SIZE and c<SIZE and solution[r][c] == 0 and maze[r][c] == 1:
        solution[r][c] = 1 #visiting the cell
        if solveMaze(r+1, c): #going down
            return True
        if solveMaze(r, c+1): #going right
            return True
        if solveMaze(r-1, c): #going up
            return True
        if solveMaze(r, c-1): #going left
            return True
        #backtracking    
        solution[r][c] = 0;
        return False;
    return False;

def printSolution( sol ):
    f1.write("***\n" + "Following the path " + moveCheck(sol) + " leads to the destination:\n\n")
    for i in sol:
        for j in i:
            f1.write(" " + str(j) + " ")
        f1.write('\n') 
    now = datetime.datetime.now()
    f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S\n" + "***\n\n"))

#function to get the movements need to be done to reach the destination.
def moveCheck(solvedMaze):
    n = len(solvedMaze)
    visited = [[False for _ in range(n)] for _ in range(n)]
    arr = ""
    i = j = 0
    while i!=n-1 or  j!=n-1:
        if j == n-1:
            if solvedMaze[i+1][j] == 1 and visited[i+1][j] == False:
                visited[i+1][j] = True
                i = i+1
                arr+="D"
            elif solvedMaze[i][j-1] == 1 and visited[i][j-1] == False:
                visited[i][j-1] = True
                j = j-1
                arr+="L"  
        elif i == n-1:
            if solvedMaze[i][j+1] == 1 and visited[i][j+1] == False:
                visited[i][j+1] = True
                j = j+1
                arr+="R"  
            elif solvedMaze[i-1][j] == 1 and visited[i-1][j] == False:
                visited[i-1][j] = True
                i = i-1
                arr+="U"    
        else:
            if solvedMaze[i+1][j] == 1 and visited[i+1][j] == False:
                visited[i+1][j] = True
                i = i+1
                arr+="D"
            elif solvedMaze[i][j+1] == 1 and visited[i][j+1] == False:
                visited[i][j+1] = True
                j = j+1
                arr+="R"  
            elif solvedMaze[i-1][j] == 1 and visited[i-1][j] == False:
                visited[i-1][j] = True
                i = i-1
                arr+="U"
            elif solvedMaze[i][j-1] == 1 and visited[i][j-1] == False:
                visited[i][j-1] = True
                j = j-1
                arr+="L"
    return arr

if __name__ == "__main__":	
    maze = []
    #taking file arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("ipFile", help="Input File")
    parser.add_argument("opFile", help="Output File")
    args = parser.parse_args()
   
    f = open(args.ipFile,'r')#input file
    f1 = open(args.opFile,'a')#output file
    
    #generating maze from inputs
    for data in f:
        [l.strip('\n\r') for l in data]
        maze.append([int(x) for x in data.split()])
    
    SIZE = len(maze)
    #list to store the solution matrix
    solution = [[0]*SIZE for _ in range(SIZE)]    
    
    '''MAZE-RUNNER'''
    if(solveMaze(0,0)):
        printSolution(solution)
    else:
        f1.write("***\n-1\n")
        f1.write("No path available to reach destination.")
        now = datetime.datetime.now()
        f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S") + "\n***\n\n\n")
