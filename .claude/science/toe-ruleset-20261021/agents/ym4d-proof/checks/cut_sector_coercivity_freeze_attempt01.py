#!/usr/bin/env python3
"""Packaging only. No mathematical or numerical test is performed by this file."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
assert Path.cwd() == ROOT, 'Run only in the assigned worktree.'
L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
B = L / 'checks'
PREFIX = 'cut_sector_coercivity_'
SOURCE = L / 'CUT_SECTOR_COERCIVITY_ASTRA.md'
RECEIPT = B / (PREFIX + 'receipt.json')
# A rerun must not silently restamp a frozen packet.
assert not RECEIPT.exists(), 'Receipt exists: frozen packet must remain immutable.'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def entry(p, **kw):
    p = Path(p)
    return {'path': str(p), 'sha256': digest(p), 'bytes': p.stat().st_size, **kw}

def save(name, obj):
    p = B / (PREFIX + name + '.json')
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + '\n')
    return p

cc_receipt = B / 'covariant_complement_receipt.json'
cc_review_receipt = B / 'review_covariant_complement_receipt.json'
assert digest(cc_receipt) == 'a9536686abb45d8f5fae790fd0c7685ce159a1a0f961cd8cdcd5145fb31d22d4'
assert digest(cc_review_receipt) == '75a01dfe36e64f83db7886528169cddac63bfd2e12258d40313b4504dc05e6bd'
cc = json.loads(cc_receipt.read_text())
cc_review = json.loads(cc_review_receipt.read_text())
for x in cc['artifacts'] + cc_review['owned_files']:
    assert digest(x['path']) == x['sha256'], 'Frozen predecessor changed: ' + x['path']

old_read_path = B / 'review_covariant_complement_read_manifest.json'
old_read = json.loads(old_read_path.read_text())
reused_methodology = []
for x in old_read['methodology']:
    assert digest(x['path']) == x['sha256'], 'Methodology/context changed: ' + x['path']
    reused_methodology.append({**x, 'reuse': 'Already read in this same continuous worker session during the completed CC review; unchanged bytes verified. Preserve its stated partial/full coverage.'})

coverage = {
    'PROCESS_LIGHT.md': ('Full, read again for this author assignment.', 'governing_process'),
    'ASSUMPTIONS_AND_IMPORTS.md': ('Full during prior CC review; unchanged input reused. Supplied model, not framework-axiom derivation.', 'premise_boundary'),
    'PROOF.md': ('Exact model definitions at1158-1218 and2214-2284, read during prior CC review; no whole-file certification.', 'original_model_definition'),
    'COVARIANT_COMPLEMENT_ASTRA.md': ('Complete527-line frozen source and own complete review during prior assignment. Rebuilt the cut-cap argument locally as CS17-CS20; other CC evidence is context, not tests of this unit.', 'cut_cap_predecessor_rebuilt'),
    'REVIEW_COVARIANT_COMPLEMENT_ASTRA.md': ('Complete own prior review, bounded LAND. Same author/reviewer identity disclosed; this is not independent review of the new CS source.', 'predecessor_review_only'),
    'COVARIANT_SOFT_BACKGROUND_ASTRA.md': ('Lines1-215 and410-490. Exact tree variables/reference/paired geometry and G-to-chart CB21-CB24, with supplied domain retained. No whole-source rereview.', 'model_and_scoped_chart_input'),
    'REVIEW_COVARIANT_SOFT_BACKGROUND_ASTRA.md': ('Complete during CC review; unchanged. Only previously reviewed bounded background/chart scope is consumed.', 'scoped_upstream_review'),
    'COVARIANT_SOURCE_ACTIVITY_ASTRA.md': ('Lines1-316,337-375,508-635 across current reads and prior unchanged reads. Includes SA13-SA15 critical branch/row bound/actual fixed sector and SA32-SA33 complementary consumer. Remaining implementation/evidence not rereviewed.', 'scoped_upstream_SA13_SA15_and_consumer'),
    'REVIEW_COVARIANT_SOURCE_ACTIVITY_ASTRA.md': ('Complete review read, including its conditional/selected-sector limits. Its numerical claims were read as predecessor evidence and not rerun or adopted as new CS checks.', 'scoped_upstream_review'),
    'SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md': ('Complete mathematical source throughH28, lines1-730, during prior CC review; unchanged bytes reused. CS33 uses H24 only under its exact completion/source/u domain and full failure-reader exclusion.', 'scoped_upstream_H24'),
    'REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md': ('Complete during prior CC review; unchanged. No broadened H24 domain or integrated return inferred.', 'scoped_upstream_review'),
    'SOURCE_SEA_CONSTRUCTION_ASTRA.md': ('Lines1-365 during prior CC review; current exact205-239 and390-431. Integrated sea/chessboard inputs do not provide fixed-V normalization; no Sea tail theorem imported.', 'prior_art_scope_comparison'),
    'STEP55.md': ('Current115-278,544-574,656-697. Includes linear local charge proof, conditional nonlinear chart argument, pointwise mismatch price and overriding errata. No numerical outputs or banked BFT conclusion adopted.', 'prior_art_scope_comparison'),
    'CODEX_REVIEW_STEP.md': ('Current24-57, relevant R7/R8 in130-215 (batch partly truncated after the relevant discussion), exact R12 at228-245. No complete-file review claimed.', 'prior_art_scope_comparison'),
    'NODEA55.md': ('Initial1-170 orientation with a truncated early paragraph; actual SPEC/LT83-170 read. Fixed-volume Laplace context only; no uniform construction imported.', 'prior_art_scope_comparison'),
    'NODEA_RES55.md': ('Current160-239,355-405,480-525. Tilt/Peierls requirements and open normalization, not numerical certificates or audit status.', 'prior_art_scope_comparison'),
    'RLARGE.md': ('270-310 and880-925 from unchanged prior CC reads, plus bounded keyword searches. Pointwise/coarse-law tail context, not a fixed-V local normalization theorem.', 'prior_art_scope_comparison'),
}
inputs = [entry(L / name, read_coverage=cov, role=role) for name, (cov, role) in coverage.items()]
new_methodology_specs = [
    ('/Users/jonBridger/.codex/skills/physics-loop/SKILL.md', 'Full installed skill read for new author work; PROCESS_LIGHT and coordinator file boundary override generic branch/packaging tasks.'),
    ('docs/ai_methodology/skills/physics-loop/references/DISCOVERY.md', 'Applicable full discovery/proof-search and empirical discriminator guidance, completed with300-434 after initial batch.'),
    ('docs/ai_methodology/skills/physics-loop/references/CLAIM_STATUS.md', 'Full336-line claim/premise status reference.'),
    ('docs/ai_methodology/skills/physics-loop/references/DELIVERY.md', 'Full, assembled from1-210 and211-309; coordinator owns publication/shared campaign records.'),
    ('docs/repo/REPO_ORGANIZATION.md', 'Full current organization/navigation guidance; history is not scientific authority.'),
]
new_methodology = [entry(p, read_coverage=c) for p,c in new_methodology_specs]
external = [
    {
        'title': 'Tadeusz Balaban, Large Field Renormalization II: Localization, Exponentiation, and Bounds for the R Operation, CMP122 (1989)',
        'url': 'https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf',
        'coverage': 'Fresh primary scan, web extracted lines0-86 (printed355-356 and beginning357) and1707-1768 (tail387 through beginning389, connected localization/activity setup around1.90-1.94). Not the complete38-page paper.',
        'use': 'Motivates normalization and connected-region obligations. Hard-block minimizers, inductive densities and running-coupling assumptions are not identified with this original soft-cut law; no external theorem/constant inserted.',
        'binary_downloaded': False, 'binary_hash_claimed': False,
    },
    {
        'title': 'J. Dimock, The Renormalization Group According to Balaban - II. Large Fields, arXiv1212.5562v2',
        'url': 'https://arxiv.org/html/1212.5562v2',
        'coverage': 'Fresh primary HTML lines1-85,114-131,1964-1983, including large-field penalty discussion and Lemma3.15 localization around covariance square roots. Prior CC AppendixF3090-3155 read is context only. Not the complete paper.',
        'use': 'Scalar d=3 action penalty/coupling/support-localization distinctions; not an import of a hard Yang-Mills complement theorem.',
        'binary_downloaded': False, 'binary_hash_claimed': False,
    },
]
read_manifest = save('read_manifest', {
    'created_utc': NOW,
    'source': entry(SOURCE),
    'methodology_revision_supplied_and_fetched': 'ca2bc7ddf64790da96cd43d42017d000fbfe4808',
    'source_inputs': inputs,
    'new_methodology_reads': new_methodology,
    'reused_methodology_reads': reused_methodology,
    'external_primary_reads': external,
    'predecessor_immutability': {
        'author_receipt': entry(cc_receipt), 'author_artifacts_verified': len(cc['artifacts']),
        'review_receipt': entry(cc_review_receipt), 'review_artifacts_verified': len(cc_review['owned_files']),
        'prior_read_manifest': entry(old_read_path),
        'literature_register': 'Author CC read snapshot282318... and the old review navigation/status distinction remain as frozen. No current literature-register status is a mathematical input to this CS unit.',
    },
    'exposure': 'Same worker previously reviewed CC and read its checker after independently freezing those review checks. New CS source has no new mathematical checker or numerical results. No author independence from the previous CC review is claimed. Fresh independent review of this new author unit is pending.',
    'not_consumed': ['SOFTHARD R3 actual hard construction (still OPEN)', 'Concurrent REC_CONT source/review as a CS premise', 'A global Gaussian replacement or selected-sector denominator', 'A main/audit retained verdict for this source'],
    'search_scope': {
        'local': 'Bounded rg statement searches in STEP55/NODEA/H/Sea/CB/CC and related lane notes before selecting this normalized producer; exact loci above. No matching original-law conditional cap comparison found in this inspected scope; no exhaustive novelty claim.',
        'main': 'One early authority fetch and read-only git grep at unchanged mainca2bc7... found no matched original-cut/soft-kernel coercivity or tail entry within searched docs/*.md and lane/*.md. No commit/push/branch/index operations.',
        'navigation': 'Narrow searches of lane registry/status board; no retained-value or audit standing imported.',
    },
})
process = save('process', {
    'created_utc': NOW,
    'author_identity': '/root/review_covariant_complement; requested Astra/max, same Codex family; no independent backend attestation',
    'ownership': ['CUT_SECTOR_COERCIVITY_ASTRA.md', 'checks/cut_sector_coercivity_*'],
    'objective': 'Produce the next original fixed-V cut-law local energy/normalization interface toward SA actual G-minus-Omega and G-complement; full4D existence and physical continuum mass gap remain open.',
    'approaches': [
        {'name': 'Complete nonlinear block/brick fillings plus exact centered kernel phase', 'result': 'CS7-CS14 absolute local coercivity. Does not assert energy above U0, Hessian positivity, or a normalized sector price.'},
        {'name': 'Original-Haar product cap at the actual local conditional minimizer', 'result': 'CS17-CS21 normalized excess-energy tail, arbitrary admissible exterior, with CC epsilon1 ceiling and per-local-region polynomial.'},
        {'name': 'Original-Haar reference cap with squared path-distance majorant', 'result': 'CS22-CS29 normalized event comparison with actual local reference and full boundary-reader cost, no extra cut ceiling; cannot assert the cost is absorbable for arbitrary exterior.'},
        {'name': 'Global reference cap', 'result': 'Not pursued as closure: whole-volume curvature cost does not solve a connected localized complement.'},
        {'name': 'Actual white-cube to free-link witness', 'result': 'CS30-CS32 conditional deterministic bridge retains curvature margin, full colour matrix, and loss of witness location; hard-event connected support still open.'},
    ],
    'preregistration': 'No new numerical experiment was proposed or run. PROCESS_LIGHT requires preregistration for numerical work; this is an analytic proof unit. Mechanical hash/link/equation-label checks are not mathematical evidence.',
    'mathematical_evidence': 'Displayed analytic derivations CS1-CS29; CS30-CS33 explicitly scoped implications from frozen SA/CB/H. Independent review required, no formal proof or audit certification claimed.',
    'self_review': [
        'Full source cold read, checking every local variable/reader collar, nonabelian filling count, root mismatch, compact cap, denominator and source domain.',
        'Clarified C subset C_R/full brick plaquettes inside P_R; retained exact weighted local curvature in CS27 before its uniform bound.',
        'Distinguished source-independent exterior selection from the varying real indicator A_ref^e<=b; no varying-indicator holomorphy claimed.',
        'No acceptance criterion changed and no new mathematical numerical failure exists. Previous CC failures/results unchanged and not counted as CS evidence.',
    ],
    'operational_records': [
        'Initial contextual read of nonexistent NODEA.md failed; actual NODEA55.md was located and read.',
        'Historical docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md path was absent during a narrow navigation search; no numerical target/value was consumed from it.',
        'Some combined read outputs truncated; exact operative proof loci were reread or partial coverage is explicitly recorded. No complete-file claim for partially read sources.',
        'Only early authority fetch/read-only Git search was used; no commit, push, branch or index operation. New author files only; coordinator lock read only.',
    ],
    'trace_gate': {
        'trace_class': 'upstream_support', 'target_claim_id': None,
        'target_blocker_text': 'A connected, normalized price for SA actual G\\Omega and G^c at fixed coarse V with correct source and reader domains.',
        'source_of_blocker_text': 'handoff', 'reachability_to_target': 'supports', 'artifact_role': 'theorem',
        'next_trace_action': 'Fresh hostile review; then organize connected bad regions with paid local collar/reference costs and localize hard whitened-cube witnesses in the actual original-source support norm.',
    },
    'remaining': ['Boundary-cost absorption under the actual correlated exterior law', 'Connected bad-region organization and full support-size hard-event localization', 'Complex nonvanishing and source logarithm of1+B_comp', 'Retained-failure and normalized higher-level returns', 'Nonlinear RG, continuum existence and physical continuum mass gap'],
    'independent_review_status': 'PENDING',
    'claim_status': 'Author proposed bounded-support theorem; no retained/audit/whole-PR verdict',
    'resource_scope': 'No numerical jobs. Packaging is short single-process Python stdlib I/O/hashing, not a scientific diagnostic. No worker pool or memory-heavy computation.',
    'coordinator_lock_snapshot': json.loads(Path('logs/physics_worker_lock.json').read_text()),
})
text = SOURCE.read_text()
labels = sorted(set(int(x) for x in re.findall(r'\(CS(\d+)\)', text)))
assert labels == list(range(1, 34)), labels
assert text.endswith('\n')
assert not any(line.rstrip() != line for line in text.splitlines())
links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text)
local_links = []
for link in links:
    if link.startswith(('https://', 'http://')):
        continue
    target = SOURCE.parent / link.split('#')[0]
    assert target.exists() or target == RECEIPT, 'Missing source link: ' + link
    local_links.append({'link': link, 'resolved': str(target), 'exists_or_planned_receipt': True})
verification = save('verification', {
    'created_utc': NOW,
    'classification': 'MECHANICAL ONLY; does not test or certify mathematics',
    'source_sha256': digest(SOURCE), 'source_lines': len(text.splitlines()),
    'equation_labels_present': labels, 'newline_and_trailing_whitespace': 'pass',
    'local_links': local_links,
    'predecessor_author_artifacts_unchanged': len(cc['artifacts']),
    'predecessor_review_artifacts_unchanged': len(cc_review['owned_files']),
    'new_numerical_runs': 0, 'new_numerical_acceptance_predicates': 0,
    'independent_review': 'pending',
})
owned = [SOURCE, Path(__file__).relative_to(ROOT), read_manifest, process, verification]
receipt = {
    'format': 'source-and-evidence-freeze-v1; not a canonical review integration receipt',
    'created_utc': NOW,
    'author_source': entry(SOURCE),
    'owned_files': [entry(p) for p in owned],
    'input_pins': inputs,
    'predecessor_receipt_pins': [entry(cc_receipt), entry(cc_review_receipt)],
    'evidence': 'Pure analytic source; mechanical checks only. No new numerical evidence. Fresh independent review pending.',
    'scope': 'CS1-CS29 local coercivity and normalized conditional comparison with retained costs; CS30-CS33 scoped upstream implications. No connected full complement or continuum/gap conclusion.',
    'immutability': 'Freeze all five bound artifacts plus this receipt. Receipt self-hash is reported separately; no self-referential hash or automatic restamp.',
}
RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + '\n')
print(json.dumps({'source_sha256': digest(SOURCE), 'receipt_sha256': digest(RECEIPT), 'owned_files_plus_receipt': len(owned)+1, 'source_lines': len(text.splitlines()), 'input_files': len(inputs), 'status': 'frozen_for_fresh_independent_review'}, sort_keys=True))
