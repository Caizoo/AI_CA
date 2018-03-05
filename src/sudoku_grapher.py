# code for plotting results in Anaconda Notebook using matplotlib

# CELL 2, DEFINE THE CODE IN SUDOKU_GENETIC FIRST
def print_results(x_b1_10, x_b2_10, x_b3_10, x_b1_100, x_b2_100, x_b3_100, x_b1_1000, x_b2_1000, x_b3_1000, x_b1_10000,
                  x_b2_10000, x_b3_10000):
    print()
    print("Board 1")
    print("Best fitness pop size 10:", x_b1_10[1], "Generations to solve:", x_b1_10[2], "Average fitness in final gen:",
          x_b1_10[3], "time:", x_b1_10[4], "s")
    print("Best fitness pop size 100:", x_b1_100[1], "Generations to solve:", x_b1_100[2],
          "Average fitness in final gen:", x_b1_100[3], "time:", x_b1_100[4], "s")
    print("Best fitness pop size 1000:", x_b1_1000[1], "Generations to solve:", x_b1_1000[2],
          "Average fitness in final gen:", x_b1_1000[3], "time:", x_b1_1000[4], "s")
    print("Best fitness pop size 10000:", x_b1_10000[1], "Generations to solve:", x_b1_10000[2],
          "Average fitness in final gen:", x_b1_10000[3], "time:", x_b1_10000[4], "s")
    print("Board 2")
    print()
    print("Best fitness pop size 10:", x_b2_10[1], "Generations to solve:", x_b2_10[2], "Average fitness in final gen:",
          x_b2_10[3], "time:", x_b2_10[4], "s")
    print("Best fitness pop size 100:", x_b2_100[1], "Generations to solve:", x_b2_100[2],
          "Average fitness in final gen:", x_b2_100[3], "time:", x_b2_100[4], "s")
    print("Best fitness pop size 1000:", x_b2_1000[1], "Generations to solve:", x_b2_1000[2],
          "Average fitness in final gen:", x_b2_1000[3], "time:", x_b2_1000[4], "s")
    print("Best fitness pop size 10000:", x_b2_10000[1], "Generations to solve:", x_b2_10000[2],
          "Average fitness in final gen:", x_b2_10000[3], "time:", x_b2_10000[4], "s")
    print("Board 3")
    print()
    print("Best fitness pop size 10:", x_b3_10[1], "Generations to solve:", x_b3_10[2], "Average fitness in final gen:",
          x_b3_10[3], "time:", x_b3_10[4], "s")
    print("Best fitness pop size 100:", x_b3_100[1], "Generations to solve:", x_b3_100[2],
          "Average fitness in final gen:", x_b3_100[3], "time:", x_b3_100[4], "s")
    print("Best fitness pop size 1000:", x_b3_1000[1], "Generations to solve:", x_b3_1000[2],
          "Average fitness in final gen:", x_b3_1000[3], "time:", x_b3_1000[4], "s")
    print("Best fitness pop size 10000:", x_b3_10000[1], "Generations to solve:", x_b3_10000[2],
          "Average fitness in final gen:", x_b3_10000[3], "time:", x_b3_10000[4], "s")

def list_addition(x1, x2):
    return [sum(x) for x in zip(x1, x2)]

def average_out_list(x1, amount_of_runs):
    return [(x / amount_of_runs) for x in x1]

