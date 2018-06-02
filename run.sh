#!/bin/sh

echo "Generating Data"
python lorenz63.py

echo "Generating forecasts"
python forecasts/persistence.py perstistence.mat
python forecasts/cheating.py cheating.mat

echo "Score of persistence forecast"
python score.py secret.mat perstistence.mat

echo "Score of cheating forecast (should be 5000)"
python score.py secret.mat cheating.mat
