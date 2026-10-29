"""Bind this review's source coverage and preserve its complete diagnostic history.

This is packaging validation, not a mathematical proof or a repository audit gate.
Never execute the diagnostic mutants from this script.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
L = ROOT / '.claude/science/toe-ruleset-20261021/agents/ym4d-proof'
C = L / 'checks'
REV = 'ca2bc7ddf64790da96cd43d42017d000fbfe4808'
OLD = '4a8afc90247d771b95c9661737dc08509456ab28'
NOTE = L / 'CROSSOVER_LITERATURE_BRIDGE_ASTRA.md'
REPORT = L / 'REVIEW_CROSSOVER_LITERATURE_BRIDGE_ASTRA.md'
MANIFEST = C / 'review_crossover_import_read_manifest.json'
VALIDATION = C / 'review_crossover_import_packaging_01.json'
RECEIPT = C / 'review_crossover_import_receipt.json'

assert Path.cwd() == ROOT
assert not any(p.exists() for p in (MANIFEST, VALIDATION, RECEIPT)), 'Preserve an existing attempt; use additive names.'

def digest(b):
    return hashlib.sha256(b).hexdigest()

def rel(p):
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)

def binding(p):
    b = p.read_bytes()
    return {'path': rel(p), 'sha256': digest(b), 'bytes': len(b)}

def git_bytes(rev, path):
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], cwd=ROOT)

def write(p, d):
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n')

now = datetime.now(timezone.utc).isoformat()
full_governance = [
    'AGENTS.md',
    'docs/ai_methodology/SCIENCE_WORKFLOW.md',
    'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',
    'docs/ai_methodology/skills/review-loop/SKILL.md',
    'docs/ai_methodology/skills/review-loop/references/REVIEW_SETUP.md',
    'docs/ai_methodology/skills/review-loop/references/REVIEW_UNITS.md',
    'docs/ai_methodology/skills/review-loop/references/SCIENCE_LENSES.md',
    'docs/ai_methodology/skills/review-loop/references/FIXES_AND_REPORTING.md',
    'docs/ai_methodology/skills/review-loop/references/AUDIT_COMPATIBILITY.md',
    'docs/ai_methodology/skills/physics-loop/SKILL.md',
    'docs/ai_methodology/skills/physics-loop/references/CLAIM_STATUS.md',
    'docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md',
    'docs/ai_methodology/skills/physics-loop/references/literature-bridge-protocol.md',
    'docs/ai_methodology/skills/no-go-discipline/SKILL.md',
    'docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md',
    'docs/audit/data/axiom_premise_nodes.json',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md',
    'docs/repo/REVIEW_FEEDBACK_WORKFLOW.md',
    'docs/repo/DEFERRED_DECISIONS.md',
]
partial_governance = {
    'docs/repo/ACTIVE_REVIEW_QUEUE.md': 'Lines 1–85; selected routing context only.',
    'docs/repo/CONTROLLED_VOCABULARY.md': 'Lines 1–120; selected vocabulary context only.',
    'docs/CANONICAL_HARNESS_INDEX.md': 'Lines 1–20; index routing only, no theorem/status adoption.',
    'docs/audit/README.md': 'Lines 1–100; authority boundary only.',
    'docs/ai_methodology/skills/physics-loop/references/DISCOVERY.md': 'Partial displayed text in a truncated read; not complete campaign workflow coverage. Reviewer did not execute a discovery campaign.',
}
governance = []
for path in full_governance + list(partial_governance):
    b = git_bytes(REV, path)
    governance.append({
        'path': path, 'revision': REV, 'sha256': digest(b), 'bytes': len(b),
        'read_scope': partial_governance.get(path, 'Complete text, including supplements to initially truncated reads.'),
        'role': 'Methodology or registered-premise context; no imported Yang–Mills dynamics.',
    })

kirk_pdf = Path('/tmp/ym-review-massgap-block-research-20261029/review_massgap_block_kirk_v4.pdf')
kirk_txt = kirk_pdf.with_suffix('.txt')
ar_pdf = Path('/tmp/ym-crossover-import-research-20261029/abdesselam_rivasseau_9409094v1.pdf')
ar_txt = ar_pdf.with_suffix('.txt')
primary = [
    {
        'name': 'Kirk, fixed compact-simple-group Yang–Mills manuscript, version 4',
        'url': 'https://zenodo.org/records/21765806',
        'version': 'Zenodo v4 dated 2026-08-02; PDF header dated 2026-08-03; 118 PDF pages.',
        'files': [binding(kirk_pdf), binding(kirk_txt)],
        'text_line_ranges_read': [[56,134],[1120,1727],[2140,2270],[2550,2592],[3900,4215],[4320,4445],[4640,4745],[5080,5185],[7460,7695]],
        'passages': ['Fixed-group conventions and normalization', 'Lemmas 3.22–3.27, Theorems 3.28/3.31', 'Corollary 4.2 and related Gaussian estimates', 'Section 4.6 tree weights', 'Sections 6.6–6.13 and row (44)', 'Lemma 6.22/(59)', 'Lemma 6.30', 'Corollary 6.40, Lemma 6.41, Theorem 6.43', 'Appendix A.18–A.20 including (233)'],
        'role': 'Candidate import screen at named printed inferences; no theorem imported as established Yang–Mills closure.',
        'limits': 'Not the whole paper. Search matches and truncated broad output do not imply full manuscript reading. Actual optical trace/source hypotheses and complete support-weight dependency proofs remain unverified.',
    },
    {
        'name': 'Abdesselam–Rivasseau, Trees, forests and jungles: a botanical garden for cluster expansions',
        'url': 'https://arxiv.org/abs/hep-th/9409094v1',
        'version': 'arXiv v1, 1994-09-16; 36 PDF pages.',
        'files': [binding(ar_pdf), binding(ar_txt)],
        'text_line_ranges_read': [[1,1655],[2335,2510]],
        'passages': ['Forest identity and proof', 'Taylor formulation III.1', 'Jungle induction IV.1 and Taylor form IV.3', 'Covariance positivity IV.5', 'Section V.E, printed pp.31–33, and the start of V.F'],
        'role': 'Literature theorem/organization with stated application hypotheses, not an imported Yang–Mills amplitude estimate.',
        'limits': 'Other applications and remaining sections were not fully read. Finite polynomial and positivity diagnostics are controls, not a model-specific convergence proof.',
    },
]
source_reads = [
    dict(binding(NOTE), read_scope='Original complete note, then every affected correction paragraph; no adjacent source unit is certified.'),
    dict(binding(L/'MASS_GAP_TARGET.md'), read_scope='Complete target: both full continuum existence and physical mass gap remain open.'),
    dict(binding(C/'crossover_import_exact.py'), read_scope='Complete, after independent implementation and its two retained runs.'),
    dict(binding(C/'crossover_import_exact_v2.py'), read_scope='Original complete runner plus complete additive correction diff, after independent scaled-mark run.'),
    dict(binding(C/'crossover_import_manifest.json'), read_scope='Structured metadata, source/version map and relevant fields; author read assertions are not inherited as reviewer coverage.'),
    dict(binding(C/'crossover_import_freeze.json'), read_scope='Complete frozen bindings; verified at entry and preservation rechecked at final packaging.'),
    dict(binding(C/'crossover_import_control_fix_receipt.json'), read_scope='Complete repair bindings and original-preservation fields; pending-review wording is historical and not edited by reviewer.'),
]
write(MANIFEST, {
    'schema': 'scoped-independent-review-source-coverage-v1', 'created_utc': now,
    'reviewer': '/root/review_crossover_bridge',
    'configuration': 'Owner-requested Astra/max, same-family fresh reviewer context; no claim of blinded or cross-family review.',
    'methodology_revision': REV,
    'methodology_freshness': 'Coordinator-supplied immutable current-main snapshot, fresh at 17:11 UTC; reviewer did not independently refresh remote main.',
    'governance_reads': governance,
    'primary_source_reads': primary,
    'source_reads': source_reads,
    'additional_web_metadata_read': {
        'url': 'https://github.com/ethanwsussman/Yang--Mills-LLM-experiment',
        'scope': 'README tentative research status and manuscript listing only; no proof imported or repository commit pinned.',
    },
    'not_claimed': ['Whole Kirk manuscript review', 'Actual Karcher optical-matrix counterexample', 'Actual many-pivot Wilson reference activity', 'Full support-weight dependency closure', 'Complete discovery/delivery workflow execution', 'Combined validation or current-main preservation gate', 'Canonical unit receipt or audit authority'],
    'read_scope_semantics': 'Human/model read assertions plus byte bindings; hashes do not prove reading or mathematical validity.',
})

checks = []
def check(name, ok, detail=None):
    checks.append({'name': name, 'passed': bool(ok), 'detail': detail})

check('corrected_source_pin', digest(NOTE.read_bytes()) == 'c0f118a5228fffd8c2841d0a254328d722c4083629427ffd176a8fc4747b835a')
check('corrected_runner_pin', digest((C/'crossover_import_exact_v2.py').read_bytes()) == '15139682cffba6fa1df2cd2beca6268b91b686a956d3546654b8bc786e929eb4')
freeze = json.loads((C/'crossover_import_freeze.json').read_text())
for item in freeze['artifacts']:
    p = ROOT/item['path']
    b = git_bytes(OLD, item['path']) if p == NOTE else p.read_bytes()
    check('preserved_original:' + p.name, digest(b) == item['sha256'], 'Original note checked at immutable commit; other artifacts checked in place.')
check('original_freeze_pin', digest((C/'crossover_import_freeze.json').read_bytes()) == '63ff7f8680d5f36c1e3d5f1021eb839cd4599854a6bc814a440b87356271689f')
check('primary_kirk_pdf_pin', digest(kirk_pdf.read_bytes()) == 'b91c6c2b9ba7cd4d5476aa6a2e823569507682c24cf103933ff9f97c73260bed')
check('primary_ar_pdf_pin', digest(ar_pdf.read_bytes()) == '6498535d584bd935cd3d57f565d9c662c4fccbba31f623850431d2de3b4d8bee')

for p in sorted(C.glob('review_crossover_import_*.py')):
    try:
        compile(p.read_text(), str(p), 'exec')
        check('python_syntax:' + p.name, True)
    except Exception as e:
        check('python_syntax:' + p.name, False, str(e))
for p in sorted(C.glob('review_crossover_import_*.json')):
    try:
        json.loads(p.read_text())
        check('json_parse:' + p.name, True)
    except Exception as e:
        check('json_parse:' + p.name, False, str(e))
for url in re.findall(r'\]\(([^)]+)\)', REPORT.read_text()):
    if '://' not in url:
        p = REPORT.parent / url.split('#',1)[0]
        check('local_link:' + url, p.exists() or p == RECEIPT)

old_result = json.loads((C/'crossover_import_attempt01.stdout.json').read_text())
new_result = json.loads((C/'crossover_import_attempt02.stdout.json').read_text())
check('replay_bytes_match_author', (C/'review_crossover_import_v2_replay.stdout.json').read_bytes() == (C/'crossover_import_attempt02.stdout.json').read_bytes())
check('old_79_records_preserved', all(item in new_result['checks'] for item in old_result['checks']) and len(old_result['checks']) == 79)
for number, expected in [('01', (298,300)), ('02', (300,300))]:
    d = json.loads((C/f'review_crossover_import_independent_{number}.stdout.json').read_text())
    check('independent_history_' + number, (d['checks_passed'], d['checks_total']) == expected)
mark = json.loads((C/'review_crossover_import_mark_admission_01.stdout.json').read_text())
check('mark_history_19_of_19', mark.get('passed') == 19 and mark.get('total') == 19, list(mark))
affected = json.loads((C/'review_crossover_import_affected_02.json').read_text())
check('four_affected_mutations_rejected', len(affected['records']) == 5 and affected['all_mutations_rejected'] and affected['exact_replay_matches_author'])
write(VALIDATION, {'schema': 'review-packaging-validation-v1', 'created_utc': now, 'checks': checks, 'all_passed': all(x['passed'] for x in checks), 'scope': 'Syntax, identity, evidence preservation and report-link checks only. No scientific or audit status promotion.'})

outputs = [REPORT] + [p for p in sorted(C.glob('review_crossover_import_*')) if p.is_file() and p != RECEIPT]
write(RECEIPT, {
    'schema': 'scoped-reviewer-confirmation-v1', 'created_utc': now,
    'reviewer': '/root/review_crossover_bridge', 'configuration': 'Owner-requested Astra/max; same-family fresh context',
    'cwd': str(ROOT), 'command': [sys.executable, rel(Path(__file__).resolve())],
    'methodology_revision': REV,
    'review_status': 'Affected source confirmed; two material findings corrected; no unresolved material finding in examined unit.',
    'findings': {'CIB-R1': 'resolved in same reviewer session', 'CIB-R2': 'resolved in same reviewer session'},
    'original_source': {'revision': OLD, 'path': rel(NOTE), 'sha256': 'de024b1d6df4a959fb85b2743be2141e93446e735a8ebe6672ff8f28f233e33f'},
    'corrected_source': binding(NOTE), 'corrected_runner': binding(C/'crossover_import_exact_v2.py'),
    'root_repair_receipt': binding(C/'crossover_import_control_fix_receipt.json'),
    'diagnostics': {'independent_attempt01': '298/300; two quadrature tolerance failures preserved', 'independent_attempt02': '300/300 with explicit 1e-60 quadrature tolerance', 'independent_scaled_mark': '19/19 before revised runner read', 'author_v2_replay': '93/93 exact match', 'original_author_mutations': '7 rejected, 1 survived and caused CIB-R1', 'affected_v2_mutations': '4/4 rejected'},
    'packaging_validation_all_passed': all(x['passed'] for x in checks),
    'artifacts': [binding(p) for p in outputs],
    'scope_limits': {'continuum_existence': 'OPEN', 'physical_continuum_mass_gap': 'OPEN', 'closed_mass_gap_rows': [], 'negative_route_packet_pass': False, 'whole_paper_verdict': False, 'whole_pr_pass': False, 'audit_verdict_applied': False, 'git_mutations_by_reviewer': False, 'canonical_unit_receipt': False, 'combined_pipeline_owner': '/root'},
    'self_binding': 'Receipt excludes its own hash; return its hash to the coordinator for an external binding.',
})
print(json.dumps({'report': binding(REPORT), 'read_manifest': binding(MANIFEST), 'validation': binding(VALIDATION), 'receipt': binding(RECEIPT), 'packaging_all_passed': all(x['passed'] for x in checks), 'failed': [x for x in checks if not x['passed']]}, indent=2))
raise SystemExit(0 if all(x['passed'] for x in checks) else 1)
