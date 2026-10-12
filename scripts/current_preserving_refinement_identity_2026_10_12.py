#!/usr/bin/env python3
"""Exact source identity/reconstruction only; zero mathematical calculations."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json
import sys

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-current-preserving-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-current-preserving-20261012/PARENT_BINDINGS.json', '.claude/science/physics-loops/toe-current-preserving-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-current-preserving-20261012/author/CURRENT_PRESERVING_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/CORE_FREEZE.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/FINAL_APPENDIX.diff.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/FINAL_CORE_ERRATUM.diff.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/FINAL_IDENTITY_CHECK.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/FINAL_RECEIPT.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/PLAN.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/PLAN_FREEZE.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/RECOVERY.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/ROOT_EXPOSURE.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/comparison_source.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/final_manifest.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/frozen/CURRENT_PRESERVING_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instruction_inventory.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/MINIMAL_AXIOMS_2026-06-29.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/SCIENCE_WORKFLOW.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/no-go-discipline/SKILL.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/physics-loop/SKILL.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/physics-loop/references/CLAIM_STATUS.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/physics-loop/references/DELIVERY.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/physics-loop/references/DISCOVERY.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/ai_methodology/skills/review-loop/SKILL.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/instructions/docs/audit/data/axiom_premise_nodes.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/seal_packet.py.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/source_inventory.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/sources/CONCRETE_GAPPED_CHAIN_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/sources/CURRENT_PRESERVING_ROOT_RECONSTRUCTION.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/sources/ENERGY_ADAPTED_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/sources/LOCAL_EVEN_CONTINUUM_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/sources/SHARP_CURRENT_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/author/current_preserving_refinement/statement_search.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/CURRENT_PRESERVING_PUBLICATION_PARENT_RECEIPT.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/CURRENT_PRESERVING_REFINEMENT_MILESTONE_GATE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/CURRENT_PRESERVING_REFINEMENT_REVIEW.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/CURRENT_PRESERVING_ROOT_RECONSTRUCTION.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/CURRENT_PRESERVING_ROOT_RECONSTRUCTION_SEAL.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/Current_preserving_refinement_root_analytic_read.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/Current_preserving_refinement_root_review_coverage.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/CHECKPOINT.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/FINAL_IDENTITY_REFRESH.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/FINAL_REVIEW_RECEIPT.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/INDEPENDENT_FINDINGS.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/INDEPENDENT_PLAN.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/SECTION_COMPARISON_ADDENDUM.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/SECTION_COMPARISON_ADDENDUM.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_final/CURRENT_PRESERVING_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_final/EXPOSURE.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_final/FINAL_APPENDIX.diff.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_final/FINAL_CORE_ERRATUM.diff.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_final/REVIEWER_COMPLETE_FINAL.diff.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_final/final_manifest.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_snapshot/CORE_FREEZE.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_snapshot/CURRENT_PRESERVING_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/author_snapshot/EXPOSURE.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/independent_seal.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/AGENTS.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/docs/ai_methodology/SCIENCE_WORKFLOW.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/docs/ai_methodology/skills/no-go-discipline/SKILL.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/docs/ai_methodology/skills/workhorse/SKILL.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/instructions/execution_AGENTS.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/source_manifest.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/sources/CONCRETE_GAPPED_CHAIN_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/sources/ENERGY_ADAPTED_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_refinement_review/sources/LOCAL_EVEN_CONTINUUM_PROBE.md.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/current_preserving_worktree_creation/receipts.json.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/finalize_current_preserving_root_gate.py.gz', '.claude/science/physics-loops/toe-current-preserving-20261012/review_and_root/sharp_current_delivery/FINAL.json.gz', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md']
PACKET = '.claude/science/physics-loops/toe-current-preserving-20261012'
NOTE = 'docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md'
AUTHOR_SHA = '1104de3922002720beecb7eb2bd106b64025aea0afb1e11b8f86750dfb59e30d'
MAP_SHA = '3fe6b6d3d384a714bee33059be0d01ac08207838aaf124f0b09bdb90071d9e7d'
EDITS_SHA = '7d8c849e34f9677a7f61ee719535770f4bed95ed144a8bbf1d5fb25cfbf0aa69'
PARENTS_SHA = 'e15f6783884a1fe00f856fbd1e7171c23d3f7527e53f880e6719fa7707032bc1'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify(root):
    reads = []
    def read(name):
        relative = PurePosixPath(name)
        need(not relative.is_absolute() and '..' not in relative.parts, 'Unsafe input path')
        path = root.joinpath(*relative.parts)
        need(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root),
             'Input missing or outside repository')
        reads.append(name)
        return path.read_bytes()
    raw_map = read(PACKET + '/EVIDENCE_MAP.json')
    need(sha(raw_map) == MAP_SHA, 'Archive map identity changed')
    rows = json.loads(raw_map)['files']
    need(len({r['original_path'] for r in rows}) == len(rows) and
         len({r['path'] for r in rows}) == len(rows), 'Duplicate archive path')
    contents = {}
    for row in rows:
        stored = read(PACKET + '/' + row['path'])
        need(sha(stored) == row['stored_sha256'], 'Stored archive changed')
        data = gzip.decompress(stored)
        need(sha(data) == row['sha256'] and len(data) == row['bytes'], 'Archived bytes changed')
        contents[row['original_path']] = data
    authors = [data for name, data in contents.items()
               if name.endswith('/resume_20261011/CURRENT_PRESERVING_REFINEMENT_PROBE.md')]
    need(len(authors) == 1 and sha(authors[0]) == AUTHOR_SHA, 'Final author source changed')
    author = authors[0]
    need(author.startswith(b'---\n'), 'Author metadata absent')
    end = author.find(b'\n---\n', 4)
    need(end > 0, 'Author metadata delimiter absent')
    body = author[end + 5:]
    edits_raw = read(PACKET + '/PUBLICATION_EDITS.json')
    need(sha(edits_raw) == EDITS_SHA, 'Publication transformation changed')
    edits = json.loads(edits_raw)
    need(sha(body) == edits['body_sha256'] and edits['author_sha256'] == AUTHOR_SHA,
         'Exact body identity changed')
    need(read(NOTE) == edits['header'].encode() + body + edits['appendix'].encode(),
         'Publication does not reconstruct byte-exactly')
    parents_raw = read(PACKET + '/PARENT_BINDINGS.json')
    need(sha(parents_raw) == PARENTS_SHA, 'Parent bindings changed')
    parents = json.loads(parents_raw)['parents']
    need(len(parents) == 2, 'Scientific dependency scope changed')
    for parent in parents:
        need(sha(read(parent['path'])) == parent['published_sha256'], 'Published parent changed')
    need(set(reads) == set(AUDIT_INPUT_PATHS), 'Declared read closure differs')
    return {'result': 'source_identities_and_reconstruction_match',
        'meaning': 'Source integrity only; no mathematical correctness check was executed.',
        'mathematical_operations_executed': False,
        'independent_review_supplied_by_tool': False,
        'no_go_packet_pass_supplied_by_tool': False,
        'external_scientific_input_reads': [p['path'] for p in parents],
        'package_local_integrity_reads': sorted(set(reads) - {p['path'] for p in parents})}


def main():
    print(json.dumps(verify(Path(__file__).resolve().parents[1]), sort_keys=True))
    print('per_element: checked and not executed — source integrity only; no coefficient or Jacobian calculation was executed.')
    print('per_site: checked and not executed — source integrity only; no spin, cell or Jordan–Wigner calculation was executed.')
    print('per_mode: checked and not executed — source integrity only; no spectral branch, phase, multiplicity or endpoint calculation was executed.')
    print('per_block: checked and not executed — source integrity only; no finite-block CAR or scientific mutation test was executed.')
    print('lattice_wide: checked and not executed — source integrity only; no inductive-limit, locality or actual-time proof was executed.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'result': 'identity_verification_incomplete', 'error': str(error),
                          'mathematical_operations_executed': False}), file=sys.stderr)
        raise SystemExit(1)
