from random import *

def evolve():
    board = create_board(read_in_file("Grid2.txt"))
    population = create_pop(board)
    fitness_population = evaluate_pop(population,board)
    for gen in range(NUMBER_GENERATION):
        mating_pool = select_pop(population,fitness_population)
        offspring_population = crossover_pop(mating_pool)
        population = mutate_pop(offspring_population)
        fitness_population = evaluate_pop(population,board)
        best_ind,best_fit = best_pop(population,fitness_population)
        if(best_fit==0): break
    print_board(best_ind)
    print(best_fit)
# population-level operators

def best_pop(population, fitness_population):
    return sorted(zip(population, fitness_population), key = lambda ind_fit: ind_fit[1])[0]

def create_pop(board):
    return [create_ind(board) for _ in range(POPULATION_SIZE)]

def select_pop(population, fitness_pop):
    return [tournement([choice(list(zip(population,fitness_pop))) for _ in range(TOURNEMENT_SIZE)]) for _ in range(0,(len(population)*2))]

def crossover_pop(population):
    return [crossover_ind(population[i],population[i+1]) for i in range(0,len(population),2)]

def mutate_pop(population):
    return [mutation_ind(individual) for individual in population]

def evaluate_pop(population,board):
    return [fitness_ind(matrix_addition(individual,board)) for individual in population]

# individual-level operators

def tournement(contenders):
    index_best = 0
    for i in range(1,len(contenders)):
        if(contenders[index_best][1]>contenders[i][1]):
            index_best = i
    return contenders[index_best][0]

def crossover_ind(parent1,parent2):
    choices = [0,1]
    row_choices = []
    for _ in range(9):
        row_choices.append(choice(choices))
    crossover_rows(parent1,parent2,row_choices)
    return parent1

def crossover_rows(p1,p2,row_choices):
    child = []
    print(p1)
    print(p2)
    print()
    print()
    for i in range(9): # for each block
        child_block = []
        for j in range(3):
            if row_choices[j+int(i/3)]==0:
                child_block.append(p1[i][j])
            else:
                child_block.append(p2[i][j])
        child.append(child_block)
    return child


def mutation_ind(individual): # need to check mutating once per individual, or once per block depending on MUTATION_RATE
    if(random()>MUTATION_RATE): return individual
    randBlock = randint(0,8)
    individual[randBlock] = mutate_block(individual[randBlock])
    return individual

def mutate_block(block):
    indexes_to_choose = []
    for i in range(len(block)):
        for j in range(len(block[0])):
            if(block[i][j]!=0):
                indexes_to_choose.append((i,j))

    ind1 = choice(indexes_to_choose)
    indexes_to_choose.remove(ind1)
    ind2 = choice(indexes_to_choose)
    num1 = block[ind1[0]][ind1[1]]
    num2 = block[ind2[0]][ind2[1]]
    block[ind1[0]][ind1[1]] = num2
    block[ind2[0]][ind2[1]] = num1

    return block

def create_ind(board):
    rand_board = []
    for block in board:
        rand_block = randomize_block(block)
        rand_board.append(rand_block)
    return rand_board

def randomize_block(block):
    block_nums = []
    new_block = []
    for i in range(3):
        new_block.append([0,0,0])
    for row in block:
        for cell in row:
            block_nums.append(cell)
    choiceList = list(set([1,2,3,4,5,6,7,8,9])-set(block_nums))
    for row in range(3):
        for cell in range(3):
            if(block[row][cell]==0):
                new_cell = choice(choiceList)
                choiceList.remove(new_cell)
                new_block[row][cell] = new_cell
            else:
                new_block[row][cell] = 0
    return list(new_block)

def fitness_ind(board):
    blocks = []
    rows = []
    cols = []
    for i in range(9):
        blocks.append([])
        rows.append([])
        cols.append([])

    for block_count in range(9):
        for row_count in range(3):
            for cell_count in range(3):
                cell = board[block_count][row_count][cell_count]
                blocks[block_count] = blocks[block_count]+[cell]
                rows[row_count+3*int(block_count/3)] = rows[row_count+3*int(block_count/3)]+[cell]
                cols[(block_count%3)*3+cell_count] = cols[(block_count%3)*3+cell_count]+[cell]
    return fitness_part(blocks,1)+fitness_part(rows,1) + fitness_part(cols,1)

def fitness_part(part,incrementValue):
    part_fitness = 0
    for ind in part:
        row = list(ind)
        row.sort()
        for i in range(len(row)-1):
            if(row[i]==row[i+1]):
                part_fitness += incrementValue
    return part_fitness

# matrix operations

def matrix_addition(m1,m2):
    return [block_addition(b) for b in zip(m1,m2)]

def block_addition(block):
    return [row_addition(row) for row in zip(block[0],block[1])]

def row_addition(row):
    return [sum(x) for x in zip(row[0],row[1])]

# io operations

def read_in_file(filename):
    try:
        file = open(filename, 'r')
        strIn = file.readlines()
    except:
        strIn = ""
    finally:
        for i in range(0,len(strIn)-1):
            strIn[i] = strIn[i][:len(strIn[i])-1]
        file.close

    return strIn # list of strings, each element is a line from the file

def create_board(file_contents):
    board = []
    for i in range(0,len(file_contents)-1,BLOCK_SIZE+1): # +1 to skip ---!---!--- line
        row_blocks = list(zip(file_contents[i],file_contents[i+1],file_contents[i+2])) # zip first 3 lines together
        for j in range(0,len(row_blocks)-1,4):
            block = create_block(list(zip(row_blocks[j],row_blocks[j+1],row_blocks[j+2])))
            board.append(block)
    return board

def create_block(block):
    intBlock = []
    for i in range(3):
        intRow = []
        for j in range(3):
            if (block[i][j]=='.'): intRow.append(0)
            else: intRow.append(int(block[i][j]))
        intBlock.append(intRow)
    return intBlock

def print_board(board):
    for i in range(0,len(board)-1,3):
        print_row(list(zip(board[i],board[i+1],board[i+2])))

def print_row(row):
    for line in row:
        for i in range(3):
            print(line[i],end=' ')
        print()
    print()

POPULATION_SIZE = 10
NUMBER_GENERATION = 100
TOURNEMENT_SIZE = int(POPULATION_SIZE/2) # reducing tournament size increases the number of 'poor' parent choices
MUTATION_RATE = 0.5
BLOCK_SIZE = 3

evolve()
b = create_board(read_in_file("GridComp.txt"))
print_board(b)
print(fitness_ind(b))