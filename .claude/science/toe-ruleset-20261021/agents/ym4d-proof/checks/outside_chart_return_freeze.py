#!/usr/bin/env python3
"""Freeze identity/read evidence only. This is not a numerical physics test."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path('/Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972')
L = ROOT / '.claude/science/toe-ruleset-20261021/agents/ym4d-proof'
C = L / 'checks'
PREFIX = 'outside_chart_return_'
SOURCE = L / 'OUTSIDE_CHART_RETURN_ASTRA.md'
EXPECTED_SOURCE = 'f8e5ac755f106cf9419f81d3d3f683949c59abfe4f8ad1a250795fa6ec1c58d4'
NOW = datetime.now(timezone.utc).isoformat()


def rel(p):
    p = Path(p)
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def pin(p):
    p = Path(p)
    if not p.is_absolute():
        p = ROOT / p
    data = p.read_bytes()
    return {'path': rel(p), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def verify(record):
    got = pin(record['path'])
    assert got['sha256'] == record['sha256'], (record['path'], record['sha256'], got)
    if 'bytes' in record:
        assert got['bytes'] == record['bytes'], (record['path'], 'byte count')
    return got


def load(p):
    return json.loads(Path(p).read_text())


def write_new(name, value):
    target = C / name
    assert target.name.startswith(PREFIX)
    with target.open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, sort_keys=True)
        stream.write('\n')


receipt_path = C / (PREFIX + 'receipt.json')
assert not receipt_path.exists(), 'A frozen receipt must never be overwritten.'
source = pin(SOURCE)
assert source['sha256'] == EXPECTED_SOURCE
source_freeze = load(C / (PREFIX + 'source_freeze.json'))
assert source == source_freeze['source'] | {} or source == {
    k: source_freeze['source'][k] for k in ('path', 'bytes', 'sha256')
}
assert len(SOURCE.read_text().splitlines()) == source_freeze['source']['lines'] == 641

gc_manifest = load(C / 'graded_complement_read_manifest.json')
old_inputs = {Path(x['path']).name: x for x in gc_manifest['source_inputs']}
methodology = []
for row in gc_manifest['reused_methodology_reads']:
    verify(row)
    methodology.append(dict(row, reuse_in_this_unit='Same continuous worker; exact unchanged bytes verified. Original coverage retained; no new full-read assertion.'))
assert len(methodology) == 27

# These four complete predecessor packets are never modified or restamped.
predecessors = []
predecessor_owned_count = 0
for name, key, expected in [
    ('covariant_complement_receipt.json', 'artifacts', 21),
    ('review_covariant_complement_receipt.json', 'owned_files', 29),
    ('cut_sector_coercivity_receipt.json', 'owned_files', 9),
    ('review_cut_sector_coercivity_receipt.json', 'owned_files', 5),
]:
    path = C / name
    data = load(path)
    assert len(data[key]) == expected
    for row in data[key]:
        verify(row)
    predecessor_owned_count += expected
    predecessors.append({'receipt': pin(path), 'owned_records_verified': expected,
                         'coverage': 'Identity verification of every bound artifact; not a new read or rerun of scientific evidence.'})
assert predecessor_owned_count == 64

# GC has a reviewed coordinator-only wording correction, not unexplained drift.
gc_receipt = load(C / 'graded_complement_receipt.json')
gc_correction = load(C / 'graded_complement_distance_correction.json')
gc_current = pin(L / 'GRADED_COMPLEMENT_ASTRA.md')
assert gc_current['sha256'] == gc_correction['source_after_sha256'] == '22e30738d5d59adc65c146c7e9fa3bd671462d694a7ae1fe14e73804774e5341'
gc_text = (L / 'GRADED_COMPLEMENT_ASTRA.md').read_text()
change = gc_correction['exact_change']
assert gc_text.count(change['after']) == 1
historical_bytes = gc_text.replace(change['after'], change['before'], 1).encode()
assert hashlib.sha256(historical_bytes).hexdigest() == gc_correction['source_before_sha256'] == '6201ec6ec1846e205dd1a3d7dd1df1a3bebb9c6bead14874aff40482d2bb0335'
assert len(historical_bytes) == 31357
non_source_gc = []
for row in gc_receipt['owned_files']:
    if Path(row['path']).name == 'GRADED_COMPLEMENT_ASTRA.md':
        assert row['sha256'] == gc_correction['source_before_sha256']
    else:
        non_source_gc.append(verify(row))
assert len(non_source_gc) == 6
non_source_gc.append(pin(C / 'graded_complement_receipt.json'))
gc_review_receipt = load(C / 'review_graded_complement_receipt.json')
for row in gc_review_receipt['owned_files']:
    verify(row)
assert len(gc_review_receipt['owned_files']) == 8

def input_row(name, coverage, use, inherited=True):
    result = pin(L / name)
    if inherited and name in old_inputs:
        verify(old_inputs[name])
        result['inherited_read_coverage'] = old_inputs[name].get('read_coverage', '')
        result['older_inherited_coverage'] = old_inputs[name].get('inherited_coverage', '')
    result['read_coverage_in_this_unit'] = coverage
    result['use'] = use
    return result

inputs = [
    input_row('PROCESS_LIGHT.md', 'Complete governing process reused, exact bytes verified.', 'Analytic author lane and fresh independent review requirement.'),
    input_row('CUT_SECTOR_COERCIVITY_ASTRA.md', 'Complete617-line author/source coverage inherited; current1-475 reread and lower-energy/cap/reference steps reconstructed.', 'Actual quotient, localized coercivity, exact compact normalizer and Haar cap; no normalized tail imported.'),
    input_row('REVIEW_CUT_SECTOR_COERCIVITY_ASTRA.md', 'Complete independent review read before this author sequence; unchanged.', 'Scoped LAND and exterior/reference limitations.'),
    input_row('COVARIANT_COMPLEMENT_ASTRA.md', 'Complete527-line source read in this worker\'s completed earlier CC review; unchanged.', 'Original cut/kernel/history producer context; evidence not rerun.'),
    input_row('REVIEW_COVARIANT_COMPLEMENT_ASTRA.md', 'Complete own earlier review reused.', 'Same-worker exposure disclosed, bounded scope and failures preserved.'),
    input_row('COVARIANT_SOFT_BACKGROUND_ASTRA.md', 'Unchanged prior1-330 and410-490 coverage reused.', 'Actual zero-source reference, local readers and CB13 background bound.'),
    input_row('REVIEW_COVARIANT_SOFT_BACKGROUND_ASTRA.md', 'Complete prior review reused.', 'Bounded background/chart scope only.'),
    input_row('COVARIANT_SOURCE_ACTIVITY_ASTRA.md', 'Current298-340 reread; previous1-316,337-375,508-635 and GC ranges retained.', 'Actual zero-source affine whitening/cube, uniform scalar row norms and the two original complementary integrals.'),
    input_row('REVIEW_COVARIANT_SOURCE_ACTIVITY_ASTRA.md', 'Complete prior review reused.', 'Selected-sector limits, no full complement imported.'),
    input_row('SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md', 'Current430-550 reread; unchanged complete mathematical1-730 throughH28 inherited.', 'H8 joint insertion and H24 actual positive gas; exact domain and complete failure-reader exclusion.'),
    input_row('REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md', 'Complete prior review reused.', 'No broad history/complex normalization inferred.'),
    input_row('SOURCE_SEA_CONSTRUCTION_ASTRA.md', 'Prior1-365 and390-431 coverage reused; no new full read.', 'Recognize pre-return sea and joint-replacement gap; not an input tail theorem.'),
    input_row('FIXED_SOURCE_RADIUS_ASTRA.md', 'Current25-110 reread; corrected source1-210 and412-550 inherited.', 'Unchanged actual sector and fixed source domain; only corrected FR9 polynomial scope, not a general full-Gaussian forest claim.'),
    input_row('REVIEW_FIXED_SOURCE_RADIUS_ASTRA.md', 'Complete prior review read.', 'Bounded review context and fixed-source limits.'),
    input_row('checks/fixed_source_radius_domain_correction.json', 'Complete metadata read in prior unit, exact identity verified.', 'Historical FR source correction remains separately bound.', inherited=False),
    input_row('checks/review_fixed_source_radius_domain_confirmation.json', 'Complete affected confirmation reread during this package.', 'Affected confirmation only, not a new whole FR review.', inherited=False),
    input_row('INTERACTING_SELECTED_CORE_ASTRA.md', 'Current448-475 exact inequalities reread; previous1-112 and440-500 reused.', 'Compatibility of sigma*p^3 and sigma^2*p^12 cutoffs only; IC conclusion not imported.'),
    input_row('GRADED_COMPLEMENT_ASTRA.md', 'Complete original580-line source authored/self-read previously; current128-165 reread; sole metric correction reconstructed exactly.', 'Definition C_ch, Omega/chart qualifications and existing graded interface; original G unchanged.', inherited=False),
    input_row('REVIEW_GRADED_COMPLEMENT_ASTRA.md', 'Complete current247-line independent report read in bounded chunks.', 'Current22e30738 scoped LAND; outside-chart/normalization limits.', inherited=False),
    input_row('checks/graded_complement_distance_correction.json', 'Complete metadata and exact before/after phrase read.', 'Historical source6201ec6e separated from current22e30738.', inherited=False),
    input_row('checks/review_graded_complement_distance_confirmation.json', 'Complete affected confirmation read.', 'Exact metric correction confirmation only.', inherited=False),
    input_row('RD.md', 'Current pass2 lines822-891 read completely, plus exact current identity from coordinator.', 'R15-R17 require a specified product reference and sup-controlled interaction atoms; OC actual-law probabilities do not instantiate that criterion.', inherited=False),
    input_row('REVIEW_RD_R2.md', 'Complete413-line report read as1-390 and390-413.', 'Finite explicit H12 identity B1 resolved; quantitative/analytic/effective reference interfaces B2/B3 still HOLD. OC does not deny the resolved finite identity.', inherited=False),
]
assert next(x for x in inputs if Path(x['path']).name == 'RD.md')['sha256'] == 'a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5'
assert next(x for x in inputs if Path(x['path']).name == 'FIXED_SOURCE_RADIUS_ASTRA.md')['sha256'] == '6304245bdf27afa6c7f364da9bc41d8971cc0f2058c1e3484edef84df44cff86'

primary = [
    {'author': 'T. Balaban', 'title': 'Large field renormalization II: localization, exponentiation, and bounds for the R operation',
     'url': 'https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf',
     'version': 'Communications in Mathematical Physics122(1989); primary article text hosted by a mirror.',
     'coverage': 'New visible extracted65-174, printed356-358 and opening359; prior GC extracted0-167 reused. No full38-page read or visual-PDF claim.',
     'matching': 'Dangerous denominator, constrained stationarity and localized quadratic cap. Its hard/analytic constraints differ from the actual soft original cut; OC3-OC15 are rebuilt locally.'},
    {'author': 'J. Dimock', 'title': 'The Renormalization Group According to Balaban - II. Large Fields',
     'url': 'https://arxiv.org/html/1212.5562v2#S3.SS13',
     'version': 'arXiv1212.5562v2 versioned HTML.',
     'coverage': 'Previous complete HTML1907-2105 including Lemma3.15 proof and preceding normalization reused; no new whole-paper read.',
     'matching': 'Scalar three-dimensional covariance/background weakening and bulk/boundary separation. Distance modulo holes is not OC full-reader cardinality. No group/cut theorem imported.'},
    {'author': 'A. D. Scott and A. D. Sokal', 'title': 'The repulsive lattice gas, the independent-set polynomial, and the Lovasz local lemma',
     'url': 'https://arxiv.org/html/cond-mat/0309352v2#S4.SS1',
     'version': 'arXiv v2 submitted2004-09-16; HTML title displays revisedSeptember8,2004.',
     'coverage': 'Official abstract metadata8-30; HTML136-166 and163-223 including Theorems1.1-1.2/avoidance1.8;1281-1316 and1311-1366 including Theorem4.1 statement and proof opening, not its complete proof. Theorem5.1 opening was navigation only.',
     'matching': 'Conditional avoidance is distinguished from independence. The specialized OC21-OC24 induction was formulated before this primary read and is proved locally; no independent-set polynomial is identified with the gauge-source partition function.'},
    {'author': 'A. D. Scott and A. D. Sokal',
     'url': 'https://people.maths.ox.ac.uk/~scott/Papers/lovasz.pdf',
     'version': 'Author-hosted103-page PDF, header revisedSeptember28,2004, distinct revision label.',
     'coverage': 'Header extracted0-72 and find/navigation snippets only; not treated as the arXiv-v2 proof or read in full. No PDF saved.'},
]

gc_binding = {
    'current_source': gc_current,
    'historical_author_source': {'bytes': len(historical_bytes), 'sha256': hashlib.sha256(historical_bytes).hexdigest(),
        'reconstruction': 'In memory only: inverse exact coordinator phrase correction on verified current source. No Git or snapshot mutation.'},
    'historical_author_receipt': pin(C / 'graded_complement_receipt.json'),
    'historical_author_non_source_files': non_source_gc,
    'coordinator_correction': pin(C / 'graded_complement_distance_correction.json'),
    'affected_confirmation': pin(C / 'review_graded_complement_distance_confirmation.json'),
    'independent_review_receipt': pin(C / 'review_graded_complement_receipt.json'),
    'independent_review_owned_records_verified': len(gc_review_receipt['owned_files']),
}

manifest = {
    'created_utc': NOW, 'author_source': source,
    'author_self_read': 'Complete source assembled in bounded reads; final edited entropy/M/history passages reread. One context-truncated source read was discarded and reissued in smaller chunks.',
    'source_inputs': inputs,
    'reused_methodology_reads': methodology,
    'inherited_read_manifest': pin(C / 'graded_complement_read_manifest.json'),
    'older_read_manifest': pin(C / 'cut_sector_coercivity_read_manifest.json'),
    'external_primary_reads': primary,
    'immutable_CC_CS_packets': predecessors,
    'GC_historical_and_current_binding': gc_binding,
    'historical_context_only': [
        {'path': old_inputs['ASSUMPTIONS_AND_IMPORTS.md']['path'], 'historical_sha256': old_inputs['ASSUMPTIONS_AND_IMPORTS.md']['sha256'],
         'treatment': 'GC50-line snapshot preserved in its receipt. Root later appended B41; current register is not a newly read mathematical input here.'},
        {'path': old_inputs['RD.md']['path'], 'historical_sha256': old_inputs['RD.md']['sha256'],
         'treatment': 'GC original583-line version/read ranges remain historical at3bba918756. Current pass2 ranges and review are separately bound above.'},
    ],
    'exposure': 'Same worker authored CS/GC and independently reviewed CC before those later author roles. Prior author/checker/review exposure is not independence for OC. A different fresh Astra/max context is now reviewing the frozen OC source.',
    'not_consumed': ['No unreviewed parallel probability-sensitive-return source.', 'No F17 theorem.', 'No new Lohmann/B41 theorem.', 'No general FR full-Gaussian analytic-reader claim.', 'No current shared status register used as a model premise.'],
    'read_limits': 'Hashes certify identity, not complete reading. Exact source ranges and inherited coverage are preserved above; evidence-code packets verified by hash were not reread or rerun here.',
}
write_new(PREFIX + 'read_manifest.json', manifest)

process = {
    'created_utc': NOW, 'requested_configuration': 'Astra/max; serving backend/effort not independently attested.',
    'role': 'Author proposal, pending different-context fresh review; no author LAND verdict.',
    'owned_scope': ['OUTSIDE_CHART_RETURN_ASTRA.md', 'checks/outside_chart_return_*'],
    'science_method': 'Pure analytic construction; no scientific numerical experiment, no new simulation or physics checker.',
    'preregistration': 'No numerical criteria needed. The routes record preserves unsuccessful analytic routes and distinctions; thresholds in OC are analytic theorem hypotheses.',
    'resource_policy': 'Numerical resource gates not triggered by proof/text/hash work. No worker launch or scientific computation. Coordinator lock read only; last supplied expiry2026-10-30T02:18:02.414292+00:00.',
    'repository_context': 'Root reported current HEADddc0515e563507c74050d9c55201abb6981d4d69 and main01589af3faf806b736c42dc2f3bd625e9edead9f. No Git command was run by this unit.',
    'mutations': 'Only owned new source/evidence files; no shared fronts, Git/PR, locks, audits, ledgers, axioms or predecessor edits.',
    'failures_preserved': [
        'Analytic routes: arbitrary conditional minimizer; fixed-width/max-boundary reset; whole-volume reference; uncollared lower bound; packing loss; dyadic alternative; probability-to-activity inference; changing G/Omega. See routes note.',
        'Discovery query initially guessed wrong arXiv number; official cond-mat/0309352v2 was then located/read. No wrong paper theorem consumed.',
        'Truncated discovery/source retrievals were not counted as full proof reads; required source ranges recovered in bounded reads.',
        'No new scientific pass/fail count. Existing CC23/24, original shell failureu40 ratio2.463807379..., separately post-hoc narrower3/3, mutation controls and resource-only RLIMIT_RSS/parser failures remain unchanged in their packets.',
        'CS/GC earlier mechanical freeze failures and the historical GC context-register drift remain intact. No historical failure is restamped as passing this unit.',
    ],
    'limits': [
        'OC15 normalized actual original-law probabilities and OC19 component expectations are not analytic activities.',
        'Real reference comparisons retain volume and the explicitly narrower shrinking coarse-curvature window.',
        'Complete-history/failure/source-sea integration, complex nonvanishing, consumer-locality, coarse law outside the window and later effective levels remain open.',
        'RD pass2 finite H12 identity resolution is recognized; its product-reference hard-cut criterion still needs an exact quantitative match.',
        'Full4D existence and physical continuum mass gap remain OPEN.',
    ],
}
write_new(PREFIX + 'process.json', process)

# Text mechanics only. Indented mathematical displays are not Markdown links.
source_text = SOURCE.read_text()
labels = re.findall(r'^\s+.*\(OC(\d+)\)\s*$', source_text, flags=re.M)
assert [int(x) for x in labels] == list(range(1, 33)), labels
pending_receipt = {receipt_path}
links = []
for path in (SOURCE, C / (PREFIX + 'routes.md')):
    inside = False
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith('```'):
            inside = not inside
            continue
        if inside or line.startswith('    '):
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', line):
            if '://' in target or target.startswith('#'):
                continue
            resolved = (path.parent / target.split('#', 1)[0]).resolve()
            assert resolved.exists() or resolved in pending_receipt, (path, number, target)
            links.append({'file': rel(path), 'line': number, 'target': rel(resolved),
                          'pre_receipt_exists': resolved.exists()})
verification = {
    'created_utc': NOW, 'scope': 'Mechanical identity/text evidence only; no independent proof verdict or numerical validation.',
    'source': source, 'source_lines': 641, 'equation_labels': list(range(1,33)),
    'source_freeze_matches': True, 'methodology_pins_verified': len(methodology),
    'current_input_pins_verified': len(inputs), 'CC_CS_owned_records_verified': predecessor_owned_count,
    'CC_CS_receipts_verified': len(predecessors),
    'GC_author_current_non_source_files_verified_including_receipt': len(non_source_gc),
    'GC_historical_source_reconstructed_exactly': True,
    'GC_fresh_review_owned_records_verified': len(gc_review_receipt['owned_files']),
    'source_relative_links': links,
    'link_note': 'Receipt target is the only intentionally pending link at this stage; the script checks actual existence after writing the receipt.',
    'scientific_numerical_runs': 0,
}
write_new(PREFIX + 'verification.json', verification)

# Closed author inventory, without self-referential hashing.
owned_paths = [SOURCE] + sorted(p for p in C.glob(PREFIX + '*') if p != receipt_path)
assert len(owned_paths) == 7, [rel(p) for p in owned_paths]
owned = [pin(p) for p in owned_paths]
receipt = {
    'format': 'bounded-analytic-author-packet-v1', 'created_utc': NOW,
    'author_source': source,
    'author_review_status': 'FROZEN_AUTHOR_PROPOSAL_PENDING_DIFFERENT_FRESH_REVIEW',
    'owned_files': owned,
    'input_pins': inputs,
    'source_freeze': pin(C / (PREFIX + 'source_freeze.json')),
    'read_manifest': pin(C / (PREFIX + 'read_manifest.json')),
    'predecessor_receipt_pins': [x['receipt'] for x in predecessors] + [pin(C / 'graded_complement_receipt.json'), pin(C / 'review_graded_complement_receipt.json')],
    'GC_binding': gc_binding,
    'evidence': 'Pure analytic source plus explicit routes/exposure and mechanically verified byte identities. No numerical pass/fail claim.',
    'scope': 'OC1-OC32: exact compact cut law, full local coercivity/reference/cap, arbitrary prescribed-set normalized real price, full-reader component expectation, actual real avoidance/reference comparisons and narrower cube comparison, complex raw envelopes, restricted H24 conditional extension.',
    'unproved': 'Local analytic connected complement, normalized complex nonvanishing, full source/history/failure/sea matching, coarse integration outside admitted window, nonlinear flow, continuum existence and physical mass gap.',
    'immutability': 'Seven bound owned files plus this receipt form eight-file author packet. Source argument frozen before packaging. No predecessor or shared artifact changed.',
}
write_new(PREFIX + 'receipt.json', receipt)
for row in owned + inputs:
    verify(row)
for row in links:
    assert (ROOT / row['target']).exists(), row
assert len([SOURCE] + list(C.glob(PREFIX + '*'))) == 8
print(json.dumps({'source': source, 'receipt': pin(receipt_path), 'author_files_including_receipt': 8,
                  'current_inputs': len(inputs), 'methodology_pins': len(methodology),
                  'CC_CS_owned_verified': predecessor_owned_count, 'GC_historical_current_separated': True,
                  'all_relative_links_exist_after_closure': True, 'scientific_numerical_runs': 0}, indent=2))
