# plushi-annealing

This project serves as an example of how to use the Plushi interpreter and
a simple simmulated annealing algorithm for inductive program synthesis.

## Usage

This project only works with python3. The use of a virtual environment is highly
recomended. Be sure to install all packages in the the requirements file with

```
pip install -r requirements.pip
```

To start the simmulated annealing algorithm on one of the included benchmark problems simply pass the name of problem as the first argument to the `plushi_annealing.py` module.

```
python plushi_annealing.py relu
```

> Warning: If you keyboard interupt or kill the python process in the middle of the run. The Pluhi java process will still be running, and will prevent you from starting another run on the same port until you kill the Plushi java process.

## Problems

The following benchmark problems are currently supported.

- `relu`

## Plushi

Plushi is an embeddable, language agnostic Push language interpreter. This repo come with a standalone `.jar` file of a stable plushi release. You can read more about the project on its GitHub page.

https://github.com/erp12/plushi
