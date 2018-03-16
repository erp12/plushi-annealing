import json
import requests
import time
from subprocess import Popen


def load_problem_data(problem_name):
    with open("data/" + problem_name + ".json", "r") as json_file:
        problem_dataset = json.load(json_file)
    inputs = []
    outputs = []
    for case in problem_dataset:
        case_dict = {}
        for k, v in case.items():
            if k == "y":
                outputs.append(v)
            else:
                case_dict[k] = v
        inputs.append(case_dict)
    return (inputs, outputs)


def plushi_request(request_body):
    r = requests.post("http://localhost:8075/", json=json.dumps(request_body))
    return r.json()


def plushi_instruction_set(arity):
    return plushi_request({
        'action': 'instructions',
        'arity': arity
    })


def start_plushi():
    p = Popen(['java', '-jar', 'plushi-standalone.jar', '-s'])
    for attempt in range(5):
        try:
            plushi_request({"action": "types"})
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    return p
