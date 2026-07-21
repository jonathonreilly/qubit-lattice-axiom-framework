"""Regression tests for the conditional-prompts generator's link healing.

Encodes the PR #5404 sol-max round-1 finding: healing must rewrite only the
generated "**Note:**" link field, never quoted evidence, inline code, or
fenced examples, and must be idempotent.
"""

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import generate_conditional_prompts as gcp  # noqa: E402


class HealLegacyLinkPrefixesTest(unittest.TestCase):
    def test_note_line_is_healed(self):
        line = "**Note:** [docs/X_NOTE.md](docs/X_NOTE.md)  |  **Descendants:** 3  |  **Class:** c"
        healed = gcp.heal_legacy_link_prefixes(line)
        self.assertIn("[docs/X_NOTE.md](../X_NOTE.md)", healed)

    def test_inline_code_and_fenced_examples_untouched(self):
        text = (
            "evidence: `[literal](docs/X.md)` stays\n"
            "```\n[example](docs/X.md)\n```\n"
            "prose [active-but-not-note-field](docs/X.md) also stays"
        )
        self.assertEqual(gcp.heal_legacy_link_prefixes(text), text)

    def test_idempotent(self):
        line = "**Note:** [docs/X.md](docs/X.md)  |  rest"
        once = gcp.heal_legacy_link_prefixes(line)
        self.assertEqual(gcp.heal_legacy_link_prefixes(once), once)


class ConditionalCategoryCoverageTest(unittest.TestCase):
    def test_missing_dependency_edge_has_generated_section(self):
        rows = {
            "claim": {
                "audit_status": "audited_conditional",
                "notes_for_re_audit_if_any": (
                    "missing_dependency_edge: cite the retained authority"
                ),
                "transitive_descendants": 3,
            }
        }

        by_class = gcp.collect_rows(rows, synthesized=set())

        self.assertEqual(
            [item["cid"] for item in by_class[
                "audited_conditional_missing_dependency_edge"
            ]],
            ["claim"],
        )


if __name__ == "__main__":
    unittest.main()
