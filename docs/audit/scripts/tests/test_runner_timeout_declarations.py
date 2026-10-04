"""Explicit caps must stay bound to the source they authorize executing."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'scripts'))
import runner_cache as rc
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "docs/ai_methodology/skills/review-loop/scripts"))
import review_receipt as receipt


class SourceBoundTimeoutTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.runner = self.root / 'scripts/check.py'
        self.runner.parent.mkdir()
        self.runner.write_text("raise RuntimeError('must not import')\n")
        self.sidecar = self.root / 'docs/audit/data/runner_timeout_declarations.json'
        self.sidecar.parent.mkdir(parents=True)
        self.patch = patch.object(rc, 'REPO_ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def declare(self, cap=120, schema=1, sha=None):
        self.sidecar.write_text(json.dumps({'schema_version': schema, 'runners': {
            'scripts/check.py': {'timeout_sec': cap, 'source_sha256': sha or hashlib.sha256(self.runner.read_bytes()).hexdigest()}
        }}))

    def test_source_change_invalidates_explicit_cap(self):
        self.declare(900)
        self.assertEqual(receipt.declared_review_timeout_for(self.root, rc, 'scripts/check.py'), 900)
        self.runner.write_text("print('changed')\n")
        self.assertIsNone(receipt.declared_review_timeout_for(self.root, rc, 'scripts/check.py'))

    def test_no_default_or_malformed_declaration_is_admitted(self):
        self.assertIsNone(receipt.declared_review_timeout_for(self.root, rc, 'scripts/check.py'))
        for cap in [True, 0, -2, 120.0, '120', None]:
            self.declare(cap)
            self.assertIsNone(receipt.declared_review_timeout_for(self.root, rc, 'scripts/check.py'))
        for schema in [2, True, 1.0, '1', None]:
            self.declare(schema=schema)
            self.assertIsNone(receipt.declared_review_timeout_for(self.root, rc, 'scripts/check.py'))
        self.sidecar.write_text('{broken')
        self.assertIsNone(receipt.declared_review_timeout_for(self.root, rc, 'scripts/check.py'))

    def test_source_cap_takes_precedence_without_execution(self):
        self.declare(900)
        self.runner.write_text("AUDIT_TIMEOUT_SEC = 37\nraise RuntimeError('must not import')\n")
        self.assertEqual(receipt.declared_review_timeout_for(self.root, rc, 'scripts/check.py'), 37)

    def test_outside_repo_cannot_claim_a_relative_sidecar_entry(self):
        self.declare(900)
        other = self.root.parent / (self.root.name + '-outside.py')
        other.write_bytes(self.runner.read_bytes())
        self.addCleanup(other.unlink)
        self.assertIsNone(receipt.declared_review_timeout_for(self.root, rc, other))


if __name__ == '__main__':
    unittest.main()
