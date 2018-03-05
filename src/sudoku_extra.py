#CELL 1

POPULATION_SIZE = 100
NUMBER_GENERATION = 2000
TRUNCATION_RATE = 0.1
MUTATION_RATE = 0.84
BLOCK_SIZE = 3

board1 = create_board(read_in_file("Grid1.txt"))
results_mutation = []
results_trunc = []

for i in range(10):
    MUTATION_RATE = 1 - i * 0.1
    x = evolve(board1)
    results_mutation.append(x[3])

MUTATION_RATE = 0.84

for i in range(10):
    TRUNCATION_RATE = 1 - i * 0.1
    x = evolve(board1)
    results_trunc.append(x[3])

print(results_mutation)
print(results_trunc)
value = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
plt.plot(value, results_mutation, '-r', value, results_trunc, '-g')
plt.legend(('Mutation', 'Truncation'))
plt.xlabel('Value')
plt.ylabel('Average fitness of last gen')

#CELL 2

POPULATION_SIZE = 100
NUMBER_GENERATION = 2000
TRUNCATION_RATE = 0.1
MUTATION_RATE = 0.84
BLOCK_SIZE = 3

board1 = create_board(read_in_file("Grid1.txt"))
results_mutation = []
results_trunc = []

for i in range(20):
    MUTATION_RATE = 0.75 + i * 0.2
    x = evolve(board1)
    results_mutation.append(x[3])

MUTATION_RATE = 0.84

for i in range(20):
    TRUNCATION_RATE = 0.05 + i * 0.02
    x = evolve(board1)
    results_trunc.append(x[3])

print(results_mutation)
print(results_trunc)

value_mut = [0.75 + i * 0.02 for i in range(20)]
value_trunc = [0.1 + i * 0.02 for i in range(20)]
print(value_mut)
plt.plot(value_mut, results_mutation, '-r')
plt.plot(value_trunc, results_trunc, '-g')
plt.legend(('Mutation', 'Truncation'))
plt.xlabel('Value')
plt.ylabel('Average fitness of last gen')