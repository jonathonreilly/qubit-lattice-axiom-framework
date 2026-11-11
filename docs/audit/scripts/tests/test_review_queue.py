"""Hermetic tests for the read-only review queue and landing history.

The fixtures under ``fixtures/review_queue`` are recorded ``gh`` output plus a
few built rows; each file says which is which.  No test opens a connection.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import review_loop_backlog_inventory as inventory
import review_queue as queue


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "review_queue"
REPORTING_DOC = (
    REPO_ROOT
    / "docs/ai_methodology/skills/review-loop/references/FIXES_AND_REPORTING.md"
)
NOW = queue.parse_utc("2026-11-11T00:00:00Z")
HEAD = "884b39e8051dd5e58989bad82b25c979d81c5192"
OTHER_HEAD = "89a50f0bd3667c641ba60c322556bfd9f60d9e50"


def _fixture(name: str) -> list[dict]:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))["prs"]


def _open_pr(number: int = 1, **changes) -> dict:
    row = {
        "number": number,
        "title": f"PR {number}",
        "isDraft": False,
        "isCrossRepository": False,
        "baseRefName": "main",
        "headRefName": f"head-{number}",
        "headRefOid": HEAD,
        "createdAt": "2026-11-10T00:00:00Z",
        "updatedAt": "2026-11-10T12:00:00Z",
        "url": f"https://example.test/{number}",
        "additions": 10,
        "deletions": 0,
        "changedFiles": 1,
        "mergeable": "MERGEABLE",
        "mergeStateStatus": "BLOCKED",
        "reviewDecision": "REVIEW_REQUIRED",
        "reviews": [],
        "comments": [],
    }
    row.update(changes)
    return row


def _review(state: str, commit: str, at: str, body: str = "") -> dict:
    return {"state": state, "commit": {"oid": commit}, "submittedAt": at, "body": body}


def _comment(body: str, at: str) -> dict:
    return {"body": body, "createdAt": at}


def _action(pr: dict) -> str:
    return queue.build_queue([pr], NOW, limit=100)["prs"][0]["next_action"]


class NextActionTest(unittest.TestCase):
    def test_first_matching_condition_decides(self):
        base = dict(
            draft=False,
            base="main",
            mergeable="MERGEABLE",
            record_count=1,
            verdict=queue.VERDICT_PASS,
            verdict_names_head=True,
        )
        cases = [
            ({}, queue.READY),
            ({"verdict": queue.VERDICT_FINDINGS}, queue.FINDINGS),
            ({"verdict_names_head": False}, queue.RE_REVIEW),
            ({"verdict": None, "verdict_names_head": None}, queue.NO_VERDICT),
            (
                {"record_count": 0, "verdict": None, "verdict_names_head": None},
                queue.FIRST_REVIEW,
            ),
            ({"mergeable": "CONFLICTING"}, queue.CONFLICTS),
            ({"mergeable": "UNKNOWN"}, queue.READY),
            ({"base": "stack-a", "mergeable": "CONFLICTING"}, queue.BASE_NOT_MAIN),
            ({"draft": True, "base": "stack-a"}, queue.DRAFT),
        ]
        for changes, expected in cases:
            with self.subTest(changes=changes):
                self.assertEqual(queue.next_action(**{**base, **changes}), expected)
        self.assertEqual(
            {expected for _, expected in cases}, set(queue.NEXT_ACTIONS)
        )

    def test_recorded_and_built_rows(self):
        result = queue.build_queue(_fixture("open_prs.json"), NOW, limit=1000)
        rows = {row["number"]: row for row in result["prs"]}
        self.assertEqual(
            {number: row["next_action"] for number, row in rows.items()},
            {
                10154: queue.BASE_NOT_MAIN,
                10150: queue.FIRST_REVIEW,
                10139: queue.DRAFT,
                10137: queue.FIRST_REVIEW,
                10133: queue.DRAFT,
                9870: queue.CONFLICTS,
                90001: queue.FINDINGS,
                90002: queue.RE_REVIEW,
                90003: queue.READY,
                90004: queue.NO_VERDICT,
            },
        )
        # Who can act now comes first; inside one action the oldest PR leads.
        self.assertEqual(
            [row["number"] for row in result["prs"]],
            [90003, 90002, 10137, 10150, 90001, 90004, 9870, 10154, 10133, 10139],
        )
        self.assertEqual(rows[10154]["parent_pr"], 10150)
        self.assertEqual(rows[10154]["base"], "claude/rules-redesign")
        self.assertEqual(
            (rows[9870]["age_days"], rows[9870]["idle_days"]), (20.2, 20.2)
        )
        self.assertEqual(
            (rows[10139]["age_days"], rows[10139]["idle_days"]), (6.2, 1.9)
        )
        self.assertEqual(
            (rows[9870]["additions"], rows[9870]["changed_files"]), (633, 8)
        )
        self.assertEqual((rows[90003]["reviews"], rows[90003]["comments"]), (0, 2))
        self.assertEqual(rows[90003]["verdict_at"], "2026-10-30T18:41:05Z")
        self.assertEqual(
            result["summary"],
            {
                "open": 10,
                "non_draft": 8,
                "draft": 2,
                "non_draft_without_review_or_comment": 4,
                "non_draft_age_days_median": 11.4,
                "non_draft_age_days_max": 20.2,
                "non_draft_additions": 3871,
                "non_draft_changed_files": 46,
                "mergeable_unknown": 0,
                "by_next_action": {
                    queue.READY: 1,
                    queue.RE_REVIEW: 1,
                    queue.FIRST_REVIEW: 2,
                    queue.FINDINGS: 1,
                    queue.NO_VERDICT: 1,
                    queue.CONFLICTS: 1,
                    queue.BASE_NOT_MAIN: 1,
                    queue.DRAFT: 2,
                },
            },
        )

    def test_github_review_states(self):
        early, late = "2026-11-10T01:00:00Z", "2026-11-10T02:00:00Z"
        self.assertEqual(
            _action(_open_pr(reviews=[_review("APPROVED", HEAD, early)])),
            queue.READY,
        )
        self.assertEqual(
            _action(_open_pr(reviews=[_review("CHANGES_REQUESTED", HEAD, early)])),
            queue.FINDINGS,
        )
        # The approval is of an older commit: the head moved after it.
        self.assertEqual(
            _action(_open_pr(reviews=[_review("APPROVED", OTHER_HEAD, early)])),
            queue.RE_REVIEW,
        )
        # The same account cannot approve its own PR, so a verdict can arrive
        # as the text of a COMMENTED review.
        self.assertEqual(
            _action(
                _open_pr(
                    reviews=[
                        _review("COMMENTED", HEAD, early, "**PASS**, no findings.")
                    ]
                )
            ),
            queue.READY,
        )
        self.assertEqual(
            _action(_open_pr(reviews=[_review("COMMENTED", HEAD, early, "A note.")])),
            queue.NO_VERDICT,
        )
        self.assertEqual(
            _action(_open_pr(reviews=[_review("DISMISSED", HEAD, early)])),
            queue.FIRST_REVIEW,
        )
        self.assertEqual(
            _action(
                _open_pr(
                    reviews=[
                        _review("CHANGES_REQUESTED", HEAD, early),
                        _review("APPROVED", HEAD, late),
                    ]
                )
            ),
            queue.READY,
        )

    def test_newest_verdict_wins_and_plain_comments_do_not_replace_it(self):
        reviewed = f"Reviewed head `{HEAD}`."
        hold = _comment(f"Result: **HOLD**.\n\n{reviewed}", "2026-11-10T01:00:00Z")
        passed = _comment(f"**PASS**.\n\n{reviewed}", "2026-11-10T03:00:00Z")
        note = _comment("Reading the findings.", "2026-11-10T04:00:00Z")
        self.assertEqual(_action(_open_pr(comments=[hold, note])), queue.FINDINGS)
        self.assertEqual(_action(_open_pr(comments=[passed, hold, note])), queue.READY)
        self.assertEqual(
            _action(_open_pr(comments=[hold], headRefOid=OTHER_HEAD)),
            queue.RE_REVIEW,
        )
        # A verdict that names no head is bound to no revision.
        self.assertEqual(
            _action(_open_pr(comments=[_comment("**PASS**.", "2026-11-10T01:00:00Z")])),
            queue.RE_REVIEW,
        )


class VerdictReadingTest(unittest.TestCase):
    def test_reads_the_first_paragraph_only(self):
        cases = {
            "Focused review-loop result: **HOLD / changes required**.": "findings",
            "Focused repo-native review-loop: **PASS / landed**.": "pass",
            "Focused repo-native **review-loop PASS**. Closed without merging.": "pass",
            "Recommendation: PASS WITH BOUNDED CLAIMS": "pass",
            "NEEDS MANUAL SCIENCE: the limit step is not proved.": "findings",
            "PASS. The earlier HOLD is resolved.": "pass",
            "HOLD: the runner's PASS line is false.": "findings",
            "The checks pass and nothing is on hold.": None,
            "BYPASS and THRESHOLD are not verdict words.": None,
            "Summary of the run.\n\nVerdict: PASS": None,
            "": None,
        }
        for body, expected in cases.items():
            with self.subTest(body=body):
                self.assertEqual(queue.read_verdict(body), expected)
        self.assertEqual(
            queue.read_verdict("Result: **HOLD**.\r\n\r\nPASS later"), "findings"
        )

    def test_names_head_needs_twelve_characters_of_the_same_sha(self):
        self.assertTrue(queue.names_head(f"Reviewed head `{HEAD}`.", HEAD))
        self.assertTrue(queue.names_head(f"at blob/{HEAD}/docs/x.py#L1", HEAD))
        self.assertTrue(queue.names_head(f"head {HEAD[:12]} reviewed", HEAD))
        self.assertFalse(queue.names_head(f"head {HEAD[:11]} reviewed", HEAD))
        self.assertFalse(queue.names_head(f"Reviewed head `{OTHER_HEAD}`.", HEAD))
        self.assertFalse(queue.names_head(f"Reviewed head `{HEAD}`.", ""))


class LandingRecordTest(unittest.TestCase):
    FULL = {
        "review_start_utc": "2026-11-11T10:00:00Z",
        "review_end_utc": "2026-11-11T12:00:00Z",
        "rounds": 2,
        "reviewer_provider": "example-provider",
        "reviewer_model": "example-model",
        "reviewer_effort": "low",
        "gate_seconds": 415.5,
        "train": "train-90",
        "frozen_head": "a" * 40,
        "landed_head": "b" * 40,
        "recovery_ref": "refs/review-loop/recovery/pr-90010/" + "a" * 40,
    }

    def test_round_trip_keeps_types(self):
        text = "Landed.\n\n" + queue.format_cost_block(self.FULL) + "\n\nDone."
        blocks = queue.find_cost_blocks(text)
        self.assertEqual(len(blocks), 1)
        fields, problems = queue.parse_cost_block(blocks[0])
        self.assertEqual(problems, [])
        self.assertEqual(fields, self.FULL)
        self.assertEqual(tuple(fields), queue.COST_FIELDS)
        self.assertEqual(queue.check_record_text(text), [])

    def test_none_is_a_value_and_an_omitted_field_is_a_problem(self):
        sparse = dict(self.FULL, gate_seconds=None, recovery_ref=None)
        fields, problems = queue.parse_cost_block(
            queue.find_cost_blocks(queue.format_cost_block(sparse))[0]
        )
        self.assertEqual(problems, [])
        self.assertIsNone(fields["gate_seconds"])
        self.assertIsNone(fields["recovery_ref"])
        fields, problems = queue.parse_cost_block("rounds: 1\n")
        self.assertEqual(fields["rounds"], 1)
        self.assertEqual(
            problems,
            [f"missing field: {key}" for key in queue.COST_FIELDS if key != "rounds"],
        )

    def test_each_bad_value_is_reported_and_left_out(self):
        bad = {
            "review_start_utc": "2026-11-11 10:00",
            "review_end_utc": "2026-11-11T12:00:00+00:00",
            "rounds": "0",
            "reviewer_provider": "two words",
            "reviewer_model": "",
            "reviewer_effort": "low",
            "gate_seconds": "-1",
            "train": "train-90",
            "frozen_head": "abc123",
            "landed_head": "B" * 40,
            "recovery_ref": "heads/main",
        }
        text = "\n".join(f"{key}: {value}" for key, value in bad.items())
        fields, problems = queue.parse_cost_block(text)
        self.assertEqual(
            {key for key, value in fields.items() if value is not None},
            {"reviewer_effort", "train"},
        )
        self.assertEqual(
            [problem.split(":")[0] for problem in problems],
            [
                key
                for key in queue.COST_FIELDS
                if key not in {"reviewer_effort", "train"}
            ],
        )

    def test_structure_problems(self):
        text = queue.format_cost_block(self.FULL).split("\n", 1)[1].rsplit("\n", 1)[0]
        _, problems = queue.parse_cost_block(
            text + "\nrounds: 3\ntokens: 5\njust words\n"
        )
        self.assertEqual(
            problems,
            [
                "repeated field: rounds",
                "unknown field: tokens",
                "not a `field: value` line: just words",
            ],
        )
        swapped = dict(
            self.FULL,
            review_start_utc=self.FULL["review_end_utc"],
            review_end_utc=self.FULL["review_start_utc"],
        )
        _, problems = queue.parse_cost_block(
            queue.find_cost_blocks(queue.format_cost_block(swapped))[0]
        )
        self.assertEqual(problems, ["review_end_utc is before review_start_utc"])

    def test_only_the_named_fence_is_a_block(self):
        block = queue.format_cost_block(self.FULL)
        other = "```text\nrounds: 9\n```"
        self.assertEqual(queue.find_cost_blocks(other), [])
        both = f"{other}\n\n{block}\n\n{block}"
        self.assertEqual(len(queue.find_cost_blocks(both)), 2)
        self.assertEqual(len(queue.find_cost_blocks(block.replace("\n", "\r\n"))), 1)
        self.assertEqual(
            queue.check_record_text(f"{block}\n\n{block}"),
            ["expected one landing-record block, found 2"],
        )
        self.assertEqual(
            queue.check_record_text("no block"),
            ["expected one landing-record block, found 0"],
        )

    def test_reporting_reference_matches_the_code(self):
        doc = REPORTING_DOC.read_text(encoding="utf-8")
        blocks = queue.find_cost_blocks(doc)
        self.assertEqual(len(blocks), 1)
        fields, problems = queue.parse_cost_block(blocks[0])
        self.assertEqual(problems, [])
        self.assertTrue(all(value is not None for value in fields.values()))
        record = doc.split("## Landing Record", 1)[1].split("## Review Queue", 1)[0]
        documented = [
            name
            for row in re.findall(r"^\| (`[^|]+) \|", record, re.MULTILINE)
            for name in re.findall(r"`([a-z_]+)`", row)
        ]
        self.assertEqual(documented, list(queue.COST_FIELDS))
        actions = re.findall(
            r"^\| `([^`]+)` \|", doc.split("## Review Queue", 1)[1], re.MULTILINE
        )
        self.assertEqual(sorted(actions), sorted(queue.NEXT_ACTIONS))


class HistoryTest(unittest.TestCase):
    def setUp(self):
        self.history = queue.build_history(_fixture("closed_prs.json"), 10, NOW)
        self.rows = {row["number"]: row for row in self.history["prs"]}

    def test_hours_and_order(self):
        self.assertEqual(
            {number: row["open_hours"] for number, row in self.rows.items()},
            {
                10152: 0.02,
                10146: 0.22,
                10143: 0.26,
                10136: 0.65,
                10116: 4.62,
                10115: 2.41,
                90010: 4.5,
                90011: 6.5,
                90012: 4.0,
                90013: 0.5,
            },
        )
        self.assertEqual(
            [row["number"] for row in self.history["prs"]],
            [90012, 90011, 90010, 90013, 10152, 10146, 10143, 10136, 10116, 10115],
        )
        self.assertEqual(self.rows[10136]["state"], "MERGED")
        self.assertEqual(self.rows[10116]["state"], "CLOSED")

    def test_cost_fields_are_read_from_comments(self):
        valid = self.rows[90010]
        self.assertEqual(valid["cost"], LandingRecordTest.FULL)
        self.assertEqual(valid["cost_problems"], [])
        self.assertEqual((valid["wait_hours"], valid["review_hours"]), (2.0, 2.0))
        crlf = self.rows[90011]
        self.assertEqual(crlf["cost"]["rounds"], 1)
        self.assertEqual((crlf["wait_hours"], crlf["review_hours"]), (5.0, 1.0))
        broken = self.rows[90012]
        self.assertIsNone(broken["cost"]["rounds"])
        self.assertIsNone(broken["cost"]["frozen_head"])
        self.assertIsNone(broken["cost"]["gate_seconds"])
        self.assertEqual(len(broken["cost_problems"]), 4)
        for recorded in (10152, 10146, 10143, 10136, 10116, 10115):
            self.assertIsNone(self.rows[recorded]["cost"])
            self.assertEqual(self.rows[recorded]["cost_blocks"], 0)

    def test_summary(self):
        summary = self.history["summary"]
        self.assertEqual(
            {
                key: summary[key]
                for key in (
                    "merged",
                    "closed_not_merged",
                    "with_cost_fields",
                    "without_cost_fields",
                    "with_cost_problems",
                )
            },
            {
                "merged": 6,
                "closed_not_merged": 4,
                "with_cost_fields": 3,
                "without_cost_fields": 7,
                "with_cost_problems": 1,
            },
        )
        merged = summary["open_to_merged_hours"]
        self.assertEqual((merged["n"], merged["p90"]), (6, 6.5))
        self.assertAlmostEqual(merged["median"], 2.325, delta=0.006)
        closed = summary["open_to_closed_hours"]
        self.assertEqual((closed["n"], closed["p90"]), (4, 4.62))
        self.assertAlmostEqual(closed["median"], 1.455, delta=0.006)
        self.assertEqual(
            summary["open_to_review_start_hours"], {"n": 3, "median": 2.0, "p90": 5.0}
        )
        self.assertEqual(summary["review_hours"], {"n": 3, "median": 2.0, "p90": 2.0})
        self.assertEqual(summary["rounds"], {"n": 2, "median": 1.5, "p90": 2})
        # #90010 and #90011 share one train, so one gate is counted.
        self.assertEqual(
            summary["gate_seconds"], {"n": 1, "median": 415.5, "p90": 415.5}
        )

    def test_gate_cost_counts_trains_with_legacy_fallback(self):
        cases = [
            (("train-a", "a" * 40), ("train-a", "b" * 40), 1),
            (("train-a", "a" * 40), ("train-b", "a" * 40), 2),
            ((None, "a" * 40), (None, "a" * 40), 1),
            ((None, None), (None, None), 2),
        ]
        for first, second, count in cases:
            with self.subTest(first=first, second=second):
                rows = []
                for number, (train, head) in enumerate((first, second), 1):
                    cost = dict(LandingRecordTest.FULL, train=train, landed_head=head)
                    rows.append({
                        "number": number, "state": "MERGED",
                        "createdAt": "2026-11-10T00:00:00Z",
                        "mergedAt": "2026-11-11T12:00:00Z",
                        "comments": [{"body": queue.format_cost_block(cost)}],
                    })
                history = queue.build_history(rows, 2, NOW)
                self.assertEqual(history["summary"]["gate_seconds"],
                                 {"n": count, "median": 415.5, "p90": 415.5})

    def test_nearest_rank_percentile(self):
        self.assertEqual(queue._percentile(list(range(1, 11)), 90), 9)
        self.assertEqual(queue._percentile([7.0], 90), 7.0)
        self.assertEqual(queue._percentile([3, 1, 2], 90), 3)
        self.assertIsNone(queue._percentile([], 90))
        self.assertIsNone(queue._median([]))

    def test_merged_pr_is_measured_to_its_merge(self):
        row = {
            "number": 1,
            "state": "MERGED",
            "createdAt": "2026-11-10T00:00:00Z",
            "mergedAt": "2026-11-10T01:00:00Z",
            "closedAt": "2026-11-10T03:00:00Z",
        }
        history = queue.build_history([row], 1, NOW)
        self.assertEqual(history["prs"][0]["open_hours"], 1.0)
        self.assertEqual(history["prs"][0]["ended_at"], "2026-11-10T01:00:00Z")

    def test_row_without_an_end_time_fails_closed(self):
        with self.assertRaises(inventory.InventoryError):
            queue.build_history(
                [{"number": 1, "state": "CLOSED", "createdAt": "2026-11-10T00:00:00Z"}],
                1,
                NOW,
            )


class RenderTest(unittest.TestCase):
    def test_queue_table_has_one_row_per_pr(self):
        result = queue.build_queue(_fixture("open_prs.json"), NOW, limit=1000)
        text = queue.render_queue(result)
        table = [line for line in text.splitlines() if line.startswith("| #")]
        self.assertEqual(len(table), 10)
        self.assertTrue(all(line.count("|") == 13 for line in table), table)
        self.assertIn(
            "| PR | title | draft | base | age d | idle d | +lines | files | "
            "reviews | comments | mergeable | next action |",
            text,
        )
        self.assertIn(
            "| #10154 | feat(land): show a landed PR as merged | no | "
            "claude/rules-redesign (#10150) | 0.1 | 0.1 | 777 | 9 | 0 | 0 | "
            "MERGEABLE | base is not main |",
            text,
        )
        self.assertIn("10 open PRs: 8 non-draft, 2 draft.", text)
        self.assertIn("4 with no review and no comment", text)
        self.assertNotIn("UNKNOWN", text)
        self.assertNotIn("query limit", text)

    def test_queue_footers_and_escaped_titles(self):
        result = queue.build_queue(
            [_open_pr(1, title="a | b\nc", mergeable="UNKNOWN")], NOW, limit=1
        )
        text = queue.render_queue(result)
        self.assertIn("| #1 | a \\| b c | no |", text)
        self.assertIn("1 PRs show mergeable UNKNOWN", text)
        self.assertIn("The query limit of 1 was reached", text)

    def test_history_tables(self):
        history = queue.build_history(_fixture("closed_prs.json"), 10, NOW)
        text = queue.render_history(history)
        self.assertIn(
            "| #90010 | built row 90010 | MERGED | 4.50 | 1 | 2 | "
            "example-provider/example-model/low | 2.0 | 2.0 | 415.5 | train-90 | "
            "bbbbbbbbbbbb |",
            text,
        )
        self.assertIn("| #10152 |", text)
        self.assertIn("| open to merged, hours | 6 |", text)
        self.assertIn("| gate seconds, one per train | 1 | 415.5 | 415.5 |", text)
        self.assertIn("7 of 10 PRs carry no cost fields", text)
        self.assertIn("1 carry a block with a problem.", text)
        self.assertIn("#90012 landing-record: missing field: recovery_ref", text)


class ReadOnlyCommandTest(unittest.TestCase):
    WRITE_WORDS = {
        "comment", "review", "close", "merge", "edit", "ready", "reopen",
        "create", "push", "fetch", "api", "label", "delete",
    }

    def _collect(self, mode: str):
        calls = []
        fixture = "open_prs.json" if mode == "queue" else "closed_prs.json"

        def fake_run(cmd, cwd):
            calls.append(cmd)
            return json.dumps(_fixture(fixture))

        if mode == "queue":
            result = queue.collect_queue(Path("/repo"), 500, runner=fake_run, now=NOW)
        else:
            result = queue.collect_history(Path("/repo"), 25, runner=fake_run, now=NOW)
        return calls, result

    def test_queue_is_one_read_only_listing(self):
        calls, result = self._collect("queue")
        self.assertEqual(len(calls), 1)
        cmd = calls[0]
        self.assertEqual(cmd[:5], ["gh", "pr", "list", "--state", "open"])
        self.assertEqual(cmd[cmd.index("--limit") + 1], "500")
        fields = cmd[cmd.index("--json") + 1].split(",")
        for field in (
            "createdAt",
            "additions",
            "changedFiles",
            "mergeable",
            "reviews",
            "comments",
        ):
            self.assertIn(field, fields)
        self.assertFalse(self.WRITE_WORDS & set(cmd), cmd)
        self.assertTrue(result["read_only"])
        json.dumps(result)

    def test_history_is_one_read_only_listing(self):
        calls, result = self._collect("history")
        self.assertEqual(len(calls), 1)
        cmd = calls[0]
        self.assertEqual(cmd[:5], ["gh", "pr", "list", "--state", "closed"])
        self.assertEqual(cmd[cmd.index("--limit") + 1], "25")
        self.assertIn("mergedAt", cmd[cmd.index("--json") + 1].split(","))
        self.assertFalse(self.WRITE_WORDS & set(cmd), cmd)
        self.assertEqual((result["requested"], result["returned"]), (25, 10))
        json.dumps(result)

    def test_inventory_listing_is_unchanged(self):
        calls = []

        def fake_run(cmd, cwd):
            calls.append(cmd)
            return "[]"

        inventory.fetch_open_prs(Path("/repo"), limit=5, runner=fake_run)
        self.assertEqual(
            calls,
            [
                ["gh", "pr", "list", "--state", "open", "--limit", "5", "--json"]
                + [inventory.GH_FIELDS]
            ],
        )

    def test_bad_arguments_and_rows_fail_before_or_without_output(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            self.assertEqual(queue.main(["--history", "0"]), 2)
            self.assertEqual(queue.main(["--limit", "0"]), 2)
        with self.assertRaises(inventory.InventoryError):
            queue.build_queue([{"number": 1, "baseRefName": "main"}], NOW, limit=10)

    def test_check_record_reads_a_file_and_calls_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            good = Path(tmp) / "good.md"
            good.write_text(
                "Landed.\n\n" + queue.format_cost_block(LandingRecordTest.FULL) + "\n",
                encoding="utf-8",
            )
            bad = Path(tmp) / "bad.md"
            bad.write_text("```landing-record\nrounds: many\n```\n", encoding="utf-8")
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                self.assertEqual(queue.main(["--check-record", str(good)]), 0)
                self.assertEqual(queue.main(["--check-record", str(bad)]), 1)
                self.assertEqual(
                    queue.main(["--check-record", str(Path(tmp) / "absent.md")]), 2
                )
            self.assertEqual(
                sorted(path.name for path in Path(tmp).iterdir()),
                ["bad.md", "good.md"],
            )
        self.assertIn("landing-record: OK", out.getvalue())
        self.assertIn("landing-record: rounds: not a whole number", out.getvalue())


if __name__ == "__main__":
    unittest.main()
