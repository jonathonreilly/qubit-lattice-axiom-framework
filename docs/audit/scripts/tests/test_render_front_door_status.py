"""Tests for the retained-backbone projection in render_front_door_status."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from render_front_door_status import retained_backbone_lines


def _row(claim_id, status, score=None, note_path="auto", audit_date="2026-07-01",
         parent=None):
    row = {
        "claim_id": claim_id,
        "effective_status": status,
        "audit_date": audit_date,
    }
    if note_path == "auto":
        row["note_path"] = f"docs/{claim_id.upper()}.md"
    elif note_path is not None:
        row["note_path"] = note_path
    if score is not None:
        row["load_bearing_score"] = score
    if parent is not None:
        row["decoration_parent_claim_id"] = parent
    return row


class RetainedBackboneTest(unittest.TestCase):
    def test_groups_counts_and_ordering(self):
        rows = {
            "a": _row("a_note", "retained", score=1.5),
            "b": _row("b_note", "retained", score=9.0),
            "c": _row("c_note", "retained_bounded", score=2.0),
            "d": _row("d_note", "unaudited", score=99.0),
            "e": _row("e_note", "audited_conditional"),
            "f": _row("f_note", "decoration_under_retained", parent="a_note"),
        }
        lines = retained_backbone_lines(rows)
        text = "\n".join(lines)
        self.assertIn("## Retained positive rows (2)", text)
        self.assertIn("## Retained bounded rows (1)", text)
        self.assertIn("## Retained no-go rows (0)", text)
        self.assertIn("## Boxed decorations under retained parents (1)", text)
        # Non-retained rows must never appear.
        self.assertNotIn("d_note", text)
        self.assertNotIn("e_note", text)
        # Descending score order inside a group.
        self.assertLess(text.index("b_note"), text.index("a_note"))
        # Decoration names its parent.
        self.assertIn("under `a_note`", text)

    def test_empty_grade_renders_none(self):
        lines = retained_backbone_lines({})
        text = "\n".join(lines)
        self.assertEqual(text.count("- none at present"), 4)

    def test_link_format_and_missing_fields(self):
        rows = {
            "x": _row("x_note", "retained", score=3.0),
            "y": _row("y_note", "retained", note_path=None, audit_date=None),
        }
        text = "\n".join(retained_backbone_lines(rows))
        self.assertIn("[`x_note`](../../docs/X_NOTE.md) — score 3.000; audited 2026-07-01", text)
        # Missing note_path degrades to plain code span; missing score/date shown as '-'.
        self.assertIn("- `y_note` — score -; audited -", text)
        # Missing score sorts after any real score.
        self.assertLess(text.index("x_note"), text.index("y_note"))

    def test_counts_table_matches_groups(self):
        rows = {
            "a": _row("a_note", "retained"),
            "b": _row("b_note", "retained_no_go", score=1.0),
        }
        text = "\n".join(retained_backbone_lines(rows))
        self.assertIn("| Retained positive rows | 1 |", text)
        self.assertIn("| Retained no-go rows | 1 |", text)
        self.assertIn("| Retained bounded rows | 0 |", text)


if __name__ == "__main__":
    unittest.main()
