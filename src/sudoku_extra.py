POPULATION_SIZE = 100
NUMBER_GENERATION = 2000
TRUNCATION_RATE = 0.1
MUTATION_RATE = 0.16
BLOCK_SIZE = 3

board1 = create_board(read_in_file("Grid1.txt"))
results_mutation = []
results_trunc = []

for i in range(20):
    for j in range(50):
        print("Run",j)
        total_gens_to_solve = 0
        MUTATION_RATE = 0.05+i*0.02
        x = evolve(board1)
        total_gens_to_solve += x[2]
    results_mutation.append((total_gens_to_solve/50))
    print("Mutation:",MUTATION_RATE)
    
MUTATION_RATE = 0.16

for i in range(20):
    for j in range(50):
        print("Run",j)
        total_gens_to_solve = 0
        TRUNCATION_RATE = 0.05+i*0.02
        x = evolve(board1)
        total_gens_to_solve += x[2]
    results_trunc.append((total_gens_to_solve/50))
    print("Truncation:",TRUNCATION_RATE)
    
print(results_mutation)
print(results_trunc)

value_mut = [0.05+i*0.02 for i in range(20)]
value_trunc = [0.05+i*0.02 for i in range(20)]
print(value_mut)
plt.plot(value_mut,results_mutation,'-r')
plt.plot(value_trunc,results_trunc,'-g')
plt.legend(('Mutation','Truncation'))
plt.xlabel('Value')
plt.ylabel('Generations to solve')