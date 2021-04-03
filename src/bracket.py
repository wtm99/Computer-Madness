from src.game import Game
from src.predictors import Predictor
"""
Class that runs through a bracket and returns predictions
"""
class Bracket:
    def __init__(self, bracket_file : str, predictor : Predictor):
        self.bracket_file = bracket_file
        self.predictor = predictor
