# def checkingWord(x, y, dx, dy):
#         word = "XMAS"
#         for k in range(len(word)):
#             nx, ny = x + k * dx, y + k * dy
#             if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[k]:
#                 return False
#         return True

# def countingWordOccurrences(grid):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
#     count = 0
#     for i in range(rows):
#         for j in range(cols):
#             for dx, dy in directions:
#                 if checkingWord(i, j, dx, dy):
#                     count += 1
#     return count

filePointer = open("day4_SampleInput.txt", "r")
grid = filePointer.readlines()
rows, cols = len(grid), len(grid[0])
# occurrences = countingWordOccurrences(grid)
# print(f"Number of occurrences of 'XMAS':", occurrences)

# Part 2
count = 0
for j in range(cols-2):
     for i in range(rows-2):
          if grid[i+1][j+1] == "A":
                if (grid[i][j] == "M" and grid[i][j+2] == "M") and (grid[i+2][j+2] == "S" and grid[i+2][j] == "S"):
                    count += 1
                elif (grid[i+2][j] == "M" and grid[i+2][j+2] == "M") and (grid[i][j] == "S" and grid[i][j+2] == "S"):
                    count += 1
                elif (grid[i][j] == "M" and grid[i+2][j] == "M") and (grid[i][j+2] == "S" and grid[i+2][j+2] == "S"):
                    count += 1
                elif (grid[i][j] == "S" and grid[i+2][j] == "S") and (grid[i][j+2] == "M" and grid[i+2][j+2] == "M"):
                    count += 1
print(count)