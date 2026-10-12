#!/usr/bin/env python3
"""Source identity/reconstruction support only. No mathematical proof execution.

No symbolic algebra, numeric predicates, scientific mutations, or flow/domain
checks are performed. An exit status of zero means the named bytes agree only.
"""
from pathlib import Path, PurePosixPath
import hashlib
import gzip
import json
import sys

AUDIT_TIMEOUT_SEC = 60
# Replaced by source generation with every actual integrity-read file and the
# two scientific parent notes. No helper-runner or policy registry is needed.
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-sharp-current-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-sharp-current-20261012/PARENT_BINDINGS.json', '.claude/science/physics-loops/toe-sharp-current-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-sharp-current-20261012/REVIEW_EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-sharp-current-20261012/author/SHARP_CURRENT_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/CHECKPOINT.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/NO_GO_LEDGER.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/PLAN.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/PLAN_CHRONOLOGY_CLARIFICATION.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/PROOF_MAP.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/README.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/analytic_freeze.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/cross_cycle_search.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/cross_cycle_search.stderr.txt.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/cross_cycle_search.stdout.txt.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/final_manifest.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/final_receipt.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/frozen/PLAN.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/frozen/SHARP_CURRENT_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/hidden_premise_scan.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/hidden_premise_scan_final.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/instruction_refresh.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/instructions/docs/ai_methodology/SCIENCE_WORKFLOW.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/instructions/docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/instructions/docs/ai_methodology/skills/ai-physics-lane-builder/SKILL.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/instructions/docs/ai_methodology/skills/no-go-discipline/SKILL.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/instructions/docs/ai_methodology/skills/physics-loop/SKILL.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/instructions/docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/parent_final_refresh.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/plan_freeze.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/source_inventory.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/sources/CONCRETE_GAPPED_CHAIN_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/sources/DYADIC_EVEN_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/sources/ENERGY_ADAPTED_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/sources/LOCAL_EVEN_CONTINUUM_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/sources/SHARP_CURRENT_REFINEMENT_ROUTE_BRIEF.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/author/sharp_current_refinement/sources/STATE_ADAPTED_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/SHARP_CURRENT_REFINEMENT_MILESTONE_GATE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/SHARP_CURRENT_REFINEMENT_REVIEW.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/Sharp_current_refinement_root_review_coverage.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/finalize_sharp_current_root_gate.py.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/CHECKPOINT.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/FINAL_RECEIPT.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/FROZEN_PLAN.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/INDEPENDENT_FINDINGS_SEALED.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/PACKET_RECONCILIATION.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/NO_GO_LEDGER.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/PLAN.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/PLAN_CHRONOLOGY_CLARIFICATION.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/PROOF_MAP.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/README.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/analytic_freeze.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/final_manifest.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/final_receipt.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/parent_final_refresh.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/plan_freeze.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/author_packet_snapshots/source_inventory.json.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/frozen_sources/CONCRETE_GAPPED_CHAIN_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/frozen_sources/ENERGY_ADAPTED_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/frozen_sources/LOCAL_EVEN_CONTINUUM_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/frozen_sources/SHARP_CURRENT_REFINEMENT_PROBE.md.gz', '.claude/science/physics-loops/toe-sharp-current-20261012/review/sharp_current_refinement_review/manifest.json.gz', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/SHARP_CURRENT_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md']
PACKET = '.claude/science/physics-loops/toe-sharp-current-20261012'
NOTE = 'docs/SHARP_CURRENT_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md'
AUTHOR_SHA256 = '2a6948ab1d98584ac77b3486f8ec1927d88fbb55cd0276123b6c24750f9d6a42'
MANIFEST_SHA256 = 'd704de97de804fa72b4968c1f8bab0197f5b2df3bdadc2d2204f67d2c3565433'
MAP_SHA256 = '07214f374c263ba1534053f5de60bb45a9bdd30d45604a12b807bdc975531136'
REVIEW_MAP_SHA256 = '341b0812172c014772a71284715d0577c278e799758bdc188d7c3931a67ee6ca'
EDITS_SHA256 = '23d351ead76b84340d9252151eb7bbcba50907b50b5073ee149e94bc1769145b'
PARENT_BINDINGS_SHA256 = '50901fb4518f942df508da46883740cad8d59fe5fdb6682e6fc6bd8d5c98565b'


