import random
import math
import time
import sys

import numpy as np
import utils as u


INITIAL_TEMPERATURE = 1
PLUSHI_LENGTH = 100
MUTATION_STENGTH = 0.02
NUM_ITERATIONS = 1e4


def generate_random_seq(length):
    return [random.choice(INSTRUCTION_SET)["name"] for x in range(length)]


def evaluate(seq, X, y):
    request_body = {
        'action': 'run',
        'code': seq,
        'arity': 1,
        'output-types': ['float'],
        'dataset': X
    }
    y_hat = np.array(u.plushi_request(request_body)).flatten()
    if 'float' not in str(y_hat.dtype):
        return (1e6, y_hat)
    else:
        rmse = np.sqrt(((y_hat - np.array(y)) ** 2).mean())
        return (rmse, y_hat)


def mutate(seq):
    new_program = []
    for token in seq:
        if random.random() < MUTATION_STENGTH:
            new_program.append(random.choice(INSTRUCTION_SET)["name"])
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

    current_plushi = generate_random_seq(PLUSHI_LENGTH)
    current_error, current_predictions = evaluate(current_plushi, X, y)

    while temperature > 0:
        print("Step:", step_count, "Temperature:", temperature, "Error:", current_error)

        new_plushi = mutate(current_plushi)
        new_error, new_predictions = evaluate(new_plushi, X, y)

        acceptance_prop = acceptance_function(current_error, new_error, temperature)
        if random.random() < acceptance_prop:
            current_plushi = new_plushi
            current_predictions = new_predictions
            current_error = new_error

        temperature = get_temp(step_count, max_steps)
        step_count += 1

    return current_plushi, current_predictions


def main(problem_name):

    X, y = u.load_problem_data(problem_name)
    start_time = time.time()
    solution, behavior = anneal(X, y, NUM_ITERATIONS)
    end_time = time.time()
    print(solution)
    print(behavior)
    print("Elapsed time was {t} seconds".format(t=end_time - start_time))


if __name__ == "__main__":
    p = u.start_plushi()
    INSTRUCTION_SET = u.plushi_instruction_set(1)
    main(sys.argv[1])
    p.terminate()
