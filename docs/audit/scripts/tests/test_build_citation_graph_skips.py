"""Generated repo status surfaces must not feed the citation graph.

A generated index of N retained rows would otherwise add +1 in-degree and
score to exactly the rows it reports on, perturbing the criticality bands the
audit queue consumes.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from build_citation_graph import is_skipped


class GeneratedSurfaceSkipTest(unittest.TestCase):
    def test_generated_repo_surfaces_skipped(self):
        self.assertTrue(is_skipped(Path("repo/RETAINED_BACKBONE.md")))
        self.assertTrue(is_skipped(Path("repo/FRONT_DOOR_STATUS.md")))

    def test_authored_repo_docs_not_skipped(self):
        self.assertFalse(is_skipped(Path("repo/CONTROLLED_VOCABULARY.md")))

    def test_class_f_repo_orientation_memos_skipped(self):
        # Class F = no premise or interpretive weight; author framing must not
        # set audit cost (FRESH_LOOK_REQUIREMENTS section 4). Scope is
        # docs/repo/ class-F memos: their row creation is already gated, so
        # the skip removes edges without deleting any existing ledger row.
        self.assertTrue(is_skipped(Path("repo/STATE_OF_THE_THEORY_2026-07-16.md")))

    def test_row_bearing_class_f_doc_outside_repo_dir_not_skipped(self):
        # This registered class-F doc already carries a ledger row; skipping
        # it would delete audit data, which the graph builder must not do.
        self.assertFalse(
            is_skipped(
                Path("GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md")
            )
        )

    def test_same_names_outside_repo_dir_not_skipped(self):
        self.assertFalse(is_skipped(Path("RETAINED_BACKBONE.md")))
        self.assertFalse(is_skipped(Path("lanes/repo/FRONT_DOOR_STATUS.md")))

    def test_existing_skips_unchanged(self):
        self.assertTrue(is_skipped(Path("audit/AUDIT_QUEUE.md")))
        self.assertTrue(is_skipped(Path("publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md")))
        self.assertTrue(is_skipped(Path("publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md")))
        self.assertFalse(is_skipped(Path("publication/ci3_z3/CLAIMS_TABLE.md")))


if __name__ == "__main__":
    unittest.main()
