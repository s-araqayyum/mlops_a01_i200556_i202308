import unittest
import pandas as pd
from train import pipeline

class TestModelTraining(unittest.TestCase):
    def test_prediction(self):
        # Example text for prediction
        test_text = ["Feeling joyful today!"]
        prediction = pipeline.predict(test_text)
        self.assertIsNotNone(prediction)  # Check if prediction is not None
        self.assertTrue(len(prediction) > 0)  # Ensure prediction returns a value

if __name__ == '__main__':
    unittest.main()