def need(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_read(root, name):
    relative = PurePosixPath(name)
    need(not relative.is_absolute() and '..' not in relative.parts,
         'Nonportable declared path')
    target = root.joinpath(*relative.parts)
    need(target.is_file() and not target.is_symlink(), 'Missing regular input')
    need(target.resolve().is_relative_to(root.resolve()), 'Input escaped root')
    return target.read_bytes()


def verify(root):
    reads = []
    def read(name):
        data = safe_read(root, name)
        reads.append(name)
        return data
    mapped = read(PACKET + '/EVIDENCE_MAP.json')
    need(digest(mapped) == MAP_SHA256, 'Evidence-map identity changed')
    rows = json.loads(mapped)['files']
    need(len({r['original_path'] for r in rows}) == len(rows), 'Duplicate original')
    need(len({r['path'] for r in rows}) == len(rows), 'Duplicate portable path')
    contents = {}
    for row in rows:
        stored = read(PACKET + '/' + row['path'])
        need(digest(stored) == row['stored_sha256'], 'Stored archive changed')
        data = gzip.decompress(stored)
        need(digest(data) == row['sha256'] and len(data) == row['bytes'],
             'Archived source identity changed: ' + row['path'])
        contents[row['original_path']] = data
    review_raw = read(PACKET + '/REVIEW_EVIDENCE_MAP.json')
    need(digest(review_raw) == REVIEW_MAP_SHA256, 'Review evidence map changed')
    for row in json.loads(review_raw)['files']:
        stored = read(PACKET + '/' + row['path'])
        need(digest(stored) == row['stored_sha256'], 'Stored review archive changed')
        data = gzip.decompress(stored)
        need(digest(data) == row['sha256'] and len(data) == row['bytes'],
             'Review source identity changed')
    def original(suffix):
        matches = [value for name, value in contents.items() if name.endswith(suffix)]
        need(len(matches) == 1, 'Ambiguous archived original: ' + suffix)
        return matches[0]
    author = original('/resume_20261011/SHARP_CURRENT_REFINEMENT_PROBE.md')
    need(digest(author) == AUTHOR_SHA256, 'Exact author note changed')
    manifest = original('/sharp_current_refinement/final_manifest.json')
    need(digest(manifest) == MANIFEST_SHA256, 'Exact author manifest changed')
    for original_path, expected in json.loads(manifest)['files'].items():
        need(original_path in contents and digest(contents[original_path]) == expected,
             'Original complete manifest does not reconstruct')
    source_inventory = json.loads(original('/sharp_current_refinement/source_inventory.json'))
    for row in source_inventory['sources']:
        need(digest(contents[row['copy']]) == row['sha256'], 'Parent archive changed')
    edits_raw = read(PACKET + '/PUBLICATION_EDITS.json')
    need(digest(edits_raw) == EDITS_SHA256, 'Publication edit specification changed')
    edits = json.loads(edits_raw)
    need(author.startswith(b'---\n'), 'Original frontmatter absent')
    end = author.find(b'\n---\n', 4)
    need(end > 0, 'Original frontmatter delimiter absent')
    body = author[end + 5:]
    need(digest(body) == edits['body_sha256'], 'Exact scientific body changed')
    expected = edits['header'].encode() + body + edits['appendix'].encode()
    need(read(NOTE) == expected, 'Publication does not reconstruct exactly')
    parent_raw = read(PACKET + '/PARENT_BINDINGS.json')
    need(digest(parent_raw) == PARENT_BINDINGS_SHA256,
         'Published parent bindings are unsealed or changed')
    bindings = json.loads(parent_raw)
    need(len(bindings['parents']) == 2, 'Scientific parent scope changed')
    for row in bindings['parents']:
        need(digest(read(row['path'])) == row['published_sha256'],
             'Published parent identity changed')
    need(set(reads) == set(AUDIT_INPUT_PATHS), 'Declared read closure differs')
    return {
        'result': 'source_identities_and_reconstruction_match',
        'meaning': 'Integrity result only; mathematical correctness not executed or established.',
        'mathematical_operations_executed': False,
        'external_scientific_input_reads': [r['path'] for r in bindings['parents']],
        'package_local_integrity_reads': sorted(set(reads) - {r['path'] for r in bindings['parents']}),
        'independent_review_supplied_by_tool': False,
        'no_go_packet_pass_supplied_by_tool': False,
    }


def main():
    result = verify(Path(__file__).resolve().parents[1])
    print(json.dumps(result, sort_keys=True))
    print('per_element: checked and not executed — source integrity only; no coefficient-vector or polynomial identity calculation was executed.')
    print('per_site: checked and not executed — source integrity only; no local spin, Jordan–Wigner or per-site current calculation was executed.')
    print('per_mode: checked and not executed — source integrity only; no spectral packet, endpoint, phase or momentum-mode calculation was executed.')
    print('per_block: checked and not executed — source integrity only; no finite-block CAR test, norm estimate or scientific mutation was executed.')
    print('lattice_wide: checked and not executed — source integrity only; no infinite-operator proof, sharp bound, continuum limit or flow theorem was executed.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'result': 'identity_verification_incomplete',
                          'error': str(error), 'mathematical_operations_executed': False}), file=sys.stderr)
        raise SystemExit(1)