def draw_graphs(results, num_gen):
    b1_10_results = [0, 0, 0, 0]  # best fitness,gens to solve, average fitness, time to find
    b2_10_results = [0, 0, 0, 0]
    b3_10_results = [0, 0, 0, 0]

    b1_100_results = [0, 0, 0, 0]
    b2_100_results = [0, 0, 0, 0]
    b3_100_results = [0, 0, 0, 0]

    b1_1000_results = [0, 0, 0, 0]
    b2_1000_results = [0, 0, 0, 0]
    b3_1000_results = [0, 0, 0, 0]

    b1_10000_results = [0, 0, 0, 0]
    b2_10000_results = [0, 0, 0, 0]
    b3_10000_results = [0, 0, 0, 0]

    for run in results:  # x_b1_10 = run[0]#x_b2_10 = run[1]
        # x_b3_10 = run[2]#x_b1_100 = run[3]#x_b2_100 = run[4]#x_b3_100 = run[5]#x_b1_1000 = run[6]
        # x_b2_1000 = run[7]#x_b3_1000 = run[8]#x_b1_10000 = run[9]#x_b2_10000 = run[10]#x_b3_10000 = run[11]
        b1_10_results = list_addition(b1_10_results, list(run[0][1:]))
        b2_10_results = list_addition(b2_10_results, list(run[1][1:])) # [1:] to ignore the best guess matrix
        b3_10_results = list_addition(b3_10_results, list(run[2][1:]))

        b1_100_results = list_addition(b1_100_results, list(run[3][1:]))
        b2_100_results = list_addition(b2_100_results, list(run[4][1:]))
        b3_100_results = list_addition(b3_100_results, list(run[5][1:]))

        b1_1000_results = list_addition(b1_1000_results, list(run[6][1:]))
        b2_1000_results = list_addition(b2_1000_results, list(run[7][1:]))
        b3_1000_results = list_addition(b3_1000_results, list(run[8][1:]))

        b1_10000_results = list_addition(b1_10000_results, list(run[9][1:]))
        b2_10000_results = list_addition(b2_10000_results, list(run[10][1:]))
        b3_10000_results = list_addition(b3_10000_results, list(run[11][1:]))

    b1_10_results = average_out_list(b1_10_results, len(results))
    b2_10_results = average_out_list(b2_10_results, len(results))
    b3_10_results = average_out_list(b3_10_results, len(results))

    b1_100_results = average_out_list(b1_100_results, len(results))
    b2_100_results = average_out_list(b2_100_results, len(results))
    b3_100_results = average_out_list(b3_100_results, len(results))

    b1_1000_results = average_out_list(b1_1000_results, len(results))
    b2_1000_results = average_out_list(b2_1000_results, len(results))
    b3_1000_results = average_out_list(b3_1000_results, len(results))

    b1_10000_results = average_out_list(b1_10000_results, len(results))
    b2_10000_results = average_out_list(b2_10000_results, len(results))
    b3_10000_results = average_out_list(b3_10000_results, len(results))

    x = [1, 2, 3, 4]
    # TIME GRAPH
    time_y_b1 = [b1_10_results[3], b1_100_results[3], b1_1000_results[3], b1_10000_results[3]]
    time_y_b2 = [b2_10_results[3], b2_100_results[3], b2_1000_results[3], b2_10000_results[3]]
    time_y_b3 = [b3_10_results[3], b3_100_results[3], b3_1000_results[3], b3_10000_results[3]]
    plt.figure(figsize=(15, 15))
    plt.plot(x, time_y_b1, 'r', x, time_y_b2, 'g', x, time_y_b3, 'b')
    plt.title('Time with number of generation: ' + str(num_gen))
    plt.legend(('Grid1', 'Grid2', 'Grid3'))
    plt.xlabel('log10 Population')
    plt.ylabel('Time /s')
    plt.show()

    # BEST_SOLUTION_GRAPH
    best_y_b1 = [b1_10_results[0], b1_100_results[0], b1_1000_results[0], b1_10000_results[0]]
    best_y_b2 = [b2_10_results[0], b2_100_results[0], b2_1000_results[0], b2_10000_results[0]]
    best_y_b3 = [b3_10_results[0], b3_100_results[0], b3_1000_results[0], b3_10000_results[0]]
    plt.figure(figsize=(15, 15))
    plt.plot(x, best_y_b1, 'r', x, best_y_b2, 'g', x, best_y_b3, 'b')
    plt.title('Best solution fitness with number of generation: ' + str(num_gen))
    plt.legend(('Grid1', 'Grid2', 'Grid3'))
    plt.xlabel('log10 Population')
    plt.ylabel('Best solution fitness')
    plt.show()

    # GENERATIONS_TO_SOLVE
    gen_y_b1 = [b1_10_results[1], b1_100_results[1], b1_1000_results[1], b1_10000_results[1]]
    gen_y_b2 = [b2_10_results[1], b2_100_results[1], b2_1000_results[1], b2_10000_results[1]]
    gen_y_b3 = [b3_10_results[1], b3_100_results[1], b3_1000_results[1], b3_10000_results[1]]
    plt.figure(figsize=(15, 15))
    plt.plot(x, gen_y_b1, 'r', x, gen_y_b2, 'g', x, gen_y_b3, 'b')
    plt.title('Generations to solve with number of generation: ' + str(num_gen))
    plt.legend(('Grid1', 'Grid2', 'Grid3'))
    plt.xlabel('log10 Population')
    plt.ylabel('Generations to solve')
    plt.show()

    # AVERAGE FITNESS LAST GEN
    av_y_b1 = [b1_10_results[2], b1_100_results[2], b1_1000_results[2], b1_10000_results[2]]
    av_y_b2 = [b2_10_results[2], b2_100_results[2], b2_1000_results[2], b2_10000_results[2]]
    av_y_b3 = [b3_10_results[2], b3_100_results[2], b3_1000_results[2], b3_10000_results[2]]
    plt.figure(figsize=(15, 15))
    plt.plot(x, av_y_b1, 'r', x, av_y_b2, 'g', x, av_y_b3, 'b')
    plt.title('Average fitness of last generation with number of generation: ' + str(num_gen))
    plt.legend(('Grid1', 'Grid2', 'Grid3'))
    plt.xlabel('log10 Population')
    plt.ylabel('Average fitness')
    plt.show()

# CELL 3, RUNS THE EXPERIMENTS AND DRAWS THE GRAPHS

POPULATION_SIZE = 10
NUMBER_GENERATION = 200
TRUNCATION_RATE = 0.1
MUTATION_RATE = 0.84
BLOCK_SIZE = 3

# create given boards
board1 = create_board(read_in_file("Grid1.txt"))
board2 = create_board(read_in_file("Grid2.txt"))
board3 = create_board(read_in_file("Grid3.txt"))

results = []
run_results = []

for i in range(5):  # 5 runs
    print()
    print("Run #", i + 1)
    POPULATION_SIZE = 10
    x_b1_10 = evolve(board1)
    x_b2_10 = evolve(board2)
    x_b3_10 = evolve(board3)
    POPULATION_SIZE = 100
    x_b1_100 = evolve(board1)
    x_b2_100 = evolve(board2)
    x_b3_100 = evolve(board3)
    POPULATION_SIZE = 1000
    x_b1_1000 = evolve(board1)
    x_b2_1000 = evolve(board2)
    x_b3_1000 = evolve(board3)
    POPULATION_SIZE = 10000
    x_b1_10000 = evolve(board1)
    x_b2_10000 = evolve(board2)
    x_b3_10000 = evolve(board3)

    run_results += [(x_b1_10, x_b2_10, x_b3_10, x_b1_100, x_b2_100, x_b3_100, x_b1_1000, x_b2_1000, x_b3_1000,
                     x_b1_10000, x_b2_10000, x_b3_10000)]
    print_results(x_b1_10, x_b2_10, x_b3_10, x_b1_100, x_b2_100, x_b3_100, x_b1_1000, x_b2_1000, x_b3_1000, x_b1_10000,
                  x_b2_10000, x_b3_10000)

draw_graphs(run_results, 10)