import json


def load_problem_data(problem_name):
    with open("data/" + problem_name + ".json", "r") as json_file:
        problem_dataset = json.load(json_file)
    inputs = []
    outputs = []
    for case in problem_dataset:
        for k, v in case.items():
            if k == "y":
                outputs.append(v)
            else:
                inputs.append(v)
    return (inputs, outputs)
