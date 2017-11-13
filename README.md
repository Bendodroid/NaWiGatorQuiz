# Readme

## Requirements

You have to run this with Python 3.6, as it uses static typing features.

## General

This program is specialized on a specific type of competition, often found in schools.
The competition consist of two parts, a theoretical part and experiments carried out in small groups.
During the theoretical part, reffered to as "quiz", the "teams" collect points.
During the experiments, they collect "marbles" for well-behaving, cleaning up afterwards ...
The team with the highest score in the quiz sets the 100%-mark.
The highest number of "marbles" is equivalent to the points in the quiz and the scores
are calculated relatively to these values.

Example:
```
  Team "A":
    Points in the quiz: 200
    Number of marbles:   25

  Team "B":
    Points in the quiz: 150
    Number of marbles:   50
```
For each team, their number of points from the quiz is added to their final score.
Because 50 marbles are the highest amount collected, 50 marbles are equivalent to 200 points
(Highest score achieved in the quiz). Therefore, team "B" receives 200 points for their "experiment-part",
team "A" gets 100 points (25 is half of 50, so 25 eq. to half of 200 -> 100).
The results would be:
```
  1. Team "B" with 350 points
  2. Team "A" with 300 points
```

## Usage

You launch the program by just launching the Main.py in a Terminal:
```
  ~$ python3 Main.py
```
You then have 3 possible options:
  - Generate the teams
    - This needs to be done first. To reset the teams,
      just select the option in the menu again.
  - Enter the results
    - Here you can enter the results for every team.
    - To overwrite, put in new results
  - Calculate Winner
    - The Results are calculated and the details are printed to the console.
