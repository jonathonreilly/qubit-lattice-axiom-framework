"""Behavior tests for exact history recovery and exclusive checkout reuse."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT/'docs/ai_methodology/skills/review-loop/scripts/review_workspace.py'
spec = importlib.util.spec_from_file_location('review_workspace', SOURCE)
ops = importlib.util.module_from_spec(spec); spec.loader.exec_module(ops)


class OperationsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve(); self.repo = self.root/'repo'
        self.repo.mkdir(); self.git('init', '-q')
        self.git('config', 'user.name', 'Test'); self.git('config', 'user.email', 'test@example.invalid')
        (self.repo/'.gitignore').write_text('ignored-data\n')
        (self.repo/'file').write_text('first\n')
        self.git('add', '.'); self.git('commit', '-qm', 'first')
        self.first = self.git('rev-parse', 'HEAD')

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], text=True).strip()

    def history(self):
        p = self.repo/'history'; p.mkdir()
        (p/'one.md').write_bytes(b'original  \n\n')
        (p/'two.md').write_bytes(b'original  \n\n')
        (p/'input.json').write_text('{"value": 3}\n')
        self.git('add', '.'); self.git('commit', '-qm', 'history')
        return self.git('rev-parse', 'HEAD')

    def test_archive_deduplicates_bytes_not_paths_and_keeps_live_target(self):
        revision = self.history(); dest = self.root/'archive'
        record = ops.archive(self.repo, revision, 'history', dest, ['input.json'], 'test')
        self.assertEqual(len(record['entries']), 3)
        self.assertEqual(len(record['unique_blobs']), 2)
        one, two = [r for r in record['entries'] if r['original_path'].endswith(('one.md', 'two.md'))]
        self.assertEqual(one['stored_path'], two['stored_path'])
        self.assertNotEqual(one['original_path'], two['original_path'])
        kept = next(r for r in record['entries'] if r['original_path'].endswith('input.json'))
        self.assertEqual(kept['encoding'], 'identity')
        self.assertEqual((dest/kept['stored_path']).read_bytes(), (self.repo/'history/input.json').read_bytes())
        self.assertEqual(ops.verify_archive(dest)['original_paths'], 3)

    def test_archive_corruption_and_missing_target_fail(self):
        revision = self.history(); dest = self.root/'archive'
        with self.assertRaises(ops.Invalid):
            ops.archive(self.repo, revision, 'history', dest, ['absent'], 'test')
        self.assertFalse(dest.exists())
        record = ops.archive(self.repo, revision, 'history', dest, [], 'test')
        (dest/record['entries'][0]['stored_path']).write_bytes(b'corrupt')
        with self.assertRaises(ops.Invalid): ops.verify_archive(dest)

    def test_archive_never_overwrites_existing_directory(self):
        revision = self.history(); dest = self.root/'archive'; dest.mkdir()
        sentinel = dest/'recovery'; sentinel.write_text('keep')
        with self.assertRaises(ops.Invalid): ops.archive(self.repo, revision, 'history', dest, [], 'test')
        self.assertEqual(sentinel.read_text(), 'keep')

    def test_archive_rejects_symlink_source_and_traversal(self):
        self.history(); (self.repo/'history/link').symlink_to('../file')
        self.git('add', '.'); self.git('commit', '-qm', 'link')
        with self.assertRaises(ops.Invalid): ops.archive(self.repo, 'HEAD', 'history', self.root/'out', [], 'test')
        with self.assertRaises(ops.Invalid): ops.archive(self.repo, 'HEAD', '../history', self.root/'out', [], 'test')

    def acquire(self, owner='one', base=None):
        return ops.checkout(self.repo, self.root/'pool', 'slot', owner, base or self.first)

    def release(self, owner='one', head=None):
        return ops.checkout(self.repo, self.root/'pool', 'slot', owner, release=True, expected_head=head or self.first)

    def test_checkout_reuses_only_released_clean_slot_and_preserves_head(self):
        first = self.acquire(); path = Path(first['path']); inode = path.stat().st_ino
        with self.assertRaises(ops.Invalid): self.acquire('two')
        state = self.release(); self.assertEqual(self.git('rev-parse', state['preserved_ref']), self.first)
        (self.repo/'file').write_text('second\n'); self.git('commit', '-qam', 'second')
        second = self.git('rev-parse', 'HEAD'); acquired = self.acquire('two', second)
        self.assertEqual(Path(acquired['path']).stat().st_ino, inode)
        self.assertEqual((path/'file').read_text(), 'second\n')
        self.assertEqual(acquired['owner'], 'two')

    def test_dirty_untracked_and_ignored_artifacts_survive_failed_release(self):
        state = self.acquire(); path = Path(state['path'])
        for name in ('file', 'untracked-proof', 'ignored-data'):
            original = (path/name).read_bytes() if (path/name).exists() else None
            (path/name).write_text('precious recovery')
            with self.assertRaises(ops.Invalid): self.release()
            self.assertEqual((path/name).read_text(), 'precious recovery')
            saved = json.loads((self.root/'pool/slot.json').read_text())
            self.assertEqual(saved['owner'], 'one')
            if original is None: (path/name).unlink()
            else: (path/name).write_bytes(original)

    def test_checkout_wrong_owner_changed_head_or_foreign_path_fail(self):
        self.acquire()
        with self.assertRaises(ops.Invalid): self.release('another')
        with self.assertRaises(ops.Invalid): self.release(head='0'*40)
        self.release()
        path = self.root/'pool/slot'; (path/'file').write_text('unreviewed')
        with self.assertRaises(ops.Invalid): self.acquire('two')
        self.assertEqual((path/'file').read_text(), 'unreviewed')

    def test_unregistered_checkout_path_is_never_adopted(self):
        p = self.root/'pool/slot'; p.mkdir(parents=True); (p/'findings').write_text('keep')
        with self.assertRaises(ops.Invalid): self.acquire()
        self.assertEqual((p/'findings').read_text(), 'keep')

    def test_unknown_archive_schema_and_path_escape_fail(self):
        revision = self.history(); dest = self.root/'archive'
        ops.archive(self.repo, revision, 'history', dest, [], 'test')
        p = dest/'archive-manifest.json'; record = json.loads(p.read_text())
        record['schema_version'] = 999; p.write_text(json.dumps(record))
        with self.assertRaises(ops.Invalid): ops.verify_archive(dest)
        record['schema_version'] = 1; record['entries'][0]['stored_path'] = '../outside'
        p.write_text(json.dumps(record))
        with self.assertRaises(ops.Invalid): ops.verify_archive(dest)

    def test_pinned_manifest_detects_omitted_duplicate_original(self):
        dest = self.root/'archive'; ops.archive(self.repo, self.history(), 'history', dest, [], 'test')
        manifest = dest/'archive-manifest.json'; expected = ops.sha(manifest.read_bytes())
        record = json.loads(manifest.read_text())
        record['entries'] = [r for r in record['entries'] if r['original_path'] != 'history/two.md']
        manifest.write_text(json.dumps(record))
        with self.assertRaises(ops.Invalid): ops.verify_archive(dest, expected)

    def test_blob_mode_and_unmapped_file_corruption_fail(self):
        dest = self.root/'archive'; record = ops.archive(self.repo, self.history(), 'history', dest, ['input.json'], 'test')
        manifest = dest/'archive-manifest.json'; original = manifest.read_bytes()
        record['entries'][0]['git_blob'] = '0'*40; manifest.write_text(json.dumps(record))
        with self.assertRaises(ops.Invalid): ops.verify_archive(dest)
        manifest.write_bytes(original)
        kept = next(r for r in record['entries'] if r['encoding'] == 'identity')
        (dest/kept['stored_path']).chmod(0o755)
        with self.assertRaises(ops.Invalid): ops.verify_archive(dest)
        (dest/kept['stored_path']).chmod(0o644)
        (dest/'unmapped').write_text('unexpected')
        with self.assertRaises(ops.Invalid): ops.verify_archive(dest)

    def test_slot_symlink_cannot_move_execution_outside_pool(self):
        self.acquire(); self.release()
        old = self.root/'pool/slot'; moved = self.root/'moved'
        self.git('worktree', 'move', str(old), str(moved)); old.symlink_to(moved, target_is_directory=True)
        with self.assertRaises(ops.Invalid): self.acquire('two')

    def test_checkout_unknown_schema_or_unfinished_operation_is_retained(self):
        self.acquire(); state_path = self.root/'pool/slot.json'
        state = json.loads(state_path.read_text()); state['schema_version'] = 2
        state_path.write_text(json.dumps(state))
        with self.assertRaises(ops.Invalid): self.release()
        state['schema_version'] = 1; state_path.write_text(json.dumps(state))
        wt = self.root/'pool/slot'
        marker = Path(ops.git(wt, 'rev-parse', '--path-format=absolute', '--git-path', 'CHERRY_PICK_HEAD'))
        marker.write_text(self.first)
        with self.assertRaises(ops.Invalid): self.release()
        self.assertEqual(json.loads(state_path.read_text())['owner'], 'one')

    def fetch_fixture(self, metadata):
        # Real local Git PR ref transport; only GitHub metadata is mocked.
        remote = self.root/'remote.git'; subprocess.run(['git', 'init', '--bare', '-q', str(remote)], check=True)
        self.git('remote', 'add', 'origin', str(remote))
        self.git('push', '-q', 'origin', self.first+':refs/pull/7/head')
        actual = subprocess.check_output
        values = iter(metadata)
        def output(args, **kwargs):
            if args[0] == 'gh': return json.dumps(next(values))
            return actual(args, **kwargs)
        return patch.object(ops.subprocess, 'check_output', side_effect=output)

    def test_fetch_new_child_freezes_actual_ref_without_checkout(self):
        meta = dict(number=7, state='OPEN', headRefOid=self.first, headRefName='child', baseRefName='parent', isDraft=True)
        with self.fetch_fixture([meta, meta]):
            result = ops.fetch_head(self.repo, 'owner/repo', 7, self.first)
        self.assertEqual(self.git('rev-parse', result['fetched_ref']), self.first)
        self.assertEqual(self.git('rev-parse', 'HEAD'), self.first)
        self.assertTrue(result['metadata']['isDraft'])

    def test_fetch_rejects_metadata_movement(self):
        meta = dict(number=7, state='OPEN', headRefOid=self.first, headRefName='child', baseRefName='parent', isDraft=False)
        moved = dict(meta, baseRefName='main')
        with self.fetch_fixture([meta, moved]):
            with self.assertRaises(ops.Invalid): ops.fetch_head(self.repo, 'owner/repo', 7, self.first)


if __name__ == '__main__': unittest.main()
