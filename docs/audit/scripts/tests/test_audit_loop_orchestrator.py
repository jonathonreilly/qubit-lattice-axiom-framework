"""Panel-aware top-level audit-loop orchestration."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import orchestrate_audit_batch as batch
import orchestrate_audit_loop as audit_loop


class GeneratedProvenanceRecoveryTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.path = self.root / batch.LANE_CERTIFICATION_PATH
        self.path.parent.mkdir(parents=True)
        self.payload = {
            "schema": "lane_certification_v2",
            "repo_head": "a" * 40,
            "lanes": [
                {"lane": "test", "certified": False, "blocking": []}
            ],
        }
        self.path.write_text(
            json.dumps(self.payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        self.source = self.root / "docs" / "SOURCE.md"
        self.source.parent.mkdir(parents=True, exist_ok=True)
        self.source.write_text("source baseline\n", encoding="utf-8")
        self.ledger = (
            self.root / "docs" / "audit" / "data" / "ledger" / "ro" / "row.json"
        )
        self.ledger.parent.mkdir(parents=True)
        self.ledger.write_text(
            '{"audit_status":"unaudited"}\n',
            encoding="utf-8",
        )
        self._git("init", "-q", "-b", "main")
        self._git("config", "user.email", "audit-test@example.invalid")
        self._git("config", "user.name", "Audit Test")
        self._git("config", "core.filemode", "true")
        self._git("add", ".")
        self._git("commit", "-q", "-m", "baseline")

    def _git(self, *args: str) -> str:
        return subprocess.run(
            ["git", *args],
            cwd=self.root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    def _git_bytes(self, *args: str) -> bytes:
        return subprocess.run(
            ["git", *args],
            cwd=self.root,
            check=True,
            capture_output=True,
        ).stdout

    def _write(self, payload: dict) -> None:
        self.path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def _refresh(self) -> dict:
        refreshed = dict(self.payload, repo_head=self._git("rev-parse", "HEAD"))
        self._write(refreshed)
        return refreshed

    def _clean_main_error(self) -> str | None:
        with mock.patch.object(batch, "REPO_ROOT", self.root):
            return batch.clean_main_error()

    def test_clean_main_recovers_current_head_only_refresh(self):
        self._refresh()
        before = self.path.read_bytes()
        error = self._clean_main_error()

        self.assertIsNone(error)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(
            self._git("status", "--porcelain"),
            f"M {batch.LANE_CERTIFICATION_PATH}",
        )

    def test_clean_main_recognizes_refresh_from_ancestor_head(self):
        self._refresh()
        before = self.path.read_bytes()
        self.source.write_text("later source commit\n", encoding="utf-8")
        self._git("add", str(self.source.relative_to(self.root)))
        self._git("commit", "-q", "-m", "move head")

        error = self._clean_main_error()

        self.assertIsNone(error)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(
            self._git("status", "--porcelain"),
            f"M {batch.LANE_CERTIFICATION_PATH}",
        )

    def test_sync_origin_main_fast_forwards_with_recognized_drift(self):
        with tempfile.TemporaryDirectory() as transport:
            transport_root = Path(transport)
            remote = transport_root / "remote.git"
            other = transport_root / "other"
            subprocess.run(
                ["git", "init", "-q", "--bare", "-b", "main", str(remote)],
                check=True,
            )
            self._git("remote", "add", "origin", str(remote))
            self._git("push", "-q", "-u", "origin", "main")
            self._refresh()
            before = self.path.read_bytes()
            subprocess.run(
                ["git", "clone", "-q", str(remote), str(other)],
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.email", "peer@example.invalid"],
                cwd=other,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Peer"],
                cwd=other,
                check=True,
            )
            peer_source = other / "docs" / "SOURCE.md"
            peer_source.write_text("remote advance\n", encoding="utf-8")
            subprocess.run(
                ["git", "add", "docs/SOURCE.md"],
                cwd=other,
                check=True,
            )
            subprocess.run(
                ["git", "commit", "-q", "-m", "advance remote"],
                cwd=other,
                check=True,
            )
            subprocess.run(
                ["git", "push", "-q", "origin", "main"],
                cwd=other,
                check=True,
            )

            with mock.patch.object(batch, "REPO_ROOT", self.root):
                synced, detail = batch.sync_origin_main()
                clean_error = batch.clean_main_error()

            self.assertTrue(synced, detail)
            self.assertIsNone(clean_error)
            self.assertEqual(self.path.read_bytes(), before)
            self.assertEqual(self._git("rev-parse", "HEAD"), detail)

    def test_clean_main_recovers_obsolete_field_removal(self):
        refreshed = dict(self.payload)
        refreshed.pop("repo_head")
        self._write(refreshed)
        before = self.path.read_bytes()
        error = self._clean_main_error()

        self.assertIsNone(error)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(
            self._git("status", "--porcelain"),
            f"M {batch.LANE_CERTIFICATION_PATH}",
        )

    def test_clean_main_recovers_without_autocrlf_conversion(self):
        self._git("config", "core.autocrlf", "true")
        self._refresh()
        before = self.path.read_bytes()
        before_mode = stat.S_IMODE(self.path.stat().st_mode)

        error = self._clean_main_error()

        self.assertIsNone(error)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), before_mode)

    def test_clean_main_recovers_without_attribute_eol_conversion(self):
        attributes = self.root / ".gitattributes"
        attributes.write_text("*.json text eol=crlf\n", encoding="utf-8")
        self._git("add", ".gitattributes")
        self._git("commit", "-q", "--amend", "--no-edit")
        self._refresh()
        before = self.path.read_bytes()
        before_mode = stat.S_IMODE(self.path.stat().st_mode)

        error = self._clean_main_error()

        self.assertIsNone(error)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), before_mode)

    def test_clean_main_refuses_noncanonical_mode_bits_without_mutation(self):
        for mode in (0o444, 0o600, 0o664, 0o2644, 0o4644):
            with self.subTest(mode=oct(mode)):
                self.path.chmod(0o644)
                self._refresh()
                self.path.chmod(mode)
                before = self.path.read_bytes()

                error = self._clean_main_error()

                self.assertEqual(error, "working tree is not clean")
                self.assertEqual(self.path.read_bytes(), before)
                self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), mode)

    def test_clean_main_recognition_preserves_xattr(self):
        self._refresh()
        before_inode = self.path.stat().st_ino
        before_bytes = self.path.read_bytes()
        xattr_name = "user.audit-recovery-test"
        xattr_value = b"preserve-me"
        xattr_command: list[str] | None = None
        if hasattr(os, "setxattr"):
            os.setxattr(self.path, xattr_name, xattr_value)
        elif shutil.which("xattr"):
            xattr_command = ["xattr", "-w", xattr_name, xattr_value.decode()]
            subprocess.run(xattr_command + [str(self.path)], check=True)

        error = self._clean_main_error()

        self.assertIsNone(error)
        self.assertEqual(self.path.stat().st_ino, before_inode)
        self.assertEqual(self.path.read_bytes(), before_bytes)
        if hasattr(os, "getxattr"):
            self.assertEqual(os.getxattr(self.path, xattr_name), xattr_value)
        elif xattr_command is not None:
            value = subprocess.run(
                ["xattr", "-p", xattr_name, str(self.path)],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            self.assertEqual(value, xattr_value.decode())

    def test_clean_main_refuses_hardlink_without_mutation(self):
        self._refresh()
        before = self.path.read_bytes()
        outside = self.root.parent / f"{self.root.name}-certification-hardlink"
        outside.unlink(missing_ok=True)
        os.link(self.path, outside)
        self.addCleanup(outside.unlink, missing_ok=True)
        before_inode = self.path.stat().st_ino

        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.stat().st_ino, before_inode)
        self.assertEqual(outside.stat().st_ino, before_inode)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(outside.read_bytes(), before)

    @unittest.skipUnless(sys.platform == "darwin", "macOS ACL semantics")
    def test_clean_main_refuses_acl_denied_write_without_mutation(self):
        self._refresh()
        before = self.path.read_bytes()
        subprocess.run(
            ["chmod", "+a", "everyone deny write", str(self.path)],
            check=True,
        )
        try:
            error = self._clean_main_error()
        finally:
            subprocess.run(
                ["chmod", "-a#", "0", str(self.path)],
                check=True,
            )

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), 0o644)

    @unittest.skipUnless(
        hasattr(os, "chflags") and hasattr(stat, "UF_IMMUTABLE"),
        "immutable file flags unavailable",
    )
    def test_clean_main_refuses_immutable_flag_without_mutation(self):
        self._refresh()
        before = self.path.read_bytes()
        os.chflags(self.path, stat.UF_IMMUTABLE)
        try:
            error = self._clean_main_error()
        finally:
            os.chflags(self.path, 0)

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), 0o644)

    def test_clean_main_refuses_payload_drift(self):
        refreshed = dict(
            self.payload,
            repo_head=self._git("rev-parse", "HEAD"),
            lanes=[{"lane": "test", "blocking": ["science-row"]}],
        )
        self._write(refreshed)
        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(json.loads(self.path.read_text()), refreshed)

    def test_clean_main_refuses_staged_provenance_drift(self):
        refreshed = self._refresh()
        self._git("add", batch.LANE_CERTIFICATION_PATH)
        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(json.loads(self.path.read_text()), refreshed)

    def test_clean_main_refuses_type_confused_payload_drift(self):
        refreshed = self._refresh()
        refreshed["lanes"][0]["certified"] = 0
        self._write(refreshed)
        before = self.path.read_bytes()

        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.read_bytes(), before)

    def test_clean_main_refuses_duplicate_json_keys(self):
        refreshed = self._refresh()
        text = json.dumps(refreshed, indent=2, sort_keys=True) + "\n"
        duplicate = text.replace(
            '      "certified": false,\n',
            '      "certified": true,\n      "certified": false,\n',
        )
        self.path.write_text(duplicate, encoding="utf-8")

        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.read_text(encoding="utf-8"), duplicate)

    def test_clean_main_refuses_null_or_stale_repo_head(self):
        for value in (None, "b" * 40):
            with self.subTest(repo_head=value):
                refreshed = dict(self.payload, repo_head=value)
                self._write(refreshed)
                before = self.path.read_bytes()

                error = self._clean_main_error()

                self.assertEqual(error, "working tree is not clean")
                self.assertEqual(self.path.read_bytes(), before)
                self._git("restore", "--worktree", "--", batch.LANE_CERTIFICATION_PATH)

    def test_clean_main_refuses_malformed_or_non_utf8_payload(self):
        for content in (b"{not-json\n", b"\xff\xfe\x00not-utf8"):
            with self.subTest(content=content):
                self.path.write_bytes(content)

                error = self._clean_main_error()

                self.assertEqual(error, "working tree is not clean")
                self.assertEqual(self.path.read_bytes(), content)
                self._git("restore", "--worktree", "--", batch.LANE_CERTIFICATION_PATH)

    def test_clean_main_refuses_line_ending_drift(self):
        self._refresh()
        content = self.path.read_bytes().replace(b"\n", b"\r\n")
        self.path.write_bytes(content)

        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.read_bytes(), content)

    def test_clean_main_refuses_committed_crlf_normalization(self):
        committed = self.path.read_bytes().replace(b"\n", b"\r\n")
        self.path.write_bytes(committed)
        self._git("add", batch.LANE_CERTIFICATION_PATH)
        self._git("commit", "-q", "--amend", "--no-edit")
        refreshed = dict(self.payload, repo_head=self._git("rev-parse", "HEAD"))
        normalized = (
            json.dumps(refreshed, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8")
        self.path.write_bytes(normalized)

        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.read_bytes(), normalized)

    def test_clean_main_refuses_preexisting_mode_change(self):
        self._refresh()
        self.path.chmod(stat.S_IMODE(self.path.stat().st_mode) | stat.S_IXUSR)
        before_bytes = self.path.read_bytes()
        before_mode = stat.S_IMODE(self.path.stat().st_mode)

        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(self.path.read_bytes(), before_bytes)
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), before_mode)

    def test_clean_main_refuses_untracked_source_ledger_and_mixed_state(self):
        cases = ("untracked", "source", "ledger", "mixed")
        for case in cases:
            with self.subTest(case=case):
                self._refresh()
                scratch = self.root / "scratch.txt"
                if case in {"untracked", "mixed"}:
                    scratch.write_text("scratch\n", encoding="utf-8")
                if case in {"source", "mixed"}:
                    self.source.write_text("source user edit\n", encoding="utf-8")
                if case in {"ledger", "mixed"}:
                    self.ledger.write_text(
                        '{"audit_status":"audited_clean"}\n',
                        encoding="utf-8",
                    )
                snapshots = {
                    path: path.read_bytes()
                    for path in (self.path, self.source, self.ledger)
                }
                if scratch.exists():
                    snapshots[scratch] = scratch.read_bytes()

                error = self._clean_main_error()

                self.assertEqual(error, "working tree is not clean")
                for path, expected in snapshots.items():
                    self.assertEqual(path.read_bytes(), expected)
                self._git("restore", "--worktree", "--", ".")
                scratch.unlink(missing_ok=True)

    def test_clean_main_refuses_deleted_certification(self):
        self.path.unlink()

        error = self._clean_main_error()

        self.assertEqual(error, "working tree is not clean")
        self.assertFalse(self.path.exists())

    def test_concurrent_same_file_edit_survives_recognition(self):
        refreshed = self._refresh()
        raced = json.loads(json.dumps(refreshed))
        raced["lanes"][0]["blocking"] = ["concurrent-user-work"]
        raced_text = json.dumps(raced, indent=2, sort_keys=True) + "\n"
        original_sh = batch.sh
        injected = False
        status_calls = 0

        def racing_sh(cmd, timeout=120, *, honor_cancel=True, text=True):
            nonlocal injected, status_calls
            if cmd == ["git", "status", "--porcelain"]:
                status_calls += 1
            if status_calls == 2 and not injected:
                injected = True
                self.path.write_text(raced_text, encoding="utf-8")
            return original_sh(
                cmd,
                timeout=timeout,
                honor_cancel=honor_cancel,
                text=text,
            )

        with mock.patch.object(batch, "REPO_ROOT", self.root), mock.patch.object(
            batch,
            "sh",
            side_effect=racing_sh,
        ):
            error = batch.clean_main_error()

        self.assertTrue(injected)
        self.assertEqual(
            error,
            "working tree is not clean after provenance recognition",
        )
        after = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(
            after["lanes"][0]["blocking"],
            ["concurrent-user-work"],
        )
        self.assertFalse(
            self.path.with_suffix(self.path.suffix + ".orig").exists()
        )

    def test_concurrent_mode_change_survives_patch_capture(self):
        self._refresh()
        original_sh = batch.sh
        injected = False

        def racing_sh(cmd, timeout=120, *, honor_cancel=True, text=True):
            nonlocal injected
            if (
                cmd[:2] == ["git", "diff"]
                and "--binary" in cmd
                and not injected
            ):
                injected = True
                mode = stat.S_IMODE(self.path.stat().st_mode)
                self.path.chmod(mode | stat.S_IXUSR)
            return original_sh(
                cmd,
                timeout=timeout,
                honor_cancel=honor_cancel,
                text=text,
            )

        with mock.patch.object(batch, "REPO_ROOT", self.root), mock.patch.object(
            batch,
            "sh",
            side_effect=racing_sh,
        ):
            error = batch.clean_main_error()

        self.assertTrue(injected)
        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(
            stat.S_IMODE(self.path.stat().st_mode) & stat.S_IXUSR,
            stat.S_IXUSR,
        )
        self.assertEqual(
            json.loads(self.path.read_text(encoding="utf-8"))["repo_head"],
            self._git("rev-parse", "HEAD"),
        )

    def test_late_concurrent_mode_change_survives_recognition(self):
        for concurrent_mode in (0o600, 0o744):
            with self.subTest(concurrent_mode=oct(concurrent_mode)):
                self.path.chmod(0o644)
                self._refresh()
                before_bytes = self.path.read_bytes()
                original_sh = batch.sh
                injected = False
                status_calls = 0

                def racing_sh(cmd, timeout=120, *, honor_cancel=True, text=True):
                    nonlocal injected, status_calls
                    if cmd == ["git", "status", "--porcelain"]:
                        status_calls += 1
                    if status_calls == 2 and not injected:
                        injected = True
                        self.path.chmod(concurrent_mode)
                    return original_sh(
                        cmd,
                        timeout=timeout,
                        honor_cancel=honor_cancel,
                        text=text,
                    )

                with mock.patch.object(
                    batch,
                    "REPO_ROOT",
                    self.root,
                ), mock.patch.object(
                    batch,
                    "sh",
                    side_effect=racing_sh,
                ):
                    error = batch.clean_main_error()

                self.assertTrue(injected)
                self.assertEqual(
                    error,
                    "working tree is not clean after provenance recognition",
                )
                self.assertEqual(self.path.read_bytes(), before_bytes)
                self.assertEqual(
                    stat.S_IMODE(self.path.stat().st_mode),
                    concurrent_mode,
                )

    def test_late_neighbor_file_is_preserved_and_no_backup_is_created(self):
        self._refresh()
        neighbor = self.path.with_suffix(self.path.suffix + ".orig")
        user_bytes = b"concurrent user backup\n"
        original_sh = batch.sh
        injected = False
        summary_calls = 0

        def racing_sh(cmd, timeout=120, *, honor_cancel=True, text=True):
            nonlocal injected, summary_calls
            if cmd[:2] == ["git", "diff"] and "--summary" in cmd:
                summary_calls += 1
            if summary_calls == 2 and not injected:
                injected = True
                neighbor.write_bytes(user_bytes)
            return original_sh(
                cmd,
                timeout=timeout,
                honor_cancel=honor_cancel,
                text=text,
            )

        with mock.patch.object(batch, "REPO_ROOT", self.root), mock.patch.object(
            batch,
            "sh",
            side_effect=racing_sh,
        ):
            error = batch.clean_main_error()

        self.assertTrue(injected)
        self.assertEqual(
            error,
            "working tree is not clean after provenance recognition",
        )
        self.assertEqual(neighbor.read_bytes(), user_bytes)
        self.assertEqual(
            json.loads(self.path.read_text(encoding="utf-8"))["repo_head"],
            self._git("rev-parse", "HEAD"),
        )

    def test_late_path_replacement_preserves_both_files(self):
        self._refresh()
        before = self.path.read_bytes()
        moved = self.path.with_suffix(self.path.suffix + ".moved")
        user_bytes = b"concurrent replacement\n"
        original_sh = batch.sh
        injected = False
        summary_calls = 0

        def racing_sh(cmd, timeout=120, *, honor_cancel=True, text=True):
            nonlocal injected, summary_calls
            if cmd[:2] == ["git", "diff"] and "--summary" in cmd:
                summary_calls += 1
            if summary_calls == 2 and not injected:
                injected = True
                self.path.replace(moved)
                self.path.write_bytes(user_bytes)
            return original_sh(
                cmd,
                timeout=timeout,
                honor_cancel=honor_cancel,
                text=text,
            )

        with mock.patch.object(batch, "REPO_ROOT", self.root), mock.patch.object(
            batch,
            "sh",
            side_effect=racing_sh,
        ):
            error = batch.clean_main_error()

        self.assertTrue(injected)
        self.assertEqual(error, "working tree is not clean")
        self.assertEqual(moved.read_bytes(), before)
        self.assertEqual(self.path.read_bytes(), user_bytes)


def _args() -> argparse.Namespace:
    return argparse.Namespace(
        lane=None,
        max_workers=4,
        max_passes=0,
        max_lane_cycles=0,
        batch_rounds=6,
        stall_minutes=45,
        runner_timeout_sec=120,
        codex_timeout_sec=2700,
        push_retries=3,
        dispatch_science_fixes=False,
        skip_forensic_canary=True,
        dry_run=False,
    )


class BatchExitSemanticsTest(unittest.TestCase):
    def test_judicial_handoff_is_resumable(self):
        report = [{"cid": "row", "result": "judicial_panel_required"}]
        self.assertFalse(batch.report_has_hard_blocker(report))

    def test_validation_failure_remains_hard(self):
        report = [{"cid": "row", "result": "validation_failed"}]
        self.assertTrue(batch.report_has_hard_blocker(report))

    def test_campaign_quarantine_makes_only_its_schema_failures_resumable(self):
        report = [
            {"cid": "quarantined", "result": "validation_failed"},
            {"cid": "quarantined", "result": "schema_invalid_quarantined"},
        ]
        self.assertFalse(batch.report_has_hard_blocker(report))

        report.append({"cid": "other", "result": "validation_failed"})
        self.assertTrue(batch.report_has_hard_blocker(report))

    def test_banked_clean_seat_defers_only_the_invalid_peer(self):
        report = [
            {"cid": "row", "result": "validation_failed"},
            {"cid": "row", "result": "critical_peer_pending"},
            {"cid": "row", "result": "schema_invalid_peer_deferred"},
            {"cid": "row", "result": "audited_clean"},
        ]
        self.assertFalse(batch.report_has_hard_blocker(report))

    def test_science_fix_dispatch_is_a_sidecar_not_an_audit_blocker(self):
        for result in ("science_fix_dispatched", "science_fix_dispatch_failed"):
            with self.subTest(result=result):
                self.assertFalse(
                    batch.report_has_hard_blocker(
                        [{"cid": "repairable", "result": result}]
                    )
                )

    def test_verified_claim_transaction_quarantine_is_resumable(self):
        report = [
            {"cid": "row", "result": "apply_or_gate_failed", "detail": "boom"},
            {
                "cid": "row",
                "result": batch.CLAIM_TRANSACTION_QUARANTINE_RESULT,
            },
        ]
        self.assertFalse(batch.report_has_hard_blocker(report))

    def test_mixed_failure_records_the_judicial_handoff(self):
        report = [{"cid": "broken", "result": "validation_failed"}]
        selected = [{"claim_id": "disputed"}]
        current = {
            "disputed": {"cross_confirmation": {"status": "disagreement"}}
        }

        disagreements = batch.append_judicial_handoffs(selected, current, report)

        self.assertEqual(disagreements, ["disputed"])
        self.assertIn(
            {"cid": "disputed", "result": "judicial_panel_required"}, report
        )
        self.assertTrue(batch.report_has_hard_blocker(report))


class SchemaRecoveryTest(unittest.TestCase):
    def test_known_n8_failure_gets_exact_mechanism_repair_guidance(self):
        blob = {
            "no_go_discipline": {
                "N8_cross_cycle_echo": {
                    "echoes": [
                        {
                            "mechanism": "projector-kernel obstruction",
                            "disposition": "paraphrased obstruction",
                        }
                    ]
                }
            }
        }

        guidance = batch.schema_repair_guidance(
            blob,
            "N8 echo 1.disposition must name its indexed mechanism",
        )

        self.assertIn('"projector-kernel obstruction"', guidance)
        self.assertIn("copy the exact mechanism string", guidance)

    def test_campaign_quarantine_persists_exact_failures_once(self):
        report = [
            {
                "cid": "row",
                "pass": 1,
                "result": "validation_failed",
                "detail": "N8 exact validator error",
            }
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quarantine.jsonl"
            batch.persist_campaign_quarantine(path, {"row"}, report)
            batch.persist_campaign_quarantine(path, {"row"}, report)

            records = [json.loads(line) for line in path.read_text().splitlines()]

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["claim_id"], "row")
        self.assertEqual(records[0]["failures"][0]["detail"], "N8 exact validator error")

    def test_compute_and_transaction_exclusions_persist_typed_causes(self):
        report = [
            {
                "cid": "compute",
                "pass": 1,
                "result": "compute_required",
                "detail": "cache missing",
            },
            {
                "cid": "transaction",
                "result": "apply_or_gate_failed",
                "detail": "pipeline failed",
                "rollback_verified": True,
                "rollback_detail": "reset to origin/main",
            },
            {
                "cid": "transaction",
                "result": batch.CLAIM_TRANSACTION_QUARANTINE_RESULT,
                "detail": "claim excluded after verified rollback",
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quarantine.jsonl"
            batch.persist_compute_required_skips(path, {"compute"}, report)
            batch.persist_claim_transaction_quarantines(
                path, {"transaction"}, report
            )
            records = batch.load_campaign_exclusion_records(path)

        self.assertEqual(
            {row["reason"] for row in records},
            {
                batch.COMPUTE_QUARANTINE_RESULT,
                batch.CLAIM_TRANSACTION_QUARANTINE_RESULT,
            },
        )
        by_claim = {row["claim_id"]: row for row in records}
        self.assertEqual(
            by_claim["compute"]["failures"][0]["detail"], "cache missing"
        )
        self.assertEqual(
            by_claim["transaction"]["failures"][0]["detail"],
            "pipeline failed",
        )

    def test_mixed_seat_causes_persist_both_typed_reasons(self):
        report = [
            {
                "cid": "mixed",
                "pass": 1,
                "result": "compute_required",
                "detail": "cache missing",
            },
            {
                "cid": "mixed",
                "pass": 2,
                "result": "validation_failed",
                "detail": "bad schema",
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quarantine.jsonl"
            batch.persist_campaign_quarantine(path, {"mixed"}, report)
            batch.persist_compute_required_skips(path, {"mixed"}, report)
            batch.persist_campaign_quarantine(path, {"mixed"}, report)
            records = batch.load_campaign_exclusion_records(path)

        self.assertEqual(
            {(row["claim_id"], row["reason"]) for row in records},
            {
                ("mixed", batch.SCHEMA_QUARANTINE_RESULT),
                ("mixed", batch.COMPUTE_QUARANTINE_RESULT),
            },
        )
        self.assertEqual(len(records), 2)

    def test_campaign_state_loader_rejects_truncated_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quarantine.jsonl"
            path.write_text(
                json.dumps(
                    {
                        "claim_id": "kept",
                        "reason": batch.SCHEMA_QUARANTINE_RESULT,
                        "failures": [{
                            "cid": "kept",
                            "pass": 1,
                            "result": "validation_failed",
                            "detail": "bad schema",
                        }],
                        "recorded_at": "2026-07-23T12:00:00+00:00",
                    }
                )
                + "\n"
                + '{"claim_id":"torn"',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                ValueError,
                "invalid campaign exclusion JSON",
            ):
                batch.load_campaign_quarantine(path)
            with mock.patch.dict(
                audit_loop.PROGRESS,
                {"quarantine_file": path},
            ):
                with self.assertRaisesRegex(
                    ValueError,
                    "invalid campaign exclusion JSON",
                ):
                    audit_loop.campaign_exclusion_counts()

    def test_campaign_state_loader_rejects_corrupt_schema_variants(self):
        valid_tail = (
            '"reason":"schema_invalid_quarantined",'
            '"failures":[{"result":"validation_failed"}],'
            '"recorded_at":"2026-07-23T12:00:00+00:00"'
        )
        cases = {
            "blank": ("\n", "blank campaign exclusion record"),
            "duplicate": (
                '{"claim_id":"first","claim_id":"second",' + valid_tail + "}\n",
                "duplicate JSON key",
            ),
            "unknown reason": (
                '{"claim_id":"row","reason":"unknown_quarantine",'
                '"failures":[{"result":"validation_failed"}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "unrecognized campaign exclusion reason",
            ),
            "invalid fields": (
                '{"claim_id":"row",' + valid_tail + ',"typo":[]}\n',
                "invalid campaign exclusion fields",
            ),
            "invalid failures": (
                '{"claim_id":"row","reason":"schema_invalid_quarantined",'
                '"failures":[],"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "failures must be a non-empty list",
            ),
            "empty failure object": (
                '{"claim_id":"row","reason":"schema_invalid_quarantined",'
                '"failures":[{}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "failure has no string result",
            ),
            "unexpected failure field": (
                '{"claim_id":"row","reason":"schema_invalid_quarantined",'
                '"failures":[{"cid":"row","pass":1,'
                '"result":"malformed_json","typo":true}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "invalid campaign exclusion failure fields",
            ),
            "wrong reason evidence": (
                '{"claim_id":"row","reason":"compute_required_quarantined",'
                '"failures":[{"cid":"row","pass":1,'
                '"result":"validation_failed","detail":"bad schema"}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "failure result is incompatible",
            ),
            "transaction without rollback proof": (
                '{"claim_id":"row","reason":"claim_transaction_quarantined",'
                '"failures":[{"cid":"row",'
                '"result":"claim_transaction_quarantined",'
                '"detail":"quarantined"}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "no verified apply/gate rollback failure",
            ),
            "failure cid mismatch": (
                '{"claim_id":"row","reason":"compute_required_quarantined",'
                '"failures":[{"cid":"other","pass":1,'
                '"result":"compute_required","detail":"cache missing"}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "failure cid does not match",
            ),
            "shard unsafe claim id": (
                '{"claim_id":"bad/id","reason":"compute_required_quarantined",'
                '"failures":[{"cid":"bad/id","pass":1,'
                '"result":"compute_required","detail":"cache missing"}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "claim_id is not shard-safe",
            ),
            "dot-only claim id": (
                '{"claim_id":".","reason":"compute_required_quarantined",'
                '"failures":[{"cid":".","pass":1,'
                '"result":"compute_required","detail":"cache missing"}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "claim_id is not shard-safe",
            ),
            "overflow float": (
                '{"claim_id":"row","reason":"compute_required_quarantined",'
                '"failures":[{"cid":"row","pass":1,'
                '"result":"compute_required","detail":1e999}],'
                '"recorded_at":"2026-07-23T12:00:00+00:00"}\n',
                "non-finite JSON number",
            ),
            "noncanonical timestamp separator": (
                '{"claim_id":"row","reason":"compute_required_quarantined",'
                '"failures":[{"cid":"row","pass":1,'
                '"result":"compute_required","detail":"cache missing"}],'
                '"recorded_at":"2026-07-23x12:00:00+00:00"}\n',
                "not canonical UTC ISO-8601",
            ),
        }
        for label, (payload, expected) in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "quarantine.jsonl"
                path.write_text(payload, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, expected):
                    batch.load_campaign_quarantine(path)

    def test_campaign_state_loader_accepts_canonical_dotted_claim_id(self):
        record = {
            "claim_id": "ai_methodology.raw.canonical_framing_paragraph",
            "reason": batch.COMPUTE_QUARANTINE_RESULT,
            "failures": [{
                "cid": "ai_methodology.raw.canonical_framing_paragraph",
                "pass": 1,
                "result": "compute_required",
                "detail": "cache missing",
            }],
            "recorded_at": "2026-07-23T12:00:00+00:00",
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quarantine.jsonl"
            path.write_text(json.dumps(record) + "\n", encoding="utf-8")
            loaded = batch.load_campaign_exclusion_records(path)

        self.assertEqual(loaded, [record])

    def test_apply_gate_failure_continues_after_explicit_verified_rollback(self):
        job = {
            "cid": "row",
            "pass": 1,
            "row": {
                "claim_id": "row",
                "criticality": "medium",
                "note_path": "docs/row.md",
            },
        }
        envelope = {"audit": {"verdict": "audited_clean"}}
        report = []
        with mock.patch.object(
            batch, "finalize_worker", return_value=(envelope, {"ok": True})
        ), mock.patch.object(
            batch,
            "apply_claim_serialized",
            return_value=(
                False,
                [{
                    "cid": "row",
                    "result": "apply_or_gate_failed",
                    "detail": "pipeline failed",
                    "rollback_verified": True,
                }],
            ),
        ):
            ok, compute, schema, handoffs = batch.apply_serialized(
                [job], report
            )

        self.assertTrue(ok)
        self.assertEqual(compute, set())
        self.assertEqual(schema, set())
        self.assertEqual(handoffs, [])
        self.assertIn(
            batch.CLAIM_TRANSACTION_QUARANTINE_RESULT,
            {item["result"] for item in report},
        )

    def test_apply_gate_failure_stops_without_explicit_rollback_proof(self):
        job = {
            "cid": "row",
            "pass": 1,
            "row": {
                "claim_id": "row",
                "criticality": "medium",
                "note_path": "docs/row.md",
            },
        }
        report = []
        with mock.patch.object(
            batch,
            "finalize_worker",
            return_value=(
                {"audit": {"verdict": "audited_clean"}},
                {"ok": True},
            ),
        ), mock.patch.object(
            batch,
            "apply_claim_serialized",
            return_value=(
                False,
                [{"cid": "row", "result": "apply_or_gate_failed"}],
            ),
        ):
            ok, _, _, _ = batch.apply_serialized([job], report)

        self.assertFalse(ok)
        self.assertNotIn(
            batch.CLAIM_TRANSACTION_QUARANTINE_RESULT,
            {item["result"] for item in report},
        )

    def test_invalid_optional_packet_is_dropped_without_completion(self):
        invocation = "a" * 32
        blob = {
            "claim_id": "row",
            "audit_invocation_id": invocation,
            "load_bearing_step": "The bounded implication follows.",
            "load_bearing_step_class": "B",
            "claim_type": "bounded_theorem",
            "claim_scope": "The bounded implication.",
            "chain_closes": False,
            "chain_closure_explanation": "A named wall remains.",
            "verdict": "audited_conditional",
            "verdict_rationale": "The named wall remains open.",
            "negative_assertion_classes": ["bounded_with_named_walls"],
            "notes_for_re_audit_if_any": "scope_too_broad: narrow the claim.",
            "no_go_discipline": {"required": True, "status": "FAIL"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw.json"
            raw.write_text(json.dumps(blob), encoding="utf-8")
            job = {
                "cid": "row",
                "pass": 1,
                "stalled": False,
                "returncode": 0,
                "raw_output": raw,
                "row": {
                    "claim_id": "row",
                    "note_path": "",
                    "claim_type": "bounded_theorem",
                },
                "evidence_manifest": {},
                "invocation_id": invocation,
                "transport_bound": None,
                "auditor": "test-auditor",
                "independence": "cross_family",
                "delivery": root / "delivery.json",
                "workdir": root,
                "isolated": root,
            }
            with mock.patch.object(batch, "packet_completion_pass") as completion:
                envelope, result = batch.finalize_worker(job)

        completion.assert_not_called()
        self.assertIsNone(envelope["audit"]["no_go_discipline"])
        self.assertEqual(
            envelope["audit"]["negative_assertion_classes"],
            ["bounded_with_named_walls"],
        )
        self.assertIn("optional", result["detail"])

    def test_invalid_optional_packet_is_not_dropped_from_clean(self):
        invocation = "b" * 32
        blob = {
            "claim_id": "row",
            "audit_invocation_id": invocation,
            "load_bearing_step": "The exact identity follows.",
            "load_bearing_step_class": "B",
            "claim_type": "bounded_theorem",
            "claim_scope": "The exact identity.",
            "chain_closes": True,
            "chain_closure_explanation": "The calculation closes.",
            "verdict": "audited_clean",
            "verdict_rationale": "The bounded calculation is complete.",
            "negative_assertion_classes": [],
            "notes_for_re_audit_if_any": None,
            "no_go_discipline": {"required": True, "status": "PASS"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw.json"
            raw.write_text(json.dumps(blob), encoding="utf-8")
            job = {
                "cid": "row",
                "pass": 1,
                "stalled": False,
                "returncode": 0,
                "raw_output": raw,
                "row": {
                    "claim_id": "row",
                    "note_path": "",
                    "claim_type": "bounded_theorem",
                },
                "evidence_manifest": {},
                "invocation_id": invocation,
                "transport_bound": None,
                "auditor": "test-auditor",
                "independence": "cross_family",
                "delivery": root / "delivery.json",
                "workdir": root,
                "isolated": root,
            }
            with mock.patch.object(
                batch, "packet_completion_pass", return_value=None
            ) as completion:
                envelope, result = batch.finalize_worker(job)

        completion.assert_called_once()
        self.assertIsNone(envelope)
        self.assertEqual(result["result"], "validation_failed")
        self.assertIn("N1_alternative_routes", result["detail"])

    def test_terminal_verdict_cannot_mix_compute_required(self):
        invocation = "c" * 32
        blob = {
            "claim_id": "row",
            "audit_invocation_id": invocation,
            "load_bearing_step": "The exact identity follows.",
            "load_bearing_step_class": "B",
            "claim_type": "bounded_theorem",
            "claim_scope": "The exact identity.",
            "chain_closes": True,
            "chain_closure_explanation": "The calculation closes.",
            "verdict": "audited_clean",
            "verdict_rationale": "The bounded calculation is complete.",
            "negative_assertion_classes": [],
            "notes_for_re_audit_if_any": None,
            "no_go_discipline": None,
            "compute_required": "run the cached certificate",
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "raw.json"
            raw.write_text(json.dumps(blob), encoding="utf-8")
            job = {
                "cid": "row",
                "pass": 1,
                "stalled": False,
                "returncode": 0,
                "raw_output": raw,
                "row": {
                    "claim_id": "row",
                    "note_path": "",
                    "claim_type": "bounded_theorem",
                },
                "evidence_manifest": {},
                "invocation_id": invocation,
                "transport_bound": None,
                "auditor": "test-auditor",
                "independence": "cross_family",
                "delivery": root / "delivery.json",
                "workdir": root,
                "isolated": root,
            }
            with mock.patch.object(batch, "packet_completion_pass") as completion:
                envelope, result = batch.finalize_worker(job)

        completion.assert_not_called()
        self.assertIsNone(envelope)
        self.assertEqual(result["result"], "validation_failed")
        self.assertIn("compute_required cannot accompany", result["detail"])

    def test_dep_ready_post_verdict_reset_is_persisted_across_batches(self):
        selected = [{"claim_id": "row"}]
        current = {
            "row": {
                "claim_id": "row",
                "audit_status": "unaudited",
                "previous_audits": [
                    {"invalidation_reason": "no_go_discipline_packet_missing"}
                ],
            }
        }
        report = [
            {
                "cid": "row",
                "result": "audited_conditional",
                "commit": "deadbeef",
            }
        ]
        with mock.patch.object(batch, "compute_targets", return_value=([current["row"]], [])):
            reentries = batch.blocked_row_reentries(selected, current, report)

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "campaign-row-exclusions.jsonl"
            batch.persist_blocked_row_reentries(path, reentries)
            batch.persist_blocked_row_reentries(path, reentries)
            records = [json.loads(line) for line in path.read_text().splitlines()]
            loaded = batch.load_campaign_quarantine(path)

        self.assertEqual(
            reentries, {"row": "no_go_discipline_packet_missing"}
        )
        self.assertEqual(loaded, {"row"})
        self.assertEqual(len(records), 1)
        self.assertEqual(
            records[0]["reason"], batch.BLOCKED_ROW_QUARANTINE_RESULT
        )
        self.assertEqual(
            report[-1]["result"], batch.BLOCKED_ROW_QUARANTINE_RESULT
        )

    def test_banked_clean_seat_remains_eligible_for_second_pass(self):
        selected = [{"claim_id": "row"}]
        current = {
            "row": {
                "claim_id": "row",
                "audit_status": "audit_in_progress",
                "cross_confirmation": {"status": "awaiting_second"},
            }
        }
        report = [
            {"cid": "row", "result": "audited_clean", "commit": "deadbeef"}
        ]
        with mock.patch.object(batch, "compute_targets") as compute_targets:
            reentries = batch.blocked_row_reentries(selected, current, report)

        self.assertEqual(reentries, {})
        compute_targets.assert_not_called()

    def test_two_batches_exclude_reset_row_and_continue_other_seats(self):
        def row(
            cid: str,
            *,
            audit_status: str = "unaudited",
            criticality: str | None = None,
            cross_status: str | None = None,
            previous_audits: list[dict] | None = None,
            effective_status: str = "ready_for_audit",
        ) -> dict:
            return {
                "claim_id": cid,
                "note_path": f"docs/nonexistent-{cid}.md",
                "claim_type": "positive_theorem",
                "criticality": criticality,
                "audit_status": audit_status,
                "effective_status": effective_status,
                "cross_confirmation": (
                    {"status": cross_status} if cross_status else None
                ),
                "deps": [],
                "previous_audits": previous_audits or [],
            }

        blocked_before = row("blocked")
        other_before = row("other")
        second_before = row(
            "second",
            audit_status="audit_in_progress",
            criticality="critical",
            cross_status="awaiting_second",
        )
        first_rows = {
            item["claim_id"]: item
            for item in (blocked_before, other_before, second_before)
        }
        blocked_after = row(
            "blocked",
            previous_audits=[
                {
                    "audit_status": "audited_conditional",
                    "invalidation_reason": "no_go_discipline_packet_missing",
                }
            ],
        )
        first_after = dict(first_rows, blocked=blocked_after)
        second_after = {
            "blocked": blocked_after,
            "other": row(
                "other",
                audit_status="audited_clean",
                effective_status="retained",
            ),
            "second": row(
                "second",
                audit_status="audited_clean",
                criticality="critical",
                effective_status="retained",
            ),
        }
        launched_by_batch: list[list[tuple[str, int]]] = []

        def run_batch(
            workdir: Path,
            exclusion_file: Path,
            before: dict[str, dict],
            after: dict[str, dict],
            max_workers: int,
        ) -> int:
            launched: list[tuple[str, int]] = []
            launched_by_batch.append(launched)

            def launch_worker(selected, _rows, pass_no, *_args):
                launched.append((selected["claim_id"], pass_no))
                return {
                    "cid": selected["claim_id"],
                    "pass": pass_no,
                    "row": selected,
                }

            def apply_serialized(jobs, report, _retries):
                for job in jobs:
                    report.append(
                        {
                            "cid": job["cid"],
                            "pass": job["pass"],
                            "result": "audited_conditional",
                            "commit": f"commit-{job['cid']}",
                        }
                    )
                return True, set(), set(), []

            argv = [
                "orchestrate_audit_batch.py",
                "--claims",
                "blocked,other,second",
                "--max-workers",
                str(max_workers),
                "--rounds",
                "1",
                "--campaign-quarantine-file",
                str(exclusion_file),
            ]
            lock = mock.Mock()
            with mock.patch.object(sys, "argv", argv), mock.patch.dict(
                os.environ,
                {"AUDIT_BATCH_WORKDIR": str(workdir)},
            ), mock.patch.object(
                batch, "acquire_exclusive_drain_lock", return_value=lock
            ), mock.patch.object(
                batch, "clean_main_error", return_value=None
            ), mock.patch.object(
                batch, "load_rows", side_effect=[before, after]
            ), mock.patch.object(
                batch, "source_requires_forensic", return_value=False
            ), mock.patch.object(
                batch, "launch_worker", side_effect=launch_worker
            ), mock.patch.object(
                batch, "wait_workers"
            ), mock.patch.object(
                batch, "start_progress_ticker"
            ), mock.patch.object(
                batch, "maybe_progress_summary"
            ), mock.patch.object(
                batch, "apply_serialized", side_effect=apply_serialized
            ):
                result = batch.main()
            lock.close.assert_called_once_with()
            return result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            exclusion_file = root / "campaign-row-exclusions.jsonl"
            first_rc = run_batch(
                root / "batch-1",
                exclusion_file,
                first_rows,
                first_after,
                max_workers=1,
            )
            records_after_first = [
                json.loads(line)
                for line in exclusion_file.read_text(encoding="utf-8").splitlines()
            ]
            second_rc = run_batch(
                root / "batch-2",
                exclusion_file,
                first_after,
                second_after,
                max_workers=2,
            )

        self.assertEqual((first_rc, second_rc), (0, 0))
        self.assertEqual(launched_by_batch[0], [("blocked", 1)])
        self.assertNotIn(("blocked", 1), launched_by_batch[1])
        self.assertEqual(
            launched_by_batch[1],
            [("other", 1), ("second", 2)],
        )
        self.assertEqual(len(records_after_first), 1)
        self.assertEqual(records_after_first[0]["claim_id"], "blocked")
        self.assertEqual(
            records_after_first[0]["invalidation_reason"],
            "no_go_discipline_packet_missing",
        )

    def test_science_handoff_requires_valid_actionable_verdict(self):
        job = {
            "cid": "row",
            "row": {
                "note_path": "docs/ROW.md",
                "claim_type": "bounded_theorem",
                "transitive_descendants": 7,
            },
        }
        clean = {"audit": {"verdict": "audited_clean"}}
        actionable = {
            "audit": {
                "verdict": "audited_conditional",
                "claim_type": "bounded_theorem",
                "claim_scope": "The asserted bound under stated inputs.",
                "load_bearing_step_class": "B",
                "notes_for_re_audit_if_any": (
                    "missing_bridge_theorem — prove the missing implication"
                ),
                "verdict_rationale": "The implication is only asserted.",
                "load_bearing_step": "Therefore the bound follows.",
                "audit_invocation_id": "a" * 32,
            }
        }

        self.assertIsNone(batch.science_fix_handoff(job, clean))
        handoff = batch.science_fix_handoff(job, actionable)
        self.assertIsNotNone(handoff)
        self.assertEqual(
            handoff["category"],
            "conditional_missing_bridge_theorem",
        )
        self.assertIn("prove the missing implication", handoff["repair_target"])
        self.assertNotIn("prompt_body", handoff)

        for verdict in (
            "audited_failed",
            "audited_renaming",
            "audited_numerical_match",
        ):
            incomplete = {"audit": dict(actionable["audit"], verdict=verdict)}
            incomplete["audit"]["verdict_rationale"] = ""
            with self.subTest(verdict=verdict):
                self.assertIsNone(batch.science_fix_handoff(job, incomplete))

    def test_batch_emits_handoff_only_after_validated_verdict_applies(self):
        job = {
            "cid": "row",
            "pass": 1,
            "row": {
                "claim_id": "row",
                "note_path": "docs/ROW.md",
                "claim_type": "bounded_theorem",
                "criticality": None,
            },
        }
        envelope = {
            "audit": {
                "verdict": "audited_failed",
                "claim_type": "bounded_theorem",
                "claim_scope": "The central equality in this note.",
                "verdict_rationale": "The central equality is contradicted.",
                "load_bearing_step": "The claimed equality holds.",
                "load_bearing_step_class": "B",
                "notes_for_re_audit_if_any": "Replace the false equality.",
                "audit_invocation_id": "c" * 32,
            }
        }
        with mock.patch.object(
            batch,
            "finalize_worker",
            return_value=(envelope, {"result": "delivery_validated"}),
        ), mock.patch.object(
            batch,
            "apply_claim_serialized",
            return_value=(True, [{"cid": "row", "result": "audited_failed"}]),
        ):
            ok, _, quarantines, handoffs = batch.apply_serialized([job], [])

        self.assertTrue(ok)
        self.assertEqual(quarantines, set())
        self.assertEqual([row["claim_id"] for row in handoffs], ["row"])

    def test_banked_clean_seat_does_not_quarantine_whole_claim(self):
        row = {
            "claim_id": "row",
            "note_path": "docs/ROW.md",
            "claim_type": "bounded_theorem",
            "criticality": "critical",
            "audit_status": "unaudited",
            "cross_confirmation": None,
        }
        jobs = [
            {"cid": "row", "pass": 1, "row": row},
            {"cid": "row", "pass": 2, "row": row},
        ]

        def finalize(job):
            if job["pass"] == 1:
                return {"audit": {"verdict": "audited_clean"}}, {"ok": True}
            return None, {
                "cid": "row",
                "pass": 2,
                "result": "validation_failed",
                "detail": "N8 exact validator error",
            }

        report = []
        with mock.patch.object(batch, "finalize_worker", side_effect=finalize), \
                mock.patch.object(
                    batch,
                    "apply_claim_serialized",
                    return_value=(True, [{"cid": "row", "result": "audited_clean"}]),
                ):
            ok, _, quarantines, _ = batch.apply_serialized(jobs, report)

        self.assertTrue(ok)
        self.assertEqual(quarantines, set())
        self.assertIn(
            "schema_invalid_peer_deferred",
            {item["result"] for item in report},
        )

    def test_dispatch_serializes_one_handoff_and_starts_detached_worker(self):
        handoff = {
            "claim_id": "row",
            "category": "failed",
            "note_path": "docs/ROW.md",
            "descendants": 0,
            "cls": "(B)",
            "audit_invocation_id": "d" * 32,
            "audit_verdict": "audited_failed",
            "claim_type": "bounded_theorem",
            "claim_scope": "The central equality.",
            "verdict_rationale": "The equality is contradicted.",
            "load_bearing_step": "The claimed equality holds.",
            "repair_target": "Replace the false equality.",
        }
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(
            batch.subprocess,
            "Popen",
            return_value=mock.Mock(pid=1234),
        ) as popen:
            launched = batch.launch_science_fix_worker([handoff], Path(tmp))
            payload = json.loads(launched[1].read_text(encoding="utf-8"))

        self.assertEqual(launched[0], 1234)
        self.assertEqual(payload["schema"], "audit_science_fix_handoff_v1")
        self.assertEqual(payload["rows"][0]["claim_id"], "row")
        self.assertTrue(popen.call_args.kwargs["start_new_session"])
        self.assertIn("--retry-failed", popen.call_args.args[0])

    def test_missing_dependency_edge_is_dispatched(self):
        job = {
            "cid": "row",
            "row": {
                "note_path": "docs/ROW.md",
                "claim_type": "bounded_theorem",
                "transitive_descendants": 2,
            },
        }
        envelope = {
            "audit": {
                "verdict": "audited_conditional",
                "claim_type": "bounded_theorem",
                "claim_scope": "The bounded implication.",
                "load_bearing_step_class": "B",
                "notes_for_re_audit_if_any": (
                    "missing_dependency_edge: cite the retained authority"
                ),
                "verdict_rationale": "The cited authority is absent.",
                "load_bearing_step": "The implication follows from the authority.",
                "audit_invocation_id": "e" * 32,
            }
        }

        handoff = batch.science_fix_handoff(job, envelope)

        self.assertEqual(
            handoff["category"], "conditional_missing_dependency_edge"
        )


class ClaimTransactionTest(unittest.TestCase):
    def test_wait_workers_streams_complete_claim_before_slower_claim(self):
        class FakeProc:
            def __init__(self, polls):
                self.polls = iter(polls)
                self.returncode = None
                self.pid = 1234

            def poll(self):
                if self.returncode is None:
                    value = next(self.polls)
                    if value is not None:
                        self.returncode = value
                return self.returncode

            def wait(self):
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(cid, polls):
                log_path = root / f"{cid}.log"
                return {
                    "cid": cid,
                    "row": {"claim_id": cid},
                    "pass": 1,
                    "proc": FakeProc(polls),
                    "raw_output": root / f"{cid}.out",
                    "log_path": log_path,
                    "log_handle": log_path.open("w", encoding="utf-8"),
                    "last_size": 0,
                    "last_progress": time.monotonic(),
                    "stalled": False,
                }

            jobs = [job("ready", [0]), job("slow", [None, 0])]
            streamed = []
            with mock.patch.object(batch.time, "sleep", return_value=None):
                result = batch.wait_workers(
                    jobs,
                    stall_minutes=45,
                    on_claim_ready=lambda claim_jobs: (
                        streamed.append(claim_jobs[0]["cid"]) or True
                    ),
                )

        self.assertTrue(result)
        self.assertEqual(streamed, ["ready", "slow"])

    def test_wait_workers_holds_critical_claim_until_both_seats_exit(self):
        class FakeProc:
            def __init__(self, polls):
                self.polls = iter(polls)
                self.returncode = None
                self.pid = 1234

            def poll(self):
                if self.returncode is None:
                    value = next(self.polls)
                    if value is not None:
                        self.returncode = value
                return self.returncode

            def wait(self):
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(pass_no, polls):
                log_path = root / f"critical-{pass_no}.log"
                return {
                    "cid": "critical",
                    "row": {"claim_id": "critical", "criticality": "critical"},
                    "pass": pass_no,
                    "proc": FakeProc(polls),
                    "raw_output": root / f"critical-{pass_no}.out",
                    "log_path": log_path,
                    "log_handle": log_path.open("w", encoding="utf-8"),
                    "last_size": 0,
                    "last_progress": time.monotonic(),
                    "stalled": False,
                }

            jobs = [job(1, [0]), job(2, [None, 0])]
            streamed = []
            with mock.patch.object(batch.time, "sleep", return_value=None):
                result = batch.wait_workers(
                    jobs,
                    on_claim_ready=lambda claim_jobs: (
                        streamed.append(sorted(job["pass"] for job in claim_jobs))
                        or True
                    ),
                )

        self.assertTrue(result)
        self.assertEqual(streamed, [[1, 2]])

    def test_wait_workers_enforces_stall_during_long_callback(self):
        class FakeProc:
            next_pid = 2000

            def __init__(self, done=False):
                self.returncode = 0 if done else None
                self.pid = FakeProc.next_pid
                FakeProc.next_pid += 1

            def poll(self):
                return self.returncode

            def wait(self):
                if self.returncode is None:
                    self.returncode = -9
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(cid, done=False):
                log_path = root / f"{cid}.log"
                log_handle = log_path.open("w", encoding="utf-8")
                os.utime(log_path, (0.0, 0.0))
                return {
                    "cid": cid,
                    "row": {"claim_id": cid},
                    "pass": 1,
                    "proc": FakeProc(done),
                    "raw_output": root / f"{cid}.out",
                    "log_path": log_path,
                    "log_handle": log_handle,
                    "last_size": 0,
                    "last_activity": (0, 0.0),
                    "last_progress": 0.0,
                    "last_progress_wall": 0.0,
                    "stalled": False,
                }

            ready = job("ready", done=True)
            slow = job("slow")
            callback_started = threading.Event()
            release_callback = threading.Event()

            def callback(claim_jobs):
                if claim_jobs[0]["cid"] == "ready":
                    callback_started.set()
                    self.assertTrue(release_callback.wait(timeout=2))
                return True

            with mock.patch.object(
                batch.time, "time", side_effect=[0.0, 3600.0]
            ), mock.patch.object(
                batch.time,
                "sleep",
                side_effect=lambda _seconds: callback_started.wait(timeout=2),
            ), mock.patch.object(
                batch.os,
                "killpg",
                side_effect=lambda _pid, _signal: release_callback.set(),
            ) as killpg:
                result = batch.wait_workers(
                    [ready, slow],
                    stall_minutes=1,
                    on_claim_ready=callback,
                )

        self.assertTrue(result)
        self.assertTrue(slow["stalled"])
        killpg.assert_called_once()

    def test_wait_workers_callback_failure_terminates_remaining_seats(self):
        class FakeProc:
            next_pid = 3000

            def __init__(self, done=False):
                self.returncode = 0 if done else None
                self.pid = FakeProc.next_pid
                FakeProc.next_pid += 1

            def poll(self):
                return self.returncode

            def wait(self):
                if self.returncode is None:
                    self.returncode = -9
                return self.returncode

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def job(cid, done=False):
                log_path = root / f"{cid}.log"
                return {
                    "cid": cid,
                    "row": {"claim_id": cid},
                    "pass": 1,
                    "proc": FakeProc(done),
                    "raw_output": root / f"{cid}.out",
                    "log_path": log_path,
                    "log_handle": log_path.open("w", encoding="utf-8"),
                    "last_size": 0,
                    "last_progress": time.monotonic(),
                    "stalled": False,
                }

            ready = job("ready", done=True)
            slow = job("slow")
            with mock.patch.object(batch.os, "killpg") as killpg:
                result = batch.wait_workers(
                    [ready, slow],
                    on_claim_ready=lambda _jobs: False,
                )

        self.assertFalse(result)
        self.assertEqual(slow["returncode"], -9)
        self.assertTrue(all(job["log_handle"].closed for job in (ready, slow)))
        killpg.assert_called_once()

    def test_committer_shell_skips_launch_when_already_cancelled(self):
        cancel = threading.Event()
        cancel.set()
        batch._COMMAND_CONTEXT.cancel_event = cancel
        started = time.monotonic()
        try:
            with mock.patch.object(batch.subprocess, "Popen") as popen:
                result = batch.sh(
                    [sys.executable, "-c", "pass"],
                    timeout=30,
                )
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        popen.assert_not_called()
        self.assertEqual(result.returncode, 125)
        self.assertIn("cancelled", result.stderr)
        self.assertLess(time.monotonic() - started, 3)

    def test_committer_shell_rechecks_cancel_after_short_command(self):
        cancel = threading.Event()
        proc = mock.Mock(returncode=0)
        proc.communicate.side_effect = lambda timeout=None: (
            cancel.set() or "stdout",
            "stderr",
        )
        batch._COMMAND_CONTEXT.cancel_event = cancel
        try:
            with mock.patch.object(batch.subprocess, "Popen", return_value=proc):
                result = batch.sh(["quick-command"])
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        self.assertEqual(result.returncode, 125)
        self.assertEqual(result.stdout, "stdout")
        self.assertEqual(result.stderr, "stderr")

    def test_committer_shell_terminates_gracefully_before_forced_kill(self):
        cancel = threading.Event()
        proc = mock.Mock(pid=7654, returncode=-15)
        calls = 0

        def communicate(timeout=None):
            nonlocal calls
            calls += 1
            if calls == 1:
                cancel.set()
                raise subprocess.TimeoutExpired(["pipeline"], timeout)
            return "stdout", "terminated"

        proc.communicate.side_effect = communicate
        batch._COMMAND_CONTEXT.cancel_event = cancel
        try:
            with mock.patch.object(
                batch.subprocess, "Popen", return_value=proc
            ), mock.patch.object(batch.os, "killpg") as killpg:
                result = batch.sh(["pipeline"], timeout=30)
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        self.assertEqual(result.returncode, 125)
        self.assertEqual(result.stdout, "stdout")
        self.assertEqual(result.stderr, "terminated")
        killpg.assert_called_once_with(7654, signal.SIGTERM)
        self.assertEqual(
            proc.communicate.call_args_list,
            [
                mock.call(timeout=1.0),
                mock.call(timeout=batch.COMMAND_TERMINATION_GRACE_SECONDS),
            ],
        )

    def test_committer_shell_preserves_normal_short_command_result(self):
        cancel = threading.Event()
        proc = mock.Mock(returncode=7)
        proc.communicate.return_value = ("stdout", "stderr")
        batch._COMMAND_CONTEXT.cancel_event = cancel
        try:
            with mock.patch.object(batch.subprocess, "Popen", return_value=proc):
                result = batch.sh(["quick-command"])
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        self.assertEqual(result.returncode, 7)
        self.assertEqual(result.stdout, "stdout")
        self.assertEqual(result.stderr, "stderr")

    def test_rollback_commands_bypass_committer_cancellation(self):
        oid = "a" * 40
        target = mock.Mock(returncode=0, stdout=f"{oid}\n", stderr="")
        reset = mock.Mock(returncode=0, stdout="", stderr="")
        branch = mock.Mock(returncode=0, stdout="main\n", stderr="")
        status = mock.Mock(returncode=0, stdout="", stderr="")
        head = mock.Mock(returncode=0, stdout=f"{oid}\n", stderr="")
        remote = mock.Mock(returncode=0, stdout=f"{oid}\n", stderr="")
        with mock.patch.object(
            batch,
            "sh",
            side_effect=[target, reset, branch, status, head, remote],
        ) as sh:
            ok, detail = batch.reset_to_origin_main()

        self.assertTrue(ok, detail)
        self.assertEqual(sh.call_count, 6)
        self.assertTrue(
            all(call.kwargs.get("honor_cancel") is False for call in sh.call_args_list)
        )

    def test_reset_to_origin_main_rejects_clean_ref_mismatch(self):
        target_oid = "a" * 40
        moved_oid = "b" * 40
        commands = [
            mock.Mock(returncode=0, stdout=f"{target_oid}\n", stderr=""),
            mock.Mock(returncode=0, stdout="", stderr=""),
            mock.Mock(returncode=0, stdout="main\n", stderr=""),
            mock.Mock(returncode=0, stdout="", stderr=""),
            mock.Mock(returncode=0, stdout=f"{target_oid}\n", stderr=""),
            mock.Mock(returncode=0, stdout=f"{moved_oid}\n", stderr=""),
        ]
        with mock.patch.object(batch, "sh", side_effect=commands):
            ok, detail = batch.reset_to_origin_main()

        self.assertFalse(ok)
        self.assertIn("HEAD synchronized with origin/main", detail)

    def test_reset_to_origin_main_rejects_recognizable_provenance_drift(self):
        target_oid = "a" * 40
        commands = [
            mock.Mock(returncode=0, stdout=f"{target_oid}\n", stderr=""),
            mock.Mock(returncode=0, stdout="", stderr=""),
            mock.Mock(returncode=0, stdout="main\n", stderr=""),
            mock.Mock(
                returncode=0,
                stdout=f" M {batch.LANE_CERTIFICATION_PATH}\n",
                stderr="",
            ),
        ]
        with mock.patch.object(batch, "sh", side_effect=commands):
            ok, detail = batch.reset_to_origin_main()

        self.assertFalse(ok)
        self.assertIn("literally clean worktree", detail)

    def test_apply_rejection_is_global_when_reset_cannot_be_verified(self):
        delivery = [(
            {
                "cid": "row",
                "pass": 1,
                "row": {"claim_id": "row", "criticality": "medium"},
            },
            {
                "audit": {"verdict": "audited_clean"},
                "evidence_manifest": {},
            },
        )]
        with mock.patch.object(
            batch, "sync_origin_main", return_value=(True, "base")
        ), mock.patch.object(
            batch.audit_runner, "apply_one", return_value=(False, "rejected")
        ), mock.patch.object(
            batch,
            "reset_to_origin_main",
            return_value=(False, "ref mismatch"),
        ):
            ok, results = batch.apply_claim_serialized(delivery, retries=1)

        self.assertFalse(ok)
        self.assertEqual(results[0]["result"], "race_reset_failed")
        self.assertIn("ref mismatch", results[0]["detail"])

    def test_packet_completion_cancel_skips_exit_grace(self):
        cancel = threading.Event()
        cancel.set()
        proc = mock.Mock(pid=4321)
        proc.poll.return_value = None
        proc.wait.return_value = -9
        batch._COMMAND_CONTEXT.cancel_event = cancel
        started = time.monotonic()
        try:
            with mock.patch.object(batch.os, "killpg") as killpg:
                polling_failed, returncode = batch._wait_for_packet_completion(proc)
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        self.assertFalse(polling_failed)
        self.assertEqual(returncode, -9)
        self.assertEqual(proc.wait.call_args_list, [mock.call()])
        killpg.assert_called_once_with(4321, signal.SIGKILL)
        self.assertLess(time.monotonic() - started, 1)

    def test_checkpoint_abort_cannot_delete_concurrent_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            checkpoint = Path(tmp) / "static_pipeline_checkpoint.json"
            checkpoint.write_text(
                json.dumps({
                    "schema": batch.static_checkpoint.BUILDING_SCHEMA,
                    "build_nonce": "a" * 32,
                }),
                encoding="utf-8",
            )
            cleanup_entered = threading.Event()
            release_cleanup = threading.Event()
            begin_started = threading.Event()
            begin_entered_checkpoint = threading.Event()
            results = {}

            def delayed_cleanup(_nonce):
                cleanup_entered.set()
                self.assertTrue(release_cleanup.wait(timeout=2))
                return True, "cleaned"

            def fingerprint(*, include_ledger_static=True):
                if threading.current_thread().name == "checkpoint-begin":
                    begin_entered_checkpoint.set()
                return "f" * 64, "fingerprinted"

            with mock.patch.object(
                batch.static_checkpoint, "CHECKPOINT", checkpoint
            ), mock.patch.object(
                batch.static_checkpoint,
                "static_input_fingerprint",
                side_effect=fingerprint,
            ), mock.patch.object(
                batch.static_checkpoint,
                "_cleanup_receipts",
                side_effect=delayed_cleanup,
            ), mock.patch.dict(
                os.environ,
                {batch.static_checkpoint.BUILD_NONCE_ENV: "a" * 32},
            ):
                abort_thread = threading.Thread(
                    target=lambda: results.update(
                        abort=batch.static_checkpoint.abort_checkpoint()
                    )
                )
                abort_thread.start()
                self.assertTrue(cleanup_entered.wait(timeout=2))
                os.environ[batch.static_checkpoint.BUILD_NONCE_ENV] = "b" * 32

                def begin_build():
                    begin_started.set()
                    results["begin"] = batch.static_checkpoint.begin_checkpoint()

                begin_thread = threading.Thread(
                    name="checkpoint-begin",
                    target=begin_build,
                )
                begin_thread.start()
                self.assertTrue(begin_started.wait(timeout=2))
                self.assertFalse(begin_entered_checkpoint.wait(timeout=0.2))
                release_cleanup.set()
                abort_thread.join(timeout=2)
                begin_thread.join(timeout=2)

            self.assertFalse(abort_thread.is_alive())
            self.assertFalse(begin_thread.is_alive())
            self.assertTrue(results["abort"][0], results["abort"][1])
            self.assertTrue(results["begin"][0], results["begin"][1])
            payload = json.loads(checkpoint.read_text(encoding="utf-8"))
            self.assertEqual(payload["build_nonce"], "b" * 32)

    def test_verdict_only_path_allowlist_is_narrower_than_commit_allowlist(self):
        self.assertTrue(
            batch.verdict_only_generated_path(
                "docs/audit/data/ledger/ro/row.json"
            )
        )
        self.assertTrue(
            batch.verdict_only_generated_path(
                "docs/publication/ci3_z3/RESULTS_INDEX_EFFECTIVE_STATUS.md"
            )
        )
        self.assertFalse(
            batch.verdict_only_generated_path(
                "docs/audit/data/lane_certification_config.json"
            )
        )
        self.assertFalse(
            batch.verdict_only_generated_path(
                "docs/audit/scripts/audit_lint.py"
            )
        )

    def test_verdict_only_eligibility_rejects_cache_hash_mismatch(self):
        checkpoint = "c" * 40
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "docs" / "audit" / "data"
            data.mkdir(parents=True)
            for name in batch.static_checkpoint.STATIC_CACHE_NAMES:
                (data / name).write_text("{}", encoding="utf-8")
            checkpoint_path = data / "static_pipeline_checkpoint.json"
            checkpoint_path.write_text(
                json.dumps({
                    "schema": batch.static_checkpoint.FINAL_SCHEMA,
                    "static_cache_sha256": {
                        name: hashlib.sha256(b"{}").hexdigest()
                        for name in batch.static_checkpoint.STATIC_CACHE_NAMES
                    },
                    "static_input_sha256": checkpoint,
                }),
                encoding="utf-8",
            )
            (data / "runner_classification.json").write_text(
                '{"stale": true}', encoding="utf-8"
            )
            with mock.patch.object(
                batch.static_checkpoint, "REPO_ROOT", root
            ), mock.patch.object(
                batch.static_checkpoint, "DATA", data
            ), mock.patch.object(
                batch.static_checkpoint, "CHECKPOINT", checkpoint_path
            ):
                eligible, detail = batch.verdict_only_pipeline_eligibility()

        self.assertFalse(eligible)
        self.assertIn("do not match", detail)

    def test_verdict_only_eligibility_rejects_git_inspection_failure(self):
        with mock.patch.object(
            batch.static_checkpoint,
            "verify_checkpoint",
            return_value=(False, "git diff --name-only failed"),
        ):
            eligible, detail = batch.verdict_only_pipeline_eligibility()

        self.assertFalse(eligible)
        self.assertIn("git diff", detail)

    def test_checkpoint_worktree_inspection_fails_closed(self):
        failed = mock.Mock(returncode=128, stdout="", stderr="index failure")
        with mock.patch.object(
            batch.static_checkpoint, "run_git", return_value=failed
        ):
            fingerprint, detail = (
                batch.static_checkpoint.static_input_fingerprint()
            )

        self.assertIsNone(fingerprint)
        self.assertIn("failed", detail)

    def test_static_checkpoint_end_to_end_accepts_only_audit_row_delta(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def git(*args):
                return subprocess.run(
                    ["git", *args],
                    cwd=root,
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout.strip()

            git("init", "-q")
            git("config", "user.email", "checkpoint-test@example.invalid")
            git("config", "user.name", "Checkpoint Test")
            (root / ".gitignore").write_text(
                "docs/audit/data/citation_graph.json\n"
                "docs/audit/data/runner_classification.json\n"
                "docs/audit/data/static_pipeline_checkpoint.json\n"
                "docs/audit/data/static_pipeline_checkpoint.lock\n"
                "docs/audit/data/static_pipeline_receipt_*.json\n"
                "docs/audit/data/ledger/hidden/\n"
                "docs/ignored_local_note.md\n"
                "scripts/ignored_*.py\n",
                encoding="utf-8",
            )
            data = root / "docs" / "audit" / "data"
            shard = data / "ledger" / "ro" / "row.json"
            shard.parent.mkdir(parents=True)
            ignored_note = root / "docs" / "ignored_local_note.md"
            ignored_note.parent.mkdir(parents=True, exist_ok=True)
            ignored_note.write_text("# Local graph input\n", encoding="utf-8")
            ignored_runner = root / "scripts" / "ignored_runner.py"
            ignored_runner.parent.mkdir(parents=True)
            ignored_runner.write_text("assert True\n", encoding="utf-8")
            ignored_helper = root / "scripts" / "ignored_helper.py"
            ignored_helper.write_text("VALUE = 1\n", encoding="utf-8")
            before = {
                "claim_id": "row",
                "deps": ["dep"],
                "runner_path": "scripts/ignored_runner.py",
                "helper_runner_paths": ["scripts/ignored_helper.py"],
                "audit_status": "unaudited",
            }
            shard.write_text(json.dumps(before), encoding="utf-8")
            ignored_ledger = data / "ledger" / "hidden" / "row.json"
            ignored_ledger.parent.mkdir(parents=True)
            ignored_ledger.write_text(
                json.dumps({"claim_id": "hidden", "deps": ["a"]}),
                encoding="utf-8",
            )
            ignored_ledger_sidecar = ignored_ledger.with_suffix(".sidecar")
            ignored_ledger_sidecar.write_text("one\n", encoding="utf-8")
            git("add", ".gitignore", str(shard.relative_to(root)))
            git("commit", "-qm", "baseline")

            citation_graph = data / "citation_graph.json"
            citation_graph.write_bytes(b'{"cache": "citation_graph.json"}\n')
            runner_classification = data / "runner_classification.json"
            checkpoint = data / "static_pipeline_checkpoint.json"

            nonce = "a" * 32
            with mock.patch.object(
                batch.static_checkpoint, "REPO_ROOT", root
            ), mock.patch.object(
                batch.static_checkpoint, "DATA", data
            ), mock.patch.object(
                batch.static_checkpoint, "CHECKPOINT", checkpoint
            ), mock.patch.dict(
                os.environ,
                {batch.static_checkpoint.BUILD_NONCE_ENV: nonce},
            ):
                began, begin_detail = batch.static_checkpoint.begin_checkpoint()
                stale_prepare_ok, stale_prepare_detail = (
                    batch.static_checkpoint.prepare_checkpoint()
                )
                graph_receipt_ok, graph_receipt_detail = (
                    batch.static_checkpoint.record_producer_receipt(
                        "citation_graph"
                    )
                )
                seed_receipt_ok, seed_receipt_detail = (
                    batch.static_checkpoint.record_producer_receipt(
                        "seed_ledger"
                    )
                )
                prepared, prepare_detail = (
                    batch.static_checkpoint.prepare_checkpoint()
                )
                runner_cache_absent_at_prepare = (
                    not runner_classification.exists()
                )
                runner_classification.write_bytes(
                    b'{"cache": "runner_classification.json"}\n'
                )
                classifier_receipt_ok, classifier_receipt_detail = (
                    batch.static_checkpoint.record_producer_receipt(
                        "runner_classification"
                    )
                )
                captured, capture_detail = (
                    batch.static_checkpoint.capture_checkpoint()
                )
                finalized, finalize_detail = (
                    batch.static_checkpoint.finalize_checkpoint()
                )
                receipts_cleaned = not list(
                    data.glob("static_pipeline_receipt_*.json")
                )
                shard.write_text(
                    json.dumps(dict(before, audit_status="audited_clean")),
                    encoding="utf-8",
                )
                audit_ok, _ = batch.static_checkpoint.verify_checkpoint()
                shard.write_text(
                    json.dumps(dict(
                        before,
                        audit_status="audited_clean",
                        direct_in_degree=7,
                        transitive_descendants=123,
                        max_descendant_status="retained",
                        max_descendant_status_rank=9,
                        load_bearing_score=42.5,
                    )),
                    encoding="utf-8",
                )
                derived_metrics_ok, derived_metrics_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                shard.write_text(
                    json.dumps(dict(
                        before,
                        audit_status="audited_clean",
                        criticality="high",
                        direct_in_degree=7,
                        transitive_descendants=123,
                        max_descendant_status="retained",
                        max_descendant_status_rank=9,
                        load_bearing_score=42.5,
                    )),
                    encoding="utf-8",
                )
                criticality_ok, criticality_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                shard.write_text(
                    json.dumps(dict(before, audit_status="audited_clean")),
                    encoding="utf-8",
                )
                with mock.patch.dict(
                    os.environ,
                    {batch.static_checkpoint.EXPECTED_NONCE_ENV: "b" * 32},
                ):
                    wrong_identity_ok, wrong_identity_detail = (
                        batch.static_checkpoint.verify_checkpoint()
                    )
                ignored_note.write_text(
                    "# Changed local graph input\n", encoding="utf-8"
                )
                ignored_note_ok, ignored_note_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_note.write_text(
                    "# Local graph input\n", encoding="utf-8"
                )
                ignored_runner.write_text("assert False\n", encoding="utf-8")
                ignored_runner_ok, ignored_runner_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_runner.write_text("assert True\n", encoding="utf-8")
                ignored_helper.write_text("VALUE = 2\n", encoding="utf-8")
                ignored_helper_ok, ignored_helper_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_helper.write_text("VALUE = 1\n", encoding="utf-8")
                ignored_ledger.write_text(
                    json.dumps({"claim_id": "hidden", "deps": ["b"]}),
                    encoding="utf-8",
                )
                ignored_ledger_ok, ignored_ledger_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_ledger.write_text(
                    json.dumps({"claim_id": "hidden", "deps": ["a"]}),
                    encoding="utf-8",
                )
                ignored_ledger_sidecar.write_text("two\n", encoding="utf-8")
                ignored_sidecar_ok, ignored_sidecar_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ignored_ledger_sidecar.write_text("one\n", encoding="utf-8")
                shard.write_text(
                    json.dumps(dict(before, novel_topology={"edge": "new"})),
                    encoding="utf-8",
                )
                unknown_field_ok, unknown_field_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                shard.write_text(json.dumps(before), encoding="utf-8")
                ledger_sidecar = shard.parent / "topology.sidecar"
                ledger_sidecar.write_text("new topology\n", encoding="utf-8")
                ledger_sidecar_ok, ledger_sidecar_detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )
                ledger_sidecar.unlink()
                shard.write_text(
                    json.dumps(dict(before, deps=["rewired"])),
                    encoding="utf-8",
                )
                topology_ok, detail = (
                    batch.static_checkpoint.verify_checkpoint()
                )

        self.assertTrue(began, begin_detail)
        self.assertFalse(stale_prepare_ok)
        self.assertIn("producer receipt", stale_prepare_detail)
        self.assertTrue(graph_receipt_ok, graph_receipt_detail)
        self.assertTrue(seed_receipt_ok, seed_receipt_detail)
        self.assertTrue(prepared, prepare_detail)
        self.assertTrue(runner_cache_absent_at_prepare)
        self.assertTrue(classifier_receipt_ok, classifier_receipt_detail)
        self.assertTrue(captured, capture_detail)
        self.assertTrue(finalized, finalize_detail)
        self.assertTrue(receipts_cleaned)
        self.assertTrue(audit_ok)
        self.assertTrue(derived_metrics_ok, derived_metrics_detail)
        self.assertFalse(criticality_ok)
        self.assertIn("static repository inputs changed", criticality_detail)
        self.assertFalse(wrong_identity_ok)
        self.assertIn("changed during fast use", wrong_identity_detail)
        self.assertFalse(ignored_note_ok)
        self.assertIn("static repository inputs changed", ignored_note_detail)
        self.assertFalse(ignored_runner_ok)
        self.assertIn("static repository inputs changed", ignored_runner_detail)
        self.assertFalse(ignored_helper_ok)
        self.assertIn("static repository inputs changed", ignored_helper_detail)
        self.assertFalse(ignored_ledger_ok)
        self.assertIn("static repository inputs changed", ignored_ledger_detail)
        self.assertFalse(ignored_sidecar_ok)
        self.assertIn("static repository inputs changed", ignored_sidecar_detail)
        self.assertFalse(unknown_field_ok)
        self.assertIn("static repository inputs changed", unknown_field_detail)
        self.assertFalse(ledger_sidecar_ok)
        self.assertIn("static repository inputs changed", ledger_sidecar_detail)
        self.assertFalse(topology_ok)
        self.assertIn("static repository inputs changed", detail)

    def test_pipeline_recomputes_status_dependent_load_bearing_after_fixed_point(self):
        script = (batch.SCRIPTS / "run_pipeline.sh").read_text(encoding="utf-8")
        pre_seed = script.index(
            'echo "==> 1c/18 compute_load_bearing.py pre-seed topology refresh"'
        )
        seed = script.index('echo "==> 2/18 seed_audit_ledger.py"')
        first = script.index(
            'echo "==> 5/18 compute_load_bearing.py"'
        )
        fixed_point_seed = script.index(
            'echo "==> 3a/18 seed_audit_ledger.py fixed-point receipt"'
        )
        checkpoint = script.index(
            'echo "==> 3b/18 static_pipeline_checkpoint.py prepare'
        )
        status = script.index(
            'echo "==> 6/18 compute_effective_status.py"'
        )
        final = script.index(
            'echo "==> 7a/18 compute_load_bearing.py post-status fixed point"'
        )
        certification = script.index(
            'echo "==> 7b/18 compute_lane_certification.py'
        )

        self.assertLess(pre_seed, seed)
        self.assertLess(seed, first)
        self.assertLess(first, fixed_point_seed)
        self.assertLess(fixed_point_seed, checkpoint)
        self.assertLess(first, checkpoint)
        self.assertLess(first, status)
        self.assertLess(status, final)
        self.assertLess(final, certification)
        self.assertEqual(
            script.count(
                "python3 docs/audit/scripts/compute_load_bearing.py"
            ),
            3,
        )
        self.assertEqual(
            script.count(
                "python3 docs/audit/scripts/seed_audit_ledger.py"
            ),
            2,
        )

    def test_run_generated_gates_selects_verdict_only_pipeline(self):
        completed = mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(
            batch,
            "verdict_only_pipeline_eligibility",
            return_value=(True, "safe"),
        ), mock.patch.object(batch, "changed_paths", return_value=[]), \
             mock.patch.object(batch, "sh", return_value=completed) as sh:
            ok, detail = batch.run_generated_gates()

        self.assertTrue(ok)
        self.assertEqual(detail, "gates passed")
        self.assertEqual(
            sh.call_args_list[0].args[0],
            ["bash", str(batch.SCRIPTS / "run_pipeline.sh"), "--verdict-only"],
        )

    def test_run_generated_gates_falls_back_to_full_pipeline(self):
        completed = mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(
            batch,
            "verdict_only_pipeline_eligibility",
            return_value=(False, "source changed"),
        ), mock.patch.object(batch, "changed_paths", return_value=[]), \
             mock.patch.object(batch, "sh", return_value=completed) as sh:
            ok, detail = batch.run_generated_gates()

        self.assertTrue(ok)
        self.assertEqual(detail, "gates passed")
        self.assertEqual(
            sh.call_args_list[0].args[0],
            ["bash", str(batch.SCRIPTS / "run_pipeline.sh")],
        )

    def test_two_seats_share_pipeline_commit_and_push(self):
        row = {"claim_id": "critical", "criticality": "critical"}
        deliveries = [
            (
                {"cid": "critical", "pass": seat, "row": row},
                {
                    "audit": {"verdict": "audited_clean"},
                    "evidence_manifest": {},
                },
            )
            for seat in (1, 2)
        ]
        pushed = mock.Mock(returncode=0, stdout="", stderr="")
        with mock.patch.object(
            batch, "sync_origin_main", return_value=(True, "base")
        ), mock.patch.object(
            batch.audit_runner, "apply_one", return_value=(True, "applied")
        ) as apply_one, mock.patch.object(
            batch, "run_generated_gates", return_value=(True, "gated")
        ) as gates, mock.patch.object(
            batch, "stage_and_commit", return_value=(True, "commit")
        ) as commit, mock.patch.object(batch, "sh", return_value=pushed) as sh:
            ok, results = batch.apply_claim_serialized(deliveries, retries=3)

        self.assertTrue(ok)
        self.assertEqual(apply_one.call_count, 2)
        gates.assert_called_once_with()
        commit.assert_called_once()
        self.assertEqual(sh.call_count, 1)
        self.assertEqual([item["pass"] for item in results], [1, 2])
        self.assertEqual({item["commit"] for item in results}, {"commit"})

    def test_push_race_replays_both_critical_seats_as_one_transaction(self):
        row = {"claim_id": "critical", "criticality": "critical"}
        deliveries = [
            (
                {"cid": "critical", "pass": seat, "row": row},
                {
                    "audit": {"verdict": "audited_clean"},
                    "evidence_manifest": {},
                },
            )
            for seat in (1, 2)
        ]
        commands = [
            mock.Mock(returncode=1, stdout="", stderr="push race"),
            mock.Mock(returncode=0, stdout="", stderr=""),
            mock.Mock(returncode=1, stdout="", stderr="not landed"),
            mock.Mock(returncode=0, stdout="", stderr=""),
        ]
        with mock.patch.object(
            batch, "sync_origin_main", return_value=(True, "base")
        ), mock.patch.object(
            batch.audit_runner, "apply_one", return_value=(True, "applied")
        ) as apply_one, mock.patch.object(
            batch, "run_generated_gates", return_value=(True, "gated")
        ) as gates, mock.patch.object(
            batch,
            "stage_and_commit",
            side_effect=[(True, "commit-1"), (True, "commit-2")],
        ) as commit, mock.patch.object(
            batch, "reset_to_origin_main", return_value=(True, "reset")
        ) as reset, mock.patch.object(
            batch, "sh", side_effect=commands
        ):
            ok, results = batch.apply_claim_serialized(deliveries, retries=2)

        self.assertTrue(ok)
        self.assertEqual(apply_one.call_count, 4)
        self.assertEqual(gates.call_count, 2)
        self.assertEqual(commit.call_count, 2)
        reset.assert_called_once_with()
        self.assertEqual({item["commit"] for item in results}, {"commit-2"})

    def test_push_race_cancellation_rolls_back_local_commit(self):
        cancel = threading.Event()
        row = {"claim_id": "row", "criticality": "high"}
        deliveries = [(
            {"cid": "row", "pass": 1, "row": row},
            {"audit": {"verdict": "audited_clean"}, "evidence_manifest": {}},
        )]

        def command(cmd, *args, **kwargs):
            if cmd[:2] == ["git", "push"]:
                return subprocess.CompletedProcess(cmd, 1, "", "push race")
            if cmd[:2] == ["git", "fetch"]:
                return subprocess.CompletedProcess(cmd, 0, "", "")
            if cmd[:2] == ["git", "merge-base"]:
                cancel.set()
                return subprocess.CompletedProcess(cmd, 125, "", "cancelled")
            raise AssertionError(cmd)

        batch._COMMAND_CONTEXT.cancel_event = cancel
        try:
            with mock.patch.object(
                batch, "sync_origin_main", return_value=(True, "base")
            ), mock.patch.object(
                batch.audit_runner, "apply_one", return_value=(True, "applied")
            ), mock.patch.object(
                batch, "run_generated_gates", return_value=(True, "gated")
            ), mock.patch.object(
                batch, "stage_and_commit", return_value=(True, "local-commit")
            ), mock.patch.object(
                batch, "reset_to_origin_main", return_value=(True, "reset")
            ) as reset, mock.patch.object(batch, "sh", side_effect=command):
                ok, results = batch.apply_claim_serialized(deliveries, retries=1)
        finally:
            del batch._COMMAND_CONTEXT.cancel_event

        self.assertFalse(ok)
        self.assertEqual(results[0]["result"], "commit_cancelled")
        reset.assert_called_once_with()

    def test_terminal_push_race_rolls_back_local_commit(self):
        row = {"claim_id": "row", "criticality": "high"}
        deliveries = [(
            {"cid": "row", "pass": 1, "row": row},
            {"audit": {"verdict": "audited_clean"}, "evidence_manifest": {}},
        )]
        commands = [
            subprocess.CompletedProcess(["git", "push"], 1, "", "push race"),
            subprocess.CompletedProcess(["git", "fetch"], 0, "", ""),
            subprocess.CompletedProcess(["git", "merge-base"], 1, "", "not landed"),
        ]
        with mock.patch.object(
            batch, "sync_origin_main", return_value=(True, "base")
        ), mock.patch.object(
            batch.audit_runner, "apply_one", return_value=(True, "applied")
        ), mock.patch.object(
            batch, "run_generated_gates", return_value=(True, "gated")
        ), mock.patch.object(
            batch, "stage_and_commit", return_value=(True, "local-commit")
        ), mock.patch.object(
            batch, "reset_to_origin_main", return_value=(True, "reset")
        ) as reset, mock.patch.object(batch, "sh", side_effect=commands):
            ok, results = batch.apply_claim_serialized(deliveries, retries=1)

        self.assertFalse(ok)
        self.assertEqual(results[0]["result"], "push_race_exhausted")
        reset.assert_called_once_with()


class AutomaticPanelResumeTest(unittest.TestCase):
    def test_disagreement_batch_is_panelled_then_same_lane_resumes(self):
        args = _args()
        # cycle 1 lands the disagreement/panel resolution; cycle 2 reaches
        # the lane fixed point. drain_lane reads HEAD before/after each cycle.
        heads = iter(["h0", "h1", "h1", "h1"])
        labels: list[str] = []

        def fake_run(label, command, env=None):
            labels.append(label)
            return 0

        with mock.patch.object(audit_loop, "git_head", side_effect=lambda: next(heads)), \
             mock.patch.object(audit_loop, "run_command", side_effect=fake_run):
            rc, progressed = audit_loop.drain_lane("lane_a", args)

        self.assertEqual(rc, 0)
        self.assertTrue(progressed)
        self.assertEqual(
            labels,
            [
                "batch-lane_a-cycle-1",
                "panel-after-lane_a-cycle-1",
                "batch-lane_a-cycle-2",
                "panel-after-lane_a-cycle-2",
            ],
        )

    def test_batch_hard_failure_panels_before_stopping(self):
        args = _args()
        labels: list[str] = []

        def fake_run(label, command, env=None):
            labels.append(label)
            return 1 if label.startswith("batch-") else 0

        with mock.patch.object(audit_loop, "git_head", return_value="h0"), \
             mock.patch.object(audit_loop, "run_command", side_effect=fake_run):
            rc, progressed = audit_loop.drain_lane("lane_a", args)

        self.assertEqual(rc, 1)
        self.assertFalse(progressed)
        self.assertEqual(
            labels,
            ["batch-lane_a-cycle-1", "panel-after-lane_a-cycle-1"],
        )


class CampaignContractTest(unittest.TestCase):
    def test_inherited_campaign_lock_is_reentrant_for_child(self):
        held = batch.acquire_exclusive_drain_lock("top-level-test")
        self.assertIsNotNone(held)
        try:
            with mock.patch.dict(
                os.environ,
                {batch.INHERITED_DRAIN_LOCK_FD_ENV: str(held.fileno())},
            ):
                inherited = batch.acquire_exclusive_drain_lock("child-test")
            self.assertIsNotNone(inherited)
            inherited.close()
        finally:
            held.close()

    def test_forensic_selector_uses_canonical_source_predicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            queue = Path(tmp) / "queue.json"
            queue.write_text(
                json.dumps(
                    {
                        "queue": [
                            {
                                "claim_id": "bounded_obstruction",
                                "ready": True,
                                "audit_status": "unaudited",
                                "claim_type": "bounded_theorem",
                                "note_path": "docs/EXAMPLE_OBSTRUCTION_NOTE.md",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with mock.patch.object(audit_loop, "QUEUE", queue), mock.patch.object(
                batch, "source_requires_forensic", return_value=True
            ):
                selected = audit_loop.first_ready_forensic_claim()
        self.assertEqual(selected, "bounded_obstruction")

    def test_unknown_lane_fails_before_opening_panel(self):
        with mock.patch.object(
            audit_loop, "configured_lane_names", return_value=["lane_a"]
        ), mock.patch.object(audit_loop, "run_panel") as run_panel:
            rc = audit_loop.main(
                [
                    "--dry-run",
                    "--skip-forensic-canary",
                    "--lane",
                    "definitely_unknown",
                ]
            )
        self.assertEqual(rc, 2)
        run_panel.assert_not_called()

    def test_verdict_summary_never_rematerializes_ledger_cache(self):
        with mock.patch.object(
            audit_loop, "audit_status_snapshot", return_value={"row": "audited_clean"}
        ), mock.patch.object(batch, "load_rows") as load_rows:
            with mock.patch.dict(
                audit_loop.PROGRESS,
                {"baseline_status": {"row": "audit_in_progress"}},
            ):
                counts = audit_loop.landed_verdict_counts()
        self.assertEqual(counts["audited_clean"], 1)
        load_rows.assert_not_called()

    def test_inner_batches_share_campaign_quarantine_and_dispatch_policy(self):
        args = _args()
        args.campaign_quarantine_file = Path("/tmp/campaign/quarantine.jsonl")

        command = audit_loop.batch_command("lane_a", args)

        self.assertIn("--campaign-quarantine-file", command)
        self.assertIn(str(args.campaign_quarantine_file), command)
        self.assertNotIn("--dispatch-science-fixes", command)

        args.dispatch_science_fixes = True
        self.assertIn(
            "--dispatch-science-fixes",
            audit_loop.batch_command("lane_a", args),
        )


if __name__ == "__main__":
    unittest.main()
