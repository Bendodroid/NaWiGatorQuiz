#!/usr/bin/env python3.6

# Copyright Bendodroid [2017]

import typing
import tc


class Team:
    name = ""
    team_id = 0
    points_quiz = 0
    num_marbles = 0
    points_marbles = 0
    points_combined = 0

    def __init__(self, num=0):
        self.name = input(tc.align_string(string="Put in a name for the {}. Team: ".format(num), position=2))
        self.team_id = num


class QuizHandler:
    teams: typing.List[Team] = []
    points_list: typing.List[int] = []
    ranklist: typing.List[typing.Tuple[str, int]] = []
    detail_list: typing.List[typing.Tuple[str, int, int]] = []
    num_of_teams = 0
    max_points_quiz = 0
    max_num_marbles = 0
    quiz_win_team_id = 0
    quiz_win_team_name = ""
    marb_win_team_id = 0
    marb_win_team_name = ""

    @staticmethod
    def reset_teams():
        QuizHandler.teams = []

    @staticmethod
    def set_max_points_quiz():
        for team in QuizHandler.teams:
            if team.points_quiz > QuizHandler.max_points_quiz:
                QuizHandler.max_points_quiz = team.points_quiz
                QuizHandler.quiz_win_team_id = team.team_id
                QuizHandler.quiz_win_team_name = team.name

    @staticmethod
    def set_max_num_marbles():
        for team in QuizHandler.teams:
            if team.num_marbles > QuizHandler.max_num_marbles:
                QuizHandler.max_num_marbles = team.num_marbles
                QuizHandler.marb_win_team_id = team.team_id
                QuizHandler.marb_win_team_name = team.name


def print_commands():
    comm_list = ["1: Generate Teams", "2: Enter Results", "3: Calculate Winner"]
    # Determine longest key
    longestkey = 0
    for key in comm_list:
        if len(key) > longestkey:
            longestkey = len(key)
    # Create printlist
    printlist = []
    # Format Commands
    for i in range(0, len(comm_list)):
        spacestoinsert = (longestkey - len(comm_list[i])) * " "
        printlist.append(comm_list[i] + spacestoinsert)
    # Print Commands
    for i in printlist:
        print(tc.align_string(string=i, position=2))
    print("\n")


def main():
    QuizHandler.reset_teams()
    teams_generated = False
    while True:
        tc.create_header(text="NaWiGator - QuizHandler", clearterm=True)
        print_commands()
        command=input(tc.align_string(string="What do you want to do?: ", position=2))
        print()
        if command != "":
            if command[0] == "1":
                if teams_generated:
                    QuizHandler.reset_teams()
                    print(tc.align_string(string="You have to enter the results again! Teams have been reset!", position=1.5))
                    print()
                QuizHandler.num_of_teams = int(input(tc.align_string(string="Enter the number of teams: ", position=2)))
                print()
                for i in range(1, QuizHandler.num_of_teams + 1):
                    QuizHandler.teams.append(Team(i))
                print("\n" + tc.align_string(string="Teams generated, press ENTER to continue...", position=2))
                teams_generated = True
            elif command[0] == "2":
                for team in QuizHandler.teams:
                    team.points_quiz = int(input(
                        tc.align_string(string="Enter points from the quiz for team '{}': ".format(team.name),
                                        position=2)))
                    team.num_marbles = int(input(
                        tc.align_string(string="Enter number of marbles for team '{}': ".format(team.name),
                                        position=2)))
                    print()
            elif command[0] == "3":
                print()
                QuizHandler.set_max_points_quiz()
                QuizHandler.set_max_num_marbles()
                print(tc.align_string(string="The highest score achieved in the quiz: {:>4} by team ".format(QuizHandler.max_points_quiz) + QuizHandler.quiz_win_team_name, position=1.75))
                print(tc.align_string(string="The highest number of marbles collected: {:>4} by team ".format(QuizHandler.max_num_marbles) + QuizHandler.marb_win_team_name, position=1.75))
                # Calculating points
                for team in QuizHandler.teams:
                    team.points_marbles = int(round(number=(team.num_marbles / QuizHandler.max_num_marbles) * QuizHandler.max_points_quiz, ndigits=0))
                for team in QuizHandler.teams:
                    team.points_combined = team.points_quiz + team.points_marbles
                    QuizHandler.points_list.append(team.points_combined)
                # Sort point_list
                QuizHandler.points_list.sort()
                QuizHandler.points_list.reverse()
                # Create ranklist with name and score
                for points in QuizHandler.points_list:
                    for team in QuizHandler.teams:
                        if team.points_combined == points:
                            QuizHandler.ranklist.append([team.name, team.points_combined])
                # Print Scores
                print("\n")
                for i in range(1, len(QuizHandler.ranklist) + 1):
                    print(tc.align_string(string=str(i) + " : " + QuizHandler.ranklist[i - 1][0] + " with {:>4} points".format(QuizHandler.ranklist[i - 1][1]), position=2))
                # Detailed Results
                for team in QuizHandler.teams:
                    QuizHandler.detail_list.append([team.name, team.points_quiz, team.points_marbles])
                longestkey = 0
                for team_detail_list in QuizHandler.detail_list:
                    if len(team_detail_list[0]) > longestkey:
                        longestkey = len(team_detail_list[0])
                # Create printlist
                printlist: typing.List[str] = []
                # Format Results
                for i in range(0, len(QuizHandler.detail_list)):
                    spacestoinsert = (longestkey - len(QuizHandler.detail_list[i][0])) * " "
                    printlist.append(tc.align_string(string="Team " + QuizHandler.detail_list[i][0] + " scored {:>4} points in the quiz and {:>4} with the Experiments.".format(QuizHandler.detail_list[i][1], QuizHandler.detail_list[i][2]), position=1.5))
                # Print Score
                print("\n")
                for i in printlist:
                    print(tc.align_string(string=i, position=3))
                print("\n\n" + tc.align_string(string="Press ENTER to continue...", position=2))
                input()


main()
