import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [111, 777, 333, 444, 555]
    
    # Tests

    # Test latest score (the last thing in the list)
    
    # Pass in scores and get last item
    def test_latest_score(self):
        latest_score = latest(self.scores)
    # Checks last item is 555
        self.assertEqual(555, latest_score)
    


    # Test personal best (the highest score in the list)
    def test_personal_best( self ):

 # pass in scores list
        best_score = personal_best( self.scores )
 #  call personalBest to get highest score in list
        self.assertEqual( 777, best_score )
 # compare

    # Test top three from list of scores
    def test_personal_top_three(self):
        top_three = personal_top_three(self.scores)
        self.assertEqual([777, 555, 444], top_three)

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
