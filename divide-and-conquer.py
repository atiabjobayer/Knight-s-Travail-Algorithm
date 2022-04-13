# KNIGHT MOVES
from math import floor
import numpy as np
import sys


KnightMoves = {(-2, -1), (-1, -2), (+1, -2), (+2, -1),
               (+2, +1), (+1, +2), (-1, +2), (-2, +1)}

######### 8x8 #########
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 1 2 3 4 5 6 7 8

# Already given closed knight's tour for 8x8 chess board (base case).
# As seen in fig. 2:
tour8x8 = {
    (1, 1): [(2, 3), (3, 2)], (2, 3): [(3, 1), (1, 1)],
    (3, 1): [(1, 2), (2, 3)], (1, 2): [(2, 4), (3, 1)],
    (2, 4): [(1, 6), (1, 2)], (1, 6): [(2, 8), (2, 4)],
    (2, 8): [(3, 6), (1, 6)], (3, 6): [(1, 5), (2, 8)],
    (1, 5): [(2, 7), (3, 6)], (2, 7): [(4, 8), (1, 5)],
    (4, 8): [(6, 7), (2, 7)], (6, 7): [(8, 8), (4, 8)],
    (8, 8): [(7, 6), (6, 7)], (7, 6): [(8, 4), (8, 8)],
    (8, 4): [(6, 5), (7, 6)], (6, 5): [(7, 7), (8, 4)],
    (7, 7): [(8, 5), (6, 5)], (8, 5): [(7, 3), (7, 7)],
    (7, 3): [(8, 1), (8, 5)], (8, 1): [(6, 2), (7, 3)],
    (6, 2): [(4, 1), (8, 1)], (4, 1): [(2, 2), (6, 2)],
    (2, 2): [(1, 4), (4, 1)], (1, 4): [(2, 6), (2, 2)],
    (2, 6): [(1, 8), (1, 4)], (1, 8): [(3, 7), (2, 6)],
    (3, 7): [(5, 8), (1, 8)], (5, 8): [(6, 6), (3, 7)],
    (6, 6): [(8, 7), (5, 8)], (8, 7): [(6, 8), (6, 6)],
    (6, 8): [(4, 7), (8, 7)], (4, 7): [(3, 5), (6, 8)],
    (3, 5): [(4, 3), (4, 7)], (4, 3): [(5, 5), (3, 5)],
    (5, 5): [(3, 4), (4, 3)], (3, 4): [(1, 3), (5, 5)],
    (1, 3): [(2, 1), (3, 4)], (2, 1): [(4, 2), (1, 3)],
    (4, 2): [(5, 4), (2, 1)], (5, 4): [(4, 6), (4, 2)],
    (4, 6): [(3, 8), (5, 4)], (3, 8): [(1, 7), (4, 6)],
    (1, 7): [(2, 5), (3, 8)], (2, 5): [(3, 3), (1, 7)],
    (3, 3): [(5, 2), (2, 5)], (5, 2): [(4, 4), (3, 3)],
    (4, 4): [(6, 3), (5, 2)], (6, 3): [(7, 1), (4, 4)],
    (7, 1): [(8, 3), (6, 3)], (8, 3): [(7, 5), (7, 1)],
    (7, 5): [(5, 6), (8, 3)], (5, 6): [(6, 4), (7, 5)],
    (6, 4): [(4, 5), (5, 6)], (4, 5): [(5, 7), (6, 4)],
    (5, 7): [(7, 8), (4, 5)], (7, 8): [(8, 6), (5, 7)],
    (8, 6): [(7, 4), (7, 8)], (7, 4): [(8, 2), (8, 6)],
    (8, 2): [(6, 1), (7, 4)], (6, 1): [(5, 3), (8, 2)],
    (5, 3): [(7, 2), (6, 1)], (7, 2): [(5, 1), (5, 3)],
    (5, 1): [(3, 2), (7, 2)], (3, 2): [(1, 1), (5, 1)]
}

# n is the number of rows/columns of the board.
# It split succesfully only if n is a multiple of 8.


def Split(n):
    if n/8 == floor(n/8):
        new_lenght = n/2
        return int(new_lenght)
    else:
        print("Failed to split", n, "in two parts")
        sys.exit('ERROR: Failed to split into 8x8 sub-boards')


