import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillValidationTests(unittest.TestCase):
    def test_validator_passes(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skill.py")],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertIn("Skill validation: PASS", proc.stdout)

    def test_skill_has_progressive_disclosure(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/output-contract.md", text)
        self.assertIn("references/review-catalog.md", text)
        self.assertLessEqual(len(text.splitlines()), 500)

    def test_trigger_eval_has_positive_and_negative_cases(self):
        text = (ROOT / "evals" / "trigger-cases.md").read_text(encoding="utf-8")
        self.assertIn("## Should trigger", text)
        self.assertIn("## Should not trigger", text)


if __name__ == "__main__":
    unittest.main()
