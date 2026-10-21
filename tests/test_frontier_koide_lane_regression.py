"""The support aggregator must not accept failed child processes."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import frontier_koide_lane_regression as regression


class ChildResultTests(unittest.TestCase):
    def run_child(self, stdout, exit_code):
        with tempfile.TemporaryDirectory() as directory:
            scripts = Path(directory)
            (scripts / "synthetic.py").write_text(
                f"import sys\nprint({stdout!r})\nsys.exit({exit_code})\n",
                encoding="utf-8",
            )
            output = io.StringIO()
            with patch.object(regression, "SCRIPTS", scripts), \
                    patch.object(regression, "RUNNERS", [("synthetic.py", 2)]), \
                    patch.object(regression, "EXPECTED_TOTAL", 2), \
                    contextlib.redirect_stdout(output):
                status = regression.main()
        return status, output.getvalue()

    def test_successful_child_with_expected_summary(self):
        status, output = self.run_child("PASSED: 2/2", 0)
        self.assertEqual(status, 0)
        self.assertIn("Support batch verified.", output)

    def test_nonzero_child_cannot_pass_with_expected_summary(self):
        for exit_code in (1, 7):
            with self.subTest(exit_code=exit_code):
                status, output = self.run_child("PASSED: 2/2", exit_code)
                self.assertEqual(status, 1)
                self.assertIn(f"exit code {exit_code}", output)
                self.assertIn("TOTAL: 0/2", output)
                self.assertNotIn("Support batch verified.", output)

    def test_zero_exit_requires_valid_complete_summary(self):
        for stdout in ("", "no summary", "PASSED: nonsense", "PASSED: 2/x",
                       "PASSED: 1/2", "PASSED: 2/3"):
            with self.subTest(stdout=stdout):
                status, output = self.run_child(stdout, 0)
                self.assertEqual(status, 1)
                self.assertIn("[FAIL]", output)
                self.assertNotIn("Support batch verified.", output)


if __name__ == "__main__":
    unittest.main()
