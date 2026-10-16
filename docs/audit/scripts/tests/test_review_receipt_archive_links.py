"""Receipt provenance links remain bound, contained and non-authoritative."""
from pathlib import Path
from types import SimpleNamespace
import importlib.util
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[4]
TOOL = ROOT / 'docs/ai_methodology/skills/review-loop/scripts/review_receipt.py'
spec = importlib.util.spec_from_file_location('receipt_archive_test', TOOL)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
class ArchiveLinkTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name).resolve()
        self.source = self.repo / 'docs/NOTE.md'; self.source.parent.mkdir()
        self.source.write_text('source')
        self.name = '.claude/science/campaign/review record.md'
        self.archive = self.repo / self.name; self.archive.parent.mkdir(parents=True)
        self.archive.write_text('historical record')
        self.graph = SimpleNamespace(resolve_link_target=lambda target, source: None)
    def valid(self, target, bound=None):
        return m.valid_source_reference(self.repo, self.graph, target, self.source,
                                        {self.name: 'receipt hash'} if bound is None else bound)
    def test_bound_relative_archive_and_url_encoding(self):
        self.assertTrue(self.valid('../' + self.name))
        self.assertTrue(self.valid('../' + self.name.replace(' ', '%20')))
    def test_missing_or_unbound_archive(self):
        self.assertFalse(self.valid('../' + self.name, {}))
        self.archive.unlink(); self.assertFalse(self.valid('../' + self.name))
    def test_directory_is_not_source(self):
        name = str(self.archive.parent.relative_to(self.repo))
        self.assertFalse(self.valid('../' + name, {name: 'hash'}))
    def test_absolute_or_escaped_archive_rejected(self):
        self.assertFalse(self.valid(str(self.archive)))
        self.assertFalse(self.valid('../../outside.md', {'../outside.md': 'hash'}))
    def test_symlink_outside_archive_rejected(self):
        actual = self.repo / 'unreviewed.md'; actual.write_text('other')
        self.archive.unlink(); self.archive.symlink_to(actual)
        self.assertFalse(self.valid('../' + self.name, {self.name: 'hash', 'unreviewed.md': 'hash'}))
    def test_unresolved_canonical_and_other_repo_paths_stay_invalid(self):
        other = self.repo / 'README.md'; other.write_text('root')
        self.assertFalse(self.valid('../README.md', {'README.md': 'hash'}))
        self.assertFalse(self.valid('MISSING.md', {'docs/MISSING.md': 'hash'}))
    def test_existing_graph_resolution_keeps_its_contract(self):
        self.graph.resolve_link_target = lambda target, source: self.source
        self.assertTrue(self.valid('NOTE.md', {}))
if __name__ == '__main__': unittest.main()
