from pathlib import Path
import importlib.util
import unittest
import sys
TOOL = Path(__file__).resolve().parents[1] / 'build_citation_graph.py'
sys.path.insert(0, str(TOOL.parent))
spec = importlib.util.spec_from_file_location('frontmatter_graph_test', TOOL)
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
class FrontmatterTypeTests(unittest.TestCase):
    def test_leading_frontmatter(self):
        self.assertEqual(g.extract_claim_type_hint('---\nclaim_type: bounded_theorem\n---\n# Note'), ('bounded_theorem', 'bounded_theorem'))
    def test_prose_precedence_unchanged(self):
        self.assertEqual(g.extract_claim_type_hint('---\nclaim_type: no_go\n---\nClaim type: bounded_theorem'), ('bounded_theorem', 'bounded_theorem'))
    def test_nested_or_later_metadata_not_used(self):
        for s in ['intro\n---\nclaim_type: bounded_theorem\n---', '---\n  claim_type: bounded_theorem\n---', '---\ntarget_claim_type: bounded_theorem\n---']:
            self.assertEqual(g.extract_claim_type_hint(s), (None,None))
    def test_duplicate_or_unclosed_metadata(self):
        for s in ['---\nclaim_type: bounded_theorem\nclaim_type: no_go\n---', '---\nclaim_type: bounded_theorem']:
            self.assertEqual(g.extract_claim_type_hint(s), (None,None))
    def test_unknown_not_promoted(self):
        self.assertEqual(g.extract_claim_type_hint('---\nclaim_type: audited_clean\n---'), ('audited_clean',None))
    def test_existing_prose_and_no_hint(self):
        self.assertEqual(g.extract_claim_type_hint('**Claim type:** bounded theorem'), ('bounded theorem','bounded_theorem'))
        self.assertEqual(g.extract_claim_type_hint('ordinary prose'), (None,None))
if __name__ == '__main__': unittest.main()
