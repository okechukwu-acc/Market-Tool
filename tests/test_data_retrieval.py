import unittest
from app.utils.data_retrieval import fetch_historical_data, preprocess_data

class TestDataRetrieval(unittest.TestCase):
    def test_fetch_historical_data(self):
        data = fetch_historical_data('AAPL', '2020-01-01', '2021-01-01')
        self.assertIsNotNone(data)
        self.assertIn('Close', data.columns)

    def test_preprocess_data(self):
        data = fetch_historical_data('AAPL', '2020-01-01', '2021-01-01')
        preprocessed_data = preprocess_data(data)
        self.assertFalse(preprocessed_data.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