class Chessboard:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.KnightPathList = {}
        self.knightTour = {}

    def SetPathList(self, KnightPathList):
        self.KnightPathList = KnightPathList.copy()

    def GetPathList(self):
        return self.KnightPathList.copy()

    def SetTour(self, tour):
        self.knightTour = tour.copy()

    def GetTour(self):
        return self.knightTour.copy()

    def GetRows(self):
        return self.rows

    def GetColumns(self):
        return self.columns

    # FindPathList allows us to create a new path list given the magnitude of the chessboard
    def FindPathList(self):
        nRows = self.GetRows()
        nColumns = self.GetColumns()

        # Base case: we set the tour for the above given chess boards
        if (nRows == 8) and (nColumns == 8):
            self.SetPathList(tour8x8)
            return

        # Recursive case: we split the boards (into 4 equal subBoards) until we find a base case
        newRows = Split(nRows)
        newColumns = Split(nColumns)

        topLeftBoard = Chessboard(newRows, newColumns)
        topRightBoard = Chessboard(newRows, newColumns)
        bottomLeftBoard = Chessboard(newRows, newColumns)
        bottomRightBoard = Chessboard(newRows, newColumns)

        topLeftBoard.FindPathList()
        topRightBoard.FindPathList()
        bottomLeftBoard.FindPathList()
        bottomRightBoard.FindPathList()

        # Build new path list from bottom left, makes sense for coordinates
        bottomLeftPL = bottomLeftBoard.GetPathList()
        bottomRightPL = bottomRightBoard.GetPathList()
        topLeftPL = topLeftBoard.GetPathList()
        topRightPL = topRightBoard.GetPathList()

        newBottomLeftPL = {}
        newBottomRightPL = {}
        newTopLeftPL = {}
        newTopRightPL = {}

        # In this step, we update the coordinates of every sub-path list starting from the bottom left PL.
        # The bottomLeftPL remain the same;
        # The bottomRightPL has its columns indeces updated;
        # The topLeftPL has its row indeces  updated;
        # The topRightPL has its row & columns indeces  updated.

        # # # # # # #
        # TL  # TR  #
        #     #     #
        # # # # # # #
        #     #     #
        # BL  # BR  #
        # # # # # # #

        for position in bottomLeftPL:
            newBottomLeftPL[position] = []
            for nextSquare in bottomLeftPL[position]:
                newBottomLeftPL[position].append(nextSquare)

        for position in bottomRightPL:
            # Add columns of bottom-left to column indeces of bottom-right
            newPosition = tuple(map(lambda i, j: int(
                i + j), position, (bottomLeftBoard.GetColumns(), 0)))
            newBottomRightPL[newPosition] = []
            for nextSquare in bottomRightPL[position]:
                # Add columns of bottom-left to column indeces of bottom-right
                newNextSquare = tuple(map(lambda i, j: int(
                    i + j), nextSquare, (bottomLeftBoard.GetColumns(), 0)))
                newBottomRightPL[newPosition].append(newNextSquare)

        for position in topLeftPL:
            # Add rows of bottom-left to row indeces of top-left
            newPosition = tuple(map(lambda i, j: int(
                i + j), position, (0, bottomLeftBoard.GetRows())))
            newTopLeftPL[newPosition] = []
            for nextSquare in topLeftPL[position]:
                # Add rows of bottom-left to row indeces of top-left
                newNextSquare = tuple(map(lambda i, j: int(
                    i + j), nextSquare, (0, bottomLeftBoard.GetRows())))
                newTopLeftPL[newPosition].append(newNextSquare)

        for position in topRightPL:
            # Add rows & columns to top-right
            newPosition = tuple(map(lambda i, j: int(
                i + j), position, (bottomLeftBoard.GetColumns(), bottomLeftBoard.GetRows())))
            newTopRightPL[newPosition] = []
            for nextSquare in topRightPL[position]:
                # Add rows & columns to top-right
                newNextSquare = tuple(map(lambda i, j: int(
                    i + j), nextSquare, (bottomLeftBoard.GetColumns(), bottomLeftBoard.GetRows())))
                newTopRightPL[newPosition].append(newNextSquare)

        # Consider Fig. 3, we have to delete edges A,B,C,D and replace them with edges E,D,F,G.
        # To do so, we have to find the coordinate in the chessboard.

                # Relevant squares in 8x8 (into a 16x16):
        A1 = (bottomLeftBoard.GetColumns()-2,
              bottomLeftBoard.GetRows()+1)  # A1 = (6,9)
        A2 = (bottomLeftBoard.GetColumns(),
              bottomLeftBoard.GetRows()+2)  # A2 = (8,10)
        B1 = (bottomLeftBoard.GetColumns()+1,
              bottomLeftBoard.GetRows()+1)  # B1 = (9,9)
        B2 = (bottomLeftBoard.GetColumns()+2,
              bottomLeftBoard.GetRows()+3)  # B2 = (10,11)
        C1 = (bottomLeftBoard.GetColumns()+1,
              bottomLeftBoard.GetRows()-1)  # C1 = (9,7)
        C2 = (bottomLeftBoard.GetColumns()+3,
              bottomLeftBoard.GetRows())  # C2 = (11,8)
        D1 = (bottomLeftBoard.GetColumns()-1,
              bottomLeftBoard.GetRows()-2)  # D1 = (7,6)
        D2 = (bottomLeftBoard.GetColumns(),
              bottomLeftBoard.GetRows())  # D2 = (8,8)
        # Pop edge A
        newTopLeftPL[A1].remove(A2)
        newTopLeftPL[A2].remove(A1)
        # Pop edge B
        newTopRightPL[B1].remove(B2)
        newTopRightPL[B2].remove(B1)
        # Pop edge C
        newBottomRightPL[C1].remove(C2)
        newBottomRightPL[C2].remove(C1)
        # Pop edge D
        newBottomLeftPL[D1].remove(D2)
        newBottomLeftPL[D2].remove(D1)
        # Add edge E
        newBottomLeftPL[D2].append(A1)
        newTopLeftPL[A1].append(D2)
        # Add edge F
        newTopLeftPL[A2].append(B2)
        newTopRightPL[B2].append(A2)
        # Add edge G
        newTopRightPL[B1].append(C2)
        newBottomRightPL[C2].append(B1)
        # Add edge H
        newBottomRightPL[C1].append(D1)
        newBottomLeftPL[D1].append(C1)

        newCompletePL = {**newBottomLeftPL, **
                         newBottomRightPL, **newTopLeftPL, **newTopRightPL}
        self.SetPathList(newCompletePL)
        return

