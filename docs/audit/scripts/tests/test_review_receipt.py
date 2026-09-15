"""Behavior checks using real graph/cache APIs inside small git repositories."""
import hashlib
import importlib.util
from types import SimpleNamespace
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
TOOL = ROOT / 'docs/ai_methodology/skills/review-loop/scripts/review_receipt.py'
APIS = ('docs/audit/scripts/build_citation_graph.py',
        'docs/audit/scripts/static_pipeline_checkpoint.py', 'scripts/runner_cache.py',
        'scripts/audit_packet_script_deps.py', 'docs/audit/scripts/ledger_io.py')


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.repo = self.home / 'repo'
        self.repo.mkdir()
        for name in APIS:
            target = self.repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        self.write('docs/PARENT.md', '# Supplied parent\n**Type:** bounded_theorem\n')
        self.write('data/input.txt', 'original input\n')
        self.git('init', '-q')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'user.name', 'Receipt test')
        self.git('add', '.')
        self.git('commit', '-qm', 'base')
        base = self.git('rev-parse', 'HEAD')
        self.write('docs/NOTE.md', '---\nclaim_id: note\nrunner: scripts/primary.py\n---\n# Note\n**Type:** bounded_theorem\n[parent](PARENT.md)\n')
        self.write('scripts/primary.py', 'AUDIT_TIMEOUT_SEC=30\nAUDIT_INPUT_PATHS=("data/input.txt",)\nfrom helper import run\n')
        self.write('scripts/helper.py', 'AUDIT_TIMEOUT_SEC=30\ndef run(): return 1\n')
        self.paths = ['docs/NOTE.md', 'scripts/primary.py', 'scripts/helper.py']
        self.git('add', '.')
        self.git('commit', '-qm', 'original')
        head = self.git('rev-parse', 'HEAD')
        tree = self.git('rev-parse', 'HEAD^{tree}')
        self.git('reset', '--soft', base)
        dispositions = [{'original_path': p, 'original_sha256': self.hash(p),
                         'final_path': p, 'final_sha256': self.hash(p),
                         'disposition': 'reviewer recorded decision', 'recovery': head + ':' + p}
                        for p in self.paths]
        report = self.home / 'immutable-report.json'
        report.write_text(json.dumps({'original_dispositions': dispositions, 'verdict': 'PENDING independent review'}))
        ref = {'path': str(report), 'sha256': hashlib.sha256(report.read_bytes()).hexdigest()}
        self.record = {'schema_version': 1, 'unit_id': 'test',
                       'source': {'base': base, 'commit': base, 'tree': tree,
                                  'paths': self.bind(self.paths), 'deleted_paths': []},
                       'constituents': [{'id': 'test-original', 'head': head, 'delta_base': base,
                                         'dispositions': dict(ref, json_pointer='/original_dispositions')}],
                       'inputs': {'runtime': self.bind(['data/input.txt']),
                                  'helpers': self.bind(['scripts/helper.py']),
                                  'parents': self.bind(['docs/PARENT.md']), 'context': [],
                                  'tooling': self.bind(APIS)},
                       'reviewer': {'session': 'independent-session', 'report': ref, 'references': []},
                       'non_science_notes': [],
                       'notes': [{'path': 'docs/NOTE.md', 'claim_id': 'note', 'declared_claim_id': 'note', 'claim_type': 'bounded_theorem',
                                  'primary_runner': 'scripts/primary.py', 'helpers': ['scripts/helper.py'],
                                  'citations': ['docs/PARENT.md'], 'repository_dependencies': ['docs/PARENT.md'],
                                  'dependency_rationale': 'Supplied model parent is load-bearing.'}]}

    def write(self, name, text):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], stderr=subprocess.PIPE).decode().strip()

    def hash(self, name):
        return hashlib.sha256((self.repo / name).read_bytes()).hexdigest()

    def bind(self, names):
        return [{'path': p, 'sha256': self.hash(p)} for p in names]

    def check(self, record=None, cache=False):
        path = self.home / 'unit.json'
        path.write_text(json.dumps(record or self.record))
        command = [sys.executable, str(TOOL), '--repo', str(self.repo), '--record', str(path)]
        if cache:
            command.append('--cache')
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertTrue(result.stdout, result.stderr)
        return result.returncode, json.loads(result.stdout)

    def invalid(self, record=None, contains=None):
        status, result = self.check(record)
        self.assertEqual(status, 1)
        self.assertEqual(result['mechanical_status'], 'invalid')
        if contains:
            self.assertIn(contains, result['error'])

    def test_valid_does_not_promote_pending_review(self):
        before = Path(self.record['reviewer']['report']['path']).read_bytes()
        status, result = self.check()
        self.assertEqual(status, 0, result)
        self.assertEqual(result['mechanical_status'], 'ok')
        self.assertNotIn('verdict', result)
        self.assertEqual(before, Path(self.record['reviewer']['report']['path']).read_bytes())

    def test_input_drift(self):
        self.write('data/input.txt', 'drift\n')
        self.invalid(contains='hash changed')

    def test_stale_index_even_with_updated_working_hash(self):
        self.write('data/input.txt', 'drift\n')
        self.record['inputs']['runtime'] = self.bind(['data/input.txt'])
        self.invalid(contains='unstaged tracked changes')

    def test_undeclared_packet_helper(self):
        self.record['notes'][0]['helpers'] = []
        self.invalid(contains='packet helper')

    def test_missing_runtime_binding(self):
        self.record['inputs']['runtime'] = []
        self.invalid(contains='undeclared receipt input')

    def test_disposition_path_mapping(self):
        path = Path(self.record['constituents'][0]['dispositions']['path'])
        content = json.loads(path.read_text())
        content['original_dispositions'][0]['original_path'] = 'docs/WRONG.md'
        path.write_text(json.dumps(content))
        h = hashlib.sha256(path.read_bytes()).hexdigest()
        self.record['constituents'][0]['dispositions']['sha256'] = h
        self.record['reviewer']['report']['sha256'] = h
        self.invalid(contains='disposition path mapping')

    def test_changed_reviewer_evidence_rejected(self):
        Path(self.record['reviewer']['report']['path']).write_text('{}')
        self.invalid(contains='evidence hash changed')

    def test_unknown_version_and_missing_category(self):
        self.record['schema_version'] = 2
        self.invalid(contains='schema version')
        self.record['schema_version'] = 1
        del self.record['inputs']['context']
        self.invalid(contains='context')

    def test_explicit_empty_model_dependencies_requires_rationale(self):
        self.record['notes'][0]['repository_dependencies'] = []
        self.record['notes'][0]['dependency_rationale'] = 'Parent citation is contextual; proof is self-contained.'
        status, result = self.check()
        self.assertEqual(status, 0, result)
        self.record['notes'][0]['dependency_rationale'] = ''
        self.invalid(contains='rationale')

    def test_ambiguous_canonical_alias(self):
        registry = 'docs/audit/data/axiom_premise_nodes.json'
        self.write(registry, json.dumps({'nodes': {'note': {'aliased_paths': ['docs/NOTE.md', 'docs/PARENT.md']}}}))
        self.git('add', registry)
        self.record['source']['tree'] = self.git('write-tree')
        self.record['source']['paths'] += self.bind([registry])
        self.record['inputs']['context'] = self.bind([registry])
        self.invalid(contains='ambiguous/noncanonical')

    def test_noncanonical_id_and_missing_cache(self):
        self.record['notes'][0]['claim_id'] = 'invented'
        self.invalid(contains='claim ID')
        self.record['notes'][0]['claim_id'] = 'note'
        status, result = self.check(cache=True)
        self.assertEqual(status, 1)
        self.assertIn('cache not fresh', result['error'])

    def add_source(self, name, body):
        self.write(name, body)
        self.git('add', name)
        self.record['source']['tree'] = self.git('write-tree')
        self.record['source']['paths'] += self.bind([name])

    def test_differing_packet_resolver_rejected(self):
        # Change only the fixture packet API to simulate a real resolver mismatch.
        name = 'scripts/audit_packet_script_deps.py'
        self.write(name, (self.repo / name).read_text() + '\ndef transitive_helpers(primary_script, seen=None): return {"packet_only"}\n')
        self.git('add', name)
        self.record['source']['tree'] = self.git('write-tree')
        self.record['source']['paths'] += self.bind([name])
        self.record['inputs']['tooling'] = self.bind(APIS)
        self.invalid(contains='packet/graph helper discovery disagreement')

    def test_packet_missing_graph_helper_rejected(self):
        name = 'scripts/audit_packet_script_deps.py'
        self.write(name, (self.repo / name).read_text() + '\ndef transitive_helpers(primary_script, seen=None): return set()\n')
        self.git('add', name)
        self.record['source']['tree'] = self.git('write-tree')
        self.record['source']['paths'] += self.bind([name])
        self.record['inputs']['tooling'] = self.bind(APIS)
        self.invalid(contains='packet/graph helper discovery disagreement')

    def test_process_only_explicit_disposition(self):
        self.record['notes'] = []
        self.invalid(contains='uncovered changed/runner-affected')
        self.record['non_science_notes'] = [{'path': 'docs/NOTE.md',
            'rationale': 'Reviewer explicitly classifies this fixture as historical process documentation.',
            'review_reference': self.record['reviewer']['report']}]
        status, result = self.check()
        self.assertEqual(status, 0, result)

    def test_omitted_changed_note_rejected(self):
        self.add_source('docs/SECOND.md', '# Science\n**Type:** bounded_theorem\n')
        self.invalid(contains='uncovered changed/runner-affected')

    def test_explicit_historical_disposition(self):
        self.add_source('docs/HISTORY.md', '# Historical prose\n')
        self.record['non_science_notes'] = [{'path': 'docs/HISTORY.md',
            'rationale': 'Immutable historical narrative, no current executable claim.',
            'review_reference': self.record['reviewer']['report']}]
        status, result = self.check()
        self.assertEqual(status, 0, result)
        self.record['non_science_notes'][0]['rationale'] = ''
        self.invalid(contains='non-science rationale')

    def test_runner_affected_unchanged_note_rejected(self):
        # The unchanged parent begins using the changed helper through its primary.
        self.write('docs/PARENT.md', '# Parent\n**Type:** bounded_theorem\nRunner: `scripts/primary.py`\n')
        self.git('add', 'docs/PARENT.md')
        self.git('commit', '-qm', 'fixture inherited parent')
        current = self.git('rev-parse', 'HEAD')
        self.record['source']['commit'] = current
        # Base contains that note but the proposal compares to its own baseline;
        # use a changed helper against this committed state.
        self.record['source']['base'] = current
        self.write('scripts/helper.py', 'AUDIT_TIMEOUT_SEC=30\ndef run(): return 2\n')
        self.git('add', 'scripts/helper.py')
        self.record['source']['tree'] = self.git('write-tree')
        self.record['source']['paths'] = self.bind(['scripts/helper.py'])
        self.record['inputs']['runtime'] += self.bind(['docs/NOTE.md', 'scripts/primary.py'])
        self.record['inputs']['helpers'] = self.bind(['scripts/helper.py'])
        self.record['inputs']['parents'] = self.bind(['docs/PARENT.md'])
        # New immutable disposition addendum maps the changed helper.
        old = Path(self.record['reviewer']['report']['path'])
        report = json.loads(old.read_text())
        report['original_dispositions'][2]['final_sha256'] = self.hash('scripts/helper.py')
        new = self.home / 'affected-review.json'
        new.write_text(json.dumps(report))
        self.record['constituents'][0]['dispositions'] = {'path':str(new),
            'sha256':hashlib.sha256(new.read_bytes()).hexdigest(), 'json_pointer':'/original_dispositions'}
        self.invalid(contains='uncovered changed/runner-affected')

    def test_legacy_declared_id_is_explicit_path_mapping(self):
        self.record['notes'][0]['declared_claim_id'] = 'unmapped'
        self.invalid(contains='declared-to-canonical')
        # A differing legacy identifier is legitimate when the actual bytes are
        # explicitly mapped; no source rewrite or canonical-ID alias is invented.
        body = (self.repo / 'docs/NOTE.md').read_text().replace('claim_id: note', 'claim_id: legacy-short')
        self.write('docs/NOTE.md', body)
        self.git('add', 'docs/NOTE.md')
        self.record['source']['tree'] = self.git('write-tree')
        self.record['source']['paths'] = self.bind(self.paths)
        report = json.loads(Path(self.record['reviewer']['report']['path']).read_text())
        report['original_dispositions'][0]['final_sha256'] = self.hash('docs/NOTE.md')
        new = self.home / 'mapping-review.json'
        new.write_text(json.dumps(report))
        self.record['constituents'][0]['dispositions'] = {'path':str(new),
            'sha256':hashlib.sha256(new.read_bytes()).hexdigest(), 'json_pointer':'/original_dispositions'}
        self.record['notes'][0]['declared_claim_id'] = 'legacy-short'
        status, result = self.check()
        self.assertEqual(status, 0, result)


class MemoizationTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('receipt_under_test', TOOL)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        (self.repo / 'scripts').mkdir()
        self.path = self.repo / 'scripts/input.py'
        self.path.write_text('before')
        self.calls = {'graph':0, 'packet':0, 'inputs':0}
        def graph(path):
            self.calls['graph'] += 1
            return {'helper'}
        def packet(path):
            self.calls['packet'] += 1
            return {'helper'}
        def inputs(path):
            self.calls['inputs'] += 1
            return ('data.txt',)
        self.graph = SimpleNamespace(_parse_script_imports=graph)
        self.packet = SimpleNamespace(parse_script_imports=packet)
        self.cache = SimpleNamespace(declared_input_paths=inputs)
        self.originals = (graph,packet,inputs)

    def context(self):
        return self.module.memoized_discovery(self.repo,self.graph,self.cache,self.packet)

    def assert_restored(self):
        self.assertIs(self.graph._parse_script_imports,self.originals[0])
        self.assertIs(self.packet.parse_script_imports,self.originals[1])
        self.assertIs(self.cache.declared_input_paths,self.originals[2])

    def test_counts_fresh_copies_and_per_invocation_lifetime(self):
        with self.context() as (stats, observe):
            value=self.graph._parse_script_imports(self.path)
            value.add('caller mutation')
            for _ in range(4):
                self.assertEqual(self.graph._parse_script_imports(self.path),{'helper'})
                self.packet.parse_script_imports(self.path)
                self.cache.declared_input_paths('scripts/input.py')
            self.assertEqual(self.calls,{'graph':1,'packet':1,'inputs':1})
            self.assertEqual(stats['graph_imports']['hits'],4)
        self.assert_restored()
        with self.context():
            self.graph._parse_script_imports(self.path)
        self.assertEqual(self.calls['graph'],2)

    def test_existing_discovery_drift_and_restore(self):
        with self.assertRaisesRegex(ValueError,'discovery input changed'):
            with self.context():
                self.graph._parse_script_imports(self.path)
                self.path.write_text('changed after discovery')
        self.assert_restored()

    def test_absent_discovery_input_appears(self):
        absent=self.repo/'scripts/absent.py'
        with self.assertRaisesRegex(ValueError,'discovery input changed'):
            with self.context():
                self.graph._parse_script_imports(absent)
                absent.write_text('now present')
        self.assert_restored()

    def test_unreturned_missing_import_appears(self):
        # Actual parsers filter missing import targets, so directory generation
        # must also catch a target that never appeared in their result set.
        with self.assertRaisesRegex(ValueError,'discovery input changed'):
            with self.context():
                self.graph._parse_script_imports(self.path)
                (self.repo/'scripts/previously_missing.py').write_text('new')
        self.assert_restored()

    def test_restore_on_body_failure(self):
        with self.assertRaisesRegex(RuntimeError,'caller failure'):
            with self.context():
                self.graph._parse_script_imports(self.path)
                raise RuntimeError('caller failure')
        self.assert_restored()

    def test_change_inside_actual_api_rejected(self):
        def changing(path):
            path.write_text('changed during actual parser')
            return set()
        self.graph._parse_script_imports=changing
        with self.assertRaisesRegex(ValueError,'discovery input changed'):
            with self.context():
                self.graph._parse_script_imports(self.path)
        self.assertIs(self.graph._parse_script_imports,changing)


if __name__ == '__main__':
    unittest.main()
