"""Exercise the real pipeline shell with fixture producers and a real Git index."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
MANIFEST = 'docs/audit/data/citation_graph_manifest.json'


class PipelineManifestStagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        scripts = self.root / 'docs/audit/scripts'
        scripts.mkdir(parents=True)
        shutil.copyfile(ROOT / 'docs/audit/scripts/run_pipeline.sh', scripts / 'run_pipeline.sh')
        (self.root / MANIFEST).parent.mkdir()
        (self.root / MANIFEST).write_text('old\n')
        (self.root / 'unrelated.txt').write_text('old\n')
        self.git('init', '-q')
        self.git('add', '--', MANIFEST, 'unrelated.txt')
        (self.root / 'unrelated.txt').write_text('do not stage\n')
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        stub = self.bin / 'python3'
        stub.write_text(f'#!{sys.executable}\n' + '''import os, sys, subprocess
from pathlib import Path
args = sys.argv[1:]
with open('calls.log', 'a') as log:
    log.write(' '.join(args) + '\\n')
name = Path(args[0]).name
if name == 'write_citation_graph_manifest.py':
    Path('docs/audit/data/citation_graph_manifest.json').write_text('new\\n')
    if os.environ.get('FAIL_GENERATION'):
        sys.exit(9)
elif name == 'compute_load_bearing.py' and os.environ.get('EXPECT_STAGED'):
    indexed = subprocess.check_output(['git', 'show', ':docs/audit/data/citation_graph_manifest.json'], text=True)
    sys.exit(0 if indexed == 'new\\n' else 7)
elif name == 'repo_invariants_check.py':
    indexed = subprocess.check_output(['git', 'show', ':docs/audit/data/citation_graph_manifest.json'], text=True)
    expected = 'old\\n' if os.environ.get('EXPECT_OLD') else 'new\\n'
    sys.exit(0 if indexed == expected else 8)
elif args[0] == '-':
    print(0)
elif args[0] == '-c':
    print('fixture-nonce')
elif name == 'static_pipeline_checkpoint.py' and args[-1] == 'identity':
    print('fixture-nonce')
''')
        stub.chmod(0o755)

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args], text=True)

    def run_pipeline(self, *args, **extra):
        env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ['PATH'], **extra)
        return subprocess.run(['bash', 'docs/audit/scripts/run_pipeline.sh', *args],
                              cwd=self.root, env=env, text=True, capture_output=True)

    def calls(self):
        p = self.root / 'calls.log'
        return p.read_text() if p.exists() else ''

    def test_opt_in_stages_fresh_manifest_before_invariant_only(self):
        result = self.run_pipeline('--stage-citation-manifest', EXPECT_STAGED='1')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.git('show', ':' + MANIFEST), 'new\n')
        self.assertEqual(self.git('show', ':unrelated.txt'), 'old\n')
        calls = self.calls()
        self.assertEqual(calls.count('run_citation_graph_build.py'), 1)
        self.assertEqual(calls.count('write_citation_graph_manifest.py'), 1)
        self.assertLess(calls.index('write_citation_graph_manifest.py'), calls.index('repo_invariants_check.py'))

    def test_default_does_not_stage_generated_manifest(self):
        result = self.run_pipeline(EXPECT_OLD='1')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.git('show', ':' + MANIFEST), 'old\n')
        self.assertEqual((self.root / MANIFEST).read_text(), 'new\n')

    def test_verdict_only_preserves_index_and_skips_graph_generation(self):
        result = self.run_pipeline('--verdict-only', EXPECT_OLD='1')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn('run_citation_graph_build.py', self.calls())
        self.assertNotIn('write_citation_graph_manifest.py', self.calls())
        self.assertEqual(self.git('show', ':' + MANIFEST), 'old\n')

    def test_failed_generation_never_stages_or_reaches_invariant(self):
        result = self.run_pipeline('--stage-citation-manifest', FAIL_GENERATION='1')
        self.assertEqual(result.returncode, 9, result.stdout + result.stderr)
        self.assertEqual(self.git('show', ':' + MANIFEST), 'old\n')
        self.assertNotIn('repo_invariants_check.py', self.calls())

    def test_failed_staging_stops_before_downstream_work(self):
        lock = self.root / '.git/index.lock'
        lock.write_text('locked')
        result = self.run_pipeline('--stage-citation-manifest')
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('compute_load_bearing.py', self.calls())
        self.assertNotIn('repo_invariants_check.py', self.calls())
        self.assertEqual(self.git('show', ':' + MANIFEST), 'old\n')

    def test_invalid_options_fail_before_pipeline_effects(self):
        for args in [('--unknown',), ('--verdict-only', '--stage-citation-manifest'),
                     ('--stage-citation-manifest', '--verdict-only'),
                     ('--stage-citation-manifest', '--stage-citation-manifest')]:
            with self.subTest(args=args):
                result = self.run_pipeline(*args)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(self.calls(), '')
                self.assertEqual(self.git('show', ':' + MANIFEST), 'old\n')


if __name__ == '__main__':
    unittest.main()
