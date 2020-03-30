#*************************************/
#           SOURCE CODE
#*************************************/

import argparse
import datetime


#******************************************************************/
#    THIS FUNCTION SOLVES THE MAZE PROBLEM USING BACKTRACKING. IT   
#    RETURNS FALSE IF NO PATH IS AVAILABLE,OTHERWISE RETURNS TRUE.
#******************************************************************/


def maze_solver( r, c ):
    if maze[SIZE-1][SIZE-1] == 0:
        return False
    if (r==SIZE-1) and (c==SIZE-1):#if destination is reached
        solution[r][c] = 1;
        return True
    if (r>=0 and c>=0 and r<SIZE and c<SIZE #checking if we can visit in the cell or not 
        and solution[r][c] == 0 and maze[r][c] == 1):
        solution[r][c] = 1 #visiting the cell
        if maze_solver(r+1, c): #going down
            return True
        if maze_solver(r, c+1): #going right
            return True
        if maze_solver(r-1, c): #going up
            return True
        if maze_solver(r, c-1): #going left
            return True    
        solution[r][c] = 0; #backtracking
        return False;
    return False;


#*****************************************************/
#    THIS FUNCTION PRINTS THE PATH IN THE FORM OF 1S.
#*****************************************************/


def print_solution( sol ):
    f1.write("***\n" + "Following the path " + moveCheck(sol) + " leads to the destination:\n\n")
    for i in sol:
        for j in i:
            f1.write(" " + str(j) + " ")
        f1.write('\n') 
    now = datetime.datetime.now()
    f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S\n" + "***\n\n"))


#**********************************************************************************************/
# THIS FUNCTION RETURNS A STRING CONTAINING MOVEMENTS NEED TO BE DONE TO REACH THE DESTINATION.
#**********************************************************************************************/


def moveCheck( solvedMaze ):
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


#*************************************/
#           DRIVER CODE
#*************************************/

if __name__ == "__main__":	
    maze = []

    #TAKING FILE ARGUMENTS FROM COMMAND LINE.
    parser = argparse.ArgumentParser()
    parser.add_argument("ipFile", help="Input File")
    parser.add_argument("opFile", help="Output File")
    args = parser.parse_args()
    f = open(args.ipFile,'r')#input file
    f1 = open(args.opFile,'a')#output file
    
    # GENERATING MAZE FROM INPUTS
    for data in f:
        [l.strip('\n\r') for l in data]
        maze.append([int(x) for x in data.split()])
    SIZE = len(maze)
    solution = [[0]*SIZE for _ in range(SIZE)]    

    # MAZE-RUNNER
    if(maze_solver(0,0)):
        print_solution(solution)
    else:
        f1.write("***\n-1\n")
        f1.write("No path available to reach destination.")
        now = datetime.datetime.now()
        f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S") + "\n***\n\n\n")
