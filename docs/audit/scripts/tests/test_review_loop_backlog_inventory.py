"""Hermetic tests for the read-only review-loop backlog inventory."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import review_loop_backlog_inventory as inventory


def _pr(
    number: int,
    head: str,
    base: str = "main",
    *,
    draft: bool = False,
    oid: str | None = None,
) -> dict:
    return {
        "number": number,
        "title": f"PR {number}",
        "isDraft": draft,
        "isCrossRepository": False,
        "baseRefName": base,
        "headRefName": head,
        "headRefOid": oid or f"oid-{number}",
        "updatedAt": "2026-08-15T00:00:00Z",
        "url": f"https://example.test/{number}",
    }


class GithubEnumerationTest(unittest.TestCase):
    def test_one_bounded_open_pr_query(self):
        calls = []

        def fake_run(cmd, cwd):
            calls.append((cmd, cwd))
            return json.dumps([_pr(1, "root")])

        rows = inventory.fetch_open_prs(Path("/repo"), limit=777, runner=fake_run)
        self.assertEqual([row["number"] for row in rows], [1])
        self.assertEqual(len(calls), 1)
        cmd = calls[0][0]
        self.assertEqual(cmd[:4], ["gh", "pr", "list", "--state"])
        self.assertEqual(cmd[cmd.index("--limit") + 1], "777")
        self.assertIn("baseRefName", cmd[cmd.index("--json") + 1])

    def test_snapshot_uses_only_read_only_commands(self):
        calls = []

        with tempfile.TemporaryDirectory() as tmp:
            def fake_run(cmd, cwd):
                calls.append(cmd)
                if cmd[:3] == ["gh", "pr", "list"]:
                    return json.dumps([_pr(1, "root")])
                if cmd[:3] == ["git", "worktree", "list"]:
                    return (
                        f"worktree {tmp}\0HEAD oid-main\0"
                        "branch refs/heads/main\0\0"
                    )
                if cmd[:3] == ["git", "--no-optional-locks", "status"]:
                    return ""
                if cmd[:2] == ["ps", "-axo"]:
                    return ""
                self.fail(f"unexpected command: {cmd}")

            snapshot = inventory.collect_snapshot(
                Path(tmp), Path(tmp), limit=100, max_processes=8, runner=fake_run
            )
        self.assertTrue(snapshot["read_only"])
        self.assertEqual(sum(cmd[:3] == ["gh", "pr", "list"] for cmd in calls), 1)
        self.assertEqual(
            sum(cmd[:3] == ["git", "--no-optional-locks", "status"] for cmd in calls),
            1,
        )
        forbidden = {"fetch", "prune", "remove", "add", "push", "merge", "close"}
        self.assertFalse(any(forbidden & set(cmd) for cmd in calls), calls)


class DeclaredTopologyTest(unittest.TestCase):
    def test_stack_order_drafts_and_unresolved_bases(self):
        result = inventory.analyze_topology(
            [
                _pr(1, "stack-a"),
                _pr(2, "stack-b", "stack-a"),
                _pr(3, "stack-c", "stack-b"),
                _pr(4, "orphan", "closed-or-missing-base"),
                _pr(5, "independent"),
                _pr(6, "draft", draft=True),
            ]
        )
        self.assertEqual(result["non_draft_count"], 5)
        self.assertEqual(result["draft_count"], 1)
        self.assertEqual(result["main_based_count"], 2)
        self.assertEqual(result["open_parent_edge_count"], 2)
        self.assertEqual(result["unresolved_non_main_base_count"], 1)
        self.assertEqual(result["declared_main_ready_prs"], [1, 5])
        self.assertIn({"base": "main", "prs": [1, 2, 3]}, result["stack_paths"])
        self.assertIn(
            {"base": "closed-or-missing-base", "prs": [4]},
            result["stack_paths"],
        )
        rows = {row["number"]: row for row in result["prs"]}
        self.assertEqual(rows[3]["stack_depth"], 2)
        self.assertIsNone(rows[4]["stack_depth"])

    def test_cycle_and_duplicate_heads_are_not_ready(self):
        result = inventory.analyze_topology(
            [
                _pr(1, "dup"),
                _pr(2, "dup"),
                _pr(3, "cycle-a", "cycle-b"),
                _pr(4, "cycle-b", "cycle-a"),
            ]
        )
        self.assertEqual(result["duplicate_head_branches"], {"dup": [1, 2]})
        self.assertEqual(result["declared_base_cycles"], [3, 4])
        self.assertEqual(result["declared_main_ready_prs"], [])

    def test_fork_head_does_not_create_a_false_stack_parent(self):
        fork = _pr(1, "same-name")
        fork["isCrossRepository"] = True
        result = inventory.analyze_topology([fork, _pr(2, "child", "same-name")])
        rows = {row["number"]: row for row in result["prs"]}
        self.assertEqual(result["declared_main_ready_prs"], [1])
        self.assertEqual(rows[2]["topology_state"], "unresolved_non_main_base")
        self.assertIsNone(rows[2]["parent_pr"])

        fork_collision = _pr(3, "duplicate")
        fork_collision["isCrossRepository"] = True
        collision = inventory.analyze_topology(
            [fork_collision, _pr(4, "duplicate"), _pr(5, "duplicate")]
        )
        self.assertEqual(collision["duplicate_head_branches"], {"duplicate": [4, 5]})
        self.assertEqual(collision["declared_main_ready_prs"], [3])


class WorktreeRecoveryTest(unittest.TestCase):
    def test_porcelain_parser_and_exact_pr_matching(self):
        text = (
            "worktree /repo\0HEAD oid-main\0branch refs/heads/main\0\0"
            "worktree /tmp/rev-2.ABCD\0HEAD oid-fix\0detached\0\0"
            "worktree /tmp/other\0HEAD oid-5\0branch refs/heads/independent\0\0"
        )
        worktrees = inventory.parse_worktree_porcelain(text)
        for tree in worktrees:
            tree["recovery_state"] = "clean_checkout"
        topology = inventory.analyze_topology(
            [_pr(1, "root"), _pr(2, "child", "root"), _pr(5, "independent")]
        )
        inventory.match_worktrees_to_prs(topology, worktrees)
        self.assertEqual(worktrees[0]["matched_open_prs"], [])
        self.assertEqual(worktrees[1]["matched_open_prs"], [2])
        self.assertEqual(worktrees[2]["matched_open_prs"], [5])
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            (tmp_root / "rev-5.recovery").mkdir()
            (tmp_root / "review-findings-pr2.recovery").touch()
            scan = inventory.scan_tmp_root(tmp_root, set())
        self.assertEqual(scan["unregistered_review_paths"][0]["pr"], 5)
        self.assertEqual(scan["findings_files"][0]["pr"], 2)


class ProcessAndCapacityTest(unittest.TestCase):
    def test_counts_only_worker_clis_and_detects_audit_ancestry(self):
        text = "\n".join(
            [
                "10 1 /Applications/Codex.app/Contents/Resources/codex app-server",
                "20 1 python3 docs/audit/scripts/orchestrate_audit_batch.py",
                "21 20 /usr/local/bin/codex exec --model gpt-5.6-sol prompt",
                "30 1 /usr/local/bin/codex resume abc",
                "40 1 /Applications/Claude.app/Contents/Helpers/disclaimer /x/claude --model x",
                "41 40 /x/claude --output-format stream-json --model opus",
            ]
        )
        result = inventory.parse_worker_processes(text)
        self.assertEqual(result["observed_worker_count"], 3)
        self.assertEqual(result["observed_audit_worker_count"], 1)
        self.assertEqual(
            [row["pid"] for row in result["workers"]],
            [21, 30, 41],
        )

    def test_capacity_preserves_disk_reserve_and_audit_review_cap(self):
        result = inventory.compute_capacity(
            free_kib=inventory.MIN_FREE_KIB + 3 * inventory.ESTIMATED_WORKTREE_KIB,
            observed_workers=5,
            observed_audit_workers=4,
        )
        self.assertEqual(result["conservative_new_worktree_slots"], 3)
        self.assertEqual(result["review_process_slots"], 3)
        blocked = inventory.compute_capacity(
            free_kib=inventory.MIN_FREE_KIB - 1,
            observed_workers=0,
            observed_audit_workers=0,
        )
        self.assertFalse(blocked["disk_guard_pass"])
        self.assertEqual(blocked["conservative_new_worktree_slots"], 0)
        with self.assertRaises(ValueError):
            inventory.compute_capacity(
                free_kib=inventory.MIN_FREE_KIB,
                observed_workers=0,
                observed_audit_workers=0,
                max_processes=11,
            )


class SlotPlanTest(unittest.TestCase):
    def test_stacked_pr_is_never_scheduled_and_recovery_blocks_duplicates(self):
        topology = inventory.analyze_topology(
            [
                _pr(1, "root-a"),
                _pr(2, "child", "root-a"),
                _pr(3, "root-b"),
                _pr(4, "root-c"),
                _pr(5, "root-d"),
            ]
        )
        worktrees = [
            {
                "path": "/tmp/rev-1.ABCD",
                "matched_open_prs": [1],
                "recovery_state": "dirty_recovery",
            }
        ]
        tmp_scan = {
            "findings_files": [{"path": "/tmp/review-findings-pr3.X", "pr": 3}],
            "unregistered_review_paths": [
                {"path": "/tmp/rev-4.X", "pr": 4, "has_git_marker": True}
            ],
        }
        capacity = {
            "review_process_slots": 2,
            "conservative_new_worktree_slots": 1,
        }
        plan = inventory.plan_slots(topology, worktrees, tmp_scan, capacity)
        self.assertEqual(
            [row["pr"] for row in plan["recovery_actions"]],
            [1, 3, 4],
        )
        self.assertEqual([row["pr"] for row in plan["ready_slots"]], [5])
        self.assertNotIn(2, [row["pr"] for row in plan["ready_slots"]])
        self.assertEqual(
            plan["recovery_actions"][1]["external_findings"],
            ["/tmp/review-findings-pr3.X"],
        )
        self.assertEqual(
            plan["recovery_actions"][2]["unregistered_review_paths"],
            ["/tmp/rev-4.X"],
        )
        self.assertEqual(
            plan["ready_slots"][0]["required_before_dispatch"],
            ["cumulative_history_check", "merge_base_delta_check"],
        )

    def test_query_limit_suppresses_slots(self):
        topology = inventory.analyze_topology([_pr(1, "root")], limit=1)
        plan = inventory.plan_slots(
            topology,
            [],
            {"findings_files": []},
            {"review_process_slots": 10, "conservative_new_worktree_slots": 10},
        )
        self.assertEqual(plan["ready_slots"], [])
        self.assertIn("limit", plan["slot_suppression_reason"])
        scan_failed = inventory.plan_slots(
            inventory.analyze_topology([_pr(1, "root")], limit=100),
            [],
            {
                "findings_files": [],
                "unregistered_review_paths": [],
                "scan_error": "permission denied",
            },
            {"review_process_slots": 10, "conservative_new_worktree_slots": 10},
        )
        self.assertEqual(scan_failed["ready_slots"], [])
        self.assertIn("recovery scan failed", scan_failed["slot_suppression_reason"])


if __name__ == "__main__":
    unittest.main()
