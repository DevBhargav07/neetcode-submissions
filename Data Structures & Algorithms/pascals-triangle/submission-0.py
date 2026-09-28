class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        new_row = [[1]]
        for row in range(numRows - 1):
            temp = [0] + new_row[-1] + [0]
            row = []
            for crnt in range(len(new_row[-1])+1):
                row.append(temp[crnt]+temp[crnt+1])
            new_row.append(row)
        return new_row
