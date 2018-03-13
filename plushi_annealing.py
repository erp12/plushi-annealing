import random
import math

import data_manager


INITIAL_TEMPERATURE = 1
PLUSHI_LENGTH = 100


def generate_random_plushi(length):
    return [random.random() for x in range(length)]


def evaluate(plushi_program, X, y):
    return abs(sum(plushi_program) - 20)


def mutate(plushi_program, temperature):
    new_program = []
    for token in plushi_program:
        if random.random() <= temperature:
            new_program.append(random.random())
        else:
            new_program.append(token)
    return new_program


def get_temp(current_step, max_steps):
    return INITIAL_TEMPERATURE - (current_step / max_steps)


def acceptance_function(current_error, next_error, temperature):
    if next_error < current_error:
        return 1
    else:
        return math.exp(-(next_error - current_error) / temperature)


def anneal(X, y, max_steps):

    step_count = 0
    temperature = get_temp(step_count, max_steps)

    current_plushi = generate_random_plushi(PLUSHI_LENGTH)
    current_error = evaluate(current_plushi, X, y)

    while temperature > 0:
        print("Step:", step_count, "Temperature:", temperature, "Error:", current_error)

        new_plushi = mutate(current_plushi, temperature)
        new_error = evaluate(new_plushi, X, y)

        acceptance_prop = acceptance_function(current_error, new_error, temperature)
        if random.random() < acceptance_prop:
            current_plushi = new_plushi
            current_error = new_error

        temperature = get_temp(step_count, max_steps)
        step_count += 1

    return current_plushi


def main(problem_name):

    X, y = data_manager.load_problem_data(problem_name)
    solution = anneal(X, y, 100000)
    print(solution)
    print(sum(solution))


if __name__ == "__main__":
    main("relu")
