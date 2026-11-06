import unittest

from backend.evaluation import EvaluationMetrics


class TestEvaluationMetrics(unittest.TestCase):

    def setUp(self):
        self.retrieved = ["D1", "D2", "D3", "D4"]
        self.relevant = {"D1", "D3", "D5"}

    def test_precision(self):
        result = EvaluationMetrics.precision(
            self.retrieved, self.relevant
        )
        self.assertAlmostEqual(result, 0.5)

    def test_recall(self):
        result = EvaluationMetrics.recall(
            self.retrieved, self.relevant
        )
        self.assertAlmostEqual(result, 2 / 3)

    def test_f1_score(self):
        result = EvaluationMetrics.f1_score(0.5, 2 / 3)
        self.assertAlmostEqual(result, 4 / 7)

    def test_precision_at_k(self):
        result = EvaluationMetrics.precision_at_k(
            self.retrieved, self.relevant, 2
        )
        self.assertAlmostEqual(result, 0.5)

    def test_recall_at_k(self):
        result = EvaluationMetrics.recall_at_k(
            self.retrieved, self.relevant, 2
        )
        self.assertAlmostEqual(result, 1 / 3)

    def test_average_precision(self):
        result = EvaluationMetrics.average_precision(
            self.retrieved, self.relevant
        )
        self.assertAlmostEqual(result, 5 / 9)

    def test_mean_average_precision(self):
        results = {
            "query1": ["D1", "D2", "D3"],
            "query2": ["D4", "D5", "D6"]
        }

        relevant_documents = {
            "query1": {"D1", "D3"},
            "query2": {"D5"}
        }

        result = EvaluationMetrics.mean_average_precision(
            results, relevant_documents
        )

        self.assertAlmostEqual(result, 2 / 3)

    def test_mean_reciprocal_rank(self):
        results = {
            "query1": ["D1", "D2", "D3"],
            "query2": ["D4", "D5", "D6"]
        }

        relevant_documents = {
            "query1": {"D3"},
            "query2": {"D5"}
        }

        result = EvaluationMetrics.mean_reciprocal_rank(
            results, relevant_documents
        )

        self.assertAlmostEqual(result, 5 / 12)

    def test_complete_evaluation(self):
        result = EvaluationMetrics.evaluate(
            self.retrieved,
            self.relevant,
            k=2
        )

        self.assertIn("precision", result)
        self.assertIn("recall", result)
        self.assertIn("f1_score", result)
        self.assertIn("precision_at_k", result)
        self.assertIn("recall_at_k", result)
        self.assertIn("average_precision", result)


if __name__ == "__main__":
    unittest.main()