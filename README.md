# Lab: Class 6,7,8,9 - Ten Thousand

## Author: Xin Deng, Andrea Thiel chatGPT

### Links and Resources

- chatGPT

### Set up

Type into your terminal:

```bash
mkdir ten-thousand
cd example-lab
touch README.md
python3 -m venv .venv
source .venv/bin/activate
git init
touch .gitignore
mkdir ten_thousand
touch ten_thousand/game_logic.py


```
Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```
Create remote repo and follow instructions


```bash
pip freeze > requirements.txt
pip install pytest-watch
touch tests/__init__.py 
mkdir tests/version_1

touch tests/version_1/__init__.py
touch tests/version_1/test_calculate_score.py
touch tests/version_1/test_roll_dice.py

pytest-watch

```

### Overview - Ten Thousand

The Ten Thousand Game is a command-line version of the popular dice game "Ten Thousand." This Python-based implementation expands your understanding of the Python standard library while providing a unique experience by incorporating code generated with the assistance of an AI.

#### Version 1.0

Build 1.0 Feature Tasks 

1) Handle calculating score for dice roll
2) Handle rolling dice
3) Use ChatGPT to help write code blocks and document your prompts and the responses.



### To run 10,000:


```bash
python ten_thousand/game_logic.py
```

## To test

```bash
pytest-watch
```

#### Version 2.0

Build 2.0 Feature Tasks 

1) Application should implement all features from previous version
2) Application should allow user to set aside dice each roll
3) Application should allow “banking” current score or rolling again.
4) Application should keep track of total score
5) Application should keep track of current round



### To run 10,000:


```bash
python -m ten_thousand.game
```

## To test

```bash
pytest -s tests/version_2/test_sim_basic.py
```


