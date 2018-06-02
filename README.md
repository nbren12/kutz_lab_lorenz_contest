This project contains routines to score the predictions made by each team in
the contest. `score.py` is the most important file.

# Quickstart

```
git clone https://github.com/nbren12/kutz_lab_lorenz_contest 
cd kutz_lab_lorenz_contest
./run.sh
```

This will clone this repository and run a script that

1. generates the lorenz data. The known burn-in-time data is stored in
   `known.mat`, and the subsequent secret time points to be predicted are in `secret.mat`.
   Each of these files contains a variable `x`, with a shape `(num_trajectories, num_time, 3)`.
2. performs a couple of trivial predictions
3. uses `score.py` to evaluate these predictions against `secret.mat`

# Directory structure

```
├── forecasts
│   ├── cheating.py
│   └── persistence.py
├── lorenz63.py          # generates the input data
├── run.sh               # quick start script
├── score.py             # scoring script
```