# Given a path list, develop the tour of the board
    def FindTour(self):
        startingPosition = (1, 1)
        currentPosition = startingPosition
        pathList = self.GetPathList()
        visitedSquares = {startingPosition: True}
        tour = {}

        while True:
            foundNextStep = False

            for square in pathList[currentPosition]:
                if square not in visitedSquares:
                    visitedSquares[square] = True
                    tour[currentPosition] = square
                    currentPosition = square
                    foundNextStep = True
                    break

            # If all next squares have already been visited...
            if not foundNextStep:
                # ... either we're at the last step...
                if tuple(map(lambda i, j: i - j, currentPosition, startingPosition)) in KnightMoves:
                    tour[currentPosition] = startingPosition
                    break
                # ... or the tour is broken.
                else:
                    print("ERROR: position", currentPosition,
                          "can't go anywhere.")
                    break

        if len(visitedSquares) != (self.GetRows() * self.GetColumns()):
            print("Tour ends after", len(visitedSquares),
                  "steps instead of", self.GetRows() * self.GetColumns(), ".")

        self.SetTour(tour)

    # Print tour matrix. Number of each square is the step when the knight visits it
    def PrintTour(self):
        nextStep = self.GetTour()
        startingPosition = (1, 1)
        currentPosition = nextStep[startingPosition]

        tourMatrix = np.zeros((self.GetRows(), self.GetColumns()), int)

        visitedPositions = {startingPosition: 1}
        tourMatrix[self.GetRows()-startingPosition[1],
                   startingPosition[0]-1] = 1
        positionCounter = 1

        while currentPosition != startingPosition:
            positionCounter += 1
            visitedPositions[currentPosition] = positionCounter
            tourMatrix[int(self.GetRows()-currentPosition[1]),
                       int(currentPosition[0]-1)] = positionCounter
            currentPosition = nextStep[currentPosition]

        print(tourMatrix)

    # Is the tour the right length?

    def TourIsComplete(self):
        return len(self.GetTour()) == self.GetColumns() * self.GetRows()

    # Can each move in the tour be performed by a knight?
    def TourIsLegal(self):
        tourNextStep = self.GetTour()
        previousPosition = (1, 1)
        currentPosition = tourNextStep[previousPosition]

        # Skip first position because it's also the last
        isLegal = True

        for i in range(self.GetColumns() * self.GetRows()):
            if tuple(map(lambda i, j: i - j, currentPosition, previousPosition)) not in KnightMoves:
                isLegal = False
                break

            previousPosition = currentPosition
            currentPosition = tourNextStep[currentPosition]

        return isLegal

    def CheckTour(self):
        print("Complete: \t", self.TourIsComplete())
        print("Legal: \t\t", self.TourIsLegal())


n = 8
board = Chessboard(n, n)


print(board.GetRows())
print(board.GetColumns())

print("Building knight path list...")
board.FindPathList()
print("Building knight tour...")
print()
board.FindTour()
board.PrintTour()
