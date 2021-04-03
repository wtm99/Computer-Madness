"""
This class runs a game with a given predictor, between the 2 teams
Can set a prediction style (i.e. percentage, n simulations, etc.)
"""
from src.predictors import Predictor

class Game:
    def __init__(self, team1 : str, team2 : str, predictor : Predictor):
        self.team1 = team1
        self.team2 = team2
        self.predictor = predictor
