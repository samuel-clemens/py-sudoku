

example_grid = [
         [5,0,0,0,0,7,0,0,0]
        ,[9,2,6,5,0,0,0,0,0]
        ,[3,0,0,8,0,9,0,2,0]
        ,[4,0,0,0,2,0,0,3,5]
        ,[0,3,5,1,0,4,9,7,0]
        ,[8,6,0,0,5,0,0,0,4]
        ,[0,4,0,3,0,8,0,0,2]
        ,[0,0,0,0,0,5,6,9,3]
        ,[0,0,0,6,0,0,0,0,7]]

def print_grid(grid):
    for row in grid:
        print(row)

def get_indices_of_empty_cells(grid):
    return [(i,j) for i in range(0,9) for j in range(0,9) if grid[i][j] == 0]

def get_rows_with_empty_cells(grid):
    indices = get_indices_of_empty_cells(grid)

    return [[grid[indices[i][0]][j] for j in range(0,9)] for i in range(0, len(indices))]

def get_columns_with_empty_cells(grid):
    indices = get_indices_of_empty_cells(grid)

    return [[grid[i][indices[j][1]] for i in range(0,9)] for j in range(0, len(indices))]

def get_indices_of_boxes():
    return [[(i + x, j + y) for i in range(3) for j in range(3)] for x in [0,3,6] for y in [0,3,6]]

def get_boxes_with_empty_cells(grid):
    indices_of_boxes = get_indices_of_boxes()
    indices_of_empty_cells = get_indices_of_empty_cells(grid)
    
    indices_of_boxes_for_each_empty_cells = [indices_of_boxes[i] 
        for x in indices_of_empty_cells 
        for i in range(len(indices_of_boxes)) 
        for y in indices_of_boxes[i] if x == y]

    return [[grid[i][j] for (i,j) in x] for x in indices_of_boxes_for_each_empty_cells]

def get_clues_of_groups(grid):
    rows = get_rows_with_empty_cells(grid)
    columns = get_columns_with_empty_cells(grid)
    boxes = get_boxes_with_empty_cells(grid)

    return [[[x[i] for i in range(len(x)) if x[i] != 0] for x in [row, column, box]] for (row, column, box) in zip(rows, columns, boxes)]

def generate_pencil_marks(grid):
    clues = get_clues_of_groups(grid)
    all_clues = [set([y for i in range(len(x)) for y in x[i]]) for x in clues]

    pencil_marks = [set(set({1, 2, 3, 4, 5, 6, 7, 8, 9}) - set(x)) for x in all_clues]

    return pencil_marks

def get_indices_and_candidates(grid):
    indices = get_indices_of_empty_cells(grid)
    pencil_marks = generate_pencil_marks(grid)

    return [(tuple_of_indices, candidate) for tuple_of_indices, candidate in zip(indices, pencil_marks)]

def insert_pencil_marks(grid):
    indices_and_candidates = get_indices_and_candidates(grid)

    for i in range(len(indices_and_candidates)):
        grid[indices_and_candidates[i][0][0]][indices_and_candidates[i][0][1]] = indices_and_candidates[i][1]
    return grid

print(insert_pencil_marks(example_grid))