import random
from math import *

INF = 999

#ham muc tieu func(x) de danh gia cac ca the, cang gan 0 cang tot
def func(x, equation):
    # print(equation)
    try:
        # Evaluate the equation using the input value of x
        result = eval(equation)

        return abs(result)  # Return the absolute value of the result
    except:
        # Handle any exceptions that occur during evaluation
        return INF  # Return a high value to penalize invalid equations or inputs

#chuyen doi tu nhi phan sang thap phan
def ieee_to_decimal(ieee_binary):
    long_value = int(ieee_binary, 2)

    sign = (long_value >> 31) & 1
    exponent = (long_value >> 23) & 0xFF
    fraction = long_value & 0x7FFFFF

    bias = 127

    actual_exponent = exponent - bias

    fraction_value = 1.0
    for i in range(22, -1, -1):
        fraction_value += ((fraction >> i) & 1) * (2 ** (i - 23))

    if exponent == 0 and fraction == 0:
        result = 0.0
    elif exponent == 255 and fraction == 0:
        result = float('inf') if sign == 0 else float('-inf')
    elif exponent == 255 and fraction != 0:
        result = float('nan')
    else:
        result = ((-1) ** sign) * fraction_value * (2 ** actual_exponent)

    return result

#Khoi tao quan the, moi ca the co do dai 32bit ngau nhien
def init_population(population_size):
    population = []
    for _ in range(population_size):
        individual = ''.join(random.choice('01') for _ in range(32))
        population.append(individual)
    return population

#sinh san : bao gom lai(crossover) và đột biến (mutate)
# Lai: Hai cá thể được chọn ngẫu nhiên sẽ được lai tạo để tạo ra một cá thể mới.
#quá trình lai được thực hiện bởi cách chọn ngẫu nhiên một điểm cắt trong bộ gen để tạo ra con từ hai cá thể cha mẹ
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

#Đột biến: Một cá thể được chọn ngẫu nhiên sẽ bị đột biến để tạo ra một cá thể mới.
# Hàm “mutate” ngẫu nhiên đảo ngược các bit trong chuỗi nhị phân của cá
# thể với một xác suất là “mutationRate”.

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        mutation_chance = random.random()
        if mutation_chance < mutation_rate:
            bit = '1' if individual[i] == '0' else '0'
            individual = individual[:i] + bit + individual[i + 1:]
    return individual


def solve(equation):
    max_generation = 10
    population_size = 10000
    population = init_population(population_size)
    best_fitness = INF
    solution = 0
    generation = 0

    best_fitness_list = []  # List to store best fitness values
    solution_list = []  # List to store corresponding solutions

    while generation < max_generation:
        mutation_rate = 0.05 * (max_generation - generation) / max_generation

        func_val = []

        for individual in population:
            fitness = func(ieee_to_decimal(individual), equation)
            # if fitness == INF:
            #     return [INF], [INF]
            func_val.append((individual, fitness))

        func_val.sort(key=lambda x: x[1])
        # thêm các giá trị tốt nhất tại mỗi thế hệ
        best_individual, best_fitness = func_val[0]

        # Convert the best individual from binary to decimal
        best_solution = ieee_to_decimal(best_individual)

        # Add to the lists
        best_fitness_list.append(best_fitness)
        solution_list.append(best_solution)

        new_population_size = population_size // 4
        new_population = [x[0] for x in func_val[:new_population_size]]

        for _ in range(new_population_size, population_size):
            parent1 = random.choice(new_population)
            parent2 = random.choice(new_population)

            child = crossover(parent1, parent2)
            new_population.append(child)

        new_population = [mutate(individual, mutation_rate) for individual in new_population]

        population = new_population

        generation += 1

    for individual in population:
        current_fitness = func(ieee_to_decimal(individual), equation)
        if current_fitness < best_fitness:
            best_fitness = current_fitness
            solution = ieee_to_decimal(individual)
            best_fitness_list.append(best_fitness)
            solution_list.append(solution)

    # print("Best Fitness:", best_fitness)
    # print("Solution:", solution)
    return best_fitness_list, solution_list
# if __name__ == "__main__":
#     main()
